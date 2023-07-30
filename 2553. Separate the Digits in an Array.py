class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            if i > 9:
                answer += [int(j) for j in str(i)]
            else:
                answer.append(i)
        return answer