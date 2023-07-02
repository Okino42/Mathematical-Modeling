# ！/usr/bin/nev python
# -*-coding:utf8-*-
from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA

dfs = pd.read_excel(r"F:\code\2022new_show\年：降水量 温度 湿度.xlsx")[["年份", "年平均湿度"]]
dfs['年份'] = pd.to_datetime(dfs['年份'])
dfs = dfs.set_index(["年份"])
print('dfs=',dfs)
decomposition = sm.tsa.seasonal_decompose(dfs, model='additive')
plt.rc('figure')
fig = decomposition.plot()
plt.show()