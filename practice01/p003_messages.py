#用引号括起来的都是字符串可以是单引号也可以是双引号
p003messages = 'p003'
print(p003messages)
p003messages = "messages p003"
print(p003messages)
#每个单词的首字母都改成大写
print(p003messages.title())
#字符串改为全部大写
print(p003messages.upper())
#字符串改为全部小写
print(p003messages.lower())

#拼接字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " +last_name
print(full_name)

