# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from appdirs import unicode
from scrapy.exceptions import DropItem

class GooglePipeline(object):

    words_to_filter=[u'교내채용'] #여기서 거르고 싶은 단어들을 설정하고 제외시킨다. settings.py도 변경해줘야 함

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['category']):
                raise DropItem("Contains forbidden word: %s" %word)
        else:
            return item