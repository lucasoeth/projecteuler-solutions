# Lucas Soeth 2021-04-29
def is_palindrome(n):
    n = str(n)
    return n==''.join(reversed(n))

# I use this fact to make my bruteforce a semi bruteforce
# 96*96=9216 => 96+96 == 97+95
# 97*95=9215 => 96*96 > 97*95

num = 999+999

while num > 0:
    i = num // 2
    j = num // 2 + num % 2

    while j < 1000:
        if is_palindrome(i*j):
            print(i*j)
            num = 0
            break
        i -= 1
        j += 1
    num -= 1