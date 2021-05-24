class course:
    name = ''
    allStudent = []
    signIn = []
    singOut = []

    def __init__(self, n, s):
        self.name = n
        self.allStudent = s
        self.singOut = s

    def sign(self, stu):
        if stu.name not in self.signIn:
            self.signIn.append(stu.name)
            stu.sign_in_or_not = True
        for i in self.allStudent:
            if i == stu.name:
                self.singOut.remove(i)

    def display_singIn(self):
        print("当前课程：", self.name)
        print("签到成功:")
        print(self.signIn)
        return self.signIn

    def display_singOut(self):
        print("迟到:")
        print(self.singOut)
        return self.singOut

    def display_allStudent(self):
        print(self.allStudent)