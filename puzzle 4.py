def next_higher_with_same_ones(n):
    c = n
    c0 = c1 = 0

    # Count trailing 0s
    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1

    # Count ones after the trailing 0s
    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    # If all bits are 1s followed by 0s (e.g., 11110000), no bigger number possible
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    # Position of rightmost non-trailing 0
    pos = c0 + c1

    # Flip rightmost non-trailing 0
    n |= (1 << pos)

    # Clear all bits to the right of pos
    n &= ~((1 << pos) - 1)

    # Insert (c1-1) ones on the right
    n |= (1 << (c1 - 1)) - 1

    return n

# === Hardcoded Input ===
input_number = 13948  # Binary: 0b11011001111100
next_number = next_higher_with_same_ones(input_number)

# === Output Result ===
print(f"Input: {input_number} (binary: {bin(input_number)})")
print(f"Next higher number with same number of 1s: {next_number} (binary: {bin(next_number)})")
