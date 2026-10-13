# O4DE change history

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
