char=input().lower()
res=""
for string in char:
    if string=="a" or string=="e" or string=="i" or string=="o" or string=="u":
        pass
    else:
        res+=string
print(res)
