class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers) - 1
        while(l<r):
            sum1 = numbers[l] + numbers[r]
            if target == sum1:
                return [l+1,r+1]
            elif target > sum1:
                l+=1
            else:
                r-=1