# O4DE 1.2.0: consolidation of the AI4SE module, the UAISE section and the thesis headings

This record explains how three remaining pieces of the received material were taken into the three O4DE files, and what was left out. The first consolidation, of Domain Engineering Ontology v5.2, is in `O4DE_Consolidation_Record_Domain_Engineering_Ontology_v5_2_v1_1_0.md`. The received files in `vendored-received/` are unchanged.

## 1. The Domain Engineering module of AI4SE

Source: `vendored-received/03-ai4se-material/Ontology_Module_DomainEngineering.ttl.txt` (20 classes, 8 object properties, 7 datatype properties, 4 individuals, 3 restrictions; the received README says "announced as 30").

- **Repair.** The file did not parse. The cause is one token: `:FaCT++` at line 167 cannot be read as a name in Turtle, because `+` is not allowed in a local name. In a working copy it was replaced by `:FaCTpp`; the file then parses (311 triples). The received file is unchanged. The reasoner keeps its true name, FaCT++, as the label of a taxonomy concept.
- **Classes.** 15 classes are new in O4DE. 4 coincide with O4DE classes (domain engineering process, domain model, domain-specific language, ontology editor) and were merged; the module's super-class for them is not needed. The module's top class, Domain Engineering Concept, was not taken: its name is already the IRI of a concept in the A-Box, and its parent, AI4SE Concept, is declared nowhere. The class "Competency Questions" became *Competency Question Validation*, because O4DE already has a Competency Question class and the module's class is a way of validating, not a question.
- **Placement.** The module's classes were attached to the closest O4DE parents: the three process classes under domain engineering process, domain ontology under ontology, the techniques under discovery method, the tool classes under tool, prompt templates under domain asset. Domain conceptualization became a domain engineering activity, because its text describes the act of forming an understanding.
- **Values.** The module states formats, query languages, reasoners, techniques and validation methods as class-level property assertions (for instance "domain ontology serialized as Turtle"). OWL cannot state these on a class without treating the class as an individual, so they are kept as concepts of the new *AI-Assisted Domain Engineering Taxonomy*, each linked to the class it concerns.
- **Left out.** The accuracy ranges and time savings (for instance "85-90%" and "weeks to hours") and the examples and notes that quote figures, because nothing in the file supports them; the three restrictions, which say that every domain model "should" be validated and every domain engineering process must produce something, and would hold for all domain models and processes of the package; the book references and the module's own identifiers; the two agent individuals, which carry the accuracy claims. The two example domain ontologies were kept with a plain description.
- **Provenance.** The creator "AI4SE Research Team", the date 2025-11-17 and the module version are kept on a module resource at the former IRI. The received file states no licence; as with v5.2, the module is taken as the owner's own work and licensed with the package. **The owner can correct that.**

## 2. UAISE section 2.1

Source: `vendored-received/04-owner-extracts/UAISE_section_2_1_Domain_Engineering.md`. Eight classes: process phase, domain engineering phase (with the Turkish label of the heading), business analysis, business process modeling, business process model, business architecture, conceptual model and conceptual ERD. The text says that the phase "involves" two key processes and "produces" five kinds of artifact; these became seven existential restrictions on the phase, through the properties has key process and produces artifact. The statement that a conceptual ERD can be "formally mapped to or serve as the basis for" a domain ontology became the property is basis for ontology. Business domain and domain ontology already existed. The link of the business process model to the BPMN namespace is not modelled: the extract names the namespace prefix but not its IRI, and the BPMN concepts it lists (process, event, gateway) are not taken over. The draft is AI-assisted and its citations are unverified, as the received README says.

## 3. The thesis headings

Source: `vendored-received/04-owner-extracts/Thesis_headings_extract.md`: section headings only, numbered as in the English numbering. Because the body text is not in the repository, the 29 classes taken from it (variation capacity, variation kinds, properties of variation capacity, the variation capacity metric, optional, exclusive and dependent elements, the variant generation process and its steps) carry **general definitions**, and each has a scope note saying that the definition is a general reading of the term and is to be confirmed against the thesis text. The heading numbers are kept as `skos:notation` in the *Variation and Variant Generation Taxonomy*. The process stages of component-based development (section 2.4.5) are concepts in that taxonomy only, without classes. The chapters on system analysis and design (3.3, 3.4) describe the thesis' own tool and were not taken. Scalability, which v5.2 already defined, was placed under variation capacity property. **If the owner supplies the thesis text, the definitions can be replaced by the thesis' own.**

## Checks

The gate, the reasoner and the structure check were run on the result; the output is in the validation record of this version.

## What the owner may want to decide

- Whether the licence reading of the AI4SE module and the UAISE extract is right.
- Whether the AI-assisted material belongs in the same ontology as the business-domain material; it is separable, because the new classes and the two taxonomies form a module of their own.
