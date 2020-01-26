
import httpx
import argparse
import threading
from logzero import logger

def main():

    parser = argparse.ArgumentParser(description='app demo')
    parser.add_argument(
        '--thread-count',
        help="thread-count.")

    args = parser.parse_args()
    thread_count = int(args.thread_count)
    logger.info("############### Thread Count {0}  ###############".format(thread_count))


    for i in range(thread_count):
        t = threading.Thread(target=post_requests, args=(str(i)))
        t.start()


def post_requests(thread_name):
    logger.info("############### APP {0} START ###############".format(thread_name))
    r = httpx.get('https://www.example.org/')
    logger.info('请求状态码:{0}'.format(r.status_code))
    # print(r.text)
    logger.info("############### APP {0} END ###############")


