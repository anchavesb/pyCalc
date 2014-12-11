"""calc.py: A simple python calculator."""

import sys

if __name__ == '__main__':
    print(sum(map(int, sys.argv[1:])))
