p002message = "simple_message"
print(p002message)

#使用制表符或换行符来添加空白

print("Python")
print("\tPython")
print("A\nB\nJavaScript")
print("C\n\td\nJavaScript")

#删除空白
p002message = "kongbai "
#确保字符串末尾没有空白使用rstrip()
print(p002message.rstrip())
#这种删除只是暂时的
print(p002message)
#要永久的删除这个字符串空白必须将删除操作的结果存回到变量中
p002message = p002message.rstrip()
print(p002message)

#剔除字符串开头的空白,或者同时剔除字符串两端的空白

message  = " first_last "
print(message)
print(message.lstrip())
print(message.rstrip())
print(message.strip())