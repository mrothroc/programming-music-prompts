#!/usr/bin/env python3
"""
Find prompts by various criteria.

Usage:
    python find_prompts.py --time-block "Midday Refresh"
    python find_prompts.py --bpm 108
    python find_prompts.py --generated no
    python find_prompts.py --rated yes
    python find_prompts.py --excellent
    python find_prompts.py --search "saxophone"
"""

import sys
from csv_utils import find_prompts, search_prompts, print_prompt

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python find_prompts.py --time-block <block_name>")
        print("  python find_prompts.py --bpm <bpm>")
        print("  python find_prompts.py --generated yes|no")
        print("  python find_prompts.py --rated yes|no")
        print("  python find_prompts.py --excellent")
        print("  python find_prompts.py --search <text>")
        sys.exit(1)

    arg = sys.argv[1]
    results = []

    if arg == '--time-block' and len(sys.argv) > 2:
        results = find_prompts(Time_Block=sys.argv[2])

    elif arg == '--bpm' and len(sys.argv) > 2:
        results = find_prompts(BPM=sys.argv[2])

    elif arg == '--generated':
        value = 'Yes' if len(sys.argv) < 3 or sys.argv[2].lower() == 'yes' else ''
        results = find_prompts(Generated=value)

    elif arg == '--rated':
        if len(sys.argv) > 2 and sys.argv[2].lower() == 'no':
            # Find prompts without ratings
            all_prompts = find_prompts()
            results = [p for p in all_prompts if not p.get('Rating') or not p['Rating'].strip()]
        else:
            # Find prompts with ratings
            all_prompts = find_prompts()
            results = [p for p in all_prompts if p.get('Rating') and p['Rating'].strip()]

    elif arg == '--excellent':
        all_prompts = find_prompts()
        results = [p for p in all_prompts if '⭐' in p.get('Rating', '')]

    elif arg == '--search' and len(sys.argv) > 2:
        results = search_prompts(sys.argv[2])

    else:
        print(f"❌ Unknown argument: {arg}")
        sys.exit(1)

    if not results:
        print("No prompts found matching criteria.")
        sys.exit(0)

    print(f"\n✅ Found {len(results)} prompt(s):\n")
    for prompt in results:
        print(f"  {prompt['Prompt_ID']:>6} | {prompt['Time_Block']:30} | BPM {prompt['BPM']:>3} | {prompt['Primary_Genres']}")
        if prompt.get('Rating') and prompt['Rating'].strip():
            print(f"         └─ {prompt['Rating']}")

if __name__ == "__main__":
    main()
