# -*- coding: utf-8 -*-
import urllib2
import json
import MySQLdb as mysql

#主函数
def main():
    conn = mysql.connect('localhost', 'root', 'root', 'touzi') #数据库连接

    #获取5分钟数据
    data = pull("http://api.huobi.com/staticmarket/ltc_kline_005_json.js")
    save(data, conn, 'data_ltc_min5')
    #获取15分钟数据
    data = pull("http://api.huobi.com/staticmarket/ltc_kline_015_json.js")
    save(data, conn, 'data_ltc_min15')
    #获取30分钟数据
    data = pull("http://api.huobi.com/staticmarket/ltc_kline_030_json.js")
    save(data, conn, 'data_ltc_min30')
    #获取小时数据
    data = pull("http://api.huobi.com/staticmarket/ltc_kline_060_json.js")
    save(data, conn, 'data_ltc_hour')
    #获取日线数据
    data = pull("http://api.huobi.com/staticmarket/ltc_kline_100_json.js")
    save(data, conn, 'data_ltc_day')
    #获取周线数据
    data = pull("http://api.huobi.com/staticmarket/ltc_kline_200_json.js")
    save(data, conn, 'data_ltc_week')
    #获取月线数据
    data = pull("http://api.huobi.com/staticmarket/ltc_kline_300_json.js")
    save(data, conn, 'data_ltc_month')

    conn.close()


# 从接口获取数据, 返回获取到的数据字符串
def pull(url):
    reqest = urllib2.Request(url)
    response = urllib2.urlopen(reqest)
    responseData = response.read()
    data = json.loads(responseData) #解析json字符串
    return data

#把行情数据存入数据库
def save(data, conn, tableName):
    cursor = conn.cursor()
    for item in data:
        time = item[0]
        open = item[1]
        high = item[2]
        low = item[3]
        close = item[4]
        amount = item[5]
        sql = "replace into %s (time,open,low,high,close,amount) values('%s',%f,%f,%f,%f,%f)" \
              % (tableName,time,open,low,high,close,amount)
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    newCount = getRecordCount(conn, tableName) #查询记录数
    print('保存 %s : %d 条记录, 当前总共 %d 条记录' % (tableName, len(data), newCount))

def getRecordCount(conn, tableName):
    cursor = conn.cursor()
    sql = "select count(*) from " + tableName
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    cursor.close()
    return result

main()
