# browser.py: Python Selenium API for Humans

Behold the power of browser.py:
```
# Print page source with Google Chrome
from browser import Chrome
with Chrome('../../selenium-drivers/chromedriver) as b:
     b.get('https://httpbin.org/get')
     print b.page_source

# Print page source with PhantomJS
from browser import PhantomJS
with PhantomJS('../../selenium-drivers/chromedriver) as b:
     b.get('https://httpbin.org/get')
     print b.page_source
```

# Installation
## Installing webdrivers for Selenium
Download the webdriver of the browser you want to use:
- Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
- PhantomJS: http://phantomjs.org/download.html

In the example above I've created a selenium-drivers folder in my home directory and copied the drivers in there.
