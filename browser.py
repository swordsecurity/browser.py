import sys
import os
from selenium import webdriver

class Chrome():

    def __init__(self,executable,verify=True,disable_extensions=True,disable_xss_auditor=False):
        args = webdriver.chrome.options.Options()

        if disable_extensions:
            args.add_argument('--disable-extensions')
        if disable_xss_auditor:
            args.add_argument('--disable-xss-auditor')
        if verify == False:
            args.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])


        if sys.version_info >= (3, 0):
            self.driver = webdriver.Chrome(executable_path=executable,options=args)
        else:        
            self.driver = webdriver.Chrome(executable_path=executable,chrome_options=args)

    def __enter__(self):
        return self.driver

    def __exit__(self, type, value, traceback):
        self.driver.quit()

class PhantomJS():

    def __init__(self,executable,verify=True):
        args = []
        if verify == False:
            args = ['--ignore-ssl-errors=true', '--ssl-protocol=any']

        self.driver = webdriver.PhantomJS(executable_path=executable, service_log_path=os.path.devnull,service_args=args)

    def __enter__(self):
        return self.driver

    def __exit__(self, type, value, traceback):
        self.driver.quit()
