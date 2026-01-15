# Write a function that calculates simple interest given (P, R, T).

def i(P, R, T):
    si = (P * R * T) / 100
    print(f"Principal: {P}, Rate: {R}%, Time: {T} year(s)")
    print(f"The simple interest is {si}.")
i(10000, 7, 1)
# OP:
# Principal: 10000, Rate: 7%, Time: 1 year(s)
# The simple interest is 700.0.