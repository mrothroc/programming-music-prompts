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
    get_random_unexplored_influences,
    get_weighted_mutation_influences
)

def get_next_prompt_id() -> int:
    """Get the next available prompt ID."""
    prompts = read_prompts()
    if not prompts:
        return 1
    # Filter to only numeric IDs
    numeric_ids = []
    for p in prompts:
        try:
            numeric_ids.append(int(p['Prompt_ID']))
        except ValueError:
            pass  # Skip non-numeric IDs like BONUS-1
    return max(numeric_ids) + 1 if numeric_ids else 1

def find_parent_prompts(time_block: str) -> List[Dict[str, str]]:
    """Find excellent/very good/pretty good prompts for the given time block."""
    prompts = read_prompts()
    parents = []

    for p in prompts:
        if p['Time_Block'] == time_block:
            rating = p.get('Rating', '').lower()
            # Include: Excellent, Very Good, Pretty Good
            if ('excellent' in rating or '⭐' in rating or
                'very good' in rating or 'pretty good' in rating):
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

def generate_prompts_plan(time_block: str, count: int):
    """Generate a plan for LLM to write prompts."""
    import random
    import json

    print(f"🧬 GENERATION PLAN for {count} prompts for {time_block}")
    print("=" * 70)
    print()

    # Find parents
    parents = find_parent_prompts(time_block)
    if not parents:
        print(f"❌ No parent prompts found for '{time_block}'")
        print("   Need at least one Excellent or Very Good rated prompt.")
        return

    # DIVERSITY CHECK: Warn if only 1 parent
    if len(parents) == 1:
        print(f"⚠️  WARNING: Only 1 parent found (#{parents[0]['Prompt_ID']})")
        print(f"   This may lead to genetic incest (too much similarity)")
        print(f"   Consider:")
        print(f"   - Rating more prompts as 'Pretty good' to expand parent pool")
        print(f"   - Using mutations to inject diversity")
        print()

    all_prompts = read_prompts()
    all_parents = [p for p in all_prompts if 'excellent' in p.get('Rating', '').lower()
                   or '⭐' in p.get('Rating', '')
                   or 'very good' in p.get('Rating', '').lower()]

    # Calculate distribution
    parent_clones = int(count * 0.5)
    hybrids = int(count * 0.3)
    mutations = count - parent_clones - hybrids

    # Get mutations - weighted by what's worked well in other time blocks
    mutation_influences = get_weighted_mutation_influences(mutations * 2) if mutations > 0 else []

    # Get next ID and BPM range
    next_id = get_next_prompt_id()
    block_prompts = [p for p in all_prompts if p['Time_Block'] == time_block and p['BPM']]
    if block_prompts:
        bpms = [int(p['BPM']) for p in block_prompts if p['BPM'].isdigit()]
        min_bpm = min(bpms) if bpms else 95
        max_bpm = max(bpms) if bpms else 122
    else:
        min_bpm, max_bpm = 95, 122

    best_parent = parents[0]
    brainwave_target = best_parent.get('Brain_Wave_Target', 'Beta Suppression + Alpha')
    duration_type = best_parent.get('Duration_Type', 'Energy Boost')

    # Build the plan
    plan = []
    prompt_id = next_id

    # Parent clones
    for i in range(parent_clones):
        parent = random.choice(parents)
        bpm = random.randint(min_bpm, max_bpm)
        plan.append({
            'id': prompt_id,
            'type': 'clone',
            'parent_id': parent['Prompt_ID'],
            'parent_full_prompt': parent.get('Full_Prompt', ''),
            'bpm': bpm,
            'genres': parent.get('Primary_Genres', '').strip('"'),
            'instruments': parent.get('Key_Instruments', '').strip('"'),
            'mood': parent.get('Mood_Keywords', ''),
            'brainwave': brainwave_target,
            'duration': duration_type
        })
        prompt_id += 1

    # Hybrids
    for i in range(hybrids):
        parent1 = random.choice(parents)
        parent2 = random.choice(all_parents)
        bpm = random.randint(min_bpm, max_bpm)

        genres1 = parent1.get('Primary_Genres', '').strip('"').split(',')[0].strip()
        genres2 = parent2.get('Primary_Genres', '').strip('"').split(',')[0].strip()
        instr1 = parent1.get('Key_Instruments', '').strip('"').split(',')[:2]
        instr2 = parent2.get('Key_Instruments', '').strip('"').split(',')[:2]

        plan.append({
            'id': prompt_id,
            'type': 'hybrid',
            'parent1_id': parent1['Prompt_ID'],
            'parent1_full_prompt': parent1.get('Full_Prompt', ''),
            'parent2_id': parent2['Prompt_ID'],
            'parent2_full_prompt': parent2.get('Full_Prompt', ''),
            'bpm': bpm,
            'genres': f'"{genres1}, {genres2}"',
            'instruments': f'"{", ".join(instr1 + instr2)}"',
            'mood': parent1.get('Mood_Keywords', '').split()[0] if parent1.get('Mood_Keywords') else 'driving',
            'brainwave': brainwave_target,
            'duration': duration_type
        })
        prompt_id += 1

    # Mutations
    for i in range(mutations):
        if i < len(mutation_influences):
            parent = random.choice(parents)
            mutation = mutation_influences[i]
            bpm = random.randint(min_bpm, max_bpm)

            plan.append({
                'id': prompt_id,
                'type': 'mutation',
                'parent_id': parent['Prompt_ID'],
                'parent_full_prompt': parent.get('Full_Prompt', ''),
                'mutation_name': mutation.get('Name', ''),
                'mutation_category': mutation.get('Category', ''),
                'mutation_use': mutation.get('Elements_To_Use', ''),
                'mutation_avoid': mutation.get('Elements_To_Avoid', ''),
                'bpm': bpm,
                'genres': parent.get('Primary_Genres', '').strip('"'),
                'base_instruments': parent.get('Key_Instruments', '').strip('"').split(',')[:2],
                'mood': parent.get('Mood_Keywords', '').split()[0] if parent.get('Mood_Keywords') else 'experimental',
                'brainwave': brainwave_target,
                'duration': duration_type
            })
            prompt_id += 1

    # Output the plan as JSON
    print(json.dumps(plan, indent=2))
    print()
    print(f"📊 Summary: {parent_clones} clones + {hybrids} hybrids + {mutations} mutations")
    print(f"🆔 IDs: #{next_id}-#{prompt_id-1}")
    print()
    print("💡 LLM should synthesize Full_Prompt descriptions based on this plan.")

