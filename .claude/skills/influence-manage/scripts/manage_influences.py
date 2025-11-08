#!/usr/bin/env python3
"""
Influence Library Management Script

Manage the influences_library.csv database for genetic algorithm mutations.
"""

import argparse
import sys
from csv_utils import (
    read_influences,
    get_influence,
    update_influence,
    add_influence,
    mark_used,
    find_influences,
    search_influences,
    get_stats,
    print_influence
)


def list_influences(category=None, status=None):
    """List all influences with optional filtering."""
    filters = {}
    if category:
        filters['Category'] = category
    if status:
        filters['Status'] = status

    influences = find_influences(**filters) if filters else read_influences()

    if not influences:
        print("No influences found matching criteria.")
        return

    print(f"\n📚 INFLUENCE LIBRARY ({len(influences)} influences)")
    print("=" * 80)

    # Group by category
    by_category = {}
    for inf in influences:
        cat = inf.get('Category', 'Unknown')
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(inf)

    for cat in sorted(by_category.keys()):
        print(f"\n{cat}:")
        for inf in sorted(by_category[cat], key=lambda x: int(x['Influence_ID'])):
            used_marker = "✓" if inf.get('Used_In_Prompts', '').strip() else " "
            status_icon = {
                'Unexplored': '○',
                'Tested': '◐',
                'Proven': '⭐',
                'Avoid': '✗'
            }.get(inf['Status'], '?')

            print(f"  [{used_marker}] #{inf['Influence_ID']:>2} {status_icon} {inf['Name']:<30} ({inf['Status']})")


def search_influences_cmd(text, fields=None):
    """Search for influences by text."""
    results = search_influences(text, fields)

    if not results:
        print(f"No influences found matching '{text}'")
        return

    print(f"\n🔍 SEARCH RESULTS for '{text}' ({len(results)} found)")
    print("=" * 80)

    for inf in results:
        used_marker = "✓" if inf.get('Used_In_Prompts', '').strip() else " "
        status_icon = {
            'Unexplored': '○',
            'Tested': '◐',
            'Proven': '⭐',
            'Avoid': '✗'
        }.get(inf['Status'], '?')

        print(f"\n[{used_marker}] #{inf['Influence_ID']:>2} {status_icon} {inf['Name']} ({inf['Category']})")
        print(f"    Status: {inf['Status']}")
        print(f"    Use: {inf['Elements_To_Use'][:80]}...")


def show_influence(influence_id):
    """Show detailed information for an influence."""
    influence = get_influence(str(influence_id))

    if not influence:
        print(f"❌ Influence {influence_id} not found")
        sys.exit(1)

    print_influence(influence, verbose=True)


def add_influence_cmd(category, name, elements, avoid, notes):
    """Add a new influence to the library."""
    influence_data = {
        'Category': category,
        'Name': name,
        'Elements_To_Use': elements,
        'Elements_To_Avoid': avoid,
        'Adaptation_Notes': notes,
        'Used_In_Prompts': '',
        'Status': 'Unexplored'
    }

    new_id = add_influence(influence_data)
    print(f"\n✅ Successfully added influence #{new_id}")

    # Show the new influence
    show_influence(new_id)


def mark_influence_used(influence_id, prompt_ids_str):
    """Mark an influence as used in prompts."""
    prompt_ids = [p.strip() for p in prompt_ids_str.split(',')]
    mark_used(str(influence_id), prompt_ids)

    print(f"\n✅ Marked influence #{influence_id} as used in prompts: {', '.join(prompt_ids)}")


def update_status(influence_id, status):
    """Update the status of an influence."""
    valid_statuses = ['Unexplored', 'Tested', 'Proven', 'Avoid']

    if status not in valid_statuses:
        print(f"❌ Invalid status. Must be one of: {', '.join(valid_statuses)}")
        sys.exit(1)

    update_influence(str(influence_id), {'Status': status})

    print(f"\n✅ Updated influence #{influence_id} status to: {status}")


def show_stats():
    """Show statistics about the influences library."""
    stats = get_stats()

    print("\n📊 INFLUENCE LIBRARY STATISTICS")
    print("=" * 50)
    print(f"  Total influences:    {stats['total']}")
    print(f"  Used:                {stats['used']}")
    print(f"  Unexplored:          {stats['unexplored']}")
    print(f"  Tested:              {stats['tested']}")
    print(f"  Proven:              {stats['proven']}")
    print(f"  Avoid:               {stats['avoid']}")

    print(f"\n📁 By Category:")
    for cat in sorted(stats['by_category'].keys()):
        count = stats['by_category'][cat]
        print(f"  {cat:<30} {count:>2}")

    print()


def main():
    parser = argparse.ArgumentParser(
        description='Manage the influences library for genetic algorithm mutations'
    )

    # List command
    parser.add_argument('--list', action='store_true',
                        help='List all influences')
    parser.add_argument('--category', type=str,
                        help='Filter by category')
    parser.add_argument('--status', type=str,
                        choices=['Unexplored', 'Tested', 'Proven', 'Avoid'],
                        help='Filter by status')

    # Search command
    parser.add_argument('--search', type=str,
                        help='Search influences by text')

    # Show command
    parser.add_argument('--show', type=int,
                        help='Show detailed information for an influence ID')

    # Add command
    parser.add_argument('--add', action='store_true',
                        help='Add a new influence')
    parser.add_argument('--name', type=str,
                        help='Name of the influence')
    parser.add_argument('--elements', type=str,
                        help='Elements to use')
    parser.add_argument('--avoid', type=str,
                        help='Elements to avoid')
    parser.add_argument('--notes', type=str,
                        help='Adaptation notes')

    # Mark used command
    parser.add_argument('--mark-used', type=int,
                        help='Mark influence as used (provide influence ID)')
    parser.add_argument('--prompt-ids', type=str,
                        help='Comma-separated list of prompt IDs')

    # Update status command
    parser.add_argument('--update-status', type=int,
                        help='Update influence status (provide influence ID)')

    # Stats command
    parser.add_argument('--stats', action='store_true',
                        help='Show statistics')

    args = parser.parse_args()

    # Execute commands
    if args.list:
        list_influences(args.category, args.status)

    elif args.search:
        search_influences_cmd(args.search)

    elif args.show is not None:
        show_influence(args.show)

    elif args.add:
        if not all([args.category, args.name, args.elements, args.avoid, args.notes]):
            print("❌ --add requires: --category, --name, --elements, --avoid, --notes")
            sys.exit(1)
        add_influence_cmd(args.category, args.name, args.elements, args.avoid, args.notes)

    elif args.mark_used is not None:
        if not args.prompt_ids:
            print("❌ --mark-used requires --prompt-ids")
            sys.exit(1)
        mark_influence_used(args.mark_used, args.prompt_ids)

    elif args.update_status is not None:
        if not args.status:
            print("❌ --update-status requires --status")
            sys.exit(1)
        update_status(args.update_status, args.status)

    elif args.stats:
        show_stats()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
