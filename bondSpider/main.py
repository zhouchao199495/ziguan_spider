from scrapy import cmdline
import time
import sys


def do_task():
    print("Spiders wake up!")
    # cmdline.execute("scrapy crawl eastmoney".split())
    cmdline.execute("scrapy crawl ifeng".split())
    print("spiders exit!")


def start_timed_task():
    # 开始时，立即执行一次
    do_task()

    print("定时任务，8点~9点开始执行")
    while True:
        localtime = time.strftime("%H:00", time.localtime())
        if localtime == "08:00":
            do_task()
            print("It's 8:00 o'clock! let's start task!")
        time.sleep(10 * 60)


if __name__ == '__main__':
    start_timed_task()
    # localtime = time.strftime("%Y%M%d")
    # month = time.strftime("%Y%M00")
    # today = int(localtime) - int(month)
    # for i in range(today, 0, -1):
    #     print(str(int(month)+i))
    # cmdline.execute("scrapy crawl ifeng".split())
    # cmdline.execute("scrapy crawl eastmoney".split())
    # print("11111")
    # t = NewsStorageThread()
    # t.start()
    # t.join(1000)
    # print("66666")
