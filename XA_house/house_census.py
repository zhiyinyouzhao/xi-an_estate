#!/usr/bin/env python
#-*-coding:utf-8-*-


import pandas as pd
import os
from house_data import store_data,get_data
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class data_census(object):
	def __init__(self,filepath):
		self.filepath = filepath
	def statistics_data(self,filename):
		li = []
		df = pd.read_csv(filename)
		house_type = df['类型'].value_counts()
		home = df[df['类型'].isin(['普通住宅'])]
		average = home['价格'].mean()
		li.append(house_type)
		li.append(average)
		return li
	#曲江楼市分析
	def qujiang(self):
		filename = self.filepath+'%s' % '/store/qujiang.csv'
		house = self.statistics_data(filename)
		print "曲江区域地产类型统计:\n%s" % house[0]
		print "曲江区域普通住宅平均价格:%s/元平米" % house[1]
	
	#高新楼市分析
	def gaoxin(self):
		filename = self.filepath+'%s' % '/store/gaoxin4.csv'
		house = self.statistics_data(filename)
		print "高新区域地产类型统计:\n%s" % house[0]
		print "高新区域普通住宅平均价格:%s/元平米" % house[1]
	#长安楼市分析
	def changan(self):
		filename = self.filepath+'%s' % '/store/changan1.csv'
		house = self.statistics_data(filename)
		print "长安区域地产类型统计:\n%s" % house[0]
		print "长安区域普通住宅平均价格:%s/元平米" % house[1]
	#城东楼市分析
	def chengdong(self):
		filename = self.filepath+'%s' % '/store/chengdong.csv'
		house = self.statistics_data(filename)
		print "城东区域地产类型统计:\n%s" % house[0]
		print "城东区域普通住宅平均价格:%s/元平米" % house[1]
	#城南楼市分析
	def chengnan(self):
		filename = self.filepath+'%s' % '/store/chengnan.csv'
		house = self.statistics_data(filename)
		print "城南区域地产类型统计:\n%s" % house[0]
		print "城南区域普通住宅平均价格:%s/元平米" % house[1]
	#城西楼市分析
	def chengxi(self):
		filename = self.filepath+'%s' % '/store/chengxi.csv'
		house = self.statistics_data(filename)
		print "城西区域地产类型统计:\n%s" % house[0]
		print "城西区域普通住宅平均价格:%s/元平米" % house[1]
	#城北楼市分析
	def chengbei(self):
		filename = self.filepath+'%s' % '/store/chengbei.csv'
		house = self.statistics_data(filename)
		print "城北区域地产类型统计:\n%s" % house[0]
		print "城北区域普通住宅平均价格:%s/元平米" % house[1]
	#经开楼市分析
	def jingkai(self):
		filename = self.filepath+'%s' % '/store/jingkai.csv'
		house = self.statistics_data(filename)
		print "经开区域地产类型统计:\n%s" % house[0]
		print "经开区域普通住宅平均价格:%s/元平米" % house[1]
	#浐灞楼市分析
	def chanba(self):
		filename = self.filepath+'%s' % '/store/chanba.csv'
		house = self.statistics_data(filename)
		print "浐灞区域地产类型统计:\n%s" % house[0]
		print "浐灞区域普通住宅平均价格:%s/元平米" % house[1]
	#西咸楼市分析
	def xixian(self):
		filename = self.filepath+'%s' % '/store/xixian.csv'
		house = self.statistics_data(filename)
		print "西咸区域地产类型统计:\n%s" % house[0]
		print "西咸区域普通住宅平均价格:%s/元平米" % house[1]
	#郊县楼市分析
	def jiaoxian(self):
		filename = self.filepath+'/store/'
		df1 = pd.read_csv(filename+'gaoling1.csv')
		df2 = pd.read_csv(filename+'huxian.csv')
		df3 = pd.read_csv(filename+'yanliang.csv')
		df4 = pd.read_csv(filename+'lintong.csv')
		frames = [df1,df2,df3,df4]
		df = pd.concat(frames,ignore_index=True)
		house = df['类型'].value_counts()
		home = df[df['类型'].isin(['普通住宅'])]
		average = home['价格'].mean()
		print "郊县区域地产类型统计:\n%s" % house
		print "郊县区域普通住宅平均价格:%s/元平米" % average
	
	#西安全城楼市分析
	def city(self):
		#合并数据
		filename = self.filepath+'/store/'
		df1 = pd.read_csv(filename+'qujiang.csv')
		df2 = pd.read_csv(filename+'gaoxin4.csv')
		df3 = pd.read_csv(filename+'changan1.csv')
		df4 = pd.read_csv(filename+'chengdong.csv')
		df5 = pd.read_csv(filename+'chengxi.csv')
		df6 = pd.read_csv(filename+'chengnan.csv')
		df7 = pd.read_csv(filename+'chengbei.csv')
		df8 = pd.read_csv(filename+'chanba.csv')
		df9 = pd.read_csv(filename+'jingkai.csv')
		df10 = pd.read_csv(filename+'xixian.csv')
		df11 = pd.read_csv(filename+'gaoling1.csv')
		df12 = pd.read_csv(filename+'lintong.csv')
		df13 = pd.read_csv(filename+'huxian.csv')
		df14 = pd.read_csv(filename+'yanliang.csv')
		frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14]
		total = pd.concat(frames,ignore_index=True)
		#全城楼盘数量分析
		print '西安市地产类型统计:\n%s' % total['类型'].value_counts()
		#计算全城楼盘普通住宅平均价格
		home = total[total['类型'].isin(['普通住宅'])]
		average = home['价格'].mean()
		print '西安市普通住宅平均价格:%s元/平米' % average
		#统计全城最贵的十大普通住宅楼盘和最便宜的十大楼盘
		home_price = home.sort_values(by = '价格')
		print '西安市普通住宅价格排行:'
		print home_price
		#统计全城最贵十大别墅价格
		villa = total[total['类型'].isin(['别墅'])]
		villa_price = villa.sort_values(by = '价格')
		print '西安市别墅价格排行:'
		print villa_price
		#将数据汇总写入csv
		total.to_csv('loupan.csv',index = False,encoding='utf-8-sig')
if __name__ == '__main__':
	get = store_data();
	get.data()
	d = data_census(os.path.dirname(os.path.abspath(__file__)))
	d.city()
	d.qujiang()
	d.gaoxin()
	d.changan()
	d.chanba()
	d.chengdong()
	d.chengxi()
	d.chengnan()
	d.chengbei()
	d.jingkai()
	d.xixian()
	d.jiaoxian()

