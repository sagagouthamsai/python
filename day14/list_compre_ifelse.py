#if else case in list comprehension

#syntax : [expression for item in iterable if condition else expression]
squares_cubes = [x**2 if x%2==0 else x**3 for x in range(10)]
print(squares_cubes)

nums = [1,2,3,4]

result = ["Even" if x%2==0 else "Odd" for x in nums]
print(result)

#nested if else in list comprehension
#syntax : [expression for item in iterable if condition else expression for item in iterable if condition else expression]
nested_result = ["Even" if x%2==0 else "Odd" if x%3==0 else "Other" for x in range(1,11)]
print(nested_result)
