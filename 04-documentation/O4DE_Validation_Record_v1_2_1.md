# O4DE 1.2.1 validation record

Produced on 2026-10-13 by running the commands shown, in this order, on the files of this package. The output is pasted unchanged, except that two lines of reasoner output are left out: the Java command line and a note of the Owlready2 library that only changes made to entities loaded in Python are listed. A later change to any file makes this record historical (L-114); a new version gets a new record. The gate takes about eight minutes on this package, because the shapes are run once for the data and once for each of the nine bad inputs.

This version changes the licence only (see `CHANGELOG_v1_2_1.md`); no class, property, individual or shape changed.

```
$ python3 05-gates/o4de_gate_v1_2_1.py .
1. file structure
  ok   exactly one tbox file  o4de_tbox_v1_2_1.ttl
  ok   exactly one abox file  o4de_abox_v1_2_1.ttl
  ok   exactly one shacl file  o4de_shacl_v1_2_1.ttl
  ok   no other Turtle file  3 found
   parsed: T-Box 11569 triples, A-Box 3118 triples, SHACL 425 triples
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
   counts: 678 classes, 975 object properties, 182 datatype properties, 15 taxonomies, 306 concepts, 126 example individuals
4. SHACL conformance
  ok   T-Box and A-Box conform to the shapes  27 shapes
5. competency questions
  ok   a competency question file exists
  ok   every competency question returns rows  47 questions
6. negative fixtures (the gate must be able to fail)
  ok   negative fixtures present  9 found
  ok   negative_class_without_definition_v1_1_0.ttl is refused  expected 'A class needs a definition'
  ok   negative_orphan_concept_v1_0_0.ttl is refused  expected 'broader concept or be the top concept'
  ok   negative_property_without_range_v1_1_0.ttl is refused  expected 'A property needs a range'
  ok   negative_score_out_of_range_v1_0_0.ttl is refused  expected 'must lie between'
  ok   negative_size_from_wrong_partition_v1_1_0.ttl is refused  expected 'must belong to the property's range'
  ok   negative_swot_incomplete_v1_0_0.ttl is refused  expected 'needs at least 1 value of'
  ok   negative_undeclared_class_v1_0_0.ttl is refused  expected 'may only be typed with classes declared'
  ok   negative_wrong_datatype_v1_0_0.ttl is refused  expected 'must have the datatype'
  ok   negative_wrong_domain_v1_0_0.ttl is refused  expected 'must belong to the property's domain'
7. licence: CC BY 4.0 for ontologies, shapes and documentation; Apache-2.0 for tooling and gates
  ok   licences match the arrangement
  ok   the licence check can fail: Apache on an ontology is refused
  ok   the licence check can fail: a tool without its Apache statement is refused
  ok   the licence check can fail: missing LICENSE.md is refused
VERDICT: PASS
```

```
$ python3 03-tooling/o4de_hermit_check_v1_2_1.py .
merged graph: 14686 triples; 70 date/duration items mapped to xsd:string for the reasoner
* Owlready2 * Running HermiT...
* Owlready2 * HermiT took 4.848413944244385 seconds
HermiT: ontology consistent
unsatisfiable classes: none
```

```
$ python3 03-tooling/o4de_hermit_check_v1_2_1.py . --with fixtures/inconsistent_test_status_v1_1_0.ttl
merged graph: 14690 triples; 70 date/duration items mapped to xsd:string for the reasoner
* Owlready2 * Running HermiT...
HermiT: ontology INCONSISTENT
```

```
$ python3 03-tooling/o4de_hermit_check_v1_2_1.py . --with fixtures/inconsistent_disjoint_v1_0_0.ttl
merged graph: 14690 triples; 70 date/duration items mapped to xsd:string for the reasoner
* Owlready2 * Running HermiT...
HermiT: ontology INCONSISTENT
```

