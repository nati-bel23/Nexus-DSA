def sortColors(self, nums: List[int]) -> None:
        red, white, blue =nums.count(0), nums.count(1), nums.coun(2)
        for i in range(red):
            nums[i] = 0
        for i in range(red,red+white):
            nums[i]=1
        for i in range(red+white,len(nums)):
            nums[i]=2
