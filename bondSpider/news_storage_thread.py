import threading
import copy
import time


class NewsStorageThread(threading.Thread):
    """新闻数据存储线程，将爬取的新闻存到数据库中"""
    lock = threading.Lock()
    items = []

    def run(self):
        while self.is_alive():
            if len(self.items) <= 0:
                time.sleep(1)
                continue

            curr_items = self.get()
            if len(curr_items) <= 0:
                time.sleep(1)
                continue

            print("NewsStorageThread Start!")
            self.storage(curr_items)

        print("NewsStorageThread quit!")

    @staticmethod
    def add(item):
        lock.acquire()
        self.items.append(item)
        self.lock.release()

    def get(self):
        self.lock.acquire()
        current_items = copy.deepcopy(self.items)
        self.items.clear()
        self.lock.release()

        return current_items

    def storage(self, items):
        for item in items:
            print(items + "do something!")

    @staticmethod
    def add_news(url, news_time, news_title, news_body):
        sql = "insert into tnews (VC_URL, VC_PUBLISH_DATE, VC_TITLE, CONTEXT) values ("
        sql += "'" + url + "',"
        sql += "'" + news_time + "',"
        sql += "'" + news_title + "',"
        sql += "'" + news_body + "')"
        # orcl = oracle_connect()
        # orcl.write(sql)
