# coding=utf-8
from typing import List


class Grade:
    def __init__(self, course: str, credit: int, grade: float) -> None:
        """
        初始化四个成员变量：course, credit, grade, gpa，其中gpa需要计算
        输入: 课程名course, 学分credit, 成绩grade
        输出：无
        TODO: 初始化成员变量course, credit, grade, gpa(需要计算)
        """

        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.course =
        self.credit =
        self.grade =
        # gpa = 4-3*（100-grade）^2／1600
        self.gpa =
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def __str__(self) -> str:
        return "%-8s\t%-2d\t%-5.1f\t%-0.2f" % (self.course, self.credit, self.grade, self.gpa)


class GPACalculator:
    def __init__(self):
        self.grades: List[Grade] = []
        self.gpa: float = 0.0

    def get_gpa(self) -> float:
        """
        计算总GPA(加权平均)
        输入：无
        输出：总GPA
        TODO: 计算self.grades中所有课程的总GPA
        """

        gpa = 0.0
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.gpa = gpa
        return self.gpa

    def add_grades(self, grades: List[Grade]) -> float:
        """
        添加成绩并计算总GPA
        输入：成绩列表 grades
        返回：更新后的总gpa
        TODO: 更新self.grades,并返回更新后的总GPA
        HINT:
            1. 加号可以连接两个列表
            2. 可以调用self.get_gpa()计算总GPA
        """

        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def remove_grade(self, course: str) -> float:
        """
        根据课程名删除一门课程成绩
        输入：课程名course
        返回：更新后的总gpa
        TODO: 更新self.grades,并返回更新后的总GPA
        HINT:
            1. 使用for循环进行查找41
            2. 使用列表的remove方法删除成绩
            3. 可以调用self.get_gpa()计算总GPA
        """

        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def show(self) -> None:
        print('-------------------------------------')
        print('课程名          学分\t成绩\tGPA')
        for g in self.grades:
            print(g)
        print('总GPA: %.2f' % self.gpa)
        print('-------------------------------------')
