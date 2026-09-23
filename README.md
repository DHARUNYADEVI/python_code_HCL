## Name: Dharunyadevi S
## Register Number: 212223220018
# Python Basic Programs

This repository contains simple Python programs for basic programming practice.

## Programs

1. Binary numbers divisible by 5

   * Accepts comma-separated 4-digit binary numbers.
   * Prints the numbers divisible by 5.
```py
a=input().split(",")
result=[]
for x in a:
    if int(x,2)%5==0:
        result.append(x)
print(",".join(result))
```

2. Count letters and digits

   * Accepts a sentence.
   * Counts and displays the number of letters and digits.
```py
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
```

3. Factorial

   * Accepts a number.
   * Calculates and displays its factorial.
```py
s=int(input())
fact=1
for i in range(1,s+1):
    fact*=i
print(fact)
```

## Sample Input

```text
0100,0011,1010,1001
hello world! 123
8
```

## Sample Output

```text
1010
LETTERS 10
DIGITS 3
40320
```
## Output
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/69412108-0edf-4b1a-a7c2-b21f65242a6d" />

