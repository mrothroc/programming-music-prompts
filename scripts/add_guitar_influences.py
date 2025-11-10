#!/usr/bin/env python3
"""
Add fingerstyle guitar influences for "Embryonic Journey" aesthetic.

Supports both pure single-influence prompts and hybrid combinations.
"""

import sys
from pathlib import Path

# Add parent directory to path to import csv_utils
sys.path.insert(0, str(Path(__file__).parent.parent / '.claude/skills/influence-manage/scripts'))

from csv_utils import read_influences, write_influences, add_influence

# Fingerstyle guitar influences
GUITAR_INFLUENCES = [
    {
        'name': 'Fingerstyle Guitar (Jorma Kaukonen/Leo Kottke)',
        'category': 'Acoustic Instruments',
        'description': 'Intricate fingerpicked acoustic guitar',
        'use': 'Spanish/flamenco-influenced arpeggios, melodic patterns, open tunings, repetitive hypnotic fingerpicking, nylon or steel strings as texture',
        'avoid': 'Strumming, power chords, rock riffs, constant melodic development demanding attention, virtuosic showpieces',
        'notes': 'Fingerstyle guitar (Jorma Kaukonen\'s "Embryonic Journey," Leo Kottke\'s "Vaseline Machine Gun") creates intricate patterns that can work as EITHER foreground or background. Key: use repetitive patterns rather than constantly developing melodies. Works beautifully solo (pure single-influence) or layered with minimal percussion/pads. The Spanish/flamenco influences add exotic color without being traditional flamenco. For programming music: keep patterns hypnotic and consistent, avoid flashy runs that demand attention.'
    },
    {
        'name': 'Psychedelic Folk Instrumentals (1960s)',
        'category': 'Genre Influences',
        'description': '1960s instrumental folk with psychedelic influences',
        'use': 'Acoustic instrumentation, Spanish influences, open tunings, modal harmony, instrumental focus, vintage recording warmth',
        'avoid': 'Protest song vocals, traditional folk melodies, political lyrics, dramatic builds, acid-rock excess',
        'notes': 'The psychedelic folk era (Jefferson Airplane instrumentals, early Grateful Dead, Pentangle) created beautiful instrumental pieces that blended folk purity with 1960s experimentation. "Embryonic Journey" is the quintessential example - solo acoustic guitar with Spanish influences, no vocals, hypnotic patterns. For programming: extract the instrumental focus and modal harmony, use vintage production warmth (tape saturation), avoid the vocal-driven protest songs. Works as pure acoustic or with subtle electronic foundation.'
    },
    {
        'name': 'Spanish/Flamenco Guitar (Texture Only)',
        'category': 'Acoustic Instruments',
        'description': 'Spanish guitar techniques adapted for ambient use',
        'use': 'Rasgueado textures (as background rhythm), melodic arpeggios, passionate tone but restrained dynamics, nylon string warmth, modal scales',
        'avoid': 'Traditional flamenco performance (too demanding), castanets, palmas (hand clapping), cante jondo vocals, virtuosic solos',
        'notes': 'CRITICAL: Use Spanish/flamenco TECHNIQUES and AESTHETIC, not traditional flamenco music. Traditional flamenco demands attention through dramatic dynamics and virtuosity. Instead: extract the rasgueado rhythm as gentle texture, use modal scales for exotic color, apply passionate tone with restrained volume. Think "Spanish guitar influence" not "flamenco performance." Works beautifully layered with electronic elements (flamenco house fusion) or pure acoustic. Artists like Paco de Lucía\'s contemplative pieces show flamenco guitar in meditative contexts.'
    },
]

def show_suggestions():
    """Display suggested guitar influences."""
    print("🎸 FINGERSTYLE GUITAR INFLUENCES")
    print("=" * 70)
    print()
    print("Inspired by 'Embryonic Journey' by Jefferson Airplane")
    print()
    print("These influences support BOTH:")
    print("  • Pure single-influence prompts (solo guitar, maximum purity)")
    print("  • Hybrid combinations (guitar + electronics, maximum diversity)")
    print()

    for i, inf in enumerate(GUITAR_INFLUENCES, 1):
        print(f"{i}. {inf['name']}")
        print(f"   Category: {inf['category']}")
        print(f"   ✓ USE: {inf['use'][:100]}...")
        print(f"   ✗ AVOID: {inf['avoid'][:80]}...")
        print()

def add_all_influences():
    """Add all guitar influences to the library."""
    influences = read_influences()

    print("Adding fingerstyle guitar influences...")
    print()

    added = []

    for inf in GUITAR_INFLUENCES:
        # Check if already exists
        existing = [i for i in influences if inf['name'].lower() in i['Name'].lower() or i['Name'].lower() in inf['name'].lower()]
        if existing:
            print(f"⚠️  Similar influence exists: {existing[0]['Name']} (ID: {existing[0]['Influence_ID']}), skipping...")
            continue

        new_influence = {
            'Category': inf['category'],
            'Name': inf['name'],
            'Elements_To_Use': inf['use'],
            'Elements_To_Avoid': inf['avoid'],
            'Adaptation_Notes': inf['notes'],
            'Used_In_Prompts': '',
            'Status': 'Unexplored'
        }

        add_influence(new_influence)
        added.append(inf['name'])

        # Refresh to get the ID
        influences = read_influences()
        new_entry = [i for i in influences if i['Name'] == inf['name']][0]
        print(f"✅ Added: {inf['name']} (ID: {new_entry['Influence_ID']})")

    if added:
        print()
        print(f"✅ Successfully added {len(added)} guitar influences!")
        print()
        print("🎸 GUITAR PALETTE EXPANDED:")
        print("  • Fingerstyle guitar (Kaukonen, Kottke)")
        print("  • Psychedelic folk instrumentals (1960s)")
        print("  • Spanish/flamenco guitar (as texture)")
        print()
        print("💡 USAGE NOTES:")
        print("  • These work as PURE single-influence prompts (solo guitar)")
        print("  • OR as hybrids (fingerstyle + house beat, flamenco + electronics)")
        print("  • Key: Repetitive patterns over melodic development")
        print("  • Key: Restrained dynamics, not virtuosic showpieces")
    else:
        print()
        print("ℹ️  No new influences to add (all already exist)")

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Add fingerstyle guitar influences'
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

    args = parser.parse_args()

    if args.show:
        show_suggestions()
    elif args.add_all:
        add_all_influences()
    else:
        # Default: show suggestions
        show_suggestions()
        print()
        print("To add these influences:")
        print("  --add-all        Add all suggestions")
        print("  --show           Show this list again")

if __name__ == '__main__':
    main()
