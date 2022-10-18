num = int(input("Enter the Number"))

def even_odd(num):
    if (num % 2) == 0:
        print("Even")
    else:
        print("Odd")


def palindrome(num):
    temp = num
    count = 0
    while(num >0):
        digit = num % 10
        count = count * 10 + digit
        num = num // 10
    if (temp == count):
        print("palindrome")
    else:
        print("not a palindorme")


def prime(num):
    if num > 1:
        for i in range(2,num):
            if(num %i) ==0:
                print("prime")
                break
            else:
                print("not a prime")


even_odd(num)
prime(num)
palindrome(num)