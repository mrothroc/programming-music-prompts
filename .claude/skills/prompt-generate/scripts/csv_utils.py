#!/usr/bin/env python3
"""
CSV utilities for programming_music_prompts.csv

Safe operations that handle quoted fields with internal commas.
Always use these instead of sed/awk/grep for modifications.
"""

import csv
from pathlib import Path
from typing import List, Dict, Optional

CSV_PATH = Path(__file__).parent.parent.parent.parent.parent / "programming_music_prompts.csv"
INFLUENCES_PATH = Path(__file__).parent.parent.parent.parent.parent / "influences_library.csv"


def read_prompts() -> List[Dict[str, str]]:
    """Read all prompts from CSV."""
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_prompts(prompts: List[Dict[str, str]]):
    """Write prompts back to CSV."""
    if not prompts:
        raise ValueError("Cannot write empty prompts list")

    # Use standard fieldnames from the CSV schema
    fieldnames = ['Prompt_ID', 'Time_Block', 'BPM', 'Brain_Wave_Target', 'Duration_Type',
                  'Primary_Genres', 'Key_Instruments', 'Mood_Keywords', 'Suno_Short_Prompt',
                  'Full_Prompt', 'Notes', 'Generated', 'Suno_Refined', 'Rating']

    with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(prompts)


def get_prompt(prompt_id: str) -> Optional[Dict[str, str]]:
    """Get a single prompt by ID."""
    prompts = read_prompts()
    for prompt in prompts:
        if prompt['Prompt_ID'] == prompt_id:
            return prompt
    return None


def update_prompt(prompt_id: str, updates: Dict[str, str]):
    """Update specific fields for a prompt."""
    prompts = read_prompts()
    found = False

    for prompt in prompts:
        if prompt['Prompt_ID'] == prompt_id:
            prompt.update(updates)
            found = True
            break

    if not found:
        raise ValueError(f"Prompt {prompt_id} not found")

    write_prompts(prompts)
    print(f"✅ Updated Prompt {prompt_id}: {updates}")


def mark_generated(prompt_id: str):
    """Mark a prompt as generated."""
    update_prompt(prompt_id, {'Generated': 'Yes'})


def add_rating(prompt_id: str, rating: str):
    """Add or update rating for a prompt."""
    update_prompt(prompt_id, {'Rating': rating})


def find_prompts(**filters) -> List[Dict[str, str]]:
    """
    Find prompts matching filters.

    Examples:
        find_prompts(Time_Block="Midday Refresh")
        find_prompts(Generated="Yes", Rating="")  # Generated but not rated
    """
    prompts = read_prompts()
    results = []

    for prompt in prompts:
        match = True
        for key, value in filters.items():
            if prompt.get(key) != value:
                match = False
                break
        if match:
            results.append(prompt)

    return results


def search_prompts(text: str, fields: Optional[List[str]] = None) -> List[Dict[str, str]]:
    """
    Search for text in prompts.

    Args:
        text: Text to search for (case-insensitive)
        fields: List of field names to search in. If None, searches all fields.

    Examples:
        search_prompts("saxophone")
        search_prompts("mellotron", fields=["Key_Instruments", "Notes"])
    """
    prompts = read_prompts()
    results = []
    text_lower = text.lower()

    for prompt in prompts:
        found = False
        search_fields = fields if fields else prompt.keys()

        for field in search_fields:
            if field in prompt and text_lower in prompt[field].lower():
                found = True
                break

        if found:
            results.append(prompt)

    return results


def get_stats() -> Dict[str, int]:
    """Get statistics about the prompts."""
    prompts = read_prompts()

    stats = {
        'total': len(prompts),
        'generated': len([p for p in prompts if p.get('Generated') == 'Yes']),
        'rated': len([p for p in prompts if p.get('Rating') and p['Rating'].strip()]),
        'excellent': len([p for p in prompts if '⭐' in p.get('Rating', '')]),
    }

    # Count by time block
    time_blocks = {}
    for prompt in prompts:
        block = prompt.get('Time_Block', 'Unknown')
        time_blocks[block] = time_blocks.get(block, 0) + 1

    stats['by_time_block'] = time_blocks

    return stats


def print_prompt(prompt: Dict[str, str], verbose: bool = False):
    """Pretty print a prompt."""
    print(f"\n{'='*60}")
    print(f"Prompt {prompt['Prompt_ID']}: {prompt['Time_Block']}")
    print(f"{'='*60}")
    print(f"BPM: {prompt['BPM']} | {prompt['Brain_Wave_Target']}")
    print(f"Genres: {prompt['Primary_Genres']}")
    print(f"Instruments: {prompt['Key_Instruments']}")

    if verbose:
        print(f"\nMood: {prompt['Mood_Keywords']}")
        print(f"\nSuno Prompt:\n{prompt['Suno_Short_Prompt']}")
        print(f"\nFull Description:\n{prompt['Full_Prompt']}")

    print(f"\nNotes: {prompt['Notes']}")
    print(f"Generated: {prompt['Generated']}")

    if prompt.get('Rating') and prompt['Rating'].strip():
        print(f"Rating: {prompt['Rating']}")


