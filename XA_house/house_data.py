#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import re
from bs4 import BeautifulSoup
import os
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class get_data(object):
	def __init__(self,area,page):
		self.area = area
		self.page = page
	def get_page(self,area,page):
		try:
			url = 'http://xa.fang.lianjia.com/loupan/%s/pg%s' % (area,str(page))
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",    "Accept-Encoding":"gzip, deflate, sdch",
			 "Accept-Language":"zh-CN,zh;q=0.8",
			 "Cache-Control":"max-age=0",
			 "Connection":"keep-alive"}
			r = requests.get(url,headers=headers,verify=False,allow_redirects=False)
			return r.text;
		except Exception as e:
			print e;
			return '连接失败！'
	def parse_data(self):
		info_list = []
		for i in range(1,self.page):
			content = self.get_page(self.area,i);
			#使用BeautifulSoup解析网页
			soup = BeautifulSoup(content,'lxml');
			items = soup.find_all(attrs={"data-index":'0'})
			for item in items:
				loupan = item.find(name = 'div',class_='col-1')
				name = loupan.find(name = 'a',href = re.compile('loupan')).string.strip()
				region = loupan.find(name = 'span',class_='region').string.strip()
				area = loupan.find(name = 'div',class_='area')
				area = area.find(name = 'span')
				if area != None:
					area = area.get_text().strip()
				else:
					area = ''
				onsold = loupan.find(name = 'span',class_='onsold').string.strip()
				live = loupan.find(name = 'span',class_='live').string.strip()
				price = item.find(name = 'div',class_='average')
				price = price.find(name='span',class_='num')
				if price != None:
					price = price.string.strip()
				else:
					price = '0' #0表示待定
				info = (name,region,area,onsold,live,price)
				info_list.append(info)
			print '第%s页完成' % str(i)
		self.data_toCsv(info_list)
	def data_toCsv(self,info):
		filepath = os.path.dirname(os.path.abspath(__file__))
		filename = filepath+'/store/%s.csv' % self.area
		csvfile = file(filename,'wb')
		csvfile.write(codecs.BOM_UTF8)
		writer = csv.writer(csvfile)
		writer.writerow([u'名称',u'位置',u'建面',u'销售状态',u'类型',u'价格'])
		data = info
		writer.writerows(data)
		csvfile.close()
class store_data(object):
	def data(self):
		diction = {'qujiang':5,'gaoxin4':5,'jingkai':4,'changan1':4,'chanba':6,'chengbei':6,'chengxi':5,
				'chengnan':4,'chengdong':4,'xixian':5,'gaoling1':2,'lintong':2,'yanliang':2,'huxian':2}
		for key in diction:
			house = get_data(key,diction[key])
			print '开始存储%s:' % key
			house.parse_data()
			



