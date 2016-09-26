# coding: utf-8
import pandas as pd
from openpyxl import load_workbook


class Data(object):
    """
    将dataFrame数据写入已有的excel中，参考：
    http://stackoverflow.com/questions/20219254/how-to-write-to-an-existing-excel-file-without-overwriting-data-using-pandas
    优点：可将dataFrame直接写入excel中
    缺点：openpyxl不支持 2003 excel
    """
    def __init__(self):
        self.df = pd.read_excel('sal.xls', skiprows=[0], converters={u'证件号码': str})
        self.book = load_workbook('result.xlsx')
        self.writer = pd.ExcelWriter('result.xlsx', engine='openpyxl')
        self.writer.book = self.book
        self.writer.sheets = dict((ws.title, ws) for ws in self.book.worksheets)

        self.df.to_excel(self.writer, u'工资表', header=None, index=False, startrow=2)
        self.writer.save()


if __name__ == '__main__':
    Data()