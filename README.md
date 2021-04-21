## 项目名称
智慧教室人脸考勤系统
***
## Current work progress
### **4.21 deploy on Jetson Nano and send Mat directly** 
### 4.18 face recognition/match and socket
***
## 项目介绍
该系统主要用于基于人脸识别的课堂考勤场景，技术实现如下：
### ①客户端
包括一台搭载摄像头的微型运算设备，具有基于深度学习AI的人脸识别功能，并通过socket网络通信将人脸特征发送至服务器；该程序运行在单片机等嵌入式系统上；
### ②服务器
包括学生个人信息数据库，能够通过socket网络通信接收人脸特征并与数据库中的信息进行匹配，并回复客户端匹配结果与个人信息；该程序运行在个人PC上。

## 创新点
该系统巧妙地将网络通信、嵌入式边缘AI、人脸识别技术运用于课堂考勤场景下，无需借助钉钉、学习通等第三方应用程序，只需进入教室前进行人脸识别，系统即可进行学生身份验证并自动汇总课堂签到结果，实现智能化课堂考勤功能。该系统成本低廉，复用性强，对未来高校智慧教室的实现与推广具有巨大积极作用。
