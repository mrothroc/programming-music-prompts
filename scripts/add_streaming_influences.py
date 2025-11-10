#!/usr/bin/env python3
"""
Add influences from Apple Music streaming behavior + strategic geographic diversity.

Two categories:
1. DATA-DRIVEN: Based on actual Recently Played streaming stations
2. STRATEGIC DIVERSITY: Geographic/cultural regions underrepresented in library
"""

import sys
from pathlib import Path

# Add parent directory to path to import csv_utils
sys.path.insert(0, str(Path(__file__).parent.parent / '.claude/skills/influence-manage/scripts'))

from csv_utils import read_influences, write_influences, add_influence

# Influences from actual streaming behavior
STREAMING_INFLUENCES = [
    # === JAZZ (Dominant in streaming) ===
    {
        'name': 'Vince Guaraldi (Peanuts Jazz Piano)',
        'category': 'Genre Influences',
        'description': 'Jazz piano designed as background music',
        'use': 'Simple jazz piano melodies, walking bass lines, gentle swing, playful but sophisticated harmony, child-friendly but adult-appreciated',
        'avoid': 'Recognizable Peanuts themes (Linus & Lucy hook), overly whimsical moments, Christmas clichés',
        'notes': 'Guaraldi created the perfect programming music before programming existed - jazz sophisticated enough for adults, simple enough to stay background. His Peanuts soundtracks are proof that "background music" can be artistically excellent. Use the gentle swing, simple melodies, and warm piano tone.',
        'evidence': 'Appears twice in Recently Played: "Charlie Brown Thanksgiving" and "Peanuts Greatest Hits"'
    },
    {
        'name': 'Lo-Fi Hip Hop (Confirmed Streaming)',
        'category': 'Genre Influences',
        'description': 'Downtempo beats with vinyl warmth',
        'use': 'Boom bap drums, vinyl crackle, jazz samples, Rhodes/Wurlitzer, anime aesthetic, study music vibe',
        'avoid': 'Vocal samples, recognizable song samples, overly busy beats',
        'notes': 'You already have Lo-Fi Hip Hop influence (#44) but streaming shows this is a CURRENT active preference (Lo-Fi Chill, Lo-Fi Japan, Lo-Fi Jazz all appear). This confirms the aesthetic works. Consider this influence PROVEN.',
        'evidence': 'Multiple lo-fi stations in Recently Played: Lo-Fi Chill, Lo-Fi Japan, Lo-Fi Jazz'
    },
    {
        'name': 'Jazz Clarinet (Benny Goodman Style)',
        'category': 'Acoustic Instruments',
        'description': 'Clarinet in jazz/swing context',
        'use': 'Warm woody tone, gentle swing melodies, duo with piano, subtle vibrato, background texture',
        'avoid': 'Virtuosic bebop runs, squeaky high register, klezmer intensity, aggressive swing',
        'notes': 'Streaming shows both "Jazz Clarinet Essentials" and "The Clarinet" stations. Clarinet has warmer, woodier tone than saxophone. Use as melodic texture like we used sax in Prompt 41 (which you loved). Benny Goodman small group recordings are perfect reference.',
        'evidence': '"Jazz Clarinet Essentials" and "The Clarinet" in Recently Played'
    },
    {
        'name': 'West Coast Jazz (Cool Jazz)',
        'category': 'Genre Influences',
        'description': 'Relaxed, cerebral jazz from 1950s California',
        'use': 'Laid-back tempos, sophisticated harmony, vibraphone, soft trumpet/sax, chamber jazz intimacy, intellectual cool',
        'avoid': 'Bebop intensity, hard bop aggression, East Coast energy, fast tempos',
        'notes': 'West Coast Jazz (Dave Brubeck, Chet Baker, Gerry Mulligan) was designed for listening, not dancing - perfect for programming. Lighter, more relaxed than East Coast bebop. Often features vibraphone and soft brass. Streaming shows "West Coast Jazz Essentials" and "Cool Jazz Essentials".',
        'evidence': '"West Coast Jazz Essentials" and "Cool Jazz Essentials" in Recently Played'
    },
    {
        'name': 'Johnny Costa (Mister Rogers Pianist)',
        'category': 'Genre Influences',
        'description': 'Sophisticated jazz piano in gentle context',
        'use': 'Jazz harmony, gentle dynamics, sophisticated voicings, accessible melodies, warm tone',
        'avoid': 'Children\'s music clichés, overly simple melodies, sing-along quality',
        'notes': 'Johnny Costa was Mister Rogers\' pianist - like Guaraldi, he played sophisticated jazz in a gentle context. His Gershwin interpretations ("Costa Plays Gershwin" in streaming) show jazz piano that\'s intellectual but comforting. Perfect programming music aesthetic.',
        'evidence': '"Costa Plays Gershwin" in Recently Played'
    },
    {
        'name': 'Tropical House (Kygo Style)',
        'category': 'Genre Influences',
        'description': 'Melodic house with tropical instruments',
        'use': 'Steel pan, marimba, gentle four-on-floor, warm pads, beach atmosphere, melodic hooks as texture',
        'avoid': 'Pop vocal features, EDM builds/drops, festival energy, aggressive bass',
        'notes': 'Tropical House uses steel pan, marimba, and island percussion over gentle house beats. "Tropical House Essentials" in streaming suggests this aesthetic works. Use instrumental versions only - the production warmth and tropical textures, not the pop vocals.',
        'evidence': '"Tropical House Essentials" in Recently Played'
    },
]

