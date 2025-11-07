#!/usr/bin/env python3
"""
Show statistics about the prompt library.

Usage:
    python stats.py
"""

from csv_utils import get_stats

def main():
    stats = get_stats()

    print("\n" + "="*60)
    print("📊 PROMPT LIBRARY STATISTICS")
    print("="*60)

    print(f"\n📈 Overall:")
    print(f"  Total prompts:       {stats['total']}")
    print(f"  Generated:           {stats['generated']} ({stats['generated']/stats['total']*100:.1f}%)")
    print(f"  Rated:               {stats['rated']} ({stats['rated']/stats['total']*100:.1f}%)")
    print(f"  Excellent (⭐):       {stats['excellent']}")

    print(f"\n📁 By Time Block:")
    for block, count in sorted(stats['by_time_block'].items()):
        print(f"  {block:30} {count:>2}")

    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
