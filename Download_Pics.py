



#! -*- coding:utf-8 -*-

import re

import pymysql
import requests
import urllib.request








def get_one_page(url):
    req= requests.get(url)
      #  requests 中文编码的终极办法！
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding

        # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        global encode_content
        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
        return  (encode_content)








if __name__ == "__main__":
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Bootstrap',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,889):
        sql = 'select * from best_website where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        pics_link = data['pics']
        name = data['title']
        try:
            urllib.request.urlretrieve(pics_link, '/home/r/Bootstrap_website_pics/%s' % name)
        except :
            print('图片下载有问题')
        print(pics_link)

