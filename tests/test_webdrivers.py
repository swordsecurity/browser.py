import sys
import os
import json
import time

from os.path import dirname,abspath
sys.path.append(dirname(dirname(abspath(__file__))))

from unittest import TestCase
from unittest import main

from browser import Chrome,PhantomJS


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


                if browser == 'chrome':
                    with Chrome(executable,verify) as b:
                        print("Testing %s with executable %s and verify %s" % (browser,executable,verify))
                        b.get('https://httpbin.org/get')
                
                elif browser == 'phantomjs':
                    with PhantomJS(executable,verify) as b:
                        print("Testing %s with executable %s and verify %s" % (browser,executable,verify))
                        b.get('https://httpbin.org/get')
                else: raise Exception('Unknown browser %s' % browser)

                    
                
            

if __name__ == "__main__":
    main()


