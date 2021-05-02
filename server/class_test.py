from student import student
from course import course
from SQLite import getNameList


test = getNameList()
cour = course('网络编程', test)
gy = student('郭赟', 28180232, 38, '信息工程')
campus = student('刘宛君', 281802452, 38, '通信工程')
mountain = student('陈嫣冉', 281806452, 38, '通信工程')



cour.sign(gy)
cour.sign(campus)
cour.sign(mountain)

cour.display_singIn()
cour.display_singOut()
gy.display_info()