#
#! -*- coding:utf-8 -*-
import datetime
import re
import time
import urllib.request

import pymysql
from lxml import etree

from selenium import webdriver

#








def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Bootstrap',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into best_website (title,link,pics) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    for item in range(1,2):
        url = 'http://www.youzhan.org/page/'+str(item)+'/'
        driver = webdriver.Chrome()

        driver.get(url)
        html = driver.page_source
        big_list = []
        selector = etree.HTML(html)
        title = selector.xpath('//*[@id="post-list"]/div/article/h2/a/text()')
        link = selector.xpath('//*[@id="post-list"]/div/article/h2/a/@href')
        pics = selector.xpath('//*[@id="post-list"]/div/article/div/a/img/@src')
        for i1, i2, i3 in zip(title, link, pics):

         # 下载2-89页的解析
            big_list.append((i1, i2, i3[:-3]))

        # for i1, i2, i3 in zip(title, link, pics):
        #
        #  # 下载首页的解析
        #     big_list.append((i1, 'http://www.youzhan.org'+i2, i3[:-3]))
        insertDB(big_list)
        driver.quit()
        print(url)


#
#

# #
# #
# create table best_website(
# id int not null primary key auto_increment,
# title varchar(30),
# link varchar(88),
#  pics varchar(88)
# ) engine=InnoDB  charset=utf8;
#
#
# # drop  table best_website;