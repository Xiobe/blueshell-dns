#! /usr/bin/python3

__version__ = "0.0.0"
__prog__ = f"dnsinfo.py {__version__}"
__description__ = 'DNS information'

import argparse

class DNSinfo:
    pass

def main():
    parser = argparse.ArgumentParser(prog=__prog__, description=__description__)
    parser.add_argument('domain', help='domain name')
    parser.add_argument('--outputfile', help='output file. Default format is json, use --format to change format.')
    parser.add_argument('--format', choices=['json','csv'], help='output format to be used with --outputfile.')
    args = parser.parse_args()

    dnsinfo = DNSInfo()
    print("Hello from dnsinfo")

if __name__ == '__main__':
    main()
