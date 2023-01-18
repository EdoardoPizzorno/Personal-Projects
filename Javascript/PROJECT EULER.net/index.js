$(document).ready(function () {
    p = $("p")
    //problem1()
    //problem2()
    //problem3()
    //problem4()
    //problem5() // NOT OPTIMIZED
    //problem6()
    //problem7() // NOT OPTIMIZED
    //problem8() // WRONG 
    problem9()

    //#region FUNCTIONS
    function problem1() {
        let somma = 0
        for (let i = 0; i < 1000; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                somma += i
            }
        }
        p.text(somma)
    }
    function problem2() {
        sum = 0
        a = 0
        b = 1

        while ((a + b) < 4000000) {
            a = a + b
            if (a % 2 == 0)
                sum += a
            b = b + a
            if (b % 2 == 0)
                sum += b
        }
        p.html(sum)
    }
    function problem3() {
        n = 600851475143
        prime_factors = []
        prod = 1
        largest = 0
        exit = false

        i = 0
        while (!exit && i < n / 2) {
            if (n % i == 0) {
                prime_factors.push(i)
                prod = 1
                for (j = 0; j < prime_factors.length; j++) {
                    prod *= prime_factors[j]
                    if (prod == n)
                        exit = true
                }
            }
            i++
        }
        p.text(prime_factors[prime_factors.length - 1])
    }
    function problem4() {
        largest = 0

        for (let i = 100; i < 1000; i++)
            for (let j = 100; j < 1000; j++)
                if (IsPalindrome(i * j) && (i * j) > largest) // the second condition is crucial, otherwise it takes the penultimate
                    largest = i * j

        p.text(largest)
    }
    function problem5() {
        i = 1
        while (!IsDivisible(i))
            i++
        p.text(i)
    }
    function problem6() {
        let sum_of_squares = GetSumOfSquares(100)
        let square_of_sum = GetSquareOfSum(100)

        let difference = square_of_sum - sum_of_squares
        p.text(difference)
    }
    function problem7() {
        count = 0
        i = 0
        j = 3
        largest = 0

        while (i != 10000) {
            count = 0
            for (let k = 0; k <= Math.floor(j / 2); k++)
                if (j % k == 0)
                    count++

            if (count == 1 && j > largest) { // if the count == 2 -> it means that's a prime number
                largest = j
                i++
            }
            j += 2
        }
        p.text(largest)
    }
    function problem8() {
        str = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
        IsAdjacent(4, str)
    }
    function problem9(){
        let c = 0
        let exit = false
        while(!exit){
            for(let a = 200; a < 333; a+=5){
                for(let b = a + 1; b < 500; b+=5){
                    c = 1000 - (a + b)
                    if((a * a) + (b * b) == (c * c)){
                        exit = true
                        console.log(a, b, c)
                    }
                }
            }
        }
        console.log("TROVATO\nProdotto: " + (a * b * c))
    }
    //#endregion
    //#region HELPERS
    function IsPalindrome(n) {
        n = n.toString()
        j = n.length - 1
        for (i = 0; i < n.length / 2; i++) {
            if (n[i] != n[j])
                return false
            j--
        }
        return true
    }
    function IsDivisible(i) {
        for (let j = 1; j < 20; j++)
            if (i % j != 0)
                return false
        return true
    }
    function GetSumOfSquares(n) {
        sum = 0
        for (i = 1; i <= n; i++)
            sum += Math.pow(i, 2)
        return sum
    }
    function GetSquareOfSum(n) {
        sum = 0
        for (i = 1; i <= n; i++)
            sum += i
        return Math.pow(sum, 2)
    }
    function IsAdjacent(n, s) {
        adj = []
        greater = 1
        prod = 1

        i = 0
        while (i != s.length) {
            if (adj.length == 0)
                adj.push(s[i])
            else {
                if (adj.includes((parseInt(s[i])).toString()) || adj.includes((parseInt(s[i]) + 1).toString()) || adj.includes((parseInt(s[i]) - 1).toString()))
                    adj.push(s[i])
                else
                    adj.splice(0, adj.length)
            }



            if (adj.length == n) {
                console.log(adj)
                prod = 1
                for (j = 0; j < adj.length; j++)
                    prod *= adj[j]
                if (prod > greater)
                    greater = prod
            }
            i++
        }
        console.log(greater)
    }
    //#endregion
})