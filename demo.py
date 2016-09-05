import re
import urllib2
import time
# import urllib
# url = "http://bilibili-service.daoapp.io/search"
# data = {
#     "content": "re",
#     "page": 1,
#     "count": 10
# }
#
# data = urllib.urlencode(data)
# req = urllib2.Request(url, data)
# try:
#     rsp = urllib2.urlopen(req)
#     print rsp.read()
# except urllib2.HTTPError, e:
#     print e.code
# except urllib2.URLError, e:
#     print e.reason
#
#
# exit(0)

start = 1000
end = 2000

for i in range(start, end):
    url = 'http://interface.bilibili.com/player?id=cid:1&aid='+str(i)

    rsp = urllib2.urlopen(url)

    result = rsp.read()

    reg = re.compile(r'<coins>.+?<')

    arr = reg.findall(result)

    for k in arr:
        print i
        print k+"\n"

exit(0)
