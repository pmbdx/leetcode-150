class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        if(k>0):
            nums[:] = nums[::-1]
            if(len(nums)>2 or k%2==0):
                nums[:k] = nums[:k][::-1]
                nums[k:] = nums[k:][::-1]
