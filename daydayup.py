# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 19:04:24 2018

@author: Administrator
"""

n=eval(input());
print("你的输入为千分之{}。".format(n));
daydayup=(n/1000+1)**365;
daydaydown=(1-n/1000)**365;
print("天天向上结果为：{:.2f}。".format(daydayup));
print("天天放任结果为：{:.2f}。".format(daydaydown));