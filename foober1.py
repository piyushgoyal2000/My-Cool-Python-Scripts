def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    x = 3
    while x * x <= n:
        if n %x == 0 :
            return False
        x += 2
    return True

def answer(n):
    ret_str = "2"
    no = 3
    index = 1
    dig = 1
    den = 10
    while index <= no + 4:
        if(isPrime(no)==True):
            index += dig
            ret_str += str(no)
        no += 2
        if int(no / den) != 0:
            den *= 10
            dig += 1
    print(ret_str[n:n+5])
