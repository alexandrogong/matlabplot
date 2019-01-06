import tushare as ts
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import pandas as pd

# 返回值说明：
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

if __name__ == '__main__':
    # 提供中文字符支持
    pl.rcParams['font.sans-serif'] = ['SimHei']

    # 获取中国平安每日成交信息
    data = ts.get_hist_data('601318', start='2018-01-01', end='2019-03-27')

    open = data['open']
    high = data['high']
    close = data['close']
    low = data['low']
    volume = data['volume']
    price_change = data['price_change']
    p_change = data['p_change']
    ma5 = data['ma5']
    ma10 = data['ma10']
    ma20 = data['ma20']
    v_ma5 = data['v_ma5']
    v_ma10 = data['v_ma10']
    v_ma20 = data['v_ma20']

    # 分析中国平安每日成交相关性
    plt.figure(figsize=[10, 6])
    plt.scatter(v_ma10, p_change)
    plt.show()



