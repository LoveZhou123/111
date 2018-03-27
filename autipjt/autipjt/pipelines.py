# -*- coding: utf-8 -*-
import codecs
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutipjtPipeline(object):

    def __init__(self):
        # self.file = open("mydata.json","w",encoding="utf-8")
        self.file = open("mydata1.json","w",encoding="utf-8")


    def process_item(self, item, spider):
        # i = json.dumps(dict(item),ensure_ascii=False)
        # #每行数据后边加上\n换行
        # line = i +"\n"
        # #数据写入到ison文件中
        # self.file.write(line)
        # return item

        #每一页中包含多个商品，可以通过循环每一次处理一个商品
        #其中len(item["name"])为商品总数，依次便利
        for j in range(0,len(item["name"])):
            #当前页的第j个商品赋值给变量name
            name=item["name"][j]
            price = item["price"][j]
            comnum = item["comnum"][j]
            link = item["link"][j]
            #将当前页下第j个商品name,price,comnum,link等信息处理一下
            #重新组合成一个字典
            goods = {"name":name,"price":price,"comnum":comnum,"link":link}
            #将组合好的当前第j页商品写入文件
            i = json.dumps(dict(goods), ensure_ascii=False)
            line = i + "\n"
            self.file.write(line)
        #返回item
        return item
    def close_spider(self,spider):
        #关闭mydata.json文件
        self.file.close()