#!/usr/bin/env python3
"""
CSV utilities for influences_library.csv

Safe operations that handle quoted fields with internal commas.
Always use these instead of sed/awk/grep for modifications.
"""

import csv
from pathlib import Path
from typing import List, Dict, Optional

CSV_PATH = Path(__file__).parent.parent.parent.parent.parent / "influences_library.csv"


def read_influences() -> List[Dict[str, str]]:
    """Read all influences from CSV."""
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_influences(influences: List[Dict[str, str]]):
    """Write influences back to CSV."""
    if not influences:
        raise ValueError("Cannot write empty influences list")

    fieldnames = list(influences[0].keys())

    with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(influences)


def get_influence(influence_id: str) -> Optional[Dict[str, str]]:
    """Get a single influence by ID."""
    influences = read_influences()
    for influence in influences:
        if influence['Influence_ID'] == influence_id:
            return influence
    return None


def update_influence(influence_id: str, updates: Dict[str, str]):
    """Update specific fields for an influence."""
    influences = read_influences()
    found = False

    for influence in influences:
        if influence['Influence_ID'] == influence_id:
            influence.update(updates)
            found = True
            break

    if not found:
        raise ValueError(f"Influence {influence_id} not found")

    write_influences(influences)
    print(f"✅ Updated Influence {influence_id}: {updates}")


def add_influence(influence_data: Dict[str, str]):
    """Add a new influence to the library."""
    influences = read_influences()

    # Generate new ID
    max_id = max(int(inf['Influence_ID']) for inf in influences)
    new_id = str(max_id + 1)

    influence_data['Influence_ID'] = new_id

    # Set default status if not provided
    if 'Status' not in influence_data:
        influence_data['Status'] = 'Unexplored'

    # Set default Used_In_Prompts if not provided
    if 'Used_In_Prompts' not in influence_data:
        influence_data['Used_In_Prompts'] = ''

    influences.append(influence_data)
    write_influences(influences)

    print(f"✅ Added new influence {new_id}: {influence_data['Name']}")
    return new_id


def mark_used(influence_id: str, prompt_ids: List[str]):
    """Mark an influence as used in specific prompts."""
    influence = get_influence(influence_id)
    if not influence:
        raise ValueError(f"Influence {influence_id} not found")

    # Merge with existing prompt IDs
    existing = influence.get('Used_In_Prompts', '').strip()
    existing_ids = set(existing.split(',')) if existing else set()
    existing_ids.update(prompt_ids)

    new_used = ','.join(sorted(existing_ids, key=lambda x: int(x) if x.isdigit() else 0))

    update_influence(influence_id, {'Used_In_Prompts': new_used})


def find_influences(**filters) -> List[Dict[str, str]]:
    """
    Find influences matching filters.

    Examples:
        find_influences(Category="Acoustic Instruments")
        find_influences(Status="Unexplored")
    """
    influences = read_influences()
    results = []

    for influence in influences:
        match = True
        for key, value in filters.items():
            if influence.get(key) != value:
                match = False
                break
        if match:
            results.append(influence)

    return results


def search_influences(text: str, fields: Optional[List[str]] = None) -> List[Dict[str, str]]:
    """
    Search for text in influences.

    Args:
        text: Text to search for (case-insensitive)
        fields: List of field names to search in. If None, searches all fields.

    Examples:
        search_influences("saxophone")
        search_influences("delay", fields=["Name", "Elements_To_Use"])
    """
    influences = read_influences()
    results = []
    text_lower = text.lower()

    for influence in influences:
        found = False
        search_fields = fields if fields else influence.keys()

        for field in search_fields:
            if field in influence and text_lower in influence[field].lower():
                found = True
                break

        if found:
            results.append(influence)

    return results


def get_stats() -> Dict:
    """Get statistics about the influences library."""
    influences = read_influences()

    stats = {
        'total': len(influences),
        'used': len([i for i in influences if i.get('Used_In_Prompts', '').strip()]),
        'unexplored': len([i for i in influences if i.get('Status') == 'Unexplored']),
        'tested': len([i for i in influences if i.get('Status') == 'Tested']),
        'proven': len([i for i in influences if i.get('Status') == 'Proven']),
        'avoid': len([i for i in influences if i.get('Status') == 'Avoid']),
    }

    # Count by category
    categories = {}
    for influence in influences:
        cat = influence.get('Category', 'Unknown')
        categories[cat] = categories.get(cat, 0) + 1

    stats['by_category'] = categories

    return stats


def print_influence(influence: Dict[str, str], verbose: bool = False):
    """Pretty print an influence."""
    print(f"\n{'='*70}")
    print(f"Influence #{influence['Influence_ID']}: {influence['Name']}")
    print(f"{'='*70}")
    print(f"Category: {influence['Category']}")
    print(f"Status: {influence['Status']}")

    if influence.get('Used_In_Prompts', '').strip():
        print(f"Used in prompts: {influence['Used_In_Prompts']}")
    else:
        print(f"Used in prompts: None (virgin territory!)")

    print(f"\n✅ Elements to USE:")
    print(f"  {influence['Elements_To_Use']}")

    print(f"\n❌ Elements to AVOID:")
    print(f"  {influence['Elements_To_Avoid']}")

    print(f"\n📝 Adaptation Notes:")
    print(f"  {influence['Adaptation_Notes']}")


if __name__ == "__main__":
    # Quick test
    stats = get_stats()
    print("📊 Influence Library Statistics:")
    print(f"  Total: {stats['total']}")
    print(f"  Used: {stats['used']}")
    print(f"  Unexplored: {stats['unexplored']}")
    print(f"  Tested: {stats['tested']}")
    print(f"  Proven: {stats['proven']}")
    print(f"  Avoid: {stats['avoid']}")
    print(f"\n📁 By Category:")
    for cat, count in stats['by_category'].items():
        print(f"  {cat}: {count}")
