#!/usr/bin/env python3
"""
Analyze Apple Music Library.xml to extract listening patterns and potential influences.

This script parses your Apple Music library export and identifies:
- Top artists by play count
- Genre clusters
- Instrumental vs vocal tracks
- Potential influences for programming music
"""

import xml.etree.ElementTree as ET
from collections import defaultdict, Counter
from pathlib import Path
import sys

def parse_track(track_dict):
    """Parse a track dictionary from the XML."""
    track = {}
    current_key = None

    for elem in track_dict:
        if elem.tag == 'key':
            current_key = elem.text
        elif current_key:
            if elem.tag == 'string':
                track[current_key] = elem.text
            elif elem.tag == 'integer':
                track[current_key] = int(elem.text)
            elif elem.tag == 'true':
                track[current_key] = True
            elif elem.tag == 'false':
                track[current_key] = False
            current_key = None

    return track

def analyze_library(xml_path):
    """Analyze the Apple Music library."""
    print("🎵 Parsing Apple Music Library...")
    print(f"   File: {xml_path}")
    print()

    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Find the Tracks dictionary
    plist = root.find('dict')
    tracks_key = None
    for i, elem in enumerate(plist):
        if elem.tag == 'key' and elem.text == 'Tracks':
            tracks_key = i
            break

    if tracks_key is None:
        print("❌ Could not find Tracks in library")
        return

    tracks_dict = plist[tracks_key + 1]

    # Parse all tracks
    tracks = []
    current_track = []

    for elem in tracks_dict:
        if elem.tag == 'key':
            if current_track:
                track = parse_track(current_track)
                tracks.append(track)
                current_track = []
        elif elem.tag == 'dict':
            current_track = elem

    if current_track:
        track = parse_track(current_track)
        tracks.append(track)

    print(f"✅ Parsed {len(tracks)} tracks")
    print()

    return analyze_patterns(tracks)

def analyze_patterns(tracks):
    """Analyze listening patterns."""

    # Filter to tracks with play counts
    played_tracks = [t for t in tracks if t.get('Play Count', 0) > 0]

    print(f"📊 LIBRARY STATISTICS")
    print(f"=" * 70)
    print(f"  Total tracks in library:     {len(tracks):,}")
    print(f"  Tracks with play history:    {len(played_tracks):,}")
    print(f"  Total plays:                 {sum(t.get('Play Count', 0) for t in tracks):,}")
    print()

    # Top artists by play count
    artist_plays = defaultdict(int)
    artist_tracks = defaultdict(int)

    for track in played_tracks:
        artist = track.get('Artist', 'Unknown')
        plays = track.get('Play Count', 0)
        artist_plays[artist] += plays
        artist_tracks[artist] += 1

    print(f"🎤 TOP 30 ARTISTS (by play count)")
    print(f"=" * 70)

    top_artists = sorted(artist_plays.items(), key=lambda x: x[1], reverse=True)[:30]

    for i, (artist, plays) in enumerate(top_artists, 1):
        track_count = artist_tracks[artist]
        avg_plays = plays / track_count if track_count > 0 else 0
        print(f"  {i:2}. {artist[:45]:45s} {plays:5,} plays ({track_count:3} tracks, {avg_plays:.1f} avg)")

    print()

    # Genre analysis
    genre_plays = defaultdict(int)
    genre_tracks = defaultdict(int)

    for track in played_tracks:
        genre = track.get('Genre', 'Unknown')
        plays = track.get('Play Count', 0)
        genre_plays[genre] += plays
        genre_tracks[genre] += 1

    print(f"🎼 TOP 20 GENRES (by play count)")
    print(f"=" * 70)

    top_genres = sorted(genre_plays.items(), key=lambda x: x[1], reverse=True)[:20]

    for i, (genre, plays) in enumerate(top_genres, 1):
        track_count = genre_tracks[genre]
        print(f"  {i:2}. {genre[:45]:45s} {plays:5,} plays ({track_count:3} tracks)")

    print()

    # Most played individual tracks
    print(f"🔥 TOP 20 MOST PLAYED TRACKS")
    print(f"=" * 70)

    top_tracks = sorted(played_tracks, key=lambda x: x.get('Play Count', 0), reverse=True)[:20]

    for i, track in enumerate(top_tracks, 1):
        name = track.get('Name', 'Unknown')
        artist = track.get('Artist', 'Unknown')
        plays = track.get('Play Count', 0)
        genre = track.get('Genre', 'Unknown')
        print(f"  {i:2}. {name[:35]:35s} - {artist[:25]:25s} ({plays:3} plays) [{genre}]")

    print()

    # Potential instrumental tracks
    instrumental_keywords = ['instrumental', 'piano', 'ambient', 'soundtrack', 'classical', 'jazz', 'electronic']

    potential_instrumental = []
    for track in played_tracks:
        genre = track.get('Genre', '').lower()
        name = track.get('Name', '').lower()

        if any(kw in genre or kw in name for kw in instrumental_keywords):
            potential_instrumental.append(track)

    print(f"🎹 POTENTIAL INSTRUMENTAL/PROGRAMMING MUSIC")
    print(f"=" * 70)
    print(f"  Found {len(potential_instrumental)} tracks with instrumental indicators")
    print()

    # Top instrumental artists
    instrumental_artist_plays = defaultdict(int)
    for track in potential_instrumental:
        artist = track.get('Artist', 'Unknown')
        plays = track.get('Play Count', 0)
        instrumental_artist_plays[artist] += plays

    print("  Top instrumental artists:")
    top_instrumental = sorted(instrumental_artist_plays.items(), key=lambda x: x[1], reverse=True)[:15]

    for i, (artist, plays) in enumerate(top_instrumental, 1):
        print(f"    {i:2}. {artist[:50]:50s} {plays:4} plays")

    print()

    return {
        'tracks': tracks,
        'played_tracks': played_tracks,
        'top_artists': top_artists,
        'top_genres': top_genres,
        'top_tracks': top_tracks,
        'instrumental_tracks': potential_instrumental,
        'instrumental_artists': top_instrumental
    }

def suggest_influences(analysis):
    """Suggest potential influences based on listening patterns."""

    print(f"💡 POTENTIAL INFLUENCES FOR PROGRAMMING MUSIC")
    print(f"=" * 70)
    print()
    print("Based on your listening history, consider adding these influences:")
    print()

    # Get top instrumental artists
    instrumental_artists = analysis['instrumental_artists'][:10]

    for i, (artist, plays) in enumerate(instrumental_artists, 1):
        print(f"{i:2}. {artist}")
        print(f"    Plays: {plays}")
        print(f"    💭 Consider: What specific sonic elements from {artist} could work as")
        print(f"       background texture? (instrumentation, rhythms, production techniques)")
        print()

    print("📝 NEXT STEPS:")
    print("=" * 70)
    print("1. Review top artists and identify which have programming-appropriate elements")
    print("2. For each artist, identify:")
    print("   - Elements to USE (textures, rhythms, production)")
    print("   - Elements to AVOID (vocals, hooks, dramatic changes)")
    print("3. Add to influences_library.csv using influence-manage skill")
    print()

def main():
    xml_path = Path('Library.xml')

    if not xml_path.exists():
        print(f"❌ Library.xml not found in current directory")
        print(f"   Expected: {xml_path.absolute()}")
        sys.exit(1)

    analysis = analyze_library(xml_path)

    if analysis:
        suggest_influences(analysis)

if __name__ == '__main__':
    main()
