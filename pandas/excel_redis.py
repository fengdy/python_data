# coding: utf-8
import pandas as pd
import redis
import time
import MySQLdb


class DataStore(object):
    """
    read data using Pandas from excel and use mysql and redis as temporary place,
    and get Pandas dataFrame from mysql and redis,
    and as temporary store, redis is better
    """
    def __init__(self):
        self.df = pd.read_excel('sal.xls', skiprows=[0])
        self._redis()
        self._mysql()

    def _mysql(self):
        """
        use mysql store data of dataFrame
        :return:
        """
        b = time.time()
        conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='12345678', db='ehr-temporary', charset='utf8')
        self.df.to_sql('dat', conn,  if_exists='replace', flavor='mysql', index=False)
        ef = pd.read_sql('select * from dat', conn)
        print time.time() - b

    def _redis(self):
        """
        use redis store data of dataFrame
        :return:
        """
        a = time.time()
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        r.set('dat',self.df.to_msgpack(compress='zlib', encoding='utf8'))
        cf = pd.read_msgpack(r.get('dat'), encoding='utf8')
        print time.time() - a


if __name__ == '__main__':
    DataStore()