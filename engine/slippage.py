# -*- coding: utf-8 -*-

"""
Slippage 滑点模型
New in V0.3.4

@author: Leon Zhang
@version: 0.4
"""
print("py38_site_packages/slippage.py")
from abc import ABCMeta, abstractmethod


class Slippage(object):
    print("slippage.py - Slippage")
    """
    滑点模型
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_trade_price(self):
        print("slippage.py - Slippage - get_trade_price")
        raise NotImplementedError("Should implement get_trade_price()!")


class ZeroSlippage(Slippage):
    print("slippage.py - ZeroSlippage")
    """
    无滑点
    """
    def get_trade_price(self, price):
        print("slippage.py - ZeroSlippage - get_trade_price")
        return price


class FixedPercentSlippage(Slippage):
    print("slippage.py - FixedPercentSlippage")
    """
    固定比率的滑点模型
    """
    def __init__(self, percent=0.1):
        print("slippage.py - FixedPercentSlippage - __init__")
        """
        参数
        rate: 滑点比率，如0.1，则买卖方向上各滑点0.1%
        """
        self.rate = percent / 100.0

    def get_trade_price(self, price, direction):
        print("slippage.py - FixedPercentSlippage - get_trade_price")
        slippage = price * self.rate * (1 if direction == "BUY" else -1)
        price = price + slippage

        return price


class VolumeShareSlippage(Slippage):
    print("slippage.py - VolumeShareSlippage")
    def get_trade_price(self, price, direction):
        print("slippage.py - VolumeShareSlippage - get_trade_price")
        pass