# -*- coding: utf-8 -*-
import MySQLdb


class Connection_factory(object):
    @staticmethod
    def get_connection():
        return MySQLdb.connect(host="localhost",
                               user='root',
                               passwd='',
                               db='rafael')
