#!/usr/bin/python3

from lib.payloads.basicpayload import BasicPayload

def main():
    print(BasicPayload().generate_script())

if __name__ == "__main__":
    main()


