class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        arr.sort()

        def count_leq(target):
            n = len(arr)
            count = 0

            for i in range(n - 2):
                left = i + 1
                right = n - 1

                while left < right:
                    total = arr[i] + arr[left] + arr[right]

                    if total <= target:
                        # Every element from left+1 to right
                        # can form a valid triplet with i and left.
                        count += right - left
                        left += 1
                    else:
                        right -= 1

            return count

        return count_leq(r) - count_leq(l - 1)