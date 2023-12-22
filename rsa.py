#!/usr/bin/env python3

import sys


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def rsa_factorize(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            if is_prime(i) and is_prime(num // i):
                return f"{num}={i}*{num // i}"
    return f"{num}={num}*1"


def main(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
        for number in numbers:
            number = int(number.strip())
            print(rsa_factorize(number))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <file>")
        sys.exit(1)
    main(sys.argv[1])
