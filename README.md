# Amazon-Crawling

## Task
Implementing Web Scrapping using Scrapy

## Synopsis
### Objective: Succeed in scraping Amazon Baby Clothing Sets products data and store it employing MongoDB Compass
### Approach:
* Taken advantage of Scrapy, Pywin32, Scrapy-User-Agents and PyMongo to create a spider for scrapping
* Applied HTML concepts and Selector Gadget Chrome Extension to select similarly placed data collectively
* Bypassed restrictions via agents and proxies, defined pipeline and encoded extraction for multiple pages
### Result: Collected scraped data of 334 documents inside the NoSQL database supported by MongoDB

## Requirements
1. Pycharm
2. Python Version - 3.10
3. MongoDB
4. Git and GitHub
5. Chrome Browser

## Note
The venv folder automatically gets created in AmazonCrawling when venv is selected on creating the project and the .idea folder just stores project-related settings

## Prerequisites
HTML and Scraping Basics

## Steps for Scrapping
* Create new project in Pycharm(VENV)
* Install packages (Only once, do upgrade) - Scrapy, pywin32 and scrapy-user-agents
1. scrapy to do scraping
2. pywin32 integrate pycharm to windows
3. scrapy-user-agents to create fake users for scraping every time (No need when scrapping a site for the first time)

* Go to terminal -> down arrow on right -> command prompt -> should have venv
* Execute below commands
1. scrapy startproject amazoncrawl (Only for the first time because already started when reworking on the project)
2. cd amazoncrawl
3. scrapy genspider amazon_spiders amazon.com (Only for the first time to create spider for crawling) (Can have any name and website)

* Go to items.py and give variable # comment name for all the variables
* Get the selector gadget extension on Chrome and enable it
* Go in amazon_spiders.py -> In class after name, write start_urls = ['url'] -> remove allowed domains -> xpath copy and paste -> give items['varname']= varname, yield items and pass
* Execute the below commands in the terminal
1. cls (clears screen)
2. scrapy crawl amazon_spiders (Always needed to see scraped data) (Do give cd amazoncrawl when reworking on the project before this)

### ..items have .. representing that we're going one step/directory back

### https://www.google.com/robots.txt to check allowed extraction from a website

* Bypass restrictions
### 3 Ways to Bypass Restrictions
1. Using Google bot user agent (Google Bot):
* Search it and open the second link with whatismybrowser.com. (Take any one) (Can extract any number of pages)
* Add this in settings.py under USER_AGENT:
```
USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
```
2. Using user agents (Different users):
* Install scrapy-user-agents.
* With this, you do not get disallowed to access links after scrolling once through rotating 2200 agents. (Will extract 25-35 pages max)
* Add in settings.py under middlewares:
```
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
```
3. Use proxies (Different IP addresses):
* Similar to 2nd.
* Install scrapy-proxy-pool.
* Add in settings.py, PROXY_POOL_ENABLED = True after ROBOTSTXT_OBEY = True and under middlewares:
```
DOWNLOADER_MIDDLEWARES = {
    # ...
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
}
```

* run scrapy crawl amazon_spiders again

## Connect with MongoDB Compass
* Create data -> db folder in C drive
* Open mongod from program files and then close it after some time
* Check that some files are there in the db folder
* Open MongoDB Compass and click connect

## Store Data in MongoDB
* Install pymongo package
* pymongo connects Python to Mongodb
* Comment out ITEM_PIPELINES in settings.py
* In pipelines.py,
1. Inside init in class, add connection (using username & port number or connection_string), database and collection 
2. Add documents in the collection as a dictionary in the process_item function of class
3. Run scrapy crawl amazon_spiders again
4. Open MongoDB Compass and refresh
5. The database will be there

## Scrape Multiple Pages
For scraping multiple pages, in spider file, add page_number = 2 as the second line and
```
next_page = 'https://www.amazon.in/s?k=clothing&i=apparel&rh=n%3A1571271031%2Cn%3A1953173031&dc&page=' + str(AmazonSpidersSpider.page_number) + '&qid=1648063354&rnid=3576079031&ref=sr_pg_' + str(AmazonSpidersSpider.page_number)
if AmazonSpidersSpider.page_number <= 334:
    yield response.follow(next_page, callback=self.parse)
    AmazonSpidersSpider.page_number += 1
```
at the end of the parse() function (after yield items and before pass)

## Push Code to GitHub
In the command prompt terminal, write,
1. git init
2. git add . && git commit -m "initial commit" (May ask for email and username if committing for the first time from your computer) (Will see n files changed)
3. git branch -M main
4. git remote add origin https://github.com/rashika-dabas/Amazon-Crawling.git
5. git push -u origin main (May ask for your GitHub password)
