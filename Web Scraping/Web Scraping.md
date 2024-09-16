The study of HTML allows for work to be done on web scraping, an automatic method to obtain large amounts of data from websites (GeeksForGeeks, 2024). 

The first use of web scraping done was experimenting with fake websites. The provided file, “BeautifulSoupTest.py”, shows the first use of BeautifulSoup done; this was the most simple application of web scraping, 
However, when this was attempted to be extended to real websites, the challenge of javascript was encountered. Most websites use javascript to dynamically load content onto a webpage; BeautifulSoup cannot access this information, as it is not loaded in on the webpage’s activation:  

Selenium was used to solve this problem. After some experimentation, information from the XBOX browse page was successfully extracted, using the script in the attached SeleniumTest.py file. 

Having the knowledge to successfully web scrape means, if data is ever required for an application or task, that data can be obtained. This is beneficial in areas such as data science, as the data first needs to be collected and stored in one location for it to be analysed. It also has applications in marketing, where competitor’s prices, customer information and other details are required. 

However, web scraping is also dangerous. If a web scraper violates the Computer Fraud and Abuse Act, Copyright Law or a company’s TOS, legal action may be involved. Thus, knowledge on how to responsibly web scrape was required to be gained alongside the web scraping techniques. 

One method of doing so is following a website's “robots.txt” file. This determines what data of the website can be legally handled. This file is important, as it details what actions taken by a web scraper are prohibited on the site. 
For example, the “robots.txt” file for the XBOX store is as follows:

---
User-agent: *
Disallow: /error
Disallow: /*Search?q*
Disallow: /*search?q*
Disallow: /*results?k*
Disallow: /*Results?k*
Disallow: /_layouts/
Disallow: /_vti_bin/
Disallow: /*/contact-us?isChatCallAvailable=false
Disallow: /*/play/user/*
Sitemap: https://www.xbox.com/sitemap.xml
---

Per the file, scraping information off of the page screenshotted as ‘xboxResultsPage’ is prohibited. But scraping information off of the page screenshotted as ‘xboxBrowsePage’ is not. Thus, the actions performed in ‘SeleniumTest.py’ are allowed to be taken. 
