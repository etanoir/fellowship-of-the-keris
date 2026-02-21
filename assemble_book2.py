#!/usr/bin/env python3
"""Assembly script for Dua Menara Berapi - Book Two Complete Novel"""

import os
import re

DIR = "/Users/iksan.aripin/projects/two_tower"
OUT = os.path.join(DIR, "DUA_MENARA_BERAPI_COMPLETE.md")
CHAPTERS = os.path.join(DIR, "chapters")

# Chapter files in order
CHAPTER_FILES = [
    "tt_01_fajar_merah.md",
    "tt_02_si_burik.md",
    "tt_03_sanghyang_wana.md",
    "tt_04_pasukan_kuda.md",
    "tt_05_dwija_putih.md",
    "tt_06_balairung_mataram.md",
    "tt_07_gerbang_malapetaka.md",
    "tt_08_candi_abang.md",
    "tt_09_amarah_sanghyang.md",
    "tt_10_gua_kalajengking.md",
]

# Three narrative parts
PARTS = {
    "I": {
        "title": "JALAN NU PEGAT",
        "subtitle": "The Sundered Paths",
        "chapters": [0, 1, 2, 3],  # Ch 1-4
    },
    "II": {
        "title": "DWIJA PUTIH SARENG RAJA SINGA",
        "subtitle": "The White Sage and the Lion King",
        "chapters": [4, 5],  # Ch 5-6
    },
    "III": {
        "title": "DUA MENARA BERAPI",
        "subtitle": "The Two Volcanic Towers",
        "chapters": [6, 7, 8, 9],  # Ch 7-10
    },
}


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def word_count(text):
    return len(text.split())


parts = []

# ========== TITLE PAGE ==========
print("Step 1: Title Page")
parts.append("""```
+====================================================================+
|  /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\   |
|  \\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/   |
|                                                                    |
|                      DUA MENARA BERAPI                             |
|                   The Two Volcanic Towers                          |
|                                                                    |
|                         Book Two of                                |
|                  The Nusantara Chronicles                          |
|                                                                    |
|                    A Javanese Adaptation                           |
|                  of J.R.R. Tolkien's Legacy                        |
|                                                                    |
|  /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\   |
|  \\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/   |
+====================================================================+
```

---

""")

# ========== THREE NARRATIVE PATHS OVERVIEW ==========
parts.append("""# The Three Paths

> *The fellowship is broken. The keris-bearer walks toward the fire.*
> *The hunters ride toward the throne. The small ones wake the forest.*
> *Three paths, one dharma. The two towers of fire wait.*

**Path of the King** (Chapters 1, 4, 5, 6, 8): Raden Wijaya, Dewi Anjani, and Tumenggung Batu pursue the captured Tuyul, encounter the Horse Lords of Kediri, find the Dwija Putih returned, free King Jayabaya from Ki Surasenta's spell, and defend Candi Abang against the Shadow King's armies.

**Path of the Forest Guardians** (Chapters 3, 9): Cepot and Dawala, captured and lost in the Wanantara, awaken the ancient Sanghyang Wana forest spirits, and lead them to war against Empu Gandring's ironworks at Merapi.

**Path of the Bearer** (Chapters 2, 7, 10): Kian Santang and Bagus, guided by the treacherous Si Burik, cross the volcanic wastelands toward Krakatau to destroy the Keris Murka in the fire that forged it.

---

""")

# ========== CHAPTERS ==========
print("Step 2: Chapters")

total_words = 0
for part_num, part_info in PARTS.items():
    # Part header
    parts.append(f"\n---\n\n# BAGIAN {part_num}: {part_info['title']}\n## *{part_info['subtitle']}*\n\n---\n\n")

    for i, ch_idx in enumerate(part_info["chapters"]):
        ch_file = CHAPTER_FILES[ch_idx]
        ch_path = os.path.join(CHAPTERS, ch_file)
        content = read_file(ch_path)
        wc = word_count(content)
        total_words += wc
        print(f"  Chapter {ch_idx + 1}: {ch_file} ({wc:,} words)")

        if i > 0:
            parts.append("\n---\n\n")
        parts.append(content)
        parts.append("\n")

# ========== CLOSING ==========
print("Step 3: Closing")
parts.append("""
---

```
+====================================================================+
|  /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\   |
|  \\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/   |
|                                                                    |
|                  END OF BOOK TWO                                   |
|                                                                    |
|            Nembah. Rahayu ka sadayana.                             |
|                                                                    |
|          The story concludes in Book Three:                        |
|              BALIKNA SANG RAJA                                     |
|            (The Return of the King)                                |
|                                                                    |
|  /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\   |
|  \\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/   |
+====================================================================+
```
""")

# ========== WRITE OUTPUT ==========
print(f"\nWriting to {OUT}...")
with open(OUT, "w", encoding="utf-8") as f:
    f.write("".join(parts))

# ========== VERIFICATION ==========
print("\n=== Verification ===")
with open(OUT, "r", encoding="utf-8") as f:
    full_content = f.read()
    lines_list = full_content.split("\n")

print(f"Total words: {total_words:,}")
print(f"Line count: {len(lines_list):,}")
print(f"Character count: {len(full_content):,}")

# Chapter headings
ch_count = sum(1 for line in lines_list if re.match(r'^# Bab', line))
print(f"Chapter headings: {ch_count}")

# Part headings
part_headings = [line for line in lines_list if line.startswith("# BAGIAN")]
print(f"Part headings ({len(part_headings)}):")
for h in part_headings:
    print(f"  {h}")

# Dalang markers
dalang_count = sum(1 for line in lines_list if "Dalang" in line)
print(f"Dalang references: {dalang_count}")

# END OF BOOK TWO
eob = any("END OF BOOK TWO" in line for line in lines_list)
print(f"END OF BOOK TWO: {'Found' if eob else 'NOT FOUND'}")

print("\nAssembly complete!")
