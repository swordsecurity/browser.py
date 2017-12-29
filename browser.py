#!/usr/bin/python3

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Browser():

    def __init__(self, browser,executable,verify=True):
        self.driver = None
        self.browser = browser
        if self.browser == 'phantomjs':
            self.load_phantomjs(executable,verify)                
        elif self.browser == 'chrome':
            self.load_chrome(executable,verify)                
        else:
            raise Exception('Browser %s not supported (choose phantomjs or chrome)')

    def load_phantomjs(self,executable,verify):
        args = []
        if verify == False:
            args = ['--ignore-ssl-errors=true', '--ssl-protocol=any']

        self.driver = webdriver.PhantomJS(executable_path=executable, service_log_path=os.path.devnull,service_args=args)

    def load_chrome(self,executable,verify):
        args = webdriver.ChromeOptions()
        args.add_argument('--disable-extensions')
        args.add_argument('--disable-xss-auditor')
        if verify == False:
            args.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

        self.driver = webdriver.Chrome(executable_path=executable,chrome_options=args)

    def __enter__(self):
        return self.driver

    def __exit__(self, type, value, traceback):
        self.driver.quit()
