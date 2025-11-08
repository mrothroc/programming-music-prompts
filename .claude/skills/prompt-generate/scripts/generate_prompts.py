#!/usr/bin/env python3
"""
Generate new music prompts using genetic algorithm approach.

This script implements the genetic diversity strategy:
- 50% Parent DNA (clones of proven excellent prompts)
- 30% Hybrids (cross-breeding between parents)
- 20% Mutations (new instruments/effects)
"""

import argparse
import csv
from pathlib import Path
from typing import List, Dict
from csv_utils import (
    read_prompts, write_prompts,
    read_influences, get_influences_by_category,
    get_influences_by_status, search_influences,
    get_random_unexplored_influences
)

def get_next_prompt_id() -> int:
    """Get the next available prompt ID."""
    prompts = read_prompts()
    if not prompts:
        return 1
    return max(int(p['Prompt_ID']) for p in prompts) + 1

def find_parent_prompts(time_block: str) -> List[Dict[str, str]]:
    """Find excellent/very good prompts for the given time block."""
    prompts = read_prompts()
    parents = []

    for p in prompts:
        if p['Time_Block'] == time_block:
            rating = p.get('Rating', '').lower()
            if 'excellent' in rating or '⭐' in rating or 'very good' in rating:
                parents.append(p)

    return parents

def list_time_blocks() -> List[str]:
    """List all unique time blocks in the library."""
    prompts = read_prompts()
    blocks = sorted(set(p['Time_Block'] for p in prompts if p['Time_Block']))
    return blocks

def show_parent_candidates(time_block: str):
    """Show potential parent prompts for a time block."""
    parents = find_parent_prompts(time_block)

    if not parents:
        print(f"⚠️  No excellent/very good prompts found for '{time_block}'")
        print("   Consider rating existing prompts first, or manually specify parents.")
        return

    print(f"📊 Found {len(parents)} potential parent prompt(s) for '{time_block}':\n")

    for p in parents:
        print(f"   Prompt {p['Prompt_ID']}: {p['Primary_Genres']}")
        print(f"   BPM: {p['BPM']} | {p['Key_Instruments']}")
        print(f"   Rating: {p['Rating']}")
        print()


