# Amazon-Crawling
## PYCHARM PROJECT: AmazonCrawling
## Python Version: 3.10
## Title: Web Scrapping using Scrapy

venv folder automatically gets created in AmazonCrawling when venv is selected on creating project

html and scraping - read general info

Create new project in Pycharm(VENV)
Install packages (Only once, do upgrade) - Scrapy, pywin32 and scrapy-user-agents
Scrapy to do scraping
pywin32 integrate pycharm to windows
scrapy-user-agents to create fake users for scraping everytime (No need when scrapping a site for first time)

Go to terminal -> down arrow on right -> command prompt -> should have venv

> scrapy startproject amazoncrawl (Only for first time because already started when reworking on project)
> cd amazoncrawl
> scrapy genspider amazon_spiders amazon.com (Only for first time to create spider for crawling) (Can have any name and website)

Go in items.py and give variable # comment name for all the variables
Get selectorgadget extension on chrome and enable it
Go in amazon_spiders.py -> In class after name, write start_urls = ['url'] -> remove allowed domains -> xpath copy and paste -> give items['varname']= varname, yield items and pass

> cls (clears screen)
> scrapy crawl amazon_spiders (Always needed to see scraped data) (Do give cd amazoncrawl when reworking on project before this)

..items has .. representing that we're going one step back

https://www.google.com/robots.txt to check allowed extraction from a website

## 3 Ways to Bypass Restrictions:
1. Using Google bot user agent (Google Bot): Search it and open the second link with whatismybrowser.com (Take any one) (Can extract any number of pages)
add this in settings.py under USER_AGENT
USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
2. Using user agents (Different users):
Install scrapy-user-agents
With this, you not get disallowed to access links after scrolling once through rotating 2200 agents (Will extract 25-35 pages max)
Add in settings.py under middlewares:
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
3. Use proxies (Different ip addresses):
Similar to 2nd
Install scrapy-proxy-pool
Add in settings.py, PROXY_POOL_ENABLED = True after ROBOTSTXT_OBEY = True and under middlewares:
DOWNLOADER_MIDDLEWARES = {
    # ...
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
}
run scrapy crawl amazon_spiders again

## Connecting with MongoDBCompass:
Create data -> db folder in C drive
Open mongod from program files and then close it after sometime
Check that some files are there in db folder
Open mongodb compass and click connect

## Storing data in MongoDB:
Install pymongo package
pymongo connects python to mongodb
ITEM_PIPELINES in settings.py comment out
pipelines.py:
Inside init in class, add connection(using username & port number or connection_string), database and collection 
add documents in collection as dictionary in process_item function of class
run scrapy crawl amazon_spiders again
open mongodb compass and refresh
database will be there

## Scraping multiple pages:
For scraping multiple pages, in spider file, add page_number = 2 as the second line and
next_page = 'https://www.amazon.in/s?k=clothing&i=apparel&rh=n%3A1571271031%2Cn%3A1953173031&dc&page=' + str(AmazonSpidersSpider.page_number) + '&qid=1648063354&rnid=3576079031&ref=sr_pg_' + str(AmazonSpidersSpider.page_number)
if AmazonSpidersSpider.page_number <= 334:
    yield response.follow(next_page, callback=self.parse)
    AmazonSpidersSpider.page_number += 1
at the end of the parse() function (after yield items and before pass)

## Pushing code to GitHub:
In the command prompt terminal, write,
1. git init
2. git add . && git commit -m "initial commit" (May ask for email and username if committing for the first time from your computer) (Will see n files changed)
3. git branch -M main
4. git remote add origin https://github.com/rashika-dabas/Amazon-Crawling.git
5. git push -u origin main (May ask for your GitHub password)
6. left files are added manually
