#使用函数str()避免类型错误
age = 23
#TypeError: must be str, not int
#message = "Happy" + age + "rd Birthday!"
#将非字符串转为字符串
message = "Happy" + str(age) + "rd Birthday!"
print(message)