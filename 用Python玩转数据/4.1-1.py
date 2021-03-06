# coding:utf-8

"""
1.数据收集　２.数据整理　３.数据描述　4.数据分析

"""
from matplotlib.finance import quotes_historical_yahoo_ochl  # 注matplotlib包里已经没有了quotes_historical_yahoo方法了，改为quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd 

from nltk.corpus import gutenberg
import nltk

today = date.today()
start = (today.year - 1, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('AXP', start, today) #美国运通公司最近一年股票代码
df = pd.DataFrame(quotes)
print df

"""
安装一下NLTK 自然语言工具包
sudo pip install -U nltk

log: Successfully installed nltk-3.2.1

用pip安装成功后无法导入，改用sudo apt-get install python-nltk安装

使用nltk.download() 下载相关语料库
"""
# print gutenberg
# nltk.download()  

print gutenberg.fileids()