# coding=utf-8
import urllib2
import json

url = "http://www.bilibili.com/mobile/video/av6136078.html"

rsp = urllib2.urlopen(url)

print rsp.read()

exit(0)
