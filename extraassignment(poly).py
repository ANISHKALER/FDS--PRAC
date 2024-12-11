n=int(input())
a=input()
b=input()
value_of_x = float(input("Enter the value of x: "))

sum_str =""

for i in range(n):
    sum_str+=a[i]+'x'+'^'+b[i]+'+'
sum_str = sum_str.rstrip(' + ')

print(sum_str)
polynomial_value = 0

polynomial_value = 0
for coeff, power in zip(a[i], b[i]):
    polynomial_value += coeff * (value_of_x ** power)

print(f"Value of the polynomial for x={value_of_x}: {polynomial_value}")