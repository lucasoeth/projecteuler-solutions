# Lucas Soeth 2021-04-29
pre = 0
cur = 1
even_fibs = list()
while (cur<4000000):
    if (cur%2==0):
        even_fibs.append(cur)
    pre,cur=cur,pre
    cur += pre

print(sum(even_fibs))
