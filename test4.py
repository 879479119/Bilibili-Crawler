# coding=utf-8
from urllib2 import urlopen, HTTPError, URLError
import json
from bs4 import BeautifulSoup
import re

# 定义爬虫类


class Crawler:

    def __init__(self):
        # 存储数据的数组,每次取出数据后要清空避免内存堆积
        self.__store_video = []
        self.__store_author = []

    def run(self, start=6136078, end=6136090):
        self.__crawl(start, end)

    # 预定义正则表达式
    __reg_uid = re.compile(r'com/\d+')
    __reg_uname = re.compile(r'alt=\".+?\"')
    __reg_face = re.compile(r'src=\".+?\"')

    # 筛选有关于UP主的数据
    @staticmethod
    def __up_filter(self, soup, request_type='video'):
        # () => list

        if soup.find(name='h1', class_='video-title') is None:
            return {}

        title = soup.find(name='h1', class_='video-title').get_text()
        desc = soup.find(name='div', class_='video-desc').get_text()
        pic = soup.find(name='img', id='share_pic').attrs['src'][:-12]

        up = soup.find(name='div', class_='up-pic')
        # 通过正则表达式解析出UP主的信息

        up = str(up)

        [uid, uname, uface] = [None, None, None]

        try:
            uid = self.__reg_uid.search(up).group()[4:]
            uname = self.__reg_uname.search(up).group()[5:-1]
            uface = self.__reg_face.search(up).group()[5:-1]
        except Exception, e:
            print e

        if request_type is 'all':
            return [title, desc, pic, uid, uname, uface]
        elif request_type is 'video':
            return [title, desc, pic]
        elif request_type is 'author':
            return [uid, uname, uface]
        else:
            return []

    # 取出数据并删除原数据
    def output(self, request_type='video'):

        if request_type is 'video':
            result = self.__store_video
        elif request_type is 'author':
            result = self.__store_author
        else:
            result = []
        self.__store_author = []
        self.__store_video = []

        return result

    # 爬虫主要方法，爬取两个URL的数据
    def __crawl(self, startaid, endaid):

        for aid in range(startaid, endaid):
            # 首先获取视频基本信息（当前排名，收藏数，分享次数，弹幕数量，reply？，硬币，历史最高排名，点击次数
            #                    now_rank,favorite,share,danmaku, reply, coin,  his_rank,   view

            url = "http://api.bilibili.com/archive_stat/stat?aid=%d&type=jsonp" % aid
            data = None
            try:
                rsp = urlopen(url)
                json_str = json.loads(rsp.read())
                if json_str is not None:
                    data = json_str['data']

            except HTTPError, e:
                print e
            except URLError, e:
                print e

            # 从手机端的页面中抓取视频的其他信息（视频title，视频描述，视频封面，UP主ID，UP主昵称，头像链接
            #                                 title  ,  desc  ,   pic  , uid  , uname  , uface
            mobile_url = "http://www.bilibili.com/mobile/video/av%d.html" % aid
            try:
                m_rsp = urlopen(mobile_url)
                soup = BeautifulSoup(
                    m_rsp.read(),
                    'html.parser',
                    from_encoding='utf8'
                )

                result = tuple(self.__up_filter(self, soup, 'video'))
                if result is ():
                    result = ('', '', '')
                group = []
                # 转换为元组，方便存入数据库
                if data is None:
                    self.__store_video.append((aid,) + (0,)*11)
                    self.__store_author.append(())
                else:
                    for a in data:
                        group.append(data[a])
                    group = tuple(group)

                    b = (aid,) + group + result
                    # b = (aid,) + group + ('', '', '')
                    # 存入视频组
                    self.__store_video.append(b)
                    # 存入UP主组
                    self.__store_author.append(self.__up_filter(self, soup, 'author'))

            except HTTPError, e:
                pass
            except URLError, e:
                pass

if __name__ == '__main__':
    crawler = Crawler()
    crawler.run(6136078, 6136080)
    result_ = crawler.output('author')

    for att in result_:
        for k in att:
            print k

    print crawler.output('author')

    exit(0)
