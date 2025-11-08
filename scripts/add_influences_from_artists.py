#!/usr/bin/env python3
"""
Add influences from Apple Music listening history to influences_library.csv

This script helps convert your favorite artists into structured influences
with clear guidance on what elements to use vs avoid for programming music.
"""

import sys
from pathlib import Path

# Add parent directory to path to import csv_utils
sys.path.insert(0, str(Path(__file__).parent.parent / '.claude/skills/influence-manage/scripts'))

from csv_utils import read_influences, write_influences, add_influence

# Top artists from Apple Music analysis that are instrumental/programming-appropriate
ARTIST_SUGGESTIONS = [
    {
        'name': 'Jazzanova',
        'plays': 177,
        'category': 'Genre Influences',
        'description': 'Nu-jazz/downtempo fusion',
        'use': 'Broken beat rhythms, jazz instrumentation, smooth grooves, organic production',
        'avoid': 'Vocal features, dramatic builds, attention-demanding solos',
        'notes': 'Jazzanova blends jazz warmth with electronic precision - use the laid-back grooves and acoustic instruments over downtempo beats, avoid their more upbeat club tracks'
    },
    {
        'name': 'Fila Brazillia',
        'plays': 185,
        'category': 'Genre Influences',
        'description': 'Trip-hop/downtempo/electronica',
        'use': 'Atmospheric textures, dub influences, analog warmth, hypnotic loops',
        'avoid': 'Dark/heavy basslines, dramatic tension, experimental noise',
        'notes': 'Fila Brazillia creates spacious, dubbed-out electronica - use the ambient textures and subtle rhythms, avoid their heavier trip-hop moments'
    },
    {
        'name': 'St. Germain',
        'plays': 168,
        'category': 'Genre Influences',
        'description': 'Deep house jazz fusion',
        'use': 'Four-on-floor pulse, jazz samples, Rhodes textures, French touch production',
        'avoid': 'Club-style builds, prominent trumpet solos, energetic sections',
        'notes': 'St. Germain pioneered jazz house - use the gentle house pulse with jazz instrumentation as background flow, avoid the more dancefloor-focused moments'
    },
    {
        'name': 'Thunderball',
        'plays': 417,
        'category': 'Genre Influences',
        'description': 'Cinematic downtempo/lounge',
        'use': 'Cinematic strings, vintage organ, retro production, medium tempos',
        'avoid': 'Dramatic orchestral swells, spy-movie intensity, vocal features',
        'notes': 'Thunderball does cinematic lounge - use the retro instrumentation and warm production as sophisticated background, avoid dramatic cinematic moments'
    },
    {
        'name': 'Blue Six',
        'plays': 587,
        'category': 'Genre Influences',
        'description': 'Soulful deep house',
        'use': 'Deep house grooves, Rhodes piano, warm bass, jazzy chords',
        'avoid': 'Soulful vocals (use instrumental versions), club energy',
        'notes': 'Blue Six makes sophisticated deep house - use the instrumental versions with Rhodes and warm house grooves, avoid vocal tracks that demand attention'
    },
    {
        'name': 'Peter Schmalfuss (Classical Piano)',
        'plays': 680,
        'category': 'Genre Influences',
        'description': 'Classical piano performances',
        'use': 'Solo piano textures, classical harmony, gentle dynamics, contemplative pieces',
        'avoid': 'Dramatic romantic pieces, loud fortissimo passages, attention-demanding virtuosity',
        'notes': 'Classical piano as background - use gentle Bach, Satie, or minimalist pieces, avoid dramatic Romantic-era showpieces. Focus on pieces that create atmosphere rather than demand attention'
    },
    {
        'name': 'Stan Getz (Bossa Nova)',
        'plays': 200,
        'category': 'Genre Influences',
        'description': 'Cool jazz/bossa nova saxophone',
        'use': 'Bossa nova rhythms, cool jazz tone, gentle saxophone texture, Latin grooves',
        'avoid': 'Bebop complexity, aggressive blowing, foreground saxophone solos',
        'notes': 'Stan Getz bossa nova era - use the gentle Latin grooves and saxophone as atmospheric texture (like we already do), avoid bebop/hard bop intensity'
    },
    {
        'name': 'Breeder',
        'plays': 186,
        'category': 'Genre Influences',
        'description': 'Downtempo electronica',
        'use': 'Minimal beats, atmospheric pads, subtle melodies, organic textures',
        'avoid': 'Experimental elements, glitchy production, dramatic changes',
        'notes': 'Breeder creates minimal downtempo - use the subtle atmospheres and gentle beats, maintain consistency without experimental departures'
    },
    {
        'name': 'Digital Analog Band',
        'plays': 520,
        'category': 'Genre Influences',
        'description': 'Organic house/nu-jazz',
        'use': 'Live instrumentation, house grooves, organic production, jazz elements',
        'avoid': 'Energetic builds, party atmosphere, prominent vocals',
        'notes': 'Digital Analog Band blends live jazz with house - use the organic grooves and warm production, avoid their more energetic club tracks'
    },
    {
        'name': 'A Forest Mighty Black',
        'plays': 140,
        'category': 'Genre Influences',
        'description': 'Deep house/ambient jazz',
        'use': 'Deep minimal house, ambient textures, jazz instrumentation, spacious production',
        'avoid': 'Club dynamics, dramatic builds, foreground elements',
        'notes': 'Deep ambient house with jazz - use the minimal grooves and spacious production as background flow, keep everything understated'
    }
]