# Strategic geographic/cultural diversity
GEOGRAPHIC_DIVERSITY = [
    # === EAST ASIA ===
    {
        'name': 'Japanese Koto (Traditional Strings)',
        'category': 'Acoustic Instruments',
        'description': 'Traditional Japanese 13-string zither',
        'use': 'Pentatonic scales, gentle plucked textures, nature imagery (water, wind), meditative pacing, minimal sustain',
        'avoid': 'Traditional melodies that demand attention, fast virtuosic passages, ceremonial drama',
        'notes': 'Koto creates gentle, pentatonic soundscapes perfect for theta states. Use as ambient texture layer, not traditional melodic instrument. Modern ambient koto (like "Koto Dream" albums) shows programming-appropriate applications. Pairs well with electronic elements.',
        'evidence': 'Lo-Fi Japan in streaming suggests Japanese aesthetic appeals'
    },
    {
        'name': 'Anime Soundtracks (Ambient Tracks)',
        'category': 'Genre Influences',
        'description': 'Japanese animation background music',
        'use': 'Emotional piano, string pads, gentle electronics, wistful melodies, nostalgic atmosphere',
        'avoid': 'Dramatic battle themes, opening/closing songs, recognizable anime themes, J-pop vocals',
        'notes': 'Anime soundtracks (Miyazaki films, slice-of-life shows) contain beautiful ambient pieces designed to enhance focus without distraction. Use the gentle piano interludes and string atmospheres from Studio Ghibli soundtracks (Joe Hisaishi). "Lo-Fi Japan" aesthetic often samples anime.',
        'evidence': 'Lo-Fi Japan in streaming; lo-fi hip hop heavily uses anime aesthetic'
    },
    {
        'name': 'Ryuichi Sakamoto (Ambient Works)',
        'category': 'Genre Influences',
        'description': 'Japanese composer - ambient/minimalist period',
        'use': 'Minimal piano, electronic textures, silence as element, emotional restraint, contemplative pacing',
        'avoid': 'Early Yellow Magic Orchestra pop, dramatic film scores, experimental noise periods',
        'notes': 'Sakamoto\'s solo ambient works (async, 12, Coda) are perfect programming music - minimal piano with electronic processing, lots of space, deeply contemplative. Use his restrained, meditative approach, not his pop or avant-garde work.',
        'evidence': 'Strategic addition for Japanese cultural diversity'
    },

    # === SOUTH ASIA (India) ===
    {
        'name': 'Indian Tabla (Rhythmic Foundation)',
        'category': 'Rhythmic Elements',
        'description': 'North Indian hand drums',
        'use': 'Gentle rhythmic cycles (slow tala), warm tuned drum tones, subtle polyrhythms, meditative pulse',
        'avoid': 'Fast virtuosic solos, loud aggressive playing, complex ragas demanding attention',
        'notes': 'Tabla can provide gentle, tuned percussion rhythms. Use slow tala (rhythmic cycles) as foundation, not foreground solos. Works beautifully with electronic music (Talvin Singh, Asian Dub Foundation ambient tracks). The warm, tuned quality bridges rhythm and melody.',
        'evidence': 'Strategic addition for Indian cultural diversity'
    },
    {
        'name': 'Bansuri Flute (Indian Bamboo Flute)',
        'category': 'Acoustic Instruments',
        'description': 'North Indian bamboo flute',
        'use': 'Breathy tone, long sustained notes, simple melodies, meditative quality, nature sounds',
        'avoid': 'Complex raga improvisation, virtuosic runs, classical Indian performance practice',
        'notes': 'Bansuri has an incredibly soothing, breathy quality perfect for ambient music. Use simple, sustained tones and gentle melodies - not traditional raga performance. Artists like Steve Gorn show bansuri in contemplative contexts. The breathy quality creates intimate, meditative atmosphere.',
        'evidence': 'Strategic addition for Indian cultural diversity'
    },
    {
        'name': 'Ravi Shankar (Ambient/Minimalist Works Only)',
        'category': 'Genre Influences',
        'description': 'Indian classical - contemplative pieces only',
        'use': 'Sitar drone (tanpura), slow alap (introductory improvisation), meditative pacing, spiritual atmosphere',
        'avoid': 'Fast jhala sections, virtuosic display, traditional raga development, tabla solo exchanges',
        'notes': 'CRITICAL: Only use Shankar\'s slow, meditative alap sections where sitar explores a raga with drone accompaniment. Avoid the fast, exciting sections. His collaborations with Philip Glass and minimalist works show ambient applications. The drone and slow exploration create deep focus states.',
        'evidence': 'Strategic addition for Indian cultural diversity; you have Sitar already as instrument'
    },

    # === MIDDLE EAST ===
    {
        'name': 'Oud (Middle Eastern Lute)',
        'category': 'Acoustic Instruments',
        'description': 'Arabic/Turkish fretless lute',
        'use': 'Warm resonant plucks, maqam scales as texture, gentle taqsim (improvisation), fretless microtonality',
        'avoid': 'Traditional maqam melodies, virtuosic display, belly dance clichés, dramatic improvisation',
        'notes': 'Oud already in library (#11) but worth emphasizing: use sustained notes and gentle plucks for exotic texture. Modern ambient oud (like Anouar Brahem) shows contemplative applications. The fretless microtones add exotic color without being demanding.',
        'evidence': 'Strategic diversity; already have Oud in library, could upgrade from Unexplored'
    },
    {
        'name': 'Nay (Middle Eastern Flute)',
        'category': 'Acoustic Instruments',
        'description': 'Arabic/Persian end-blown flute',
        'use': 'Breathy tone, mystical quality, long sustained notes, maqam flavors, meditative pacing',
        'avoid': 'Traditional maqam melodies, virtuosic ornaments, belly dance music, dramatic dynamics',
        'notes': 'Nay has an incredibly mystical, breathy quality - similar to bansuri but with Middle Eastern character. Use for ambient textures and sustained tones. Creates spiritual, meditative atmosphere without being overly "world music" cliché.',
        'evidence': 'Strategic addition for Middle Eastern cultural diversity'
    },

    # === AFRICA (Beyond what we have) ===
    {
        'name': 'Mbira (Zimbabwean Thumb Piano)',
        'category': 'Acoustic Instruments',
        'description': 'Southern African lamellophone',
        'use': 'Hypnotic repetitive patterns, metallic shimmer, polyrhythmic layers, trance-inducing cycles',
        'avoid': 'Traditional ceremonial contexts, loud aggressive playing, vocals',
        'notes': 'Mbira creates mesmerizing, cyclical patterns perfect for flow states. Different from kalimba (which you already have) - more metallic, more polyrhythmic. Zimbabwe\'s mbira music is designed to induce trance. Use the hypnotic patterns, not traditional ceremonial contexts.',
        'evidence': 'Strategic addition for African diversity; different from existing kalimba/thumb piano'
    },
    {
        'name': 'Kora (West African Harp-Lute)',
        'category': 'Acoustic Instruments',
        'description': '21-string West African bridge harp',
        'use': 'Cascading arpeggios, harp-like textures, gentle melodic patterns, warm resonance',
        'avoid': 'Griot storytelling vocals, traditional songs, virtuosic display',
        'notes': 'Kora has a beautiful, harp-like quality but with African rhythmic sensibility. Artists like Toumani Diabaté show kora in contemplative, instrumental contexts. The cascading arpeggios create water-like textures perfect for ambient music. Use instrumental pieces only.',
        'evidence': 'Strategic addition for West African diversity'
    },

    # === LATIN AMERICA (Expand beyond Bossa/Samba) ===
    {
        'name': 'Andean Panpipes (Zampoña)',
        'category': 'Acoustic Instruments',
        'description': 'South American bamboo panpipes',
        'use': 'Airy flute textures, pentatonic scales, nature imagery (mountains, wind), gentle melodies',
        'avoid': 'El Condor Pasa clichés, tourist music, overly recognizable melodies',
        'notes': 'Andean panpipes create gentle, airy textures with natural, organic quality. Use for ambient atmosphere, not traditional folk melodies. The breathy, multi-pipe sound creates ethereal quality. Modern ambient applications (like Inkuyo\'s contemplative work) show programming potential.',
        'evidence': 'Strategic addition for Andean/South American diversity beyond Brazil'
    },
]

