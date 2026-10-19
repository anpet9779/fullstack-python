# floating and real numbers

import sys

ideal_temp = 95.5
current_temp = 95.4999999999

print(f"ideal_temp: {ideal_temp}")
print(f"current_temp: {current_temp}")

print(f"difference temp: {ideal_temp - current_temp}") 
# Output: difference temp is 1.000017846308765e-10 instead of  0.0000000001

# This is because floating point numbers are not exact, they have a limited number of digits of precision.

# To get a more accurate result, we can use 'sys' package it has float_info attribute which give info about precision of floating point numbers.

print(sys.float_info) 
# Output:sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)


# We can also use 'fractions' and 'decimals' as well to get more accurate results