def list_mutations_by_category(category: str = None):
    """List available mutation influences, optionally filtered by category."""
    if category:
        influences = get_influences_by_category(category)
        print(f"🧬 Mutation influences in '{category}':\n")
    else:
        influences = read_influences()
        print("🧬 All mutation influences:\n")

    if not influences:
        print(f"   No influences found for category: {category}")
        return

    # Group by category
    by_category = {}
    for inf in influences:
        cat = inf['Category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(inf)

    for cat, items in sorted(by_category.items()):
        print(f"   {cat} ({len(items)}):")
        for inf in items:
            status_icon = {
                'Unexplored': '○',
                'Tested': '◐',
                'Proven': '✓',
                'Avoid': '✗'
            }.get(inf['Status'], '?')
            print(f"     {status_icon} {inf['Influence_ID']:>2}. {inf['Name']}")
        print()


def show_unexplored_mutations(count: int = 10):
    """Show random unexplored mutation ideas."""
    influences = get_random_unexplored_influences(count)

    if not influences:
        print("🎉 All influences have been explored!")
        return

    print(f"🔍 Suggesting {len(influences)} unexplored mutation ideas:\n")

    for inf in influences:
        print(f"   {inf['Influence_ID']:>2}. {inf['Name']} ({inf['Category']})")
        print(f"       Use: {inf['Elements_To_Use'][:80]}...")
        print(f"       Avoid: {inf['Elements_To_Avoid'][:80]}...")
        print()


def search_mutation_ideas(query: str):
    """Search mutation influences by text."""
    results = search_influences(query)

    if not results:
        print(f"❌ No influences found matching: '{query}'")
        return

    print(f"🔍 Found {len(results)} influence(s) matching '{query}':\n")

    for inf in results:
        status_icon = {
            'Unexplored': '○',
            'Tested': '◐',
            'Proven': '✓',
            'Avoid': '✗'
        }.get(inf['Status'], '?')
        print(f"   {status_icon} {inf['Influence_ID']:>2}. {inf['Name']} ({inf['Category']})")
        print(f"       {inf['Elements_To_Use'][:100]}")
        print()

def interactive_generate():
    """Interactive prompt generation wizard."""
    print("🧬 GENETIC ALGORITHM PROMPT GENERATOR")
    print("=" * 60)
    print()

    # Step 1: Choose time block
    blocks = list_time_blocks()
    print("Available time blocks:")
    for i, block in enumerate(blocks, 1):
        print(f"  {i}. {block}")
    print()

    choice = input("Select time block (number or name): ").strip()
    try:
        time_block = blocks[int(choice) - 1]
    except (ValueError, IndexError):
        time_block = choice

    if time_block not in blocks:
        print(f"❌ Unknown time block: {time_block}")
        return

    print(f"\n✓ Selected: {time_block}\n")

    # Step 2: Show parent candidates
    show_parent_candidates(time_block)

    # Step 3: Get generation parameters
    print("Generation parameters:")
    try:
        count = int(input("  How many prompts to generate? [20]: ").strip() or "20")
    except ValueError:
        count = 20

    # Calculate distribution
    parent_clones = int(count * 0.5)
    hybrids = int(count * 0.3)
    mutations = count - parent_clones - hybrids

    print()
    print(f"📊 Distribution for {count} prompts:")
    print(f"   50% Parent DNA: {parent_clones} clones")
    print(f"   30% Hybrids: {hybrids} combinations")
    print(f"   20% Mutations: {mutations} new DNA")
    print()

    # Step 4: Show mutation suggestions
    if mutations > 0:
        print("🧬 MUTATION IDEAS (20% new DNA):\n")
        show_unexplored_mutations(mutations)

        print("💡 For more mutation ideas:")
        print("   - Use `influence-manage --list --category \"<category>\"` to browse by category")
        print("   - Use `influence-manage --search \"<keyword>\"` to find specific influences")
        print("   - Use `influence-manage --show <id>` for detailed guidance")
        print()

    print()
    print(f"📝 Ready to generate {count} prompts for '{time_block}'")
    print()
    print("⚠️  Manual generation workflow:")
    print("   1. Select parent prompts from candidates above")
    print("   2. Create variations (parent clones)")
    print("   3. Combine parents creatively (hybrids)")
    print("   4. Apply mutation influences from suggestions above")
    print("   5. Add new prompts to CSV using appropriate tools")
    print()
    print("For now, use this skill as documentation of the process.")
    print("Actual generation is done manually following the genetic algorithm principles.")

def main():
    parser = argparse.ArgumentParser(
        description='Generate new music prompts using genetic algorithm'
    )
    parser.add_argument(
        '--time-block',
        help='Time block to generate prompts for'
    )
    parser.add_argument(
        '--count',
        type=int,
        default=20,
        help='Number of prompts to generate (default: 20)'
    )
    parser.add_argument(
        '--list-blocks',
        action='store_true',
        help='List all available time blocks'
    )
    parser.add_argument(
        '--show-parents',
        help='Show parent candidates for a time block'
    )
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run interactive generation wizard'
    )
    parser.add_argument(
        '--list-mutations',
        nargs='?',
        const='all',
        help='List mutation influences (optionally filter by category)'
    )
    parser.add_argument(
        '--suggest-mutations',
        type=int,
        nargs='?',
        const=10,
        help='Suggest random unexplored mutations (default: 10)'
    )
    parser.add_argument(
        '--search-mutations',
        help='Search mutation influences by keyword'
    )

    args = parser.parse_args()

    if args.list_blocks:
        blocks = list_time_blocks()
        print("Available time blocks:")
        for block in blocks:
            prompts = read_prompts()
            count = sum(1 for p in prompts if p['Time_Block'] == block)
            print(f"  - {block} ({count} prompts)")
        return

    if args.show_parents:
        show_parent_candidates(args.show_parents)
        return

    if args.list_mutations:
        if args.list_mutations == 'all':
            list_mutations_by_category()
        else:
            list_mutations_by_category(args.list_mutations)
        return

    if args.suggest_mutations is not None:
        show_unexplored_mutations(args.suggest_mutations)
        return

    if args.search_mutations:
        search_mutation_ideas(args.search_mutations)
        return

    if args.interactive or not args.time_block:
        interactive_generate()
        return

    # Non-interactive mode
    print(f"Generating {args.count} prompts for {args.time_block}...")
    print("(Not yet implemented - use interactive mode)")

if __name__ == '__main__':
    main()
