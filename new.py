import os
import sys

def A(n):
    if n == 0:
        return 1
    else:
        return n * A(n-1)

def main():
    num = int(sys.argv[1])
    print("The A of", num, "is", A(num))

if __name__ == "__main__":
    main()
