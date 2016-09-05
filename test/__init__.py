import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)
    cur = conn.cursor()

    conn.select_db('python_crawl')

    value = ['hi rollen']
    cur.execute('insert into test (name) value(%s)', value)

    values = []
    for i in range(20):
        values.append(('hi rollen' + str(i)))

    cur.executemany('insert into test (name) value(%s)', values)

    conn.commit()
    cur.close()
    conn.close()

except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])