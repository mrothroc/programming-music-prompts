#!/usr/bin/env python3
"""
Add diverse genre influences from Rock and Classical listening to break electrolounge convergence.

Based on actual Apple Music listening data to ensure these are proven personal preferences.
"""

import sys
from pathlib import Path

# Add parent directory to path to import csv_utils
sys.path.insert(0, str(Path(__file__).parent.parent / '.claude/skills/influence-manage/scripts'))

from csv_utils import read_influences, write_influences, add_influence

# Diverse influences from Rock and Classical listening history
DIVERSE_INFLUENCES = [
    # === ROCK INFLUENCES ===
    {
        'name': 'The Ventures (Surf Instrumental)',
        'plays': 119,
        'category': 'Genre Influences',
        'description': 'Instrumental surf rock',
        'use': 'Reverb guitar textures, tremolo picking as ambient layer, vintage spring reverb atmosphere',
        'avoid': 'Dominant melodic riffs, twangy aggressive leads, surf clichés (Wipeout drums)',
        'notes': 'Unlike Dick Dale (pure surf), The Ventures do melodic instrumentals - use the reverb wash and tremolo texture as background ambience, not the melodies themselves. Think distant beach soundtrack.'
    },
    {
        'name': 'Steely Dan (Jazz Rock Production)',
        'plays': 367,
        'category': 'Genre Influences',
        'description': 'Sophisticated jazz-rock production',
        'use': 'Studio perfectionism, jazz chord progressions, Fender Rhodes textures, pristine engineering',
        'avoid': 'Vocals, complex narrative lyrics, attention-demanding solos, sardonic hooks',
        'notes': 'Steely Dan\'s genius is in production and harmony - extract the lush chord voicings, Rhodes/Wurlitzer pads, and studio-quality mixing. Avoid their lyrical complexity and vocal hooks which demand attention.'
    },
    {
        'name': 'Peter Gabriel (Atmospheric Production)',
        'plays': 100,
        'category': 'Genre Influences',
        'description': 'World music fusion, experimental production',
        'use': 'Ethnic percussion layers, gated reverb on drums, world instruments as texture, sonic experimentation',
        'avoid': 'Dramatic vocals, emotional intensity, narrative lyrics, theatrical builds',
        'notes': 'Peter Gabriel pioneered world music fusion in rock - use the African/Middle Eastern percussion, atmospheric production techniques, and ethnic instruments. Avoid the dramatic vocal performances and emotional narratives.'
    },
    {
        'name': 'The Cure (Atmospheric Guitar)',
        'plays': 90,
        'category': 'Genre Influences',
        'description': 'Post-punk atmospheric guitar textures',
        'use': 'Chorus-drenched guitar pads, minor key atmospheres, reverb soundscapes, melancholic ambience',
        'avoid': 'Gothic vocals, depressive lyrics, dramatic dynamics, attention-demanding hooks',
        'notes': 'The Cure created lush guitar atmospheres through effects - extract the chorus/reverb textures and minor-key ambience. Use as background wash, not foreground melodies. Think Disintegration album production.'
    },
    {
        'name': 'Sting (Jazz-Tinged Rock)',
        'plays': 121,
        'category': 'Genre Influences',
        'description': 'Jazz-rock fusion, sophisticated arrangements',
        'use': 'Jazz chord progressions, upright bass textures, sophisticated harmony, subtle world music elements',
        'avoid': 'Distinctive vocals, lyrical complexity, foreground bass lines, pop hooks',
        'notes': 'Sting\'s solo work incorporates jazz harmony and world music - use the sophisticated chord progressions, upright bass grooves, and world percussion. Avoid his distinctive voice and melodic bass lines which demand attention.'
    },

    # === CLASSICAL INFLUENCES ===
    {
        'name': 'Debussy (Impressionist Piano)',
        'plays': 680,  # Peter Schmalfuss performing Debussy
        'category': 'Genre Influences',
        'description': 'French impressionist piano music',
        'use': 'Whole-tone scales, parallel chords, gentle arpeggios, water/nature imagery, soft dynamics',
        'avoid': 'Dramatic crescendos, virtuosic passages, Romantic-era emotionalism, Children\'s Corner playfulness',
        'notes': 'Debussy created "painting with sound" - use the gentle impressionistic textures (Arabesque, Clair de Lune) as ambient background. Avoid the playful Children\'s Corner suite (too whimsical). Focus on Estampes, Nocturnes, Préludes for atmospheric programming music.'
    },
    {
        'name': 'Chopin (Nocturnes Only)',
        'plays': 131,
        'category': 'Genre Influences',
        'description': 'Romantic piano - nocturnes specifically',
        'use': 'Nocturnes only - gentle dynamics, singing melodies, rubato timing, nighttime contemplation',
        'avoid': 'Dramatic études, virtuosic showpieces (Heroic Polonaise), loud passages, Revolutionary Étude intensity',
        'notes': 'CRITICAL: Only use Chopin\'s Nocturnes for programming music - these are gentle, contemplative pieces. Avoid the dramatic études, polonaises, and ballades which demand attention. Nocturnes were designed as "night music" for reflection.'
    },
    {
        'name': 'Chamber Music (String Quartets)',
        'plays': 227,  # Daniel Barenboim + chamber ensembles
        'category': 'Genre Influences',
        'description': 'Small ensemble classical (2-8 players)',
        'use': 'Intimate textures, conversational interplay, moderate dynamics, warm acoustics',
        'avoid': 'Symphonic drama, operatic intensity, virtuosic showpieces, loud passages',
        'notes': 'Chamber music is "music for friends" - smaller than orchestra, more intimate. String quartets, piano trios, wind quintets. Use the gentle interplay and warm textures, avoid dramatic moments. Perfect for sophisticated background.'
    },
    {
        'name': 'Edgar Meyer (Contemporary Upright Bass)',
        'plays': 86,
        'category': 'Genre Influences',
        'description': 'Bluegrass/classical crossover bassist',
        'use': 'Upright bass as melodic instrument, Americana harmonies, sophisticated acoustic textures',
        'avoid': 'Bluegrass virtuosity, fast picking passages, attention-demanding solos',
        'notes': 'Edgar Meyer bridges classical and bluegrass - use the warm upright bass textures and sophisticated harmonies. His work with Yo-Yo Ma and Chris Thile shows acoustic instruments in contemplative settings.'
    },
    {
        'name': 'Baroque Simplicity (Bach, Scarlatti)',
        'plays': 77,  # Murray Perahia performing Bach
        'category': 'Genre Influences',
        'description': 'Pre-classical period keyboard music',
        'use': 'Counterpoint, mathematical structure, harpsichord/piano textures, moderate tempos',
        'avoid': 'Fast virtuosic passages (Goldberg Variations), complex fugues demanding attention, organ drama',
        'notes': 'Baroque music is mathematically structured - use simple preludes, slow movements, gentle inventions. Bach\'s Well-Tempered Clavier has many contemplative pieces. Scarlatti sonatas are elegant but often too virtuosic. Use slow, simple pieces only.'
    }
]

