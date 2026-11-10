def odd(nums):
    odd=[]
    for num in nums:
        if num%2!=0:
            odd.append(num)
    return odd
print(odd([10, 20, 30, 40, 50, 51]))

