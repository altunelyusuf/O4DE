# O4DE: Ontology for Domain Engineering

O4DE is a formal ontology that gives analysts and architects one shared, machine-checkable vocabulary for **domain engineering**: the activities, assets, features and variability of the discipline, the processes, roles, rules and metrics that govern it, and the business context it works in (customers, products, channels, vendors, organization and agility), and the structure of the enterprise domain itself: foundations, organization, governance, capabilities, work, requirements, data and technology, assets, change and knowledge.

Current version: **1.1.0** (2026-10-13). Licence: Apache License 2.0 (`LICENSE`). Owner: Yusuf Altunel.

## What is in the package

| Folder or file | What it is |
|---|---|
| `01-ontologies/o4de_tbox_v1_1_0.ttl` | The T-Box: every class, property and axiom, each with a label and a definition. |
| `01-ontologies/o4de_abox_v1_1_0.ttl` | The A-Box: thirteen SKOS taxonomies (twelve mirror the class hierarchies, one divides the enterprise domain structure into its parts), and illustrative example individuals (invented, not sourced facts). |
| `02-shacl-safeguards/o4de_shacl_v1_1_0.ttl` | The shapes: they check documentation, taxonomy structure, domain, range, cardinality and value restrictions on data written with the T-Box. |
| `03-tooling/o4de_hermit_check_v1_1_0.py` | Consistency check with the HermiT reasoner. |
| `04-documentation/` | The documentation template, the 40 competency questions with SPARQL, the measured comparison with Domain Engineering Ontology v5.2, the record of its consolidation, the text of the meta-definition the ontology follows, and the validation record (`O4DE_Validation_Record_v1_1_0.md`). |
| `05-gates/o4de_gate_v1_1_0.py` | The release gate: runs every check below and exits non-zero if one fails. |
| `vendored-received/` | The domain engineering material that reached this repository before the package was built, kept byte for byte (see its `RECEIPT_NOTE_v1_0_0.md`): the first framework files, Domain Engineering Ontology v5.2, the AI4SE material and two extracts from the owner's writing. |
| `fixtures/` | Deliberately wrong inputs. The gate must refuse each one; a gate that cannot fail verifies nothing. |

The package follows the OE Operating Discipline rule of **one T-Box, one A-Box and one SHACL file**, each with one ontology header and one version.

## At a glance

626 classes, 972 object properties and 182 datatype properties; 13 taxonomies with 238 concepts; 123 example individuals; 40 competency questions. The gate prints these counts from the files, so they can be reproduced:

```
pip install rdflib pyshacl
python3 05-gates/o4de_gate_v1_1_0.py .
```

## Checks run on 1.1.0

- The gate passes: one file per role, no mixing of roles, every term used is declared, the shapes accept the T-Box and A-Box together, all 40 competency questions return rows, and all 9 negative fixtures are refused.
- HermiT finds the ontology consistent with no unsatisfiable class, and finds a deliberately contradictory input inconsistent (`pip install owlready2`, Java needed). HermiT has no `xsd:date` or `xsd:duration` in its datatype map, so it runs on a copy in which those two are replaced by `xsd:string`; the shipped files keep the real datatypes.

## Origin and scope

O4DE 1.0.0 formalised the domain engineering framework worked out in a series of working sessions. Version 1.1.0 consolidates the earlier **Domain Engineering Ontology v5.2** into it: 489 more classes and 967 more properties, grouped in nineteen parts, with every taken-over term linking to its original through `rdfs:seeAlso`. What was decided on the way, and what was left out, is in `04-documentation/O4DE_Consolidation_Record_Domain_Engineering_Ontology_v5_2_v1_1_0.md`.

Not yet consolidated: the AI4SE material in `vendored-received/`. The provenance of v5.2 (its creator line and earlier licence statement) is kept on its module resource; the module is licensed with the package, and the owner can correct that reading.

## Using it

- Namespace: `http://www.zt4swe.io/o4de#`. The T-Box ontology IRI is `http://www.zt4swe.io/o4de`; the A-Box imports it.
- Open the T-Box in Protégé, load both files into a triple store, or query them with the SPARQL in the competency questions.
- Validate your own data: put it in a file that uses the O4DE terms, load it together with the T-Box, and run the shapes with SHACL advanced features on (see the gate for a working call).