def show_suggestions():
    """Display all suggested influences for review."""
    print("🎵 STREAMING-BASED + GEOGRAPHIC DIVERSITY INFLUENCES")
    print("=" * 70)
    print()

    print("📊 PART 1: DATA-DRIVEN (From Your Actual Streaming)")
    print("=" * 70)
    print(f"Based on Recently Played analysis - {len(STREAMING_INFLUENCES)} influences")
    print()

    for i, inf in enumerate(STREAMING_INFLUENCES, 1):
        print(f"{i}. {inf['name']}")
        print(f"   Category: {inf['category']}")
        print(f"   ✓ USE: {inf['use'][:100]}...")
        print(f"   ✗ AVOID: {inf['avoid'][:80]}...")
        print(f"   📝 Evidence: {inf['evidence']}")
        print()

    print()
    print("🌍 PART 2: STRATEGIC GEOGRAPHIC DIVERSITY")
    print("=" * 70)
    print(f"Underrepresented regions - {len(GEOGRAPHIC_DIVERSITY)} influences")
    print()
    print("Current library geographic breakdown:")
    print("  🇺🇸 North America: Strong (jazz, blues, electronica)")
    print("  🇧🇷 Brazil: Present (bossa nova, samba)")
    print("  🇪🇺 Europe: Present (classical, electronica)")
    print("  🌏 East Asia: MISSING → Adding Japan")
    print("  🇮🇳 South Asia: MINIMAL → Adding India")
    print("  🌍 Africa: LIMITED → Adding Zimbabwe, West Africa")
    print("  🌎 Andean South America: MISSING → Adding Peru/Bolivia")
    print("  🕌 Middle East: MINIMAL → Adding Arabic/Persian")
    print()

    for i, inf in enumerate(GEOGRAPHIC_DIVERSITY, 1):
        region = ""
        if "Japanese" in inf['name'] or "Anime" in inf['name'] or "Sakamoto" in inf['name']:
            region = "🇯🇵 JAPAN"
        elif "Indian" in inf['name'] or "Tabla" in inf['name'] or "Bansuri" in inf['name'] or "Ravi" in inf['name']:
            region = "🇮🇳 INDIA"
        elif "Oud" in inf['name'] or "Nay" in inf['name']:
            region = "🕌 MIDDLE EAST"
        elif "Mbira" in inf['name']:
            region = "🇿🇼 ZIMBABWE"
        elif "Kora" in inf['name']:
            region = "🌍 WEST AFRICA"
        elif "Andean" in inf['name']:
            region = "🇵🇪 ANDES"

        print(f"{i}. {region} - {inf['name']}")
        print(f"   Category: {inf['category']}")
        print(f"   ✓ USE: {inf['use'][:100]}...")
        print(f"   ✗ AVOID: {inf['avoid'][:80]}...")
        print()

