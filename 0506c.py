import random
checkcode=""
for i in range(4):
    index=random.randrange(0,4)
    if index!=i and index+1!=i:
        checkcode+=chr(random.randint(97,122))
    elif index+1==i:
        checkcode+=chr(random.randint(65,90))
    else:
        checkcode+=str(random.randint(0,9))
print(checkcode)
    
