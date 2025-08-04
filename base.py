def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
for i in range(1,21):
    if(i>=6 and i<=10):
        if(isPrime(i)):
            print(i,'prime')
        else:
            print(i,i)
    else:            
        if(i%2==1):
            if(isPrime(i)):
                print(i,'odd','prime')
            else:
                print(i,'odd')       
        else:
            if(isPrime(i)):
                print(i,'even','prime')         
            else:
                print(i,'even')

            
            
    