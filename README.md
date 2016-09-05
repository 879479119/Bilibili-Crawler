# Bilibili-Crawler
---

> 多线程Bilibili数据爬虫，目前仅支持将数据存储到本地MySQL数据库，代码有冗余，在Windows环境下500KB/s网速+1.7GHz机器上八线程的爬取速度大概为一小时十万条

+ 使用前请自行安装好所需要的插件
+ 数据库连接设置在test6文件中，使用前请先配置好
+ 厄。。。没有做自动建表的配置，请先按照以下命令建好表
```
CREATE TABLE `t_video_info` (
  `aid` int(10) NOT NULL,
  `now_rank` int(10) unsigned zerofill DEFAULT NULL,
  `favorite` int(10) unsigned zerofill DEFAULT NULL,
  `share` int(10) unsigned zerofill DEFAULT NULL,
  `danmaku` int(10) unsigned zerofill DEFAULT NULL,
  `reply` int(10) unsigned zerofill DEFAULT NULL,
  `coin` int(10) unsigned zerofill DEFAULT NULL,
  `his_rank` int(10) unsigned zerofill DEFAULT NULL,
  `view` int(10) unsigned zerofill DEFAULT NULL,
  `title` char(64) CHARACTER SET utf8 DEFAULT NULL,
  `desc` text CHARACTER SET utf8,
  `pic` char(128) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```
+ 爬虫主程序在test5中，请务必运行test5的文件，有几个文件是自己写的垃圾代码
+ **注意：** 爬虫运行过程中可能出现MySQL连接失效的情况，请不要在意，他会接着爬的