def show_suggestions():
    """Display artist suggestions for review."""
    print("🎵 ARTIST INFLUENCES FROM YOUR APPLE MUSIC LIBRARY")
    print("=" * 70)
    print()
    print("Based on your listening history, here are suggested influences:")
    print()

    for i, artist in enumerate(ARTIST_SUGGESTIONS, 1):
        print(f"{i:2}. {artist['name']} ({artist['plays']} plays)")
        print(f"    Category: {artist['category']}")
        print(f"    Description: {artist['description']}")
        print()
        print(f"    ✓ Elements to USE:")
        print(f"       {artist['use']}")
        print()
        print(f"    ✗ Elements to AVOID:")
        print(f"       {artist['avoid']}")
        print()
        print(f"    📝 Adaptation Notes:")
        print(f"       {artist['notes']}")
        print()
        print("-" * 70)
        print()

def add_all_influences():
    """Add all suggested influences to the library."""
    influences = read_influences()

    print("Adding influences to library...")
    print()

    added = []

    for artist in ARTIST_SUGGESTIONS:
        # Check if already exists
        existing = [inf for inf in influences if inf['Name'].lower() == artist['name'].lower()]
        if existing:
            print(f"⚠️  {artist['name']} already exists (ID: {existing[0]['Influence_ID']}), skipping...")
            continue

        new_influence = {
            'Category': artist['category'],
            'Name': artist['name'],
            'Elements_To_Use': artist['use'],
            'Elements_To_Avoid': artist['avoid'],
            'Adaptation_Notes': artist['notes'],
            'Used_In_Prompts': '',
            'Status': 'Unexplored'
        }

        add_influence(new_influence)
        added.append(artist['name'])

        # Refresh to get the ID
        influences = read_influences()
        new_entry = [inf for inf in influences if inf['Name'] == artist['name']][0]
        print(f"✅ Added: {artist['name']} (ID: {new_entry['Influence_ID']})")

    if added:
        print()
        print(f"✅ Successfully added {len(added)} influences to library!")
        print()
        print("Added:")
        for name in added:
            print(f"  - {name}")
    else:
        print()
        print("ℹ️  No new influences to add (all already exist)")

def interactive_add():
    """Interactive mode to review and selectively add influences."""
    print("🎵 INTERACTIVE INFLUENCE ADDITION")
    print("=" * 70)
    print()

    for i, artist in enumerate(ARTIST_SUGGESTIONS, 1):
        print(f"\n{i}/{len(ARTIST_SUGGESTIONS)}: {artist['name']} ({artist['plays']} plays)")
        print(f"Category: {artist['category']}")
        print()
        print(f"✓ USE: {artist['use']}")
        print(f"✗ AVOID: {artist['avoid']}")
        print(f"📝 NOTE: {artist['notes']}")
        print()

        response = input("Add this influence? [Y/n/q]: ").strip().lower()

        if response == 'q':
            print("\nExiting...")
            break
        elif response in ['', 'y', 'yes']:
            # Add this influence
            influences = read_influences()

            # Check if exists
            existing = [inf for inf in influences if inf['Name'].lower() == artist['name'].lower()]
            if existing:
                print(f"⚠️  Already exists (ID: {existing[0]['Influence_ID']})")
                continue

            new_influence = {
                'Category': artist['category'],
                'Name': artist['name'],
                'Elements_To_Use': artist['use'],
                'Elements_To_Avoid': artist['avoid'],
                'Adaptation_Notes': artist['notes'],
                'Used_In_Prompts': '',
                'Status': 'Unexplored'
            }

            add_influence(new_influence)

            # Refresh to get the ID
            influences = read_influences()
            new_entry = [inf for inf in influences if inf['Name'] == artist['name']][0]
            print(f"✅ Added (ID: {new_entry['Influence_ID']})")
        else:
            print("⏭️  Skipped")

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Add artist influences from Apple Music to the library'
    )
    parser.add_argument(
        '--show',
        action='store_true',
        help='Show suggested influences (review before adding)'
    )
    parser.add_argument(
        '--add-all',
        action='store_true',
        help='Add all suggested influences automatically'
    )
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Interactively review and add influences'
    )

    args = parser.parse_args()

    if args.show:
        show_suggestions()
    elif args.add_all:
        add_all_influences()
    elif args.interactive:
        interactive_add()
    else:
        # Default: show suggestions
        show_suggestions()
        print()
        print("To add these influences:")
        print("  --add-all        Add all suggestions")
        print("  --interactive    Review and selectively add")
        print("  --show           Show this list again")

if __name__ == '__main__':
    main()
