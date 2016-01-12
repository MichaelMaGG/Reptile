# -*- coding:utf-8 -*-

'''
Created on 2016��1��12��

@author: michaelGG
'''

import urllib2

url = "http://www.baidu.com/"

response1 = urllib2.urlopen(url)

print response1.getcode()

print len(response1.read())
