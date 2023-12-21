import sys

def factorize(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return i, num // i
    return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        return

    file_name = sys.argv[1]
    try:
        with open(file_name, 'r') as file:
            numbers = file.read().splitlines()
            for num in numbers:
                num = int(num)
                factor1, factor2 = factorize(num)
                print(f"{num}={factor1}*{factor2}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except ValueError:
        print("Invalid input in the file.")
