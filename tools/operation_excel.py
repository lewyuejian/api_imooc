#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: operation_excel.py
@time: 2019/12/19 16:54
@desc:
'''
import xlrd
from xlutils.copy import copy
class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        # 如果file_name存在
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
            self.data = self.get_data()
        else:
            self.file_name = '../dataconfig/indence.xlsx'
            self.sheet_id = 0
            self.data = self.get_data()

    def get_data(self):
        """
        获取sheets的内容
        :return:
        """
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """
        获取单元格的行数
        :return:
        """
        tables = self.data
        return tables.nrows

    def get_cell_value(self,row,col):
        """
        获取某一个单元格的内容
        :param row: 行
        :param col: 列
        :return:
        """
        return self.data.cell_value(row,col)

    def write_value(self,row,col,value):
        """
        将数据写入excel
        :param row:
        :param col:
        :param value:
        :return:
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    # 根据对应的caseId找到对应行的内容
    def get_rows_data(self,case_id):
        pass


    # 根据对应的caseId找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.get_clos_data()
        for cols_data in clols_data:
            if case_id in cols_data:
                return num
            num = num + 1

    # 根据行号，找到该行的内容
    def get_row_value(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_clos_data(self,col_id=None):
        if col_id != None:
           cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_cell_value(1,3))
