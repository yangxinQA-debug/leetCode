if __name__ == "__main__":
    # def remainder(x, a, p):
    x = 3
    a = 10
    p = 100
    rem = 1
    for _ in range(a):
        rem = (rem * x) % p
    print(rem)
