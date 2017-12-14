
#if return logic을 본다



def isPrimeNumber(numParam1):
    #콜론은 블락스테잇먼트를 나타낸다
    for itr in range(2, numParam1):
        #반복시키는 동안에
        if numParam1 % itr == 0:
            #반복시키는 동안에 확인해라
            break
    else:
        return True
    #브렉이 걸릴경우 바깥에 있는 리턴으로 간다(뽈쓰)
    return False


'''
스테이트먼트(메쏘드 연산), 결과값으로 선언=리턴
파이썬에는 리턴타입이 존재하지 않는다
여러개의 정해지지 않은 타입들을 모두 리턴할 수 있는게 파이쏜의 특징이다

*멀티플리턴은 리턴에 콤마를 넣은거야
return numParam1*3, numParam2*2

*****램다펑션       :콜론으로 뒤에있는 것을 리턴한다
lambdaAdd = lambda numPr1, numPr2 : numPr1+numPr2

'''

def findPrimes(numParam1, numParam2):
    numCount = 1
    for itr in range(numParam1, numParam2):
        if isPrimeNumber(itr) == True:
            print(numCount, "th prime: ", itr)
            numCount += 1


print(findPrimes(1,10))
