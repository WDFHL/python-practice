#Python列表
#使用方括号[]表示列表,使用逗号来分隔其中的元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#访问列表元素
#列表为有序集合，索引从0开始
print(bicycles[0])
#Python为访问最后一个列表元素提供了一种特殊语法索引指定为-1
#-2倒数第二个列表元素-3就是倒数第三个列表元素以此类推
print(bicycles[-1])

#使用列表中的各个值
names = ["道法","浩然","西天","雷池重地","剑气长存"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names)
names[0] = "平安"
print(names)
#在列表末尾添加元素
names.append("猛")
print(names)
#在列表中插入元素
names.insert(1,"齐")
print(names)
#从列表中删除元素
#1.使用del语句删除元素
del  names[2]
print(names)
#2.使用方法pop()删除元素 删除列表末尾元素并让你能够接着使用它
motos = ["h","y","s"]
print(motos)
motos_pop = motos.pop()
print(motos)
print(motos_pop)
#3.弹出列表中任意位置的元素
print(names.pop(4))
print(names)
#根据值删除元素
names.remove("西天")
print(names)

dalaos = ["马云","马化腾","李彦宏"]
print(dalaos)
dalao = "李彦宏"
dalaos.insert(2,"比尔")
dalaos.remove(dalao)
print(dalaos)

#使用方法sort()对列表进行永久性排序 假设所有值都是小写
cars = ["bmw","audi","cooo","def"]
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#使用函数sorted对列表进行临时排序
cars = ["bmw","audi","cooo","def"]
print(cars)
print(sorted(cars))
print(cars)

#倒着打印列表方法reverse永久性的打印
cars.reverse()
print(cars)
#确定列表长度
print(len(cars))