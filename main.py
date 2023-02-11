
coeff = input("Please write the coefficients of polynomial function: ")
all_coeff = coeff.split(" ")
def print_polynomial(sol):
    poly = ""
    for a, i in zip(sol, range(len(sol)-1, -1, -1)):
        if eval(a) > 0:
            poly += "+ "
        poly += a
        if i == 0:
            break
        poly += "x^" + str(i) + " "
    print("f(x): ", poly)
print_polynomial(all_coeff)

print("Please write the boundaries of integration:")
a = eval(input("a = "))
b = eval(input("b = "))

def find_value(polynomial, x):
    poly_val = 0
    for s, p in zip(polynomial, range(len(polynomial)-1, -1, -1)):
        poly_val += s * x ** p
    return poly_val

polynomial = [eval(p) for p in all_coeff]
f_at_b = find_value(polynomial, b)
f_at_a = find_value(polynomial, a)

# integration by trapezoidal method
h = (b - a)/100
integration = 0
x_i = a
for i in range(100):
    x_i += h
    f_x_i = find_value(polynomial, x_i)
    integration += f_x_i

integration *= 2
integration += find_value(polynomial, a) + find_value(polynomial, b)
integration *= h/2
print("Integration by trapezoidal method:", round(integration, 4))

# Integration by simpson method
x_i = a
integration = 0
even_sum = 0
# integration += find_value(polynomial, a)
h = (b-a)/100
for i in range(100):
    x_i += h
    f_at_xi = find_value(polynomial, x_i)
    if i % 2 == 0:
        even_sum += f_at_xi
even_sum *= 2

odd_sum = 0
x_i = a
for i in range(100):
    x_i += h
    f_at_xi = find_value(polynomial, x_i)
    if i % 2 != 0:
        odd_sum += f_at_xi
odd_sum *= 4
integration = find_value(polynomial, a) + odd_sum + even_sum + find_value(polynomial, b)
integration *= h/3
print("Integration by Simpson method:", round(integration, 4))


def find_value_for_x(equation, x):
    putting_x = ""
    for i in equation:
        if i == "x":
            putting_x += str(x)
        elif i == "^":
            putting_x += "**"
        else:
            putting_x += i
    value_of_x = eval(putting_x)
    return value_of_x

print()
equation = input("Please write the function:\n")
print("The function you have entered is:")
print(equation)

print("Please write the boundaries of integration:")
a = eval(input("a = "))
b = eval(input("b = "))

# integration by trapezoidal method
h = (b - a)/100
integration = 0
x_i = a
for i in range(100):
    x_i += h
    f_x_i = find_value_for_x(equation, x_i)
    integration += f_x_i

integration *= 2
integration += find_value_for_x(equation, a) + find_value_for_x(equation, b)
integration *= h/2
print("Integration by trapezoidal method:", round(integration, 4))


# Integration by simpson method
x_i = a
integration = 0
even_sum = 0
# integration += find_value(polynomial, a)
h = (b-a)/100
for i in range(100):
    x_i += h
    f_at_xi = find_value_for_x(equation, x_i)
    if i % 2 == 0:
        even_sum += f_at_xi
even_sum *= 2

odd_sum = 0
x_i = a
for i in range(100):
    x_i += h
    f_at_xi = find_value_for_x(equation, x_i)
    if i % 2 != 0:
        odd_sum += f_at_xi
odd_sum *= 4
integration = find_value_for_x(equation, a) + odd_sum + even_sum + find_value_for_x(equation, b)
integration *= h/3
print("Integration by Simpson method:", round(integration, 4))