# O4DE change history

## 1.1.0 (2026-10-13), consolidation of Domain Engineering Ontology v5.2

Predecessor: 1.0.0 of this repository. The earlier Domain Engineering Ontology v5.2, which 1.0.0 only compared with O4DE, is now part of the package as a module of the three O4DE files. The full account of the decisions is in `04-documentation/O4DE_Consolidation_Record_Domain_Engineering_Ontology_v5_2_v1_1_0.md`.

Added:
- 489 classes from v5.2 (626 in all), grouped in a new taxonomy of nineteen parts, the *Enterprise Domain Structure Taxonomy*: domain foundations, organizational taxonomy, governance models, business capabilities, work structure, people and roles, requirements, data architecture, systems and technology, domain assets, physical assets, products, automation, change management, knowledge management, discovery methods, quality and metrics, tools, and ontology lifecycle, testing and deployment.
- 967 properties from v5.2 (1,154 in all: 972 object and 182 datatype properties), 112 restrictions, 26 disjointness groups and 8 property chains of v5.2, so that the T-Box carries 145 restrictions, 37 disjointness groups and 8 property chains (1.0.0 had none).
- A definition on every new class and property: 445 class definitions written for this release, 44 kept from v5.2; 962 property definitions generated from the label, domain and range of the property, 5 kept from v5.2.
- The 29 Fashion Retail example individuals of v5.2 in the A-Box, and one example business role that the shapes require for the order fulfilment process (123 example individuals in all).
- A module resource at the former IRI of v5.2, carrying its version, its creator and its earlier licence statement as provenance. Every taken-over term links to its original term through `rdfs:seeAlso`.
- 13 competency questions on the enterprise domain structure (40 in all); three negative fixtures (a size taken from the wrong value partition, a property without a range, a class without a definition) and one contradictory fixture (a test result both passing and failing).

Changed against v5.2 while taking it over (each is explained in the consolidation record):
- Three v5.2 terms mean something else in O4DE and were renamed: Inventory became Inventory Waste, has maturity level became has organization maturity, supports capability became supports business capability.
- 39 v5.2 classes and 15 v5.2 properties are the same term as an O4DE term; the O4DE declaration stands and v5.2 only adds its super-classes, disjointness and restrictions. Three O4DE properties (has organizational unit, uses asset, utilization rate) had their domain widened to cover both uses, and has version was generalised to any thing.
- Eight v5.2 object properties whose range was an XML Schema datatype (cycle time, lead time, process time, wait time, throughput, error reduction, reuse rate, has version) became datatype properties; their eight meaningless inverses were left out.
- Ten repeated disjointness groups were left out, and each of three pairs of requirement priority classes, which v5.2 declares twice under different names, was declared equivalent.
- The terms that v5.2 uses without declaring were declared: 322 classes, from their use as a type or super-class, and the properties used as a predicate or in a restriction.
- A range of automation candidate was widened from process to work item, because the v5.2 example offers an operation as a candidate.
- The ontology purpose statement and the descriptions of both files now include the enterprise domain structure; the version of every file is 1.1.0.
- The shapes mirror the same 33 restrictions as before. The 112 restrictions taken over from v5.2 are OWL axioms for reasoners and are not turned into data-entry rules, because they would mark every example in the package incomplete (an organization would need at least three key performance indicators, for instance). The shapes now accept a class as the value of an object property when that class is a subclass of the property range, which is how v5.2 states organization size, ownership type and similar value partitions.

Left out of the take-over: the 37 individuals with which v5.2 describes itself (its versions, tests, benchmarks and deployment) and the long version history in its comments.

Known limits: the example individuals are illustrative; 18 object properties taken over from v5.2 have `owl:Thing` as range because v5.2 gives none and nothing in its text suggests one; the AI4SE material in `vendored-received/` is not yet consolidated.

## 1.0.0 (2026-10-13), first release

First release of the package. Predecessor: none in this repository.

Added: the T-Box (137 classes, 187 properties), the A-Box (12 taxonomies, 218 concepts, 93 example individuals), the shape file (27 shapes, 33 of them mirroring T-Box restrictions), the gate, the HermiT check, six negative fixtures and one contradictory fixture, the documentation template, 27 competency questions, the comparison with Domain Engineering Ontology v5.2 and the text of the meta-definition.

Changes against the working-session version the files were rebuilt from:
- 223 definitions written: 36 classes and all 187 properties had no definition (some had only a short comment).
- Two example individuals (a sprint and a retrospective) given the duration that the T-Box requires of every process activity.
- The disjointness between Vendor Solution and its own subclass Alternative Solution was already removed in the rebuild because it made that class unsatisfiable; the reasoner confirms no class is unsatisfiable.
- Namespace moved from a placeholder to `http://www.zt4swe.io/o4de#`, the family used by the O4SDLC package of the same owner.
- Licence set to Apache License 2.0, the licence of this repository, in place of the Creative Commons statement in the working-session version.

Known limits: Domain Engineering Ontology v5.2 is not absorbed (see its comparison note); the example individuals are illustrative.
