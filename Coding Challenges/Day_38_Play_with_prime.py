# Prime number utility functions

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nearest_prime(num):
    """Find nearest prime to num"""
    offset = 0
    while True:
        lower = num - offset
        upper = num + offset
        if lower > 1 and is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        offset += 1

def primes_in_range(start, end):
    """List primes in a range"""
    return [n for n in range(start, end + 1) if is_prime(n)]

def first_n_primes(n):
    """Get first n primes"""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def sum_primes_upto(n):
    """Sum of primes up to n"""
    return sum(num for num in range(2, n + 1) if is_prime(num))


# Main menu
while True:
    print("\nPrime Number Operations")
    print("1. Check if a number is prime")
    print("2. Find nearest prime to a number")
    print("3. Display all primes in a range")
    print("4. Display first N prime numbers")
    print("5. Sum of primes up to N")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        num = int(input("Enter a number: "))
        print(f"{num} is prime? {is_prime(num)}")

    elif choice == '2':
        num = int(input("Enter a number: "))
        print(f"Nearest prime to {num} is {nearest_prime(num)}")

    elif choice == '3':
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        print("Primes in range:", primes_in_range(start, end))

    elif choice == '4':
        n = int(input("How many primes you want: "))
        print(f"First {n} primes:", first_n_primes(n))

    elif choice == '5':
        n = int(input("Enter N: "))
        print(f"Sum of primes up to {n} = {sum_primes_upto(n)}")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-6.")
