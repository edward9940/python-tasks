def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
for i in range(1,31):
    if(i>=11 and i<=15):
        if(isPrime(i)):
            print('hidden prime')
        else:
            print('hidden')
    elif(i%3==0 and i%5==0):
        print('fifteen')
    elif(i%3==0):
        print('three')
    elif(i%5==0):
        print('five')
    else:
        if(isPrime(i)):
            print('prime')
        else:
            print(i)
    