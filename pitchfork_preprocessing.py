from time import sleep
import json
import csv
import urllib
import urllib.request as ur

delay = 5

with open('scrape-output-1.json', 'r') as f:
    x = 0
    for row in f:
        url = row

        review_url = url.strip('/\n')
        #review_url = review_url.strip('htt')
        #review_url = review_url.strip('ps')
        #review_url = review_url.strip('://')
        #print(row)
        #print(review_url)

        html_name = review_url.strip('htt')
        html_name = html_name.strip('ps')
        html_name = html_name.strip('://')
        html_name = html_name.strip('pitchfork')
        html_name = html_name.strip('.com')
        html_name = html_name.strip('/reviews/albums/')

        #print(html_name)

        html = './raw-html/' + html_name + '.html'

        urllib.request.urlretrieve(review_url, html)
        #ur.urlretrieve(review_url, review_url_html)

        #print(review_url_html)
        print(review_url)
        x = x + 1
        print(x)


        sleep(delay)

