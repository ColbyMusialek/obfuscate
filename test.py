import os
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    num = int(sys.argv[1])
    print("The factorial of", num, "is", factorial(num))

if __name__ == "__main__":
    main()
