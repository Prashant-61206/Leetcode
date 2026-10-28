class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output=[]
        for i_,i in enumerate(nums):
            for j_,j in enumerate(nums):
                sum= i+j
                if sum==target and i_!=j_:
                    output.extend([i_,j_])
        output=set(output)
        return list(output)
