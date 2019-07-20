# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy_redis.spiders import RedisCrawlSpider

class A3gSpider(RedisCrawlSpider):
    name = 'a3g'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    redis_kk='a3g'
    def parse(self, response):
        res = response.text.replace('allTopicList(',"")
        res = res.replace(")","")
        res_dic = json.loads(res)
        for i in res_dic['data']:
            for item in res_dic['data'][i]:
                dic_taget = {'title': '', 'img': ''}
                dic_taget['title'] = item['title']
                if item['picInfo']:
                    dic_taget['img'] = item['picInfo'][0]['url']
                item['dic_taget']=dic_taget
                yield item

