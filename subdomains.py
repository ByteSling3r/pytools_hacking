#!/usr/bin/python3
import sys
import requests 
from os import path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Indicate domain')
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists('subdomains.txt'):
            word_list = open('subdomains.txt','r')
            word_list = word_list.read().split('\n')
            
            for protocol in ['https', 'http']:
                for word in word_list:
                    url = f'{protocol}://{word}.{parser.target}'
                    try:
                        requests.get(url)
                    except requests.ConnectionError:
                        continue
                    else:
                        print(f'[+] Subdomain found: {url}')
            
    else:
        print(f'[-] No domain was indicated')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()