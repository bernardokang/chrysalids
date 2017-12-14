
#if return logic을 본다



def isPrimeNumber(numParam1):
    for itr in range(2, numParam1):
        #반복시키는 동안에
        if numParam1 % itr == 0:
            #반복시키는 동안에 확인해라
            break
    else:
        return True
    #브렉이 걸릴경우 바깥에 있는 리턴으로 간다(뽈쓰)
    return False


def findPrimes(numParam1, numParam2):
    numCount = 1
    for itr in range(numParam1, numParam2):
        if isPrimeNumber(itr) == True:
            print(numCount, "th prime: ", itr)
            numCount += 1


print(findPrimes(1,10))
