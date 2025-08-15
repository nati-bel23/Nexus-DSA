def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        size = len(nums)
        for i in range(size):
            for j in range(size - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        for k in range(size):
            if nums[k]==target:
                output.append(k)
        return output
