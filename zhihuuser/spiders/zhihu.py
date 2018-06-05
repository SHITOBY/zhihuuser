# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider

from zhihuuser.items import ZhihuuserItem


class ZhihuSpider(RedisSpider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']

    redis_key = 'zhihu:start_urls'

    start_urls = ['http://zhihu.com/']
    start_user = 'xiaolunzi'

    user_url = 'https://www.zhihu.com/api/v4/members/{user_name}?include={include}'
    user_query = 'allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    followee_url = 'https://www.zhihu.com/api/v4/members/{user_name}/followees?include={include}&offset={offset}&limit={limit}'
    followee_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    follower_url = 'https://www.zhihu.com/api/v4/members/{user_name}/followers?include={include}&offset={offset}&limit={limit}'
    follower_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer' \
                     ')].topics'

    def start_requests(self):

        yield Request(url= self.user_url.format(user_name= self.start_user,include = self.user_query),callback = self.user_parse)
        yield Request(url = self.followee_url.format(user_name = self.start_user,include = self.followee_query,offset = 0,limit = 20),callback = self.followee_parse)

    def user_parse(self,response):

        result = json.loads(response.text)
        item = ZhihuuserItem()

        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

    def followee_parse(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(url=self.user_url.format(user_name=result.get('url_token'),
                                                       include = self.user_query,
                                                       ),
                              callback=self.user_parse
                              )

        if 'paging' in results.keys() and results.get('paging').get('is_end')==False:
            next_page = results.get('paging').get('next')
            yield Request(url = next_page,callback=self.followee_parse)

    def follower_parse(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(url=self.user_url.format(user_name=result.get('url_token'),
                                                       include=self.user_query,
                                                       ),
                              callback=self.user_parse
                              )

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get(next)
            yield Request(url=next_page, callback=self.follower_parse)











