num = input("Enter number: ")
number = [int(x) for x in str(num)]
def nextPermutation(nums):
    found = False
    i = len(nums)-2
    while i >=0:
        if nums[i] < nums[i+1]:
            found =True
            break
        i-=1
    if not found:
        nums.sort()
    else:
        m = findMaxIndex(i+1,nums,nums[i])
        nums[i],nums[m] = nums[m],nums[i]
        nums[i+1:] = nums[i+1:][::-1]
    return nums
def findMaxIndex(index,a,curr):
    ans = -1
    index = 0
    for i in range(index,len(a)):
        if a[i]>curr:
            if ans == -1:
                ans = curr
                index = i
            else:
                ans = min(ans,a[i])
                index = i
    return index
print(nextPermutation(number))