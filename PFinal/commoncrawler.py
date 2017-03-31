import requests
import argparse
import time
import json
import StringIO
import gzip
import csv
import codecs

from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# parse the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d","--domain",required=True,help="The domain to target ie. cnn.com")
args = vars(ap.parse_args())

file = args['domain']


with open(file) as f:
    content = f.readlines()

domains = [x.strip("\n") for x in content] 

values = []

# list of available indices
index_list = ["2017-09"]

#
# Searches the Common Crawl Index for a domain.
#
def search_domain(domain):

    record_list = []
    
    print "[*] Trying target domain: %s" % domain
    
    for index in index_list:
        
        print "[*] Trying index %s" % index
        
        cc_url  = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
        cc_url += "url=%s&matchType=domain&output=json" % domain
        
        response = requests.get(cc_url)
        
        if response.status_code == 200:
            
            records = response.content.splitlines()
            
            for record in records:
                record_list.append(json.loads(record))
            
            print "[*] Added %d results." % len(records)
            
    
    print "[*] Found a total of %d hits." % len(record_list)
    
    return record_list        


# Downloads a page from Common Crawl

def download_page(record):

    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1

    
    # Getting the file on S3 is equivalent however - you can request a Range
    prefix = 'https://commoncrawl.s3.amazonaws.com/'
    
    # We can then use the Range header to ask for just this set of bytes

    print prefix
    resp = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
    print resp

    # The page is stored compressed
    # We can extract it using the GZIP library
    raw_data = StringIO.StringIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)
    
    # What we have now is just the WARC response, formatted:
    data = f.read()
    
    response = ""
    
    if len(data):
        try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
        except:
            pass
            
    return response

#
# Extract title from the HTML  
#

def extract_title(html_content):
    parser = BeautifulSoup(html_content)
    title = parser.find_all("title")
    return title[0].contents[0].encode('ascii','ignore').strip("\n")

#
# Extract text from the HTML  
#

def extract_text(html_content):
    parser = BeautifulSoup(html_content)

    for script in parser(["script", "style"]):
        script.extract()    # rip it out

    text = parser.get_text()
    text = text.replace("\"", "\'")
    text = " ".join(text.split())
    return text

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    return True

for i in range(0,60):
    values.append("1")

for i in range(0, 60):
    values.append("0")

with codecs.open("data.csv","wb",encoding="utf-8") as output:

    fields = ["domain","title","text", "value"]
        
    logger = csv.DictWriter(output,fieldnames=fields)
    logger.writeheader()
    i= 0
    for domain in domains:

        record_list = search_domain(domain)
        record = record_list[0]

        html_content = download_page(record)

        print "[*] Retrieved %d bytes for %s" % (len(html_content),record['url'])

        text = extract_text(html_content)
        title = extract_title(html_content)

        
        logger.writerow({"domain":domain,"title":title,"text":text,"value":values[i]})
        i = i+1
