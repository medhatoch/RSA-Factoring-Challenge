import sys

def factorize(n):
    factors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                n = int(line.strip())
                factor_pairs = factorize(n)
                if factor_pairs:
                    for p, q in factor_pairs:
                        print(f"{n}={p}*{q}")
                else:
                    print(f"{n} is a prime number")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print(f"Invalid input in '{filename}'. All lines must contain valid natural numbers greater than 1.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    main(filename)
