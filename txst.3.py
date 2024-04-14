str1 = input("请输入一个字符串:")
str_sum = 0
dig_sum = 0
spa_sum = 0
other_sum = 0
for strs in str1:
    if strs.isalpha():
        str_sum+=1
    elif strs.isdigit():
        dig_sum+=1
    elif strs == " ":
        spa_sum+=1
    else:
        other_sum+=1
    print("该字符串中的字符有:",str_sum)
    print("该字符串中的数字有:",dig_sum)
    print("该字符串中的空格有:",spa_sum)
    print("该字符串中的特殊字符有:",other_sum)
strl = input('请输入一个字符串：')
str_sum = 0
dig_sum = 0
spa_sum = 0
other_sum = 0
for strs in strl:
    if strs.isalpha():
            str_sum += 1
    elif strs.isdigit():
            dig_sum += 1
    elif strs == ' ':
            spa_sum += 1
    else:
            other_sum += 1
print("该字符串中的字符有:", str_sum)
print("该字符串中的数字有:", dig_sum)
print("该字符串中的空格有:", spa_sum)
print("该字符串中的特殊字符有:", other_sum)
ID = input("请输入十八位身份证号码:")
if len(ID) == 18:
    print("你的身份证号码是"+ID)
else:
    print("错误的身份证号码")
year = ID[6:10]
moon = ID[10:12]
day = ID[12:14]
print("出生年月:"+ year + '年'+ moon +'月'+ day + '日')
strl="hello,Python,hello,c"
print(strl.split())
print(strl.split((",")))
print(strl.split(",",2))
lst=['hello','Python','hello,c!']
s=""
print(s.join(lst))
strl="hello,Python!hello,c!"
print(strl[6:12])
print(strl[-8:-1])
print(strl[:-3])
print('java'in strl)
print('Python'in strl)
name = "小帅"
dz = "广东白云学院"
print("我的名字是:" + name + ",学校是："+ dz)'''
name = "小帅"
xx = "广东白云学院"
quanbu = "我的名字是%s,学校是%s"%(name,xx)
print(quanbu)
