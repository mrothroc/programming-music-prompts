#!/usr/bin/env python3
"""
Add or update rating for a prompt.

Usage:
    python add_rating.py 40 "Excellent ⭐"
    python add_rating.py 41 "Excellent - sax texture perfect for midday refresh! ⭐"
"""

import sys
from csv_utils import add_rating

def main():
    if len(sys.argv) < 3:
        print("Usage: python add_rating.py <prompt_id> <rating>")
        print('Example: python add_rating.py 40 "Excellent ⭐"')
        sys.exit(1)

    prompt_id = sys.argv[1]
    rating = sys.argv[2]

    try:
        add_rating(prompt_id, rating)
    except ValueError as e:
        print(f"❌ {e}")

if __name__ == "__main__":
    main()
