import MySQLdb
from time import sleep


class MySQLConnect:
    __conn = None
    __cur = None
    __num = 100000

    def __init__(self):
        self.__create()

    @classmethod
    def __clean(cls):
        cls.__cur.close()
        cls.__conn.close()
        cls.__cur = None
        cls.__conn = None

    @classmethod
    def __create(cls):
        cls.__conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)
        cls.__cur = cls.__conn.cursor()
        cls.__conn.select_db('python_crawl')
        cls.__conn.set_character_set('utf8')
        cls.__cur.execute('SET NAMES utf8;')
        cls.__cur.execute('SET CHARACTER SET utf8;')
        cls.__cur.execute('SET character_set_connection=utf8;')

    @classmethod
    def insert_video(cls, v):
        try:
            # print cls.__conn
            cls.__cur.executemany('INSERT INTO t_video_info VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', v)
            cls.__conn.commit()
        except MySQLdb.OperationalError, e:
            print e
            sleep(1)
            cls.__create()
            print '-'*80 + "SOMETHING WRONG"
            cls.insert_video(v)

    @classmethod
    def last_modified(cls):
        try:
            cls.__cur.execute('SELECT MAX(aid) FROM t_video_info')
        except MySQLdb.OperationalError, e:
            print '?? WRONG ??' + e.message

    def insert_author(self, values):
        self.__cur.excutemany('INSERT INTO t_author_info VALUES (%s, %s, %s, %s, %s)', values)
        self.__cur.commit()

    def clear_all(self):
        self.__cur.execute('DELETE FROM t_video_info')
        self.__cur.execute('DELETE FROM t_author_info')
        self.__cur.commit()
