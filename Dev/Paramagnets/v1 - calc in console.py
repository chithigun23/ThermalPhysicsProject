import math as m

# Convert exponential notation to a float value
#eg.  5e6 becomes 5*10**6
def convert_to_float(s):
    if 'e' in s:
        base, exponent = s.split('e')
        return float(base) * 10 ** int(exponent)
    else:
        return float(s)

# Ask user for omega
omega_str = input("Enter the value of omega: ")

# Convert the input string to a float value, accounting for exponential notation
omega = convert_to_float(omega_str.replace("*10^", "e"))

# Set the value of k
k = 1.380649e-23

# Calculate S using equation S=k∙ln(Ω)
S = k * m.log(omega)

# Display the result
print(f"S = {S}")
