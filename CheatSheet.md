
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
|||
