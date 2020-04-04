
# How to use the scrapy Tool

## Create Scrapy Projects:
  scrapy startproject Project_Name

## Create Spider:
  scrapy genspider Name_of_Spider  URL
  
# Usage:
  scrapy command options args

|  Global Commands | Running Command |
|---|---|
| genspider  | Create a spider |
| runspider | Run a self-contained spider (without creating a project)|
| settings |Get the value of a Scrapy setting, RUN: scrapy settings (options)  |
| shell |  Interactive scraping console, scrapy shell 'http://www.NHL.com/' |
| startproject | Create new project |
| version | Print Scrapy version, RUN: scrapy version |
| view | Open URL in browser, as seen by Scrapy, RUN:scrapy view |
| fetch | Fetch a URL using the Scrapy downloader RUN: scrapy fetch |

|  Project-Only Commands | Running command |
|---|---|
| crawl  | scrapy crawl spid, This runs the spider with the name spid in the current project |
| check | Run contract checks, RUN: scrapy check Name_of_Spider |
| list  |List all available spiders in the current project, RUN: Scrapy list |
| edit |Edit the given spider, RUN: scrapy edit Name_of_Spider | 
| parse  | called to handle each of the requests for URLs |
| bench | Run quick benchmark test, RUN: Scrapy bench|

# More Detailed options

|  Commands | Options |
|---|---|
| settings| Multiple Options use for reference: https://docs.scrapy.org/en/latest/topics/settings.html|
|parse||
|fetch|--spider=SPIDER,   --headers,   --no-redirect|
|view| --spider=SPIDER,  --no-redirect|
|shell|-c code,  |

## Parse Options

--spider=SPIDER: bypass spider autodetection and force use of specific spider
--a NAME=VALUE: set spider argument 
--callback or -c: spider method to use as callback for parsing the response
--meta or -m: additional request meta that will be passed to the callback request. 
--cbkwargs: additional keyword arguments that will be passed to the callback. This must be a valid json string. 
--pipelines: process items through pipelines
--rules or -r: use CrawlSpider rules to discover the callback (i.e. spider method) to use for parsing the response
--noitems: don’t show scraped items
--nolinks: don’t show extracted links
--nocolour: avoid using pygments to colorize the output
--depth or -d: depth level for which the requests should be followed recursively (default: 1)
--verbose or -v: display information for each depth level


