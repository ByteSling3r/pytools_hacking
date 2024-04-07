#!/usr/bin/python3
import requests 
from os import path
import argparse
import re
import threading

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Indicate domain')
parser.add_argument('-d', '--dict', help='Indicate the brute force dictionary')
parser = parser.parse_args()

def get_dict(dict='subdomains.txt'):
    if path.exists(dict):
        with open(dict,'r') as word_list:
            word_list = word_list.read().split('\n')
        return word_list
    else:
        print('[-] The path is not correct or the dictionary does not exist')

def enumerate_domains(dict):
    for protocol in ['https', 'http']:
        for word in dict:
            url = f'{protocol}://{word}.{parser.target}'
            try:
                requests.get(url)
            except requests.ConnectionError as e:
                continue
            else:
                print(f'[+] Subdomain found: {url}')
            
def main():
    if parser.target:
        if re.match(r"\w+\.\w+", parser.target):
            enumerate_domains(get_dict(parser.dict)) if parser.dict else enumerate_domains(get_dict())
        else:
            print('[-] Not the expected format (example.com)')
    else:
        print('[-] No domain was indicated')

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    try:
        thread.start()
    except KeyboardInterrupt:
        pass