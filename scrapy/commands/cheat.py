import scrapy
from scrapy.commands import ScrapyCommand
from scrapy.utils.versions import scrapy_components_versions


class Command(ScrapyCommand):

    default_settings = {'LOG_ENABLED': False,
                        'SPIDER_LOADER_WARN_ONLY': True}


    def short_desc(self):
        return "Print Scrapy Cheat Sheet for quick commands"

     def long_desc(self):
        
