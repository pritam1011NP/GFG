class Solution:
    def prefixStrings(self, n: int) -> int:
        MOD = 10**9 + 7

    # Calculate (2n)!
        fact_2n = 1
        for i in range(1, 2 * n + 1):
            fact_2n = (fact_2n * i) % MOD

    # Calculate n!
        fact_n = 1
        for i in range(1, n + 1):
            fact_n = (fact_n * i) % MOD

    # C(2n, n) = (2n)! / (n! * n!)
        numerator = fact_2n
        denominator = (fact_n * fact_n) % MOD

    # Modular inverse using Fermat's Little Theorem
        inverse = pow(denominator, MOD - 2, MOD)

        combination = (numerator * inverse) % MOD

    # Catalan number = C(2n,n) / (n+1)
        answer = (combination * pow(n + 1, MOD - 2, MOD)) % MOD

        return answer