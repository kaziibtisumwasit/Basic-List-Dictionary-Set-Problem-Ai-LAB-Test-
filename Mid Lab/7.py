# Write a Python program to find the second smallest and largest number in a list .
# Unsorted list

l1 = [30, 10, 50, 20, 40, 90, 60, 100, 70, 80]

l1.sort()

print(f"Second Smallest Number : {l1[1]}")
print(f"Second Largest Number : {l1[len(l1)-2]}")
