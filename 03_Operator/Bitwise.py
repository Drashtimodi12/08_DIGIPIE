# Bitwise Operators: &, |, ^, ~, <<, >>

a = 10  # 1010 in binary
b = 4   # 0100 in binary


# Bitwise AND
c = a & b  # Bitwise AND operation
print("Bitwise AND:", c)  # Output: 0 (0000 in binary)

# Bitwise OR
c = a | b  # Bitwise OR operation   
print("Bitwise OR:", c)  # Output: 14 (1110 in binary)

# Bitwise XOR
c = a ^ b  # Bitwise XOR operation
print("Bitwise XOR:", c)  # Output: 14 (1110 in binary)

# Bitwise NOT
c = ~a  # Bitwise NOT operation
print("Bitwise NOT:", c)  # Output: -11 (inverts all bits, 1010 becomes 0101, which is -11 in two's complement)

# Left Shift
c = a << 2  # Left shift by 2 bits
print("Left Shift:", c)  # Output: 40 (101000 in binary)

# Right Shift
c = a >> 2  # Right shift by 2 bits
print("Right Shift:", c)  # Output: 2 (0010 in binary)