# -*- coding: utf-8 -*-
import cx_Oracle
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BondspiderPipeline(object):
    user = "ziguan"
    password = "ziguan"
    server = "56.222"

    def process_item(self, item, spider):
        self.insert_to_db(item)
        return item

    def insert_to_db(self, item):
        if self.exist(item["url"]):
            print("url:" + item["url"] + "已存在！")
            return

        db_conn = cx_Oracle.connect(self.user, self.password, self.server)
        cursor = db_conn.cursor()

        # 若未抓取，则写入数据库
        context = item["news_context"]
        clob_data = cursor.var(cx_Oracle.CLOB)
        clob_data.setvalue(0, context)

        sql = "insert into tnews (VC_URL, VC_PUBLISH_DATE, VC_TITLE, CONTEXT, C_NLP_FLAG) values ("
        sql += "'" + item["url"] + "',"
        sql += "'" + item["publish_date"] + "',"
        sql += "'" + item["title"] + "',"
        sql += ":1,"
        sql += "'0')"
        print(sql)
        cursor.prepare(sql)

        cursor.execute(None, {'1': context})
        db_conn.commit()
        db_conn.close()

    def exist(self, url):
        db_conn = cx_Oracle.connect(self.user, self.password, self.server)
        cursor = db_conn.cursor()

        # 查询url是否已经被抓取过
        sql = "select * from tnews where vc_url ='" + url + "'"
        cursor.execute(sql)
        result = cursor.fetchall()
        ret = len(result)
        db_conn.close()

        return 0 != ret
