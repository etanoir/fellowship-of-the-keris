#!/usr/bin/env python3
"""Assembly script for Persekutuan Keris - Complete Novel"""

import re
import os

DIR = "/Users/iksan.aripin/projects/fellowship_of_the_keris"
OUT = os.path.join(DIR, "persekutuan_keris_complete.md")
CHAPTERS = os.path.join(DIR, "chapters")
BACK = os.path.join(DIR, "back_matter", "glossary_and_appendices.md")
COVER = os.path.join(DIR, "temp_art_cover_map.md")
VIG1 = os.path.join(DIR, "temp_art_vignettes_1_10.md")
VIG2 = os.path.join(DIR, "temp_art_vignettes_11_20.md")


def read_lines(filepath):
    """Read file and return list of lines (1-indexed access via [i-1])."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()


def extract_line_range(lines, start, end):
    """Extract lines from start to end (1-indexed, inclusive)."""
    return "".join(lines[start - 1 : end])


def read_file(filepath):
    """Read entire file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def extract_vignette(filepath, heading):
    """Extract a vignette section: heading through closing backticks."""
    lines = read_lines(filepath)
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith(heading):
            start = i
            break
    if start is None:
        print(f"WARNING: Could not find '{heading}' in {filepath}")
        return ""

    # Find the two ``` markers after the heading
    backtick_count = 0
    end = start
    for i in range(start, len(lines)):
        if lines[i].strip() == "```":
            backtick_count += 1
            if backtick_count == 2:
                end = i
                break

    return "".join(lines[start : end + 1])


# Load all source files
cover_lines = read_lines(COVER)
back_lines = read_lines(BACK)

parts = []

# ========== STEP 1: Cover Page ==========
print("Step 1: Cover Page")
parts.append(extract_line_range(cover_lines, 3, 53))

# ========== STEP 2: Author's Note ==========
print("Step 2: Author's Note")
parts.append("\n---\n\n")
parts.append(extract_line_range(back_lines, 10, 43))

# ========== STEP 3: Map ==========
print("Step 3: Map")
parts.append("\n---\n\n")
parts.append(extract_line_range(cover_lines, 57, 125))

# ========== STEP 4: Character List ==========
print("Step 4: Character List")
parts.append("\n---\n\n")
parts.append(extract_line_range(back_lines, 188, 394))

# ========== STEP 5: Chapters with Vignettes ==========
print("Step 5: Chapters")

# Helper to add a chapter with its vignette
def add_chapter(vig_file, vig_heading, chapter_file, skip_lines=0):
    """Add vignette + chapter content."""
    vig = extract_vignette(vig_file, vig_heading)
    parts.append(vig)
    parts.append("\n")
    ch_lines = read_lines(chapter_file)
    if skip_lines > 0:
        parts.append("".join(ch_lines[skip_lines:]))
    else:
        parts.append("".join(ch_lines))
    parts.append("\n")


def add_separator():
    parts.append("\n---\n\n")


def add_act(act_num, title_upper, subtitle):
    parts.append(f"\n---\n\n# ACT {act_num}: {title_upper}\n## *{subtitle}*\n\n---\n\n")


# ---- ACT I ----
add_act("I", "TANAH ASAL", "The Homeland")

# Prologue
add_chapter(VIG1, "## Vignette: Prologue", os.path.join(CHAPTERS, "00_prologue.md"), skip_lines=14)

# Bab 1
add_separator()
add_chapter(VIG1, "## Vignette: Bab 1", os.path.join(CHAPTERS, "01_tanah_sunda.md"))

# Bab 2
add_separator()
add_chapter(VIG1, "## Vignette: Bab 2", os.path.join(CHAPTERS, "02_warisan.md"))

# Bab 3
add_separator()
add_chapter(VIG1, "## Vignette: Bab 3", os.path.join(CHAPTERS, "03_bayangan.md"))

# Bab 4
add_separator()
add_chapter(VIG1, "## Vignette: Bab 4", os.path.join(CHAPTERS, "04_pelarian.md"))

# ---- ACT II ----
add_act("II", "PERJALANAN", "The Journey")

# Bab 5
add_chapter(VIG1, "## Vignette: Bab 5", os.path.join(CHAPTERS, "05_perjalanan_ke_dieng.md"))

# Bab 6
add_separator()
add_chapter(VIG1, "## Vignette: Bab 6", os.path.join(CHAPTERS, "06_dataran_dieng.md"))

# ---- ACT III ----
add_act("III", "PERSEKUTUAN", "The Fellowship")

# Bab 7
add_chapter(VIG1, "## Vignette: Bab 7", os.path.join(CHAPTERS, "07_sang_prabu_siliwangi.md"))

# Bab 8
add_separator()
add_chapter(VIG1, "## Vignette: Bab 8", os.path.join(CHAPTERS, "08_balairung_agung.md"))

