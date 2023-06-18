class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        counter = 0
        max_counter = 0
        max_divisitor = min(divisors)
        for i in divisors:
            for j in nums:
                if j % i == 0:
                    counter += 1
            if counter > max_counter:
                max_divisitor = i
                max_counter = counter
            elif counter == max_counter:
                max_divisitor = min(i, max_divisitor)
                max_counter = counter
            counter = 0
        return max_divisitor