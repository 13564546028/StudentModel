"""
    学生管理系统表示层
"""
from bll import *
from models import *


class StudentManagerview:
    """
            学生管理系统视图类
    """
    def __init__(self):
        self.__controller = StudentManagerController()
    def __input__int(self,msg):
        while True:
            try:
                return  int(input(msg))
            except:
                print("输入有误")


    def __display_menu(self):
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("1)添加学生信息")
        print("2)显示学生信息")
        print("3)删除学生信息")
        print("4)修改学生信息")
        print("5)按照成绩降序排列学生")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    #做成私有属性 外部无法直接引用
    def __select_menu(self):
        number = input("请输入选项:")
        if number == "1":
           self.__input_students()
        elif number == "2":
            self.__output_students(self.__controller.list_stu)
        elif number == "3":
            self.__remove_student_data()
        elif number == "4":
            self.__update_student_data()
        elif number == "5":
            self.__order_by_score_data()
        else:
            print("请重新输入选项")
    def main(self):
        """
                学生管理器入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()
    def __input_students(self):
        while True:
            stu = StudentModel()
            stu.name = input("请输入学生姓名:")
            # stu.age = int(input("请输入学生年龄:"))
            # stu.score = int(input("请输入学生成绩:"))
            stu.age = self.__input__int("请输入学生年龄:")
            stu.score = self.__input__int("请输入学生成绩:")
            self.__controller.add_student(stu)
            if input("按y键继续") != "y":
                break

    def __output_students(self,list_stu):
        for item in list_stu:
            print("编号:%d|名字:%s|年龄:%d|成绩:%d" %(item.id,item.name,item.age,item.score))

    def __remove_student_data(self):
        # id = int(input("请输入需要删除的学生编号:"))
        id = self.__input__int("请输入学生编号:")
        result = self.__controller.remove_data(id)
        if result:
            print("删除成功")
        else:
            print("删除失败")

    def __update_student_data(self):
        stu_info = StudentModel()
        # stu_info.id = int(input("请输入需要修改的学生编号"))
        stu_info.id =self.__input__int("请输入学生编号:")
        stu_info.name = (input("请输入需要修改的学生姓名"))
        stu_info.age =self.__input__int("请输入学生年龄:")
        stu_info.score =self.__input__int("请输入学生成绩:")
        # stu_info.age = int(input("请输入需要修改的学生年龄"))
        # stu_info.score = int(input("请输入需要修改的学生成绩"))
        if self.__controller.update_student(stu_info):
            print("修改成功")
        else:
            print("修改失败")
    def __order_by_score_data(self):
        result = self.__controller.order_by_score()
        self.__output_students(result)











