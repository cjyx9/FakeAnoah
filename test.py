from FakeAnoah import *

#* tests *#
user = User("1765830")

input("优学派服务器时间戳(按回车键以继续):")
print(user.server_time)
input("用户名:")
print(user.user_name)
input("头像:")
print(user.user_head_img)
input("积分数:")
print(user.uesr_point)
input("班级id:")
print(user.user_class_ids)
input("全部学科:")
print(user.subject_json)
input("保存头像")
user.save_head()
input("未完成作业:")
print(user.get_undo_homework())
input("作业等级评估:")
print(user.analysis_grade())
input = input("请输入一个学科(默认语文):")
subject = "语文" if not(input) else input
print(user.get_homeworks(subject))
input("全部信息:")
print(user.get_message())