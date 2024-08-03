'''
需求：学生管理系统
学生

老师

班级

课程
'''


class User(object):
    # 属性：姓名、年龄、性别、学号
    def __init__(self, name, age, gender, id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    def show_infos(self):  # 显示学生信息
        print('*' * 30)
        print('姓名：%s' % self.name)
        print('年龄：%d' % self.age)
        print('性别：%s' % self.gender)
        print('编号：%d' % self.id_number)
        print('*' * 30)


class Student(User):
    # 属性：姓名、年龄、性别、学号
    def __init__(self, name, age, gender, id_number):
        super().__init__(name, age, gender, id_number)
        self.course = []

    def show_infos(self):  # 显示学生信息
        super().show_infos()
        print('该学生的选课信息：')
        if self.course == []:
            print('未选课')
        else:
            for i in self.course:
                print(i.name)
        print('*' * 15 + '学生信息' + '*' * 15)

    def add_course(self, course):
        self.course.append(course)


class Teacher(User):
    # 属性、姓名、年龄、性别、工号、是否是辅导员、班级列表
    def __init__(self, name, age, gender, id_number, is_dao, clas):
        super().__init__(name, age, gender, id_number)
        self.is_dao = is_dao
        self.clas = clas

    def show_infos(self):
        super().show_infos()
        print('是否是辅导员：%s' % ['否', '是'][self.is_dao])
        print('辅导班级：')
        if not self.clas:
            print('空')
        else:
            for i in self.clas:
                print('--' + i)
        print('*' * 30)


class Clazz(object):
    # 属性：班级名称、班级号、辅导员、学生
    def __init__(self, name, id_number, teacher, students):
        self.name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students

    def show_infos(self):
        print('*' * 15 + '班级信息' + '*' * 15)
        print('班级名称：%s' % self.name)
        print('班级班号：%d' % self.id_number)
        print('辅导员：%s' % self.teacher.name)
        print('学生信息：')
        if not self.students:
            print('空')
        else:
            for i in self.students:
                print(i.name)
        print('*' * 15 + '班级信息' + '*' * 15)

    def add_student(self, student):
        if student in self.students:
            raise Exception('此学生已在本班级里')
        self.students.append(student)

    def del_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return True
        raise Exception('此学生不在本班级里')


class Course(object):
    courses = []

    # 属性：课名、课程id、老师、学生列表、课程性质、课程容量
    def __init__(self, name, id_number, teacher, students, type, number):
        self.__name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students
        self.type = type
        self.number = number
        self.student_number = len(self.students)
        self.valid_number = self.number - self.student_number
        Course.courses.append(self.__name)

    def show_infos(self):
        print('*' * 15 + '班级信息' + '*' * 15)
        print('课程名称：%s' % self.__name)
        print('课程号：%d' % self.id_number)
        print('授课老师：%s' % self.teacher.name)
        print('课程类型：%s' % self.type)
        print('课程容量：%d' % self.number)
        print('已选学生人数：%d' % self.student_number)
        print('剩余学生空位：%d' % self.valid_number)
        print('学生信息：')
        if not self.students:
            print('空')
        else:
            for i in self.students:
                print(i.name)
        print('*' * 15 + '班级信息' + '*' * 15)

    def add_student(self, student):
        if student in self.students:
            raise Exception('学生重复！')
        elif self.valid_number == 0:
            raise Exception('此课程已满，请选择其他课程')
        self.students.append(student)
        self.valid_number -= 1
        self.student_number += 1
        student.add_course(self)
        return True

    def del_student(self, student):
        if student not in self.students:
            raise Exception('学生未报名改课程！')
        self.students.remove(student)
        self.valid_number += 1
        self.student_number -= 1
        return True

    @classmethod
    def show_courseList(cls):
        return Course.courses

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == '':
            raise Exception('出现错误')
        elif not isinstance(name, str):
            raise Exception('出现错误')
        self.__name = name

# 创建学生
mia = Student('mia', 18, '女', 1)
mia.show_infos()
rose = Student('rose', 17, '女', 2)
lili = Student('lili', 19, '女', 3)

# 创建老师
jack = Teacher('jack', 50, '男', 5, False, [])
jack.show_infos()
tom = Teacher('tom', 26, '男', 53, True, ['计算机二班', '法律三班'])
tom.show_infos()

# 创建班级
computer_2 = Clazz('计算机二班', 1002, tom, [])
computer_2.show_infos()
computer_1 = Clazz('计算机一班', 1002, tom, [mia])
computer_1.show_infos()

computer_2.add_student(rose)
computer_2.show_infos()
# computer_2.del_student(rose)
# computer_2.show_infos()
# computer_2.del_student(mia)
# computer_2.add_student(rose)

# 创建课程
python = Course('python', 1, jack, [mia, rose], '必修课', 6)
java = Course('java', 2, tom, [mia, lili], '选修课', 4)

python.add_student(lili)
python.del_student(mia)
python.show_infos()
lili.show_infos()

print(Course.show_courseList())
python.name = 'python精讲课程'
print(python.name)
# python.name = 1