def generate_prompts_automated(time_block: str, count: int):
    """Generate prompt structure using genetic algorithm for LLM to complete."""
    import random
    import json

    print(f"🧬 Generating structure for {count} prompts for {time_block}...")
    print()

    # Find parents in this time block
    parents = find_parent_prompts(time_block)

    if not parents:
        print(f"❌ No parent prompts found for '{time_block}'")
        print("   Need at least one Excellent or Very Good rated prompt to generate from.")
        return

    # Get all excellent/very good prompts for cross-breeding
    all_prompts = read_prompts()
    all_parents = [p for p in all_prompts if 'excellent' in p.get('Rating', '').lower()
                   or '⭐' in p.get('Rating', '')
                   or 'very good' in p.get('Rating', '').lower()]

    # Calculate distribution (50/30/20)
    parent_clones = int(count * 0.5)
    hybrids = int(count * 0.3)
    mutations = count - parent_clones - hybrids

    print(f"📊 Distribution:")
    print(f"   50% Parent DNA: {parent_clones} clones from {len(parents)} parent(s)")
    print(f"   30% Hybrids: {hybrids} cross-breeds")
    print(f"   20% Mutations: {mutations} with new influences")
    print()

    # Get mutation suggestions
    mutation_influences = get_random_unexplored_influences(mutations * 2) if mutations > 0 else []

    # Get next ID
    next_id = get_next_prompt_id()

    # Get BPM range for this time block from existing prompts
    block_prompts = [p for p in all_prompts if p['Time_Block'] == time_block and p['BPM']]
    if block_prompts:
        bpms = [int(p['BPM']) for p in block_prompts if p['BPM'].isdigit()]
        min_bpm = min(bpms) if bpms else 95
        max_bpm = max(bpms) if bpms else 122
    else:
        min_bpm, max_bpm = 95, 122

    # Get brainwave target from best parent
    best_parent = parents[0]
    brainwave_target = best_parent.get('Brain_Wave_Target', 'Beta Suppression + Alpha')
    duration_type = best_parent.get('Duration_Type', 'Energy Boost')

    generated_prompts = []
    prompt_id = next_id

    # Generate parent clones
    print(f"🧬 Generating {parent_clones} parent clones...")
    for i in range(parent_clones):
        parent = random.choice(parents)
        bpm = random.randint(min_bpm, max_bpm)

        # Parse parent genres and instruments
        genres = parent.get('Primary_Genres', '').strip('"')
        instruments = parent.get('Key_Instruments', '').strip('"')
        mood = parent.get('Mood_Keywords', '')

        prompt = {
            'Prompt_ID': str(prompt_id),
            'Time_Block': time_block,
            'BPM': str(bpm),
            'Brain_Wave_Target': brainwave_target,
            'Duration_Type': duration_type,
            'Primary_Genres': genres,
            'Key_Instruments': instruments,
            'Mood_Keywords': mood,
            'Suno_Short_Prompt': '',
            'Full_Prompt': f"[Generated] Clone of prompt #{parent['Prompt_ID']} at {bpm} BPM. {genres} with {instruments}. {mood}.",
            'Notes': f"Parent #{parent['Prompt_ID']} clone (proven DNA). Auto-generated.",
            'Generated': 'No',
            'Suno_Refined': '',
            'Rating': ''
        }
        generated_prompts.append(prompt)
        print(f"   #{prompt_id}: Clone of #{parent['Prompt_ID']} ({genres}) at {bpm} BPM")
        prompt_id += 1

    # Generate hybrids
    print(f"\n🧬 Generating {hybrids} hybrid combinations...")
    for i in range(hybrids):
        parent1 = random.choice(parents)
        parent2 = random.choice(all_parents)
        bpm = random.randint(min_bpm, max_bpm)

        # Combine genres and instruments
        genres1 = parent1.get('Primary_Genres', '').strip('"').split(',')[0].strip()
        genres2 = parent2.get('Primary_Genres', '').strip('"').split(',')[0].strip()

        instr1 = parent1.get('Key_Instruments', '').strip('"').split(',')[:2]
        instr2 = parent2.get('Key_Instruments', '').strip('"').split(',')[:2]
        combined_instruments = ', '.join(instr1 + instr2)

        mood1 = parent1.get('Mood_Keywords', '').split()[0] if parent1.get('Mood_Keywords') else 'driving'
        mood2 = parent2.get('Mood_Keywords', '').split()[0] if parent2.get('Mood_Keywords') else 'hypnotic'

        prompt = {
            'Prompt_ID': str(prompt_id),
            'Time_Block': time_block,
            'BPM': str(bpm),
            'Brain_Wave_Target': brainwave_target,
            'Duration_Type': duration_type,
            'Primary_Genres': f'"{genres1}, {genres2}"',
            'Key_Instruments': f'"{combined_instruments}"',
            'Mood_Keywords': f'{mood1} {mood2} sophisticated hybrid',
            'Suno_Short_Prompt': '',
            'Full_Prompt': f"[Generated] Hybrid of prompts #{parent1['Prompt_ID']} and #{parent2['Prompt_ID']} at {bpm} BPM. {genres1} meets {genres2} with {combined_instruments}.",
            'Notes': f"Hybrid: Parent #{parent1['Prompt_ID']} + Parent #{parent2['Prompt_ID']}. Auto-generated.",
            'Generated': 'No',
            'Suno_Refined': '',
            'Rating': ''
        }
        generated_prompts.append(prompt)
        print(f"   #{prompt_id}: {genres1} + {genres2} at {bpm} BPM")
        prompt_id += 1

    # Generate mutations
    print(f"\n🧬 Generating {mutations} mutations with new influences...")
    for i in range(mutations):
        if i < len(mutation_influences):
            parent = random.choice(parents)
            mutation = mutation_influences[i]
            bpm = random.randint(min_bpm, max_bpm)

            genres = parent.get('Primary_Genres', '').strip('"')
            base_instruments = parent.get('Key_Instruments', '').strip('"').split(',')[:2]
            mutation_name = mutation.get('Name', 'unknown')

            combined_instruments = ', '.join(base_instruments + [mutation_name.lower()])
            mood = parent.get('Mood_Keywords', '').split()[0] if parent.get('Mood_Keywords') else 'experimental'

            prompt = {
                'Prompt_ID': str(prompt_id),
                'Time_Block': time_block,
                'BPM': str(bpm),
                'Brain_Wave_Target': brainwave_target,
                'Duration_Type': duration_type,
                'Primary_Genres': genres,
                'Key_Instruments': f'"{combined_instruments}"',
                'Mood_Keywords': f'{mood} experimental mutation',
                'Suno_Short_Prompt': '',
                'Full_Prompt': f"[Generated] Mutation of prompt #{parent['Prompt_ID']} with {mutation_name} at {bpm} BPM. Testing unexplored influence: {mutation['Category']}.",
                'Notes': f"Mutation: {mutation_name} ({mutation['Category']}). Based on prompt #{parent['Prompt_ID']}. Auto-generated.",
                'Generated': 'No',
                'Suno_Refined': '',
                'Rating': ''
            }
            generated_prompts.append(prompt)
            print(f"   #{prompt_id}: {genres} + {mutation_name} at {bpm} BPM")
            prompt_id += 1

    # Write to CSV
    print(f"\n💾 Writing {len(generated_prompts)} prompts to CSV...")
    all_prompts = read_prompts()
    all_prompts.extend(generated_prompts)
    write_prompts(all_prompts)

    print(f"✅ Successfully generated prompts #{next_id}-#{prompt_id-1}")
    print()
    print("📝 Next steps:")
    print(f"   1. Review generated prompts: prompt-show {next_id}")
    print(f"   2. Generate in Suno (mark with prompt-mark-generated)")
    print(f"   3. Rate the results (prompt-rate)")
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

    # Non-interactive mode - generate plan for LLM
    generate_prompts_plan(args.time_block, args.count)

if __name__ == '__main__':
    main()
