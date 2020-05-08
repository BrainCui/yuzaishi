#-*-coding:utf-8-*-
from pymongo import MongoClient
def sql_exxcute(self,sql):
    """
    :param self:
    :param sql:
    :return:
    """
    self._db_connect()
    last_id = -1
    try:
        if self.conn and self.cur:
            self.cur.execute(sql)
            self.conn.commit()
            last_id = self.cur.lastrowid
    except Exception as e:
        self.conn.rollback()
        raise Exception(e)
    finally:
        self._db_close()
    return last_id

def main():
    client = MongoClient()

    db = client.doc
    collection = db.news

    for item in sql_exxcute(collection.find_one()):
        print(item)
