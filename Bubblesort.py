def sort(nums):
    for i in range(0, len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                t = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = t


def bubble(nums):
    for i in range(len(nums)-1):
        min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min]:
                min = j
        t = nums[i]
        nums[i] = nums[min]
        nums[min] = t


nums = [5, 2, 7, 3, 1,4,8,9, 6]
bubble(nums)
print(nums)
