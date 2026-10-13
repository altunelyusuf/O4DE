# O4DE against Domain Engineering Ontology v5.2: measured fit and gap (version 1.0.0)

This note compares two ontologies of domain engineering that exist in the owner's work: **O4DE** (this package) and **Domain Engineering Ontology v5.2**, the earlier enterprise ontology. It is a measurement, not a merge. Version 1.0.0 of O4DE does **not** contain v5.2; the section "Proposal for 1.1.0" says what absorbing it would take and what only the owner can decide.

## Where the numbers come from

- v5.2 was read from the repository `altunelyusuf/O4SWE`, folder `domain-engineering-ontology-v5.2/`, file `Domain_Engineering_Ontology_v5_2_Enhanced.ttl`, at commit `5564127` ("source files as received"). Its namespace is `http://domainengineering.org/ontology#`.
- O4DE was read from `01-ontologies/o4de_tbox_v1_0_0.ttl` in this package.
- Every figure was produced by parsing both files with rdflib on 2026-10-13. Classes are matched by normalised label (lower case, letters and digits only); properties by normalised local name.

## What each ontology contains

| Measure | v5.2 | O4DE 1.0.0 |
|---|---|---|
| Classes with an IRI | 206 | 137 |
| Classes that have a definition (`skos:definition`) | 29 | 137 |
| Object properties | 881 | 103 |
| Datatype properties | 83 | 84 |
| Taxonomies (SKOS) and example individuals | none | 12 taxonomies, 93 individuals |
| Shape file, competency questions, reasoner check | none shipped | all three |

The v5.2 summary documents claim 513 classes and a definition for every class. The file itself holds 206 classes and 29 definitions; the claim does not match the bytes (BP-D2: the bytes govern).

## How much they overlap

Only **15 classes** appear in both: Business Rule, Domain Asset, Feature, Metric, Operation, Organizational Unit, Product, Quality Attribute, Quality Standard, Role, Stakeholder, Tool, Variability Mechanism, Variant and Variation Point. Only **9 object properties** share a name: depends on, excludes feature, has feature, has organizational unit, has variant, has variation point, requires feature, supports capability and uses asset.

So the two are **complementary**, not duplicates. O4DE covers the method of domain engineering and a broad business context; v5.2 covers the structure of the business domain itself.

## What v5.2 adds that O4DE 1.0.0 lacks

Class counts per part of v5.2, from its own part headings (the version-history part repeats classes and properties and is left out):

| Part of v5.2 | Classes | What it covers |
|---|---|---|
| Domain foundations | 13 | domain, sub-domain, scope, boundary, bounded context, domain types |
| Organizational taxonomy | 11 | organization, size, ownership, geographic scope, lifecycle phase, maturity |
| Governance models | 19 | governance framework, decision rights, boards, policy, standard, procedure, on-chain and off-chain governance |
| Business capabilities | 12 | capability, function, service, value stream, business event, operating model |
| Work structure | 20 | process, operation, activity, task, bottleneck, waste, improvement, simulation |
| People and roles | 5 | person, role, stakeholder, responsibility assignment |
| Requirements | 11 | requirement classes |
| Data architecture | 15 | data entities and structures |
| Systems and technology | 18 | applications, platforms, infrastructure |
| Domain assets | 8 | asset hierarchy |
| Physical assets | 16 | equipment, facilities |
| Products | 4 | product structure |
| Automation | 5 | automation concepts |
| Change management | 10 | change control |
| Knowledge management | 9 | knowledge assets |
| Discovery methods, quality and metrics, tools | 11 | methods, metrics, tools |

O4DE 1.0.0 has no counterpart for the business-domain foundations, the governance models, the capability and value-stream layer, the data and technology architecture, the physical assets, change management or knowledge management.

## Defects found in v5.2 (relevant if it is absorbed)

- 177 of 206 classes have no definition.
- 8 object properties carry an XML Schema datatype as range (reuse rate, error reduction, cycle time, lead time, process time, wait time, throughput, has version); they should be datatype properties.
- 1 object property and 3 datatype properties have no domain.
- The work structure of v5.2 is a fixed four-level hierarchy (process, operation, activity, task). O4DE 1.0.0 has no task class, and its operation class sits under operations management instead of between process and activity, so the two would have to be aligned first.

## Provenance and licence of v5.2

The v5.2 header states the creator as "Domain Engineering Consortium", the year 2025 and the licence Creative Commons Attribution 4.0. The note that came with the received material (`vendored-received/README.md`) describes everything in it as "the domain engineering material of the Owner", AI-assisted or unreviewed drafts, with the licence to be decided by the owner; the repository licence is Apache License 2.0. O4DE 1.0.0 copies **nothing** from v5.2. When v5.2 is consolidated (1.1.0) it is taken as the owner's own work: the creator line and the earlier licence statement are kept as provenance on the module, and the module is licensed with the rest of the package. If any part is in fact third-party work, the owner should say so before 1.1.0 and it will be attributed instead.

## Proposal for 1.1.0 (not enforced; for the owner)

1. Add v5.2 as **modules** of the three O4DE files (domain foundations, governance, capabilities, work structure, and so on). Its terms get O4DE identifiers, each carrying a link to the v5.2 term it came from. The 15 shared classes are merged with the O4DE ones.
2. Write the 177 missing definitions, turn the 8 mistyped properties into datatype properties, give the 4 properties without a domain one, and declare the terms v5.2 uses but never declares (the measurement found 422 such names, classes and individuals together).
3. Extend the shape file and the competency questions to the new modules and run the gate and the reasoner again.

**What only the owner can decide:** whether all 16 parts belong in a domain engineering ontology or only some (for example, the on-chain governance classes). Nothing in the rules or the files settles that point; the proposal is to take all of them, because the owner's collection note names them as domain engineering material.
