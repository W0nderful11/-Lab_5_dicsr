#!/usr/bin/env python3
import sys
import re

def main():
    word_pattern = re.compile(r"[\w']+")

    for line in sys.stdin:
        line = line.strip()
        words = word_pattern.findall(line)
        
        for word in words:
            print(f"{word.lower()}\t1")

if __name__ == "__main__":
    main()