#!/usr/bin/env python3

import requests
from urllib.parse import unquote
from sys import argv

user_agent = 'wikipedia-dl/1.0 PDF downloader bot github.com/sl4vkek/wikipedia-dl'
session = requests.Session()
session.headers = {'User-Agent': user_agent}


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
    if len(argv) >= 2:
        if argv[1] == "-v":
            print("""wikipedia-dl by sl4vkek
Version: 1.0
User agent: {}
Licensed under the Unlicense, see unlicense.org for more information.
NO COPYRIGHT intended.""".format(user_agent))
            exit()
        if argv[1] == '-h':
            print("""
Usage: wikipedia-dl [URL] OR wikipedia-dl [OPTION]
Options:
-h     -  Displays help information and exits
-v     -  Displays version information and exits
""")
            exit()
        download_pdf(argv[1])
    else:
        print("Usage: wikipedia-dl [url]")
