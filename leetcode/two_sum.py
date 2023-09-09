class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx, x in enumerate(nums):
            i = idx + 1
            while i <= len(nums) - 1:
                if (x + nums[i] == target):
                    return [idx, i]
                else:
                    i += 1
                    continue
        return []

# test cases #
solution = Solution()
nums = ([2,7,11,15], [3,2,4], [3,3])
target = (9,6,6)
submissions = []
answers = ([0,1], [1,2], [0,1])

for i in range(len(nums)):
    submissions.append(solution.twoSum(nums[i], target[i]))

for i in range(len(submissions)):
    if submissions[i] == answers[i]:
        print(f"Test case {i + 1} correct")
    else:
        print(f"Test case {i + 1} incorrect")
        
'''
testcases

[2,7,11,15]
9

[3,2,4]
6

[3,3]
6
'''