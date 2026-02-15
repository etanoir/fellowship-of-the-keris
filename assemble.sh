#!/bin/bash
# Assembly script for Persekutuan Keris - Complete Novel
# Assembles all chapters, art, and back matter into a single markdown file

DIR="/Users/iksan.aripin/projects/fellowship_of_the_keris"
OUT="$DIR/persekutuan_keris_complete.md"
CHAPTERS="$DIR/chapters"
BACK="$DIR/back_matter/glossary_and_appendices.md"
COVER="$DIR/temp_art_cover_map.md"
VIG1="$DIR/temp_art_vignettes_1_10.md"
VIG2="$DIR/temp_art_vignettes_11_20.md"

# Helper function: extract a vignette section from a file
# Usage: extract_vignette FILE "## Vignette: LABEL"
extract_vignette() {
    local file="$1"
    local heading="$2"
    # Find the line number of the heading, then extract from there through the closing ```
    local start_line
    start_line=$(grep -n "^${heading}" "$file" | head -1 | cut -d: -f1)
    if [ -z "$start_line" ]; then
        echo "WARNING: Could not find '${heading}' in $file" >&2
        return 1
    fi
    # From the heading, find the closing ``` (the second ``` after the heading)
    # Structure: heading, blank, opening ```, 25 art lines, closing ```
    local end_line
    end_line=$(tail -n "+${start_line}" "$file" | grep -n '```' | sed -n '2p' | cut -d: -f1)
    if [ -z "$end_line" ]; then
        echo "WARNING: Could not find closing backticks for '${heading}'" >&2
        return 1
    fi
    end_line=$((start_line + end_line - 1))
    sed -n "${start_line},${end_line}p" "$file"
}

# Start fresh
> "$OUT"

echo "=== STEP 1: Cover Page ==="
sed -n '3,53p' "$COVER" >> "$OUT"

echo "=== STEP 2: Author's Note ==="
cat >> "$OUT" << 'SEPARATOR'

---

SEPARATOR
sed -n '10,43p' "$BACK" >> "$OUT"

echo "=== STEP 3: Map ==="
cat >> "$OUT" << 'SEPARATOR'

---

SEPARATOR
sed -n '57,125p' "$COVER" >> "$OUT"

echo "=== STEP 4: Character List ==="
cat >> "$OUT" << 'SEPARATOR'

---

SEPARATOR
sed -n '188,394p' "$BACK" >> "$OUT"

echo "=== STEP 5: Chapters with Vignettes ==="

# ---- ACT I ----
cat >> "$OUT" << 'ACT'

---

# ACT I: TANAH ASAL
## *The Homeland*

---

ACT

# Prologue
extract_vignette "$VIG1" "## Vignette: Prologue" >> "$OUT"
echo "" >> "$OUT"
sed -n '15,$p' "$CHAPTERS/00_prologue.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 1
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG1" "## Vignette: Bab 1" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/01_tanah_sunda.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 2
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG1" "## Vignette: Bab 2" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/02_warisan.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 3
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG1" "## Vignette: Bab 3" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/03_bayangan.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 4
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG1" "## Vignette: Bab 4" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/04_pelarian.md" >> "$OUT"
echo "" >> "$OUT"

# ---- ACT II ----
cat >> "$OUT" << 'ACT'

---

# ACT II: PERJALANAN
## *The Journey*

---

ACT

# Bab 5
extract_vignette "$VIG1" "## Vignette: Bab 5" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/05_perjalanan_ke_dieng.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 6
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG1" "## Vignette: Bab 6" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/06_dataran_dieng.md" >> "$OUT"
echo "" >> "$OUT"

# ---- ACT III ----
cat >> "$OUT" << 'ACT'

---

# ACT III: PERSEKUTUAN
## *The Fellowship*

---

ACT

# Bab 7
extract_vignette "$VIG1" "## Vignette: Bab 7" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/07_sang_prabu_siliwangi.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 8
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG1" "## Vignette: Bab 8" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/08_balairung_agung.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 9
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG1" "## Vignette: Bab 9" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/09_pasukan_sembilan.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 10
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG1" "## Vignette: Bab 10" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/10_sumpah_di_candi.md" >> "$OUT"
echo "" >> "$OUT"

