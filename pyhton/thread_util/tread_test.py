#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 13:32
# @Author  : Zheng guoliang
# @Version : 1.0
# @File    : {NAME}.py
# @Software: PyCharm
"""
1.需求功能：
  顺序执行单线程与同时执行两个线程多个并发线程所用的时间差不多。
  并没有节省一定的时间。

2.实现过程：


"""

from threading import Thread
import time


def my_conter():
    i = 0
    for _ in range(100000000):
        i += 1
    return True


def single_thread():
    thread_array = {}
    start_time = time.time()
    for tid in range(4):
        t = Thread(target=my_conter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time:{}".format(end_time - start_time))
    # Total time:16.183770656585693


def double_thread():
    thread_array = {}
    start_time = time.time()
    for tid in range(4):
        t = Thread(target=my_conter)
        t.start()
        thread_array[tid] = t
    for i in range(4):
        thread_array[i].join()
    end_time = time.time()
    print("Total time:{}".format(end_time - start_time))
    # Total time:16.417961835861206


if __name__ == '__main__':
    single_thread()
    double_thread()
