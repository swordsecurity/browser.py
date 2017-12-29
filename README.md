# browser.py: Python Selenium API for Humans

Behold the power of browser.py:
```
from browser import Browser
browser = 'chrome'
executable = '../../selenium-drivers/chromedriver'
with Browser(browser,executable) as b:
     b.get('https://httpbin.org/get')
     print b.page_source

```


# Installation
## Installing webdrivers for Selenium
==========
Download the webdriver of the browser you want to use:

- Firefox: https://github.com/mozilla/geckodriver/releases
- Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
- PhantomJS: http://phantomjs.org/download.html

In the example above I've created a selenium-drivers folder in my home directory and copied the drivers in there.
