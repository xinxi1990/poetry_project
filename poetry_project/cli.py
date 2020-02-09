# -*- coding: utf-8 -*-

import os
import httpx
import argparse
import threading
import time
from datetime import datetime
import asyncio
from aiohttp import ClientSession
from aiohttp import FormData
import aiohttp
import numpy as np
from logzero import logger


sample_count = 0


def main():

    parser = argparse.ArgumentParser(description='app demo')
    parser.add_argument(
        '--thread-count',
        help="thread-count.")
    parser.add_argument(
        '--load-time',
        help="thread-count.")
    parser.add_argument(
        '--load-url',
        help="load-url.")

    args = parser.parse_args()
    thread_count = int(args.thread_count)
    load_time = int(args.load_time)
    load_url = str(args.load_url)
    logger.info("############### 当前线程数 {0}  ###############".format(thread_count))
    tools_start_time = time.time()
    # for i in range(thread_count):
    #     t = threading.Thread(target=post_requests, args=(str(i)))
    #     t.start()

    loop = asyncio.get_event_loop()
    run(thread_count,load_time,load_url,loop)
    loop.run_until_complete(asyncio.wait(tasks))

    logger.info("############### 程序耗时 {0}  ###############".format(round(time.time() - tools_start_time)))





def post_requests(thread_name):
    """

    :param thread_name:
    :return:
    """
    logger.info("############### APP {0} START ###############".format(thread_name))
    r = httpx.get('https://www.example.org/')
    logger.info('请求状态码:{0}'.format(r.status_code))
    # print(r.text)
    logger.info("############### APP {0} END ###############".format(thread_name))




############################
# 多链接异步访问

tasks = []
async def async_request(url):
    start_time = time.time()
    conn = aiohttp.TCPConnector(verify_ssl=False)  # 防止ssl报错
    async with ClientSession(connector=conn) as session:
        async with session.get(url) as response:
            respons = await response.read()
            end_time = time.time()
            cost = round(end_time - start_time,3)
            status = response.status
            global sample_count
            sample_count +=1
            logger.info("############### 请求接口 {0} 发生时间 {1} ###############".format(url,time.time()))
            return respons,status,cost



def run(thread_count,load_time,url,loop):

    expr_time = time.time() + load_time
    logger.info("############### 预计结束时间 {}  ###############".format(expr_time))
    is_running = True

    while is_running:
        for i in range(thread_count):
            task = asyncio.ensure_future(async_request(url))
            tasks.append(task)
        result = loop.run_until_complete(asyncio.gather(*tasks))
        reps_time = [ i[2] for i in result ]
        end_time = time.time()

        if end_time > expr_time:
            is_running = False
            logger.info("############### 结束本次测试 ###############")

    a = np.array((reps_time))
    time_avg = np.median(a)  # 中位数
    tim_95 = np.percentile(a, 95)  # 95%分位数
    tim_99 = np.percentile(a, 99)  # 95%分位数

    message = '\n' +'平均线耗时: {}'.format(round(time_avg,3)) + \
              '\n' + '95线耗时: {}'.format(round(tim_95,3)) + \
              '\n' + '99线耗时: {} '.format(round(tim_99,3)) + \
              '\n' + '总请求数: {} '.format(sample_count)

    logger.info("############### 接口耗时  ###############" + message)


