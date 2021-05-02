class student:
    name = ''
    id = 0
    class_number = 0
    major = ''
    sign_in_or_not = False

    def __init__(self, n, i, c, m):
        self.name = n
        self.id = i
        self.class_number = c
        self.major = m

    def display_info(self):
        print('姓名：', self.name)
        print('学号：', self.id)
        print('班级：', self.class_number)
        print('专业：', self.major)
        print('签到情况：', self.sign_in_or_not)

