class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers[-1] > target:
            for i in range(len(numbers)):
                if numbers.count(target - numbers[i]) > 0:
                    if target - numbers[i] == numbers[i]:
                        return [(i+1), (i + 2)]
                    else:
                        return [(i + 1),(numbers.index(target - numbers[i]) + 1)]
        else:
            for i in range(len(numbers)-1, 0, -1):
                if numbers.count(target - numbers[i]) > 0:
                    if target - numbers[i] == numbers[i]:
                        return [(i), (i + 1)]
                    else:
                        return [(numbers.index(target - numbers[i]) + 1),(i + 1)]