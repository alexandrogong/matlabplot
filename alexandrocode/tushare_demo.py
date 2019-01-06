import tushare as ts
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import pandas as pd

# 返回值说明：
# get_hist_data
# date：日期
# open：开盘价
# high：最高价
# close：收盘价
# low：最低价
# volume：成交量
# price_change：价格变动
# p_change：涨跌幅
# ma5：5日均价
# ma10：10日均价
# ma20:20日均价
# v_ma5:5日均量
# v_ma10:10日均量
# v_ma20:20日均量
# turnover:换手率[注：指数无此项]

# get_today_all
# code：代码
# name:名称
# changepercent:涨跌幅
# trade:现价
# open:开盘价
# high:最高价
# low:最低价
# settlement:昨日收盘价
# volume:成交量
# turnoverratio:换手率
# amount:成交量
# per:市盈率
# pb:市净率
# mktcap:总市值
# nmc:流通市值

if __name__ == '__main__':
    # 提供中文字符支持
    pl.rcParams['font.sans-serif'] = ['SimHei']

    # 显示所有列
    pd.set_option('display.max_columns', None)

    # =====获取中国平安一个时间段的历史信息=====
    # data = ts.get_hist_data('601318', start='2018-01-01', end='2019-03-27')
    #
    # open = data['open']
    # high = data['high']
    # close = data['close']
    # low = data['low']
    # volume = data['volume']
    # price_change = data['price_change']
    # p_change = data['p_change']
    # ma5 = data['ma5']
    # ma10 = data['ma10']
    # ma20 = data['ma20']
    # v_ma5 = data['v_ma5']
    # v_ma10 = data['v_ma10']
    # v_ma20 = data['v_ma20']
    #
    # '''分析中国平安每日成交相关性'''
    # plt.figure(figsize=[10, 6])
    # plt.scatter(v_ma10, p_change)
    # plt.show()

    # =====获取实时行情数据=====
    filename = '实时行情数据'
    filename = filename + '.csv'
    data = ts.get_today_all()

    data.to_csv(filename)

    with open(filename, 'w') as f:
        f.write(data)

    per = data['per']
    trade = data['trade']

    plt.figure(figsize=[8, 6])
    plt.plot(per, trade)
    plt.show()





