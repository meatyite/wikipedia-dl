#!/usr/bin/env python3

import requests
from urllib.parse import unquote
from sys import argv

session = requests.Session()
session.headers = {'User-Agent': 'wikipedia-dl github.com/sl4vkek/wikipedia-dl'}


def download_pdf(url):
    print("Parsing URL...")
    url_split = url.split('/')
    domain = url_split[2]
    real_page_name = ' slash '.join(url_split[4:]).replace('_', ' ')
    real_page_name = unquote(real_page_name)
    page_name = real_page_name.replace(' slash ', '/')
    print('Article {} on website {}'.format(real_page_name, url_split[0] + '//' + domain))
    print('Sending request...')
    pdf = session.post(
        url_split[0] + '//' + domain + '/wiki/Special:DownloadAsPdf',
        data={
            'page': page_name,
            'action': 'redirect-to-electron'
        }
    )
    file_name = real_page_name.strip() + '.pdf'
    print('PDF Received. Writing to file {}...'.format(file_name))
    open(file_name, 'wb').write(pdf.content)
    print('Done!')


if __name__ == '__main__':
    if len(argv) >= 1:
        download_pdf(argv[2])
    else:
        print("Usage: wikipedia-dl [url]")
