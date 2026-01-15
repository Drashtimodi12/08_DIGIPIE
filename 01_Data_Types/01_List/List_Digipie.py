# # List Tasks

# # Add an element at end
# nums = [3, 1, 5, 2, 4]
# nums.append([1, 4])     
# print(nums)         # [3, 1, 5, 2, 4, [1, 4]]

# print("------------------------")

# # Insert element at index 2
# nums[2] = 6
# print(nums)         # [3, 1, 6, 2, 4, [1, 4]]

# print("------------------------")

# # Remove element by value
# nums.remove(3)
# print(nums)         # [1, 6, 2, 4, [1, 4]]

# print("------------------------")

# # Sort list
# nums1 = [3, 1, 5, 2, 4]
# nums1.sort()
# print(nums1)        # [1, 2, 3, 4, 5]

# print("------------------------")

# # Reverse list
# nums1.sort(reverse=True)
# print(nums1)        # [5, 4, 3, 2, 1]

# print("------------------------")

# # extend
# nums1.extend([10,20,30])
# print(nums1)            # [5, 4, 3, 2, 1, 10, 20, 30]

# print("------------------------")

# # Check if two lists have same elements — order doesn’t matter

# a = [1,2,3]
# b = [3,1,2]


# if sorted(a) == sorted(b):
#     print("Same")
# else:
#     print("Different")
# # Same



import datetime

list1 = ['apple - add time: 17', 'banana - add time: 17']

value = input("Enter item: ")

current_hour = datetime.datetime.now().hour

list1.append(f"{value} - add time: {current_hour}")

print(list1)
# OP:
# Enter item: 2
# ['apple - add time: 17', 'banana - add time: 17', '2 - add time: 11']