def next_higher_with_same_ones(n):
    count = bin(n).count('1')  # count of 1s in n's binary

    current = n + 1
    while True:
        if bin(current).count('1') == count:
            return current
        current += 1
n = 20
result = next_higher_with_same_ones(n)
print("Binary of input 20:", bin(n)[2:])
print("Next number with same 1s:", result)  
print("Binary:", bin(next_higher_with_same_ones(n))[2:])
