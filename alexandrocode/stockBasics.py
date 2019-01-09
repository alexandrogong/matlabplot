# -*- coding: utf-8 -*-
import tushare as ts
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import pandas as pd

if __name__ == "__main__":

    # 提供pyplot中文字符支持
    pl.rcParams['font.sans-serif'] = ['SimHei']

    # 显示所有列
    pd.set_option('expand_frame_repr', False)
    pd.set_option('display.max_columns', 100)

    # define file name & path
    filepath = "./StockDatas/"
    # filename = 'stockBasics'
    # filename = filepath + filename + ".csv"

    # # get basic data & save to csv file
    # flag = 0
    # if flag:
    #     data = ts.get_stock_basics()
    #     df = pd.DataFrame(data)
    #     '''支持中文格式写入csv'''
    #     df.to_csv(filename, encoding="utf_8_sig")
    # else:
    #     '''csv里面包含中文字符，使用read_csv会报错，需要先转码'''
    #     f = open(filename, encoding="utf_8_sig")
    #     data = pd.read_csv(f)

    # # 获取三年内年度和季度业绩报告
    # flag = 1
    # years = [2016, 2017, 2018]
    # quarters = [1, 2, 3, 4]
    # if flag:
    #     for year in years:
    #         for quarter in quarters:
    #             filename = filepath + '业绩报告' + str(year) + "年" + str(quarter) + '季度' + ".csv"
    #             data = ts.get_report_data(year, quarter)
    #             df = pd.DataFrame(data)
    #             '''支持中文格式写入csv'''
    #             df.to_csv(filename, encoding="utf_8_sig")
    # else:
    #     '''csv里面包含中文字符，使用read_csv会报错，需要先转码'''
    #     # f = open(filename, encoding="utf_8_sig")
    #     # data = pd.read_csv(f)

    # # 获取三年内年度和季度盈利能力
    # flag = 1
    # years = [2016, 2017, 2018]
    # quarters = [1, 2, 3, 4]
    # if flag:
    #     for year in years:
    #         for quarter in quarters:
    #             filename = filepath + '盈利能力' + str(year) + "年" + str(quarter) + '季度' + ".csv"
    #             data = ts.get_profit_data(year, quarter)
    #             df = pd.DataFrame(data)
    #             '''支持中文格式写入csv'''
    #             df.to_csv(filename, encoding="utf_8_sig")
    # else:
    #     '''csv里面包含中文字符，使用read_csv会报错，需要先转码'''
    #     # f = open(filename, encoding="utf_8_sig")
    #     # data = pd.read_csv(f)

    # # 获取三年内年度和季度成长能力
    # flag = 1
    # years = [2016, 2017, 2018]
    # quarters = [1, 2, 3, 4]
    # if flag:
    #     for year in years:
    #         for quarter in quarters:
    #             filename = filepath + '成长能力' + str(year) + "年" + str(quarter) + '季度' + ".csv"
    #             data = ts.get_growth_data(year, quarter)
    #             df = pd.DataFrame(data)
    #             '''支持中文格式写入csv'''
    #             df.to_csv(filename, encoding="utf_8_sig")
    # else:
    #     '''csv里面包含中文字符，使用read_csv会报错，需要先转码'''
    #     # f = open(filename, encoding="utf_8_sig")
    #     # data = pd.read_csv(f)

    # 获取三年内年度和季度现金流量
    # flag = 1
    # years = [2016, 2017, 2018]
    # quarters = [1, 2, 3, 4]
    # if flag:
    #     for year in years:
    #         for quarter in quarters:
    #             filename = filepath + '现金流量' + str(year) + "年" + str(quarter) + '季度' + ".csv"
    #             data = ts.get_cashflow_data(year, quarter)
    #             df = pd.DataFrame(data)
    #             '''支持中文格式写入csv'''
    #             df.to_csv(filename, encoding="utf_8_sig")
    # else:
    #     '''csv里面包含中文字符，使用read_csv会报错，需要先转码'''
    #     # f = open(filename, encoding="utf_8_sig")
    #     # data = pd.read_csv(f)

    # # 获取三年内年度和季度偿债能力
    # flag = 1
    # years = [2016, 2017, 2018]
    # quarters = [1, 2, 3, 4]
    # if flag:
    #     for year in years:
    #         for quarter in quarters:
    #             filename = filepath + '偿债能力' + str(year) + "年" + str(quarter) + '季度' + ".csv"
    #             data = ts.get_debtpaying_data(year, quarter)
    #             df = pd.DataFrame(data)
    #             '''支持中文格式写入csv'''
    #             df.to_csv(filename, encoding="utf_8_sig")
    # else:
    #     '''csv里面包含中文字符，使用read_csv会报错，需要先转码'''
    #     # f = open(filename, encoding="utf_8_sig")
    #     # data = pd.read_csv(f)

    # 获取三年内年度和季度运营能力
    flag = 1
    years = [2016, 2017, 2018]
    quarters = [1, 2, 3, 4]
    if flag:
        for year in years:
            for quarter in quarters:
                filename = filepath + '运营能力' + str(year) + "年" + str(quarter) + '季度' + ".csv"
                data = ts.get_operation_data(year, quarter)
                df = pd.DataFrame(data)
                '''支持中文格式写入csv'''
                df.to_csv(filename, encoding="utf_8_sig")
    else:
        '''csv里面包含中文字符，使用read_csv会报错，需要先转码'''
        # f = open(filename, encoding="utf_8_sig")
        # data = pd.read_csv(f)








