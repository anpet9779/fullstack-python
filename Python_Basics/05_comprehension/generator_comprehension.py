# Generator comprehension is same as list comprehension only change comes in for expression -- which is ultimate goal is considered as expression

# (expression for item in iterable if condition)

# difference between list and generator comprehension is that entire list is not stored in memory at a time. while generator is like stream(on the fly)



# example 1: 

daily_sales = [5, 10, 12, 7, 3, 8, 9, 6, 11, 4]

# find sales above 5 and make sum of them

total_sales = sum(sale for sale in daily_sales if sale > 5)

print(f"Total sales : {total_sales}")

""" 
Here, each sale is considered as expression and sum is considered as ultimate goal so every sale is getting added to sum one by one

So the out would be sum of all sales above 5

whereas if we had used list comprehension then the out would be list of all sales above 5

then we would have to convert it to sum separately
which is again memory intensive

"""