def show_suggestions():
    """Display suggested diverse influences for review."""
    print("🌈 DIVERSE GENRE INFLUENCES (Breaking Electrolounge Convergence)")
    print("=" * 70)
    print()
    print("Based on your Rock (6,876 plays) and Classical (1,698 plays) listening:")
    print()

    # Split into rock and classical
    rock_influences = [i for i in DIVERSE_INFLUENCES if any(kw in i['description'].lower() for kw in ['rock', 'guitar', 'surf', 'punk', 'fusion'])]
    classical_influences = [i for i in DIVERSE_INFLUENCES if any(kw in i['description'].lower() for kw in ['piano', 'chamber', 'bass', 'baroque', 'classical', 'impressionist', 'nocturne'])]

    print("🎸 ROCK INFLUENCES (5):")
    print("-" * 70)
    for i, inf in enumerate(rock_influences, 1):
        print(f"{i}. {inf['name']} ({inf['plays']} plays)")
        print(f"   Description: {inf['description']}")
        print(f"   ✓ USE: {inf['use']}")
        print(f"   ✗ AVOID: {inf['avoid']}")
        print(f"   📝 NOTE: {inf['notes'][:150]}...")
        print()

    print()
    print("🎹 CLASSICAL INFLUENCES (5):")
    print("-" * 70)
    for i, inf in enumerate(classical_influences, 1):
        print(f"{i}. {inf['name']} ({inf['plays']} plays)")
        print(f"   Description: {inf['description']}")
        print(f"   ✓ USE: {inf['use']}")
        print(f"   ✗ AVOID: {inf['avoid']}")
        print(f"   📝 NOTE: {inf['notes'][:150]}...")
        print()

def add_all_influences():
    """Add all suggested influences to the library."""
    influences = read_influences()

    print("Adding diverse influences to library...")
    print()

    added = []

    for inf in DIVERSE_INFLUENCES:
        # Check if already exists
        existing = [i for i in influences if i['Name'].lower() == inf['name'].lower()]
        if existing:
            print(f"⚠️  {inf['name']} already exists (ID: {existing[0]['Influence_ID']}), skipping...")
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
        print(f"✅ Successfully added {len(added)} diverse influences!")
        print()
        print("GENRE DIVERSITY ACHIEVED:")
        print("  🎸 Rock influences: Surf, Jazz-Rock, World Fusion, Post-Punk, Jazz-Tinged")
        print("  🎹 Classical influences: Impressionist Piano, Romantic Nocturnes, Chamber, Bluegrass-Classical, Baroque")
        print()
        print("This breaks the electrolounge convergence by introducing:")
        print("  • Guitar textures (reverb wash, chorus effects)")
        print("  • Acoustic piano (impressionist, romantic, baroque)")
        print("  • Chamber music intimacy")
        print("  • World music fusion elements")
        print("  • Jazz-rock sophistication")
    else:
        print()
        print("ℹ️  No new influences to add (all already exist)")

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Add diverse genre influences from Rock and Classical listening'
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
