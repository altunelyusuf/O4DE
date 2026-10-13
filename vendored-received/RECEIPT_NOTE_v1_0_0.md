# Receipt note for the material in this folder (version 1.0.0)

These files reached the repository on 2026-10-13 in commit `98cd3e8` ("Add domain engineering material as received") and are kept here **byte for byte**. The commit is the record of how they arrived; the receipt README (`README.md` in this folder) and the inventory (`INVENTORY.tsv`) were written by whoever pushed them.

What changed when they were moved into this folder (BP-D7: nothing was edited):

- The four folders, the receipt README and the inventory moved from the repository root into `vendored-received/`. The paths in `INVENTORY.tsv` are therefore relative to the repository root **as it was at commit `98cd3e8`**; to check a file, prefix its path with `vendored-received/`. The hashes still hold.
- The received checksum list `MANIFEST_SHA256.txt` was replaced by the repository's root manifest, which now lists every file including these.
- Two Turtle files that do not parse had `.txt` added to their names: `03-ai4se-material/Ontology_Module_DomainEngineering.ttl` (syntax error at line 167) and `03-ai4se-material/enterprise-edition-v4.5/AI4SE_Ontology_v4_5_ENTERPRISE_EDITION.ttl` (syntax error at line 14). The release publisher parses every Turtle file in the package, so a file known not to parse cannot keep the `.ttl` ending. Their bytes are unchanged and the errors are recorded in `INVENTORY.tsv`.

Why the folder is named `vendored-received`: the OE structure class table treats a folder whose name starts with `vendored` as a copy of material that belongs to other sources; the structure check does not count its Turtle files as live corpus of this package.

How the material is used: see `04-documentation/` of the package for what each source contributed and what is still to be consolidated.