def add_all_influences():
    """Add all suggested influences to the library."""
    influences = read_influences()

    all_new_influences = STREAMING_INFLUENCES + GEOGRAPHIC_DIVERSITY

    print(f"Adding {len(all_new_influences)} new influences...")
    print()

    added_streaming = []
    added_geographic = []
    skipped = []

    for inf in all_new_influences:
        # Check if already exists (basic name match)
        existing = [i for i in influences if inf['name'].lower() in i['Name'].lower() or i['Name'].lower() in inf['name'].lower()]
        if existing:
            print(f"⚠️  Similar influence exists: {existing[0]['Name']} (ID: {existing[0]['Influence_ID']}), skipping {inf['name']}...")
            skipped.append(inf['name'])
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

        # Track which category
        if inf in STREAMING_INFLUENCES:
            added_streaming.append(inf['name'])
        else:
            added_geographic.append(inf['name'])

        # Refresh to get the ID
        influences = read_influences()
        new_entry = [i for i in influences if i['Name'] == inf['name']][0]
        print(f"✅ Added: {inf['name']} (ID: {new_entry['Influence_ID']})")

    print()
    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)

    if added_streaming:
        print(f"✅ DATA-DRIVEN (Streaming): {len(added_streaming)} influences")
        for name in added_streaming:
            print(f"   • {name}")
        print()

    if added_geographic:
        print(f"✅ STRATEGIC DIVERSITY: {len(added_geographic)} influences")
        print()
        # Group by region
        regions = {
            'Japan': [n for n in added_geographic if any(k in n for k in ['Japanese', 'Anime', 'Sakamoto'])],
            'India': [n for n in added_geographic if any(k in n for k in ['Indian', 'Tabla', 'Bansuri', 'Ravi'])],
            'Middle East': [n for n in added_geographic if any(k in n for k in ['Oud', 'Nay'])],
            'Africa': [n for n in added_geographic if any(k in n for k in ['Mbira', 'Kora'])],
            'Andes': [n for n in added_geographic if 'Andean' in n],
        }

        for region, names in regions.items():
            if names:
                print(f"   🌍 {region}:")
                for name in names:
                    print(f"      • {name}")
        print()

    if skipped:
        print(f"⏭️  SKIPPED (already exist): {len(skipped)} influences")
        for name in skipped:
            print(f"   • {name}")
        print()

    print(f"✅ Total added: {len(added_streaming) + len(added_geographic)}")
    print()
    print("🌈 DIVERSITY ACHIEVED:")
    print("   • Streaming behavior validated (jazz, lo-fi confirmed)")
    print("   • Geographic coverage: Asia, Africa, Middle East, Andes")
    print("   • Cultural breadth: 6+ distinct musical traditions")

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Add streaming + geographic diversity influences'
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