# Bab 9
add_separator()
add_chapter(VIG1, "## Vignette: Bab 9", os.path.join(CHAPTERS, "09_pasukan_sembilan.md"))

# Bab 10
add_separator()
add_chapter(VIG1, "## Vignette: Bab 10", os.path.join(CHAPTERS, "10_sumpah_di_candi.md"))

# ---- ACT IV ----
add_act("IV", "KEGELAPAN", "The Darkness")

# Bab 11
add_chapter(VIG2, "## Vignette: Bab 11", os.path.join(CHAPTERS, "11_bukit_barisan.md"))

# Bab 12
add_separator()
add_chapter(VIG2, "## Vignette: Bab 12", os.path.join(CHAPTERS, "12_gua_sewu.md"))

# Bab 13
add_separator()
add_chapter(VIG2, "## Vignette: Bab 13", os.path.join(CHAPTERS, "13_jatuhnya_eyang_guru.md"))

# Bab 14
add_separator()
add_chapter(VIG2, "## Vignette: Bab 14", os.path.join(CHAPTERS, "14_ngarai_sianok.md"))

# Bab 15-16
add_separator()
add_chapter(VIG2, "## Vignette: Bab 15-16", os.path.join(CHAPTERS, "15_16_cermin_laut_jawa.md"))

# Bab 17-18
add_separator()
add_chapter(VIG2, "## Vignette: Bab 17-18", os.path.join(CHAPTERS, "17_18_rawa_pening_pelabuhan.md"))

# ---- ACT V ----
add_act("V", "PERPECAHAN", "The Breaking")

# Bab 19-20
add_chapter(VIG2, "## Vignette: Bab 19-20", os.path.join(CHAPTERS, "19_20_godaan_pertempuran.md"))

# Bab 21-23
add_separator()
add_chapter(VIG2, "## Vignette: Bab 21-23", os.path.join(CHAPTERS, "21_22_23_perpecahan.md"))

# Bab 24-25
add_separator()
add_chapter(VIG2, "## Vignette: Bab 24-25", os.path.join(CHAPTERS, "24_25_epilog.md"))

# End of Book One
parts.append("\n---\n\n# END OF BOOK ONE\n\n---\n\n")

# ========== STEP 6: Back Matter ==========
print("Step 6: Back Matter")

# Glossary (lines 395-978)
parts.append(extract_line_range(back_lines, 395, 978))

add_separator()

# Pupuh and Poetic Forms (lines 979-1063)
parts.append(extract_line_range(back_lines, 979, 1063))

add_separator()

# Language Registers (lines 1064-1157)
parts.append(extract_line_range(back_lines, 1064, 1157))

add_separator()

# Legends and Folklore (lines 1158-1257)
parts.append(extract_line_range(back_lines, 1158, 1257))

add_separator()

# Pronunciation Guide (lines 1258-1454)
parts.append(extract_line_range(back_lines, 1258, 1454))

add_separator()

# Kingdoms of Nusantara (lines 1455-1524)
parts.append(extract_line_range(back_lines, 1455, 1524))

add_separator()

# Copyright/closing (lines 1527-1542)
parts.append(extract_line_range(back_lines, 1527, 1542))

# ========== STEP 7: Closing Border ==========
print("Step 7: Closing Border")
closing_border = "\n---\n\n```\n"
closing_border += "+--------------------------------------------------------------------+\n"
closing_border += "|  /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\   |\n"
closing_border += "|  \\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/   |\n"
closing_border += "|                                                                    |\n"
closing_border += "|                    Nembah. Terima kasih.                            |\n"
closing_border += "|                                                                    |\n"
closing_border += "|  /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\   |\n"
closing_border += "|  \\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/   |\n"
closing_border += "+--------------------------------------------------------------------+\n"
closing_border += "```\n"
parts.append(closing_border)

# ========== Write output ==========
print(f"Writing to {OUT}...")
with open(OUT, "w", encoding="utf-8") as f:
    f.write("".join(parts))

print("Assembly complete!")
print()

# ========== Verification ==========
with open(OUT, "r", encoding="utf-8") as f:
    content = f.read()
    lines_list = content.split("\n")

print(f"Line count: {len(lines_list)}")
print(f"Character count: {len(content)}")

import subprocess

# Chapter headings
chapter_count = 0
for line in lines_list:
    if re.match(r'^(#|##) (Bab|Prologue)', line):
        chapter_count += 1
print(f"Chapter headings: {chapter_count}")

# Code fences
fence_count = sum(1 for line in lines_list if line.strip() == "```")
print(f"Code fence count (should be even, ~44): {fence_count}")

# ACT headings
act_headings = [line for line in lines_list if line.startswith("# ACT")]
print(f"ACT headings ({len(act_headings)}):")
for h in act_headings:
    print(f"  {h}")

# END OF BOOK ONE
eob = [line for line in lines_list if "END OF BOOK ONE" in line]
print(f"END OF BOOK ONE: {'Found' if eob else 'NOT FOUND'}")