# ---- ACT IV ----
cat >> "$OUT" << 'ACT'

---

# ACT IV: KEGELAPAN
## *The Darkness*

---

ACT

# Bab 11
extract_vignette "$VIG2" "## Vignette: Bab 11" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/11_bukit_barisan.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 12
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG2" "## Vignette: Bab 12" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/12_gua_sewu.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 13
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG2" "## Vignette: Bab 13" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/13_jatuhnya_eyang_guru.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 14
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG2" "## Vignette: Bab 14" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/14_ngarai_sianok.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 15-16
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG2" "## Vignette: Bab 15-16" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/15_16_cermin_laut_jawa.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 17-18
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG2" "## Vignette: Bab 17-18" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/17_18_rawa_pening_pelabuhan.md" >> "$OUT"
echo "" >> "$OUT"

# ---- ACT V ----
cat >> "$OUT" << 'ACT'

---

# ACT V: PERPECAHAN
## *The Breaking*

---

ACT

# Bab 19-20
extract_vignette "$VIG2" "## Vignette: Bab 19-20" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/19_20_godaan_pertempuran.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 21-23
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG2" "## Vignette: Bab 21-23" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/21_22_23_perpecahan.md" >> "$OUT"
echo "" >> "$OUT"

# Bab 24-25
cat >> "$OUT" << 'SEP'

---

SEP
extract_vignette "$VIG2" "## Vignette: Bab 24-25" >> "$OUT"
echo "" >> "$OUT"
cat "$CHAPTERS/24_25_epilog.md" >> "$OUT"
echo "" >> "$OUT"

# End of Book One
cat >> "$OUT" << 'END_BOOK'

---

# END OF BOOK ONE

---

END_BOOK

echo "=== STEP 6: Back Matter ==="

# Glossary (lines 395-978)
sed -n '395,978p' "$BACK" >> "$OUT"

cat >> "$OUT" << 'SEP'

---

SEP

# Pupuh and Poetic Forms (lines 979-1063)
sed -n '979,1063p' "$BACK" >> "$OUT"

cat >> "$OUT" << 'SEP'

---

SEP

# Language Registers (lines 1064-1157)
sed -n '1064,1157p' "$BACK" >> "$OUT"

cat >> "$OUT" << 'SEP'

---

SEP

# Legends and Folklore (lines 1158-1257)
sed -n '1158,1257p' "$BACK" >> "$OUT"

cat >> "$OUT" << 'SEP'

---

SEP

# Pronunciation Guide (lines 1258-1454)
sed -n '1258,1454p' "$BACK" >> "$OUT"

cat >> "$OUT" << 'SEP'

---

SEP

# Kingdoms of Nusantara (lines 1455-1524)
sed -n '1455,1524p' "$BACK" >> "$OUT"

cat >> "$OUT" << 'SEP'

---

SEP

# Copyright/closing (lines 1527-1540)
sed -n '1527,1542p' "$BACK" >> "$OUT"

echo "=== STEP 7: Closing Border ==="
cat >> "$OUT" << 'CLOSING'

---

```
+--------------------------------------------------------------------+
|  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\   |
|  \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/   |
|                                                                    |
|                    Nembah. Terima kasih.                            |
|                                                                    |
|  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\   |
|  \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/   |
+--------------------------------------------------------------------+
```
CLOSING

echo ""
echo "=== Assembly complete! ==="
echo ""
echo "--- Verification ---"
echo "Line count:"
wc -l "$OUT"
echo ""
echo "Byte count:"
wc -c "$OUT"
echo ""
echo "Chapter headings count:"
grep -c '^# Bab\|^## Bab\|^# Prologue\|^## Prologue' "$OUT"
echo ""
echo "Code fence count (should be even, ~44):"
grep -c '```' "$OUT"
echo ""
echo "ACT headings:"
grep '^# ACT' "$OUT"
echo ""
echo "END OF BOOK ONE check:"
grep '# END OF BOOK ONE' "$OUT"
