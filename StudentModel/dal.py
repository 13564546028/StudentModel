"""
    数据访问层 由bll的方法调用
    1 保存学生列表
    2 加载学生列表
"""

from models import StudentModel
import os

# 常量 : 不允许修改的数值
FILE_PATH = "list_stu.txt"
class TexDao:
    """
        文本文件 数据访问对象
    """
    @staticmethod
    def save_student_list(list_stu):
        with open(FILE_PATH,"w",encoding="utf-8") as stu_file:
            for stu in list_stu:
                stu_file.write(stu.__repr__()+"\n")
    @staticmethod
    def load_student_list():
        list_stu = []
        if not os.path.isfile(FILE_PATH ):
            return list_stu
        with open(FILE_PATH,"r",encoding="utf-8") as stu_file:
            for line in stu_file:
                list_stu.append(eval(line))
        return list_stu


# list_stu = [
#     StudentModel(1,"zs",12,13),
#     StudentModel(2,"ls",18,14)
# ]
#
# TexDao.save_student_list(list_stu)
# #
# for item in TexDao.load_student_list():
#     print(item)
#





