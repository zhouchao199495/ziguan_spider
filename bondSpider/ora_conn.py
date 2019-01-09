import cx_Oracle


class OraConn(object):

    def __int__(self, conn_str):
        self.conn_str = conn_str
        self.db_conn = None

    def connect(self):
        if self.db_conn == None:
            self.db_conn = OraConn.connect(self.conn_str)

        if self.db_conn != None:
            return True
        else:
            return False

    def close(self):
        if self.db_conn:
            self.db_conn.close()
            self.db_conn = None

    def newcur(self):
        cur = self.db_conn.cursor()

        if cur:
            return cur
        else:
            print("#Error# Get New Cursor Failed.")
        return None

    def closecur(self, cur):
        if cur:
            cur.close()

    def commit(self):
        self.db_conn.commit()

    def rollback(self):
        self.db_conn.rollback()

    def select_sql(self, sql, cur):
        c = cur.execute(sql)
        result = c.fetchall()
        return result

    def exec_sql(self, sql, cur, parm_list=None):
        if parm_list:
            cur.prepare(sql)
            result = cur.executemany(None, parm_list)
        else:
            result = cur.execute(sql)
        return result
