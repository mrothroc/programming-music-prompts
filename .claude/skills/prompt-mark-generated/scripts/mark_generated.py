#!/usr/bin/env python3
"""
Mark one or more prompts as generated.

Usage:
    python mark_generated.py 40
    python mark_generated.py 40 41 42
    python mark_generated.py --all
"""

import sys
from csv_utils import mark_generated, read_prompts, write_prompts

def main():
    if len(sys.argv) < 2:
        print("Usage: python mark_generated.py <prompt_id> [<prompt_id> ...]")
        print("       python mark_generated.py --all")
        sys.exit(1)

    if sys.argv[1] == '--all':
        prompts = read_prompts()
        for prompt in prompts:
            prompt['Generated'] = 'Yes'
        write_prompts(prompts)
        print(f"✅ Marked all {len(prompts)} prompts as Generated=Yes")
    else:
        prompt_ids = sys.argv[1:]
        for prompt_id in prompt_ids:
            try:
                mark_generated(prompt_id)
            except ValueError as e:
                print(f"❌ {e}")

if __name__ == "__main__":
    main()
