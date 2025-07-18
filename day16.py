#linear search (brute force)
# def brute(nums,key):
#     for i in range(len(nums)):
#         if nums[i] == key:
#             return i
#     return -1
# num = [10,20,1,45,2,98,101]
# print(brute(num,2))

#binary search (divide & conqueer)
# def binary(nums,key):
#     low = 0
#     high = len(nums) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] == key:
#             return mid
#         elif nums[mid] < key:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# num = [10,20,30,40,50,60,70]
# print(binary(num,10))

#bubble sort(swapping)
# def bubble(nums):
#     length = len(nums)
#     for i in range(length):
#         for j in range(0,length-i-1):
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums
# num = [1,5,2,9,4,2,8,5,3]
# print(bubble(num))

#selection sort (select min vlue each time)
# def select(nums):
#     n = len(nums)
#     for i in range(n):
#         m = i
#         for j in range(i+1, n):
#             if nums[j] < nums[m]:
#                 m = j
#         nums[i], nums[m] = nums[m], nums[i]
#     return nums
# num = [5,3,8,2,1,9,2,1]
# print(select(num))

#insertion sort (like card sorting in hand)
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key

# nums = [12, 11, 13, 5, 6]
# insertion_sort(nums)
# print(nums)