def read_influences() -> List[Dict[str, str]]:
    """Read all influences from influences_library.csv."""
    with open(INFLUENCES_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def get_influences_by_category(category: str) -> List[Dict[str, str]]:
    """Get all influences in a specific category."""
    influences = read_influences()
    return [inf for inf in influences if inf['Category'] == category]


def get_influences_by_status(status: str) -> List[Dict[str, str]]:
    """Get all influences with a specific status (Unexplored, Tested, Proven, Avoid)."""
    influences = read_influences()
    return [inf for inf in influences if inf['Status'] == status]


def search_influences(text: str) -> List[Dict[str, str]]:
    """Search influences by text in Name, Elements_To_Use, or Adaptation_Notes."""
    influences = read_influences()
    results = []
    text_lower = text.lower()

    for inf in influences:
        if (text_lower in inf['Name'].lower() or
            text_lower in inf['Elements_To_Use'].lower() or
            text_lower in inf['Adaptation_Notes'].lower()):
            results.append(inf)

    return results


def get_random_unexplored_influences(count: int = 5, category: str = None) -> List[Dict[str, str]]:
    """Get random unexplored influences, optionally filtered by category."""
    import random

    influences = get_influences_by_status('Unexplored')

    if category:
        influences = [inf for inf in influences if inf['Category'] == category]

    if len(influences) <= count:
        return influences

    return random.sample(influences, count)


def get_weighted_mutation_influences(count: int = 5) -> List[Dict[str, str]]:
    """
    Get mutation influences weighted by prompt ratings across all time blocks.

    Strategy:
    1. Extract instruments/genres from highly-rated prompts (excellent, very good)
    2. Match against influences library
    3. Prioritize unexplored influences that appear in rated prompts
    4. Fall back to random unexplored if no matches

    Returns influences weighted toward what's worked well in other time blocks.
    """
    import random
    from collections import Counter

    prompts = read_prompts()
    influences = read_influences()

    # Get highly-rated prompts across ALL time blocks
    rated_prompts = [p for p in prompts if 'excellent' in p.get('Rating', '').lower()
                     or '⭐' in p.get('Rating', '')
                     or 'very good' in p.get('Rating', '').lower()]

    # Extract instruments from rated prompts
    rated_instruments = []
    for p in rated_prompts:
        instruments = p.get('Key_Instruments', '').lower()
        # Split by comma and clean up
        for instr in instruments.split(','):
            rated_instruments.append(instr.strip())

    # Count frequency of instruments in rated prompts
    instrument_freq = Counter(rated_instruments)

    # Score unexplored influences by how often they appear in rated prompts
    unexplored = get_influences_by_status('Unexplored')
    scored_influences = []

    for inf in unexplored:
        name_lower = inf['Name'].lower()
        # Check if influence name appears in rated instruments
        score = 0
        for instr, freq in instrument_freq.items():
            if name_lower in instr or instr in name_lower:
                score += freq

        scored_influences.append((score, inf))

    # Sort by score (highest first), then shuffle within same score
    scored_influences.sort(key=lambda x: x[0], reverse=True)

    # Take weighted selection: 70% from top-scoring, 30% random for diversity
    weighted_count = int(count * 0.7)
    random_count = count - weighted_count

    result = []

    # Get top-scoring influences (those that appear in rated prompts)
    top_scored = [inf for score, inf in scored_influences if score > 0]
    if top_scored and weighted_count > 0:
        result.extend(random.sample(top_scored, min(weighted_count, len(top_scored))))

    # Fill remaining with random unexplored
    remaining_needed = count - len(result)
    if remaining_needed > 0:
        available = [inf for score, inf in scored_influences if inf not in result]
        if available:
            result.extend(random.sample(available, min(remaining_needed, len(available))))

    return result[:count]


if __name__ == "__main__":
    # Quick test
    stats = get_stats()
    print("📊 Prompt Statistics:")
    print(f"  Total: {stats['total']}")
    print(f"  Generated: {stats['generated']}")
    print(f"  Rated: {stats['rated']}")
    print(f"  Excellent (⭐): {stats['excellent']}")
    print(f"\n📁 By Time Block:")
    for block, count in stats['by_time_block'].items():
        print(f"  {block}: {count}")
