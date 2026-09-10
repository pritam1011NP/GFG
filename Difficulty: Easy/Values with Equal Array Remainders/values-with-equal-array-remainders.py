from math import gcd

class Solution:
    def sameMod(self, arr):
        n = len(arr)

        # If all elements are equal, infinitely many k are possible
        if len(set(arr)) == 1:
            return -1

        # GCD of differences from the first element
        g = 0
        for i in range(1, n):
            g = gcd(g, abs(arr[i] - arr[0]))

        # Number of positive divisors of g
        count = 0
        d = 1

        while d * d <= g:
            if g % d == 0:
                count += 1
                if d != g // d:
                    count += 1
            d += 1

        return count