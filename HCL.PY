# 1
a=input().split(",")
result=[]
for x in a:
    if int(x,2)%5==0:
        result.append(x)
print(",".join(result))
#2
s=input()
letters=0
digits=0
for x in s:
    if x.isalpha():
        letters+=1
    elif x.isdigit():
        digits+=1
print("LETTERS: ",letters)
print("DIGITS: ",digits)
#3
s=int(input())
fact=1
for i in range(1,s+1):
    fact*=i
print(fact)
