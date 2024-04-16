'''n=int(input("请输入一个整数:"))
if(n%3==0 and n%5==0):
    print(n,"能同时被3和5整除")
else:
    print(n,"不能同时被3和5整除")
year = int(input("请输入年份:"))
if(year%4==0 and year%100!=0)or(year%400==0):
    print(year,"是闰年")
else:
    print(year,"不是闰年")
大家都知道，男大当婚，女大当嫁。那么女方家长要嫁女儿，当然要提出一定的条件：
高：180cm以上; 富:1000万以上; 帅:500以上;
如果这三个条件同时满足，则:‘我一定要嫁给他’
如果三个条件有为真的情况，则:‘嫁吧，比上不足，比下有余。’
如果三个条件都不满足，则:‘不嫁！’
提示：通过键盘获取用户的三个数据，身高、财富,颜值'''
height = int(input("请输入身高(cm):"))
money = int(input("请输入财富(万):"))
appearance = int(input("请输入颜值:"))
if(height>180 and money>1000 and appearance>500):
    print("我一定要嫁给他！")
elif(height>180 or money>1000 or appearance>500):
    print("嫁吧，比上不足，比下有余。")
else:
    print("不嫁！")