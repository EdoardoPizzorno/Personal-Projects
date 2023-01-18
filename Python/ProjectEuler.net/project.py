import math

def problem1():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)

#problem1()

def Fibonacci(): 
    a = 0
    b = 1
    sum = 0
    while(sum < 4000000):
        a += b
        if(a % 2 == 0):
            sum += a
        b += a
        if(b % 2 == 0):
            sum += b
    return sum
#print(Fibonacci())

def LargestPrimeFactor():
    n = 600851475143
    out = False
    prime_factors = []
    i = 1

    while not out:
        prod = 1
        if n % i == 0:
            prime_factors.append(i)
            for j in range(len(prime_factors)):
                prod *= prime_factors[j]
                if prod == n:
                    out = True
        i += 1
    return prime_factors[len(prime_factors) - 1]
#print(LargestPrimeFactor())

def isPalindrome(n):
    n = str(n)
    j = len(n) - 1
    for i in range(len(n)):
        if n[i] != n[j]:
            return False
        j -= 1
    return True

def LargestPalindromeProduct():
    prod = 1
    greater = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if isPalindrome(prod) and prod > greater:
                greater = prod
    return greater
#print(LargestPalindromeProduct())

def isDivisible(final_number, n):
    for i in range(1, n):
        if final_number % i != 0:
            return False
    return True

def SmallestMultiple(n):
    out = False
    final_number = 1

    while not out:
        if isDivisible(final_number, n):
            out = True
        else: 
            final_number += 1
    return final_number
#print(SmallestMultiple(20))

def SumSquareDifference(n):
    sum_squares = 0
    square_sum = 0

    n = n + 1
    # calculating the squares' sum
    for i in range(1, n):
        sum_squares += math.pow(i, 2)
    # calculating the sum's square 
    for i in range(1, n):
        square_sum += i
    square_sum = math.pow(square_sum, 2)

    return int(square_sum - sum_squares)
#print(SumSquareDifference(100))

def isPrime(n):
    for i in range(2, math.floor(n / 2) + 1):
        if n % i == 0:
            return False
    return True

def NthPrime(n):
    n = n - 1
    i = 3
    prime_number = 0
    counter = 0

    while counter != n:
        if isPrime(i):
            prime_number = i
            counter += 1
        i += 2

    return prime_number
#print(NthPrime(10001))

def isAdjacent(n1, n2):
    if len(n1) > 1 and len(n2) > 1:
        print(f"n1: {n1}")
        print(f"n2: {n2}")
        if n1[0] == n2[1] and n1[1] == n2[0]:
            return True
    return False

def clear_vect(v1, v2):
    v1.clear()
    v2.clear()

def LargestProductSeries(n):
    s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    greatest = 0
    prod = 1

    shift1 = []
    shift2 = []
    j = 2
    for i in range(len(s) - 1):
        shift1.append(s[i])
        shift1.append(s[i + 1])
        if j < len(s) - 2:
            shift2.append(s[j])
            shift2.append(s[j + 1])
            j += 1

        if len(shift1) == n and len(shift2) == n: 
            if isAdjacent(shift1, shift2):
                print(shift1)
                print(shift2)
                #calculating the current prudect
                for k in range(len(shift1)):
                    prod *= int(shift1[k]) * int(shift2[k])
                # checking if the current product is the greatest one
                if prod > greatest:
                    greatest = prod
                clear_vect(shift1, shift2)
            else:
                clear_vect(shift1, shift2)

    return greatest
print(LargestProductSeries(12))