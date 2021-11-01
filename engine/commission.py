# -*- coding: utf-8 -*-

"""
Commission 佣金+费税模型
New in V0.3.4

@author: Leon Zhang
@version: 0.4
"""

from abc import ABCMeta, abstractmethod
import math

print("py38_site_packages/commission.py")
class Commission(object):
    print("commission.py - Commission")
    """
    佣金和费税
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_commission(self):
        print("commission.py - Commission - get_commission")
        raise NotImplementedError("Should implement get_commission()!")


class ZeroCommission(Commission):
    print("commission.py - ZeroCommission")
    """
    无费率
    """
    def get_commission(self):
        print("commission.py - ZeroCommission - get_commission")
        return 0.0
    def __repr__(self):
        print("commission.py - ZeroCommission - __repr__")
        return "{class_name}".format(class_name=self.__class__.__name__)


class PerShareCommission(Commission):
    print("commission.py - PerShareCommission")
    """
    基于交易份额（或称数量）计算手续费，一般是上交所的过户费，每1000股收费1元
    """
    def __init__(self, rate=0.001, min_comm=0.0):
        print("commission.py - PerShareCommission - __init__")
        self.rate_per_share = rate
        self.min_comm = min_comm

    def get_commission(self, quantity):
        print("commission.py - PerShareCommission - get_commission")
        return max(math.ceil(quantity * self.rate_per_share), self.min_comm)

    def __repr__(self):
        print("commission.py - PerShareCommission - __repr__")
        return "{class_name}(rate_per_share={rate}, min_commission={min_comm})".format(
            class_name=self.__class__.__name__, rate=self.rate_per_share, min_comm=self.min_comm)


class PerMoneyCommission(Commission):
    print("commission.py - PerMoneyCommission")
    """
    基于交易花费（trade cost）计算手续费，可以是期货点数或者人民币，允许设置最小手续费
    """
    def __init__(self, rate=1.5e-4, min_comm=0.0):
        print("commission.py - PerMoneyCommission - __init__")
        """
        例如买焦合约共计10000点（单份合约*数量），默认费率万分1.5，则交易成本是1.5个点
        参数：
        rate: 单边费率
        min_comm: 最低手续费，默认为股票5元
        """
        self.rate_per_money = float(rate)
        self.min_comm = float(min_comm)

    def get_commission(self, full_cost):
        print("commission.py - PerMoneyCommission - get_commission")
        return max(full_cost * self.rate_per_money, self.min_comm)

    def __repr__(self):
        print("commission.py - PerMoneyCommission - __repr__")
        return "{class_name}(rate_per_money={rate}, min_commission={min_comm})".format(
            class_name=self.__class__.__name__, rate=self.rate_per_money, min_comm=self.min_comm)


class PerTradeCommission(Commission):
    print("commission.py - PerTradeCommission")
    """
    基于交易次数计算手续费
    """
    pass
