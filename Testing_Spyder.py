# 1. TwoSum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


nums = [2,7,11,15]
target = 9
def twoSum(nums, target):
    seen = {}
    
    for i, s in enumerate(nums):
        remainder = target - nums[i]
        if remainder in seen:
            return [i, seen[remainder]]
        else:
            seen[s] = i
        
    return None

twoSum(nums,target)



# =============================================================================
# 121. Best time to buy and sell stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# =============================================================================


prices = [7,1,5,3,6,4]

def maxProfit(prices):
        maxprofit, minprice = 0, float('inf')
        for price in prices:
            minprice = min(price, minprice)
            profit = price - minprice
            maxprofit = max(maxprofit, profit)
        return maxprofit
maxProfit(prices)    
    
# =============================================================================       
# #217 Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.        
# =============================================================================

def duplicate(nums):
    return (len(list(set(nums))) == len(nums))

def maxSubArray(A):
    if not A:
        return 0

    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum
nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)
