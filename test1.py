# coding=utf-8
import urllib2
import bs4
import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)
cur = conn.cursor()

conn.select_db('python_crawl')

values = []

count = 0

for i in range(60000, 100000):

    url = "http://interface.bilibili.com/player?id=cid:1&aid=" + str(i)

    rsp = urllib2.urlopen(url)
    result = rsp.read()
    soup = bs4.BeautifulSoup(
        result,
        'html.parser',
        from_encoding='utf8'
    )

    if soup.find('aid') is not None:

        aid = int(soup.find('aid').get_text())
        vtype = int(soup.find('vtype').get_text() or '0')
        credits_ = int(soup.find('credits').get_text() or '0')
        favourites = int(soup.find('favourites').get_text() or '0')
        coins = int(soup.find('coins').get_text() or '0')
        danmu = int(soup.find('danmu').get_text() or '0')
        typeid = int(soup.find('typeid').get_text() or '0')
        click = int(soup.find('click').get_text() or '0')

        values.append((aid, vtype, credits_, favourites, coins, danmu, typeid, click))

    print "正在爬取AV号为" + str(i) + "的数据"

    if count > 100:
        cur.executemany('insert into bili_v_info values(%s, %s, %s, %s, %s, %s, %s, %s)', values)
        conn.commit()
        values = []
        count = 0
    count += 1

cur.close()
conn.close()

exit(0)
