#!/usr/bin/env python3
"""
Show details for a specific prompt.

Usage:
    python show_prompt.py 40
    python show_prompt.py 40 --verbose
"""

import sys
from csv_utils import get_prompt, print_prompt

def main():
    if len(sys.argv) < 2:
        print("Usage: python show_prompt.py <prompt_id> [--verbose]")
        sys.exit(1)

    prompt_id = sys.argv[1]
    verbose = '--verbose' in sys.argv or '-v' in sys.argv

    prompt = get_prompt(prompt_id)

    if not prompt:
        print(f"❌ Prompt {prompt_id} not found")
        sys.exit(1)

    print_prompt(prompt, verbose=verbose)

if __name__ == "__main__":
    main()
