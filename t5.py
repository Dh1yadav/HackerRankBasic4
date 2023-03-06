if __name__ == '__main__':
    s = input()

r_1 = False
for i in s:
    if i.isalnum():
        r_1 = True
        break
print(r_1)

r_2 = False
for j in s:
    if j.isalpha():
        r_2 = True
        break
print(r_2)

r_3 = False
for k in s:
    if k.isdigit():
        r_3 = True
        break
print(r_3)

r_4 = False
for l in s:
    if l.islower():
        r_4 = True
        break
print(r_4)

r_5 = False
for l in s:
    if l.isupper():
        r_5 = True
        break
print(r_5)
            
