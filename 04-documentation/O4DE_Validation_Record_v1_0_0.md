# O4DE 1.0.0 validation record

Produced on 2026-10-13 by running the commands shown, in this order, on the files of this package. The output is pasted unchanged. A later change to any file makes this record historical (L-114); a new version gets a new record.

## 1. Release gate

```
$ python3 05-gates/o4de_gate_v1_0_0.py .
1. file structure
  ok   exactly one tbox file  o4de_tbox_v1_0_0.ttl
  ok   exactly one abox file  o4de_abox_v1_0_0.ttl
  ok   exactly one shacl file  o4de_shacl_v1_0_0.ttl
  ok   no other Turtle file  3 found
   parsed: T-Box 1859 triples, A-Box 1763 triples, SHACL 418 triples
2. role purity
  ok   T-Box holds no named individual
  ok   T-Box holds no taxonomy concept
  ok   A-Box declares no class or property
  ok   SHACL file declares no class or property
  ok   T-Box has one ontology header
  ok   A-Box has one ontology header
  ok   SHACL has one ontology header
3. declared terms
  ok   every O4DE term used is declared
   counts: 137 classes, 103 object properties, 84 datatype properties, 12 taxonomies, 218 concepts, 93 example individuals
4. SHACL conformance
  ok   T-Box and A-Box conform to the shapes  27 shapes
5. competency questions
  ok   a competency question file exists
  ok   every competency question returns rows  27 questions
6. negative fixtures (the gate must be able to fail)
  ok   negative fixtures present  6 found
  ok   negative_orphan_concept_v1_0_0.ttl is refused  expected 'broader concept or be the top concept'
  ok   negative_score_out_of_range_v1_0_0.ttl is refused  expected 'must lie between'
  ok   negative_swot_incomplete_v1_0_0.ttl is refused  expected 'needs at least 1 value of'
  ok   negative_undeclared_class_v1_0_0.ttl is refused  expected 'may only be typed with classes declared'
  ok   negative_wrong_datatype_v1_0_0.ttl is refused  expected 'must have the datatype'
  ok   negative_wrong_domain_v1_0_0.ttl is refused  expected 'must belong to the property's domain'
VERDICT: PASS
```

## 2. Reasoner (HermiT), data as shipped

```
$ python3 03-tooling/o4de_hermit_check_v1_0_0.py .
merged graph: 3621 triples; 41 date/duration items mapped to xsd:string for the reasoner
* Owlready2 * Running HermiT...
* Owlready2 * HermiT took 1.395045518875122 seconds
HermiT: ontology consistent
unsatisfiable classes: none
```

## 3. Reasoner, same data plus a deliberately contradictory individual (the check must fail)

```
$ python3 03-tooling/o4de_hermit_check_v1_0_0.py . --with fixtures/inconsistent_disjoint_v1_0_0.ttl
merged graph: 3625 triples; 41 date/duration items mapped to xsd:string for the reasoner
* Owlready2 * Running HermiT...
HermiT: ontology INCONSISTENT
```

## 4. OE structure check (rules N1, N2, V1, R1, H1, U1, A1, X1)

```
$ python3 oe_structure_check_v1_6_0.py . --as-package o4de --classes OE_STRUCTURE_CLASSES_v1_6_0.tsv
examined 3 Turtle file(s) in 1 package(s); 0 violation(s)
  class table: OE_STRUCTURE_CLASSES_v1_6_0.tsv; not read, by class: C1 2, T1 7
by rule: 
VERDICT: CLEAN (no register given)
```
