# Assignment 1 feedback - Vedant Gattani

**Formative feedback | Rubric 2026.2**

All five FASTA answers matched the independent checks. The explanations of why sequence lines must be joined are useful, and your README and commit history give a specific account of help, checking and subsequent changes.

The most important remaining bug is in csvtospace.sh: it still performs the tab-to-comma substitution rather than the requested comma-to-space conversion. This is an easy mistake when adapting a script, but a useful test should catch it immediately. Use a tiny CSV for which you can write down the expected output, then compare the contents, not just the filename or Done message.

Both converters also need quoted input paths, reliable output-directory creation and proper failure handling. Their ../results paths assume code/ as the starting directory, whereas these scripts should run from the repository root. Test a filename containing spaces and a run with no existing results directory.

Your own TSV is currently empty. Populate it with a small real table containing an empty field, and check that the field survives conversion. Then tidy the explanations: Q4 counts the literal ATGC motif, not individual bases; [AT] and [GC] match either individual base, not the adjacent pairs AT and GC. Correct the tab-converter description in the README, list bc as a dependency and ignore generated results. Keep the focused commits, but make the tests strong enough to expose a copied transformation that has not been changed.

---

## Project structure

Relevant tracked layout (simplified; missing required paths are marked):

```text
README.md
.gitignore
code/  unixPrac1.txt, tabtocsv.sh, csvtospace.sh
data/fasta/  3 required files present
data/temperatures/  4 required files present
data/tab-example.tsv [empty]
results/  no files tracked; generated on run
sandbox/  no files tracked; optional
```

All required filenames are present under the root layout, and no files are tracked in results/ or sandbox/. However, data/tab-example.tsv is empty: the structure is complete by filename, but the required example is not yet usable.

Populate that file with a small tab-delimited table and keep results/ as a generated destination. Sandbox is already ignored; add an explicit results rule too. Use the README to make the connection between each file in code/, its input in data/ and its expected output clear.

**Assessed snapshot:** `4acd812fef7f6b0b73c19f031ccdd1594488229f`
