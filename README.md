**关于我：**  
Life is short,I use Python!  
Author：zhiyinyouzhao  
Email：5251870@qq.com  
Date：April 17,2017  
**项目说明：**  
该项目主要分析了西安房地产市场，数据来源于链家网，数据更新截止于2017年4月17日。  
安装说明：  
cd /opt  
git clone git@git@github.com:zhiyinyouzhao/xi-an_estate.git  
cd XA_house  
python house_census.py  
**结果分析：**  
分区域(例如曲江，高新等)采集数据，并清洗数据，最后存为csv文件。  
最后使用第三方工具完成数据可视化。  
1.西安市楼盘分布:  
![西安楼盘分布](https://github.com/zhiyinyouzhao/xi-an_estate/raw/master/result_images/xi-an_estate.jpg)  
很明显，普通住宅占比很大，高端别墅，商业欠发达，还有很大潜力可挖。  
2.西安市各区域楼盘分布:  
![西安楼盘上市数量统计](https://github.com/zhiyinyouzhao/xi-an_estate/raw/master/result_images/xi-an_region_estate.jpg)  
可以看出浐灞，城北，西郊方向土地充足，是目前的地产开发主要方向。高新和曲江的房产开发重点在商业楼盘。  
3.西安市普通住宅均价:  
![西安普通住宅均价](https://github.com/zhiyinyouzhao/xi-an_estate/raw/master/result_images/xi-an_home_average.jpg)  
各区域普通住宅均价基本反映了西安市各区域经济发展的差异，老百姓最终还是用脚投票了。  
4.西安市普通住宅Top10排行:  
![西安市普通住宅Top10](https://github.com/zhiyinyouzhao/xi-an_estate/raw/master/result_images/xi-an_home_Top10.jpg)  
中产小伙伴们可以去这瞅瞅，高端住宅曲江，高新，城北三雄鼎立。  
城北大明宫，凤城路沿线很强势，整体有盖过曲江，高新之势。    
5.西安市普通住宅Low10排行:  
![西安市普通住宅Low10](https://github.com/zhiyinyouzhao/xi-an_estate/raw/master/result_images/xi-an_home_Low10.jpg)  
看完贵的我们再来看看便宜的，压压惊。最便宜的大都在大北郊泾渭工业园一代。基本推测这地，房子比人多，存量太大。  
6.西安市别墅Top5排行:  
![西安市别墅Top5](https://github.com/zhiyinyouzhao/xi-an_estate/raw/master/result_images/xi-an_villa_Top5.jpg)  
最后的最后，我们来看看土豪们的选择。曲江，浐灞二分天下，曲江是老的富人区，浐灞新兴势力。  
要想房子卖得贵，最重要的是什么？是水，有水有money。  
**个人小结：**  
1.在采集数据时，受限于网络环境以及网站的防范机制，有时候爬的数据不全，所以要核实下，多运行几次程序，确定采集完全，方可进行后续分析。  
3.数据可视化工具使用第三方工具][ECharts](http://echarts.baidu.com/)和[Highcharts](https://www.hcharts.cn/)。  
4.store目录下是采集到的各个区域数据，loupan.csv是合并后的全市数据，result_images目录存放的是上传的分析图。  
5.写入和读取csv文件，中文乱码依旧是需要小心的地方。  
6.解析网页使用的是[BeautifulSoup](http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/),数据分析使用的是[Pandas](http://pandas.pydata.org/)。  
