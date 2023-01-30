import math
import sys

sys.set_int_max_str_digits(1000000)

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
    aus = math.floor(n / 2) + 1
    for i in range(2, aus):
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

    for i in range(len(s) - n):
        prod = 1
        for j in range(i, i + n):
            prod *= int(s[j])
        if prod > greatest:
            greatest = prod

    return greatest
#print(LargestProductSeries(13))

def PythagoreanTriplet():
    c = 0
    for a in range(200, 333):
        for b in range(a + 1, 500):
            c = 1000 - (a + b)
            if(a*a + b*b == c*c and a + b + c == 1000):
                print(a * b * c)
#print(PythagoreanTriplet())

def SummationPrime(n):
    sum = 2
    for i in range(3, n, 2):
        if isPrime(i):
            sum += i
            print(i)
    return sum
#print(SummationPrime(2000000))

def swapGreatest(n, greater):
    if n > greater:
        greater = n
    return greater

def LargestProductGrid(n):
    grid = [[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
            [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
            [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
            [52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
            [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
            [24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
            [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
            [67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
            [24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
            [21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
            [78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
            [16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
            [86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
            [19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
            [4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
            [88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
            [4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
            [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
            [20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
            [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]
    greatest = 0
    prod = 1

    length = len(grid) # it's a square grid (rows == cols)
    # rows
    for i in range(length): # all rows
        for j in range(length - n + 1): # cols - n
            prod = 1
            for k in range(n):
                prod *= grid[i][j + k]
            greatest = swapGreatest(prod, greatest)
    # cols
    for i in range(length - n + 1):
        for j in range(length):
            prod = 1
            for k in range(n):
                prod *= grid[i + k][j]
            greatest = swapGreatest(prod, greatest)
    # full right-diagonal
    for i in range(length - n + 1):
        for j in range(length - n + 1):
            prod = 1
            for k in range(n):
                prod *= grid[i + k][j + k]
            greatest = swapGreatest(prod, greatest)
    # full left-diagonal
    for i in range(length - n + 1):
        for j in range(length - 1, n + 1, -1):
            prod = 1
            for k in range(n):
                prod *= grid[i + k][j - k]
            greatest = swapGreatest(prod, greatest)
    
    return greatest

#print(LargestProductGrid(4))

def isTriangle(n):
    sum = 0
    for i in range(1, n):
        sum += i
        if sum == n:
            return True
    return False

def countDivisors(n):
    aus = math.floor(n / 2)
    count = 0

    for i in range(1, aus):
        if n % i == 0:
            count += 1
    return count

def HighlyDivisibleTriangleNumber(n):
    i = 3
    out = False
    result = 0
    aus = 2

    while not out:
        if isTriangle(i):
            aus += 1
            print(i)
            if countDivisors(i) == n - 1:
                out = True
                result = i
            else: 
                i += aus
    return result
#print(HighlyDivisibleTriangleNumber(502))

def LargeSum():
    numbers = [37107287533902102798797998220837590246510135740250,
            46376937677490009712648124896970078050417018260538,
            74324986199524741059474233309513058123726617309629,
            91942213363574161572522430563301811072406154908250,
            23067588207539346171171980310421047513778063246676,
            89261670696623633820136378418383684178734361726757,
            28112879812849979408065481931592621691275889832738,
            44274228917432520321923589422876796487670272189318,
            47451445736001306439091167216856844588711603153276,
            70386486105843025439939619828917593665686757934951,
            62176457141856560629502157223196586755079324193331,
            64906352462741904929101432445813822663347944758178,
            92575867718337217661963751590579239728245598838407,
            58203565325359399008402633568948830189458628227828,
            80181199384826282014278194139940567587151170094390,
            35398664372827112653829987240784473053190104293586,
            86515506006295864861532075273371959191420517255829,
            71693888707715466499115593487603532921714970056938,
            54370070576826684624621495650076471787294438377604,
            53282654108756828443191190634694037855217779295145,
            36123272525000296071075082563815656710885258350721,
            45876576172410976447339110607218265236877223636045,
            17423706905851860660448207621209813287860733969412,
            81142660418086830619328460811191061556940512689692,
            51934325451728388641918047049293215058642563049483,
            62467221648435076201727918039944693004732956340691,
            15732444386908125794514089057706229429197107928209,
            55037687525678773091862540744969844508330393682126,
            18336384825330154686196124348767681297534375946515,
            80386287592878490201521685554828717201219257766954,
            78182833757993103614740356856449095527097864797581,
            16726320100436897842553539920931837441497806860984,
            48403098129077791799088218795327364475675590848030,
            87086987551392711854517078544161852424320693150332,
            59959406895756536782107074926966537676326235447210,
            69793950679652694742597709739166693763042633987085,
            41052684708299085211399427365734116182760315001271,
            65378607361501080857009149939512557028198746004375,
            35829035317434717326932123578154982629742552737307,
            94953759765105305946966067683156574377167401875275,
            88902802571733229619176668713819931811048770190271,
            25267680276078003013678680992525463401061632866526,
            36270218540497705585629946580636237993140746255962,
            24074486908231174977792365466257246923322810917141,
            91430288197103288597806669760892938638285025333403,
            34413065578016127815921815005561868836468420090470,
            23053081172816430487623791969842487255036638784583,
            11487696932154902810424020138335124462181441773470,
            63783299490636259666498587618221225225512486764533,
            67720186971698544312419572409913959008952310058822,
            95548255300263520781532296796249481641953868218774,
            76085327132285723110424803456124867697064507995236,
            37774242535411291684276865538926205024910326572967,
            23701913275725675285653248258265463092207058596522,
            29798860272258331913126375147341994889534765745501,
            18495701454879288984856827726077713721403798879715,
            38298203783031473527721580348144513491373226651381,
            34829543829199918180278916522431027392251122869539,
            40957953066405232632538044100059654939159879593635,
            29746152185502371307642255121183693803580388584903,
            41698116222072977186158236678424689157993532961922,
            62467957194401269043877107275048102390895523597457,
            23189706772547915061505504953922979530901129967519,
            86188088225875314529584099251203829009407770775672,
            11306739708304724483816533873502340845647058077308,
            82959174767140363198008187129011875491310547126581,
            97623331044818386269515456334926366572897563400500,
            42846280183517070527831839425882145521227251250327,
            55121603546981200581762165212827652751691296897789,
            32238195734329339946437501907836945765883352399886,
            75506164965184775180738168837861091527357929701337,
            62177842752192623401942399639168044983993173312731,
            32924185707147349566916674687634660915035914677504,
            99518671430235219628894890102423325116913619626622,
            73267460800591547471830798392868535206946944540724,
            76841822524674417161514036427982273348055556214818,
            97142617910342598647204516893989422179826088076852,
            87783646182799346313767754307809363333018982642090,
            10848802521674670883215120185883543223812876952786,
            71329612474782464538636993009049310363619763878039,
            62184073572399794223406235393808339651327408011116,
            66627891981488087797941876876144230030984490851411,
            60661826293682836764744779239180335110989069790714,
            85786944089552990653640447425576083659976645795096,
            66024396409905389607120198219976047599490197230297,
            64913982680032973156037120041377903785566085089252,
            16730939319872750275468906903707539413042652315011,
            94809377245048795150954100921645863754710598436791,
            78639167021187492431995700641917969777599028300699,
            15368713711936614952811305876380278410754449733078,
            40789923115535562561142322423255033685442488917353,
            44889911501440648020369068063960672322193204149535,
            41503128880339536053299340368006977710650566631954,
            81234880673210146739058568557934581403627822703280,
            82616570773948327592232845941706525094512325230608,
            22918802058777319719839450180888072429661980811197,
            77158542502016545090413245809786882778948721859617,
            72107838435069186155435662884062257473692284509516,
            20849603980134001723930671666823555245252804609722,
            53503534226472524250874054075591789781264330331690]

    sum = 0
    aus = ""
    result = ""

    for i in range(len(numbers)):
        sum += numbers[i]
    
    print(sum)
    aus = str(sum)
    
    for i in range(10):
        result += aus[i]
    return result

#print(LargeSum())

def LongestCollatzSequence(n):
    count = 0
    greatest_count = 0
    greatest_number = 0

    for i in range(13, n):
        number = i
        count = 0
        while number != 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = 3 * number + 1
            count += 1
            # swapping the greatest number and counter
            if count > greatest_count:
                greatest_count = count
                greatest_number = i
    return greatest_number

#print(LongestCollatzSequence(1000000))

def PowerDigitSum(n):
    n = math.pow(2, n)
    sum = 0

    n = str(math.floor(n))
    for i in range(len(n)):
        sum += int(n[i])
    return sum
#print(PowerDigitSum(1000))

def calculateWordsNumber(n, basic, tens):
    number_word = ""
    if n == 1000:
        number_word = "onethousand"
    if n < 10:
        number_word = basic[n - 1]
    else:
        if n > 10 and n < 20:
            if n == 11:
                number_word = "eleven"
            elif n == 12:
                number_word = "twelve"
            elif n == 13:
                number_word = "thirteen"
            elif n == 15:
                number_word = "fifteen"
            elif n == 18:
                number_word = "eighteen"
            else:
                number_word = basic[n-10 - 1] + "teen"
        else:
            if n % 10 == 0 and n % 100 != 0:
                if n > 100:
                    number_word = basic[math.floor(n/100) - 1] + "hundredand" + tens[math.floor(n/10 - (10 * math.floor(n / 100))) - 1]
                else:
                    number_word = tens[math.floor(n/10) - 1]
            else:
                rest = n % 10 # taking the rest --> 52 % 10 = 5 (rest 2)
                if n < 100:
                    number_word = tens[(math.floor(n / 10)) - 1] + basic[rest - 1] # if n == 52 --> tens[math.floor(52 / 10) - 1] --> tens[4] --> fifty + basic[1] --> fiftytwo
                else:
                    rest = n % 100
                    if n % 100 == 0 and n != 1000:
                        number_word = basic[math.floor(n/100) - 1] + "hundred"
                    else:
                        if n % 10 == 0 and n != 1000:
                            number_word = basic[math.floor(n/100) - 1] + "hundredand" + tens[(math.floor(n / 10)) - 1] + basic[rest - 1]
                        else:
                            if n != 1000:
                                number_word = basic[math.floor(n/100) - 1] + "hundredand" + calculateWordsNumber(rest, basic, tens)
    return number_word

def NumberLetterCounts(n):
    n += 1
    basic = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    number_word = ""
    letter_counter = 0

    for i in range(1, n):
        number_word = calculateWordsNumber(i, basic, tens)
        letter_counter += len(number_word)
        print(i, number_word)

    return letter_counter
#print(NumberLetterCounts(1000)) # no spaces or hyphens || NOT OPTIMIZED

def calculateLeftRight(left, right, matrix, current_index):
    left_sum = 0
    right_sum = 0
    greatest = 0

    j = 0
    for i in range(current_index, len(matrix)):
        #calculating the left's route
        left_sum += left + matrix[i + 1][0]
        #calculating the right's route
        right_sum += right + matrix[i + 1][j]
        j += 1
        #calculating ...
        if left_sum > right_sum:
            greatest = left_sum
        else:
            greatest = right_sum
    return greatest

def MaximumPathSum():
    matrix = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
    
    sum = 0
    maximum = matrix[0]
    j=0

    greatest = 0
    for i in range(len(matrix) - 1):
        left = matrix[i + 1][j]
        right = matrix[i + 1][j + 1]
        greatest = calculateLeftRight(left, right, matrix, i)
    return greatest

#print(MaximumPathSum())

def CountingSundays(y_start, y_end):
    # from 01-01-1901 to 31-12-2000
    # 01-01-1900 was a Monday
    sundays_number = 0

    total_days = []
    daysname_in_month = ["monday", "thursday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    daysnumber_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    j = 0
    for year in range(y_start+1, y_end):
        for month in range(1, 13):
            # calculating the February's days number    
            if year % 4 == 0:
                daysnumber_in_month[1] = 29
            else:
                daysnumber_in_month[1] = 28
            # shifting all the current month's days
            for day in range(0, daysnumber_in_month[month-1]):
                new_day = str(day) + daysname_in_month[j]
                total_days.append(new_day)
                if j < 6:
                    j += 1
                else:
                    j = 0

    for i in range(len(total_days)):
        if total_days[i] == "1sunday":
            sundays_number += 1

    return sundays_number

#print(CountingSundays(1900, 2001))

def FactorialDigitSum(n):
    sum = 0
    prod = 1

    for i in range(n, 1, -1):
        prod *= i

    prod = str(prod)
    for i in range(len(prod)):
        sum += int(prod[i])
    return sum

#print(FactorialDigitSum(100))

def findAmicableNumber(n):
    for_range = math.floor(n / 2) + 1

    sum1 = 0
    sum2 = 0

    for i in range(1, for_range):
        if n % i == 0:
            sum1 += i # summing the divisor
    
    for i in range(1, math.floor(sum1 / 2) + 1):
        if sum1 % i == 0:
            sum2 += i # summing the divisor
    
    if sum2 == n:
        return sum1
    return -1

def AmicableNumbers(n):
    sum = 0
    i = 200

    while i < n:
        amicable_number = findAmicableNumber(i)
        if amicable_number != -1 and amicable_number != i:
            sum += amicable_number + i
            i = amicable_number
        i += 1

    return sum

#print(AmicableNumbers(10000))

def NamesScores():
    f = open("Python/ProjectEuler.net/names.txt", "r") # Relative path
    file_content = f.read()
    f.close()
    
    all_words = []
    sum = 0
    score = 1
    score_sum = 0

    word = file_content.replace('"', "")
    
    current_word = ""
    i = 0
    while word[i] != '*':
        if word[i] != ',':
            current_word += word[i]
        else:
            all_words.append(current_word)
            current_word = ""
        i += 1
    # sorting the array with all words
    all_words.sort()
    # calculating the final score
    for i in range(0, len(all_words)):
        sum = 0
        score = 1
        for j in range(0, len(all_words[i])):
            sum += (ord(all_words[i][j]) - 64)
        score *= sum * (i + 1)
        score_sum += score

    return score_sum

print(NamesScores())