import sys
import os
import json
import time

from os.path import dirname,abspath
sys.path.append(dirname(dirname(abspath(__file__))))

from unittest import TestCase
from unittest import main

from browser import Browser


class test_webdrivers(TestCase):

    def test_get(self):
        
        with open('config.js','r') as f:
            c = f.read()
        j = json.loads(c) 
        print(j)       
        for browser_config in j:
            for browser in browser_config.keys():
                executable = browser_config[browser]['executable']
                verify = browser_config[browser]['verify']
                print(executable,verify)
                with Browser(browser,executable,verify) as b:
                    print("Testing %s with executable %s and verify %s" % (browser,executable,verify))
                    b.get('https://httpbin.org/get')
#                    time.sleep(2) 
                    
                
            

if __name__ == "__main__":
    main()


