import random
checkcode=""
print("请输入生成验证码位数：")
a=0
c=0
a=eval(input())
print("请输入生成验证码次数：")
c=eval(input())
for b in range(c):
    for i in range(a):
        index=random.randrange(0,4)
        if index!=i and index+1!=i:
            checkcode+=chr(random.randint(97,122))
        elif index+1==i:
            checkcode+=chr(random.randint(65,90))
        else:
            checkcode+=str(random.randint(0,9))
    print(checkcode)
    checkcode=""
