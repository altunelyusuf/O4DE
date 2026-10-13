# O4DE 1.1.0: consolidation of Domain Engineering Ontology v5.2

This record explains how the earlier **Domain Engineering Ontology v5.2** (file `Domain_Engineering_Ontology_v5_2_Enhanced.ttl`, namespace `http://domainengineering.org/ontology#`) was taken into the three O4DE files, which decisions were made on the way, and what was measured. It carries out the proposal at the end of the fit-gap note and supersedes it; the note itself now ends with a pointer to this record.

## Source and method

- Source: the copy kept byte for byte in `vendored-received/02-ontology-v5.2/`, which is unchanged by this release. It was read with rdflib, term by term; nothing was copied by hand except the class definitions listed below.
- v5.2 holds 528 classes (206 declared, 322 used without a declaration), 990 properties and 66 individuals. Its summary documents claim 513 classes with a definition for each; the file itself declares 206 classes and defines 29 (the bytes govern).
- A conversion script produced the 1.1.0 T-Box and A-Box from the 1.0.0 files and the v5.2 file; the shapes and competency questions were regenerated from the result, and the release gate and the reasoner were run on the output (see the validation record of this version).

## What was taken over

| Part of v5.2 | New classes |
|---|---|
| Domain foundations | 44 |
| Organizational taxonomy | 66 |
| Governance models | 39 |
| Business capabilities | 31 |
| Work structure | 37 |
| People and roles | 20 |
| Requirements | 30 |
| Data architecture | 23 |
| Systems and technology | 30 |
| Domain assets | 14 |
| Physical assets | 39 |
| Products | 4 |
| Automation | 15 |
| Change management | 10 |
| Knowledge management | 9 |
| Discovery methods | 11 |
| Quality and metrics | 18 |
| Tools | 7 |
| Ontology lifecycle, testing and deployment | 42 |

Total: 489 new classes, so O4DE has 626. Each part is a concept of the *Enterprise Domain Structure Taxonomy* in the A-Box and lists its classes through `rdfs:seeAlso`. Every taken-over class and property links to its original term in v5.2 through `rdfs:seeAlso`. The v5.2 header became a module resource at the former IRI `http://domainengineering.org/ontology`, with its version, creator and earlier licence statement.

Properties: 21 of the properties v5.2 uses without declaring had no range and were given the datatype of the values found in v5.2. The undeclared classes were declared from how v5.2 uses them (as a type or as a super-class), the undeclared properties from how it uses them (as a predicate or in a restriction).

## Decisions

1. **Same name, different meaning: renamed.** Inventory (v5.2: excess stock as a kind of process waste; O4DE: the stock a unit holds) became *Inventory Waste*. Has maturity level (v5.2: organization to a maturity level class; O4DE: process to an integer from 1 to 5) became *has organization maturity*. Supports capability (v5.2: application system to business capability; O4DE: vendor solution to system capability) became *supports business capability*. A misspelt v5.2 term used only in a property chain, `involvestakeholder`, is the O4DE property *involves stakeholder*.
2. **Same term: merged.** 39 classes of v5.2 have the same name as an O4DE class and 15 properties have the same name as an O4DE property. The O4DE label, definition, domain and range stand; v5.2 adds only its super-classes, disjointness and restrictions to the classes. The classes are: AlternativeFeature, BusinessProcess, BusinessRule, Component, CompositionVariability, CoreBusinessProcess, DomainAnalysis, DomainAnalyst, DomainArchitect, DomainAsset, DomainDesign, DomainEngineeringProcess, DomainEvolution, DomainImplementation, DomainModel, DomainSpecificLanguage, Feature, FeatureModel, FeatureModelingTool, Framework, InheritanceVariability, MandatoryFeature, Metric, Operation, OptionalFeature, OrganizationalUnit, ParameterVariability, Product, QualityAttribute, QualityStandard, ReferenceArchitecture, ReuseMetric, Role, Stakeholder, SupportingProcess, Tool, VariabilityMechanism, Variant, VariationPoint.
3. **Domains widened.** Has organizational unit now applies to organizational structure or organization; uses asset to domain engineering activity or product; utilization rate to operational environment or process; has version to anything.
4. **Mistyped properties corrected.** cycleTime, errorReduction, hasVersion, leadTime, processTime, reuseRate, throughput, waitTime were object properties whose range was an XML Schema datatype; they are datatype properties. The inverses that v5.2 declares for them (cycleTimeOf, errorReductionOf, isVersionOf, leadTimeOf, processTimeOf, reuseRateOf, throughputOf, waitTimeOf) have no meaning for a datatype value and were left out.
5. **Two domains or ranges.** v5.2 gives 4 properties two domains, which OWL reads as an intersection. They are read as the union v5.2 evidently intends: componentOf, errorReduction, transportation, transportationOf.
6. **Domain supplied.** 37 properties had no domain; it was taken from the classes of the individuals that use the property, or of the class that carries the restriction on it, or else set to owl:Thing. They are: apiVersion, authenticationMethod, baseURL, benchmarkDate, boundedBy, changeLogContent, changeLogDate, communityMember, concurrentUsers, conflictBetween, containsAsset, dependsOnRequirement, endpointURL, estimatedMigrationTime, failingTests, hasBusinessUnit, hasGovernanceFramework, hasSubProcess, loadTime, maxQueryTimeout, migrationComplexity, migrationGuide, operatesInDomain, partOfOrganization, passingTests, producesDeliverable, queryResponseTime, reasoningTime, requirementPriority, requirementStatus, requiresCodeChanges, requiresDataMigration, satisfiesRequirement, supportsInference, testEnvironment, testVersion, totalTests.
7. **Range owl:Thing.** 18 object properties have no range in v5.2 and nothing in its text suggests one; their range is owl:Thing and the owner may refine it: boundedBy, communityMember, conflictBetween, containsAsset, dependsOnRequirement, flowsFrom, flowsTo, hasBusinessUnit, hasGovernanceFramework, hasSubProcess, impactedBy, impacts, operatesInDomain, partOfOrganization, producesDeliverable, requirementOf, satisfiesRequirement, tracesTo.
8. **Repeated axioms.** v5.2 states ten disjointness groups twice; the repeats were left out. It also names three requirement priorities twice (Must Have and Must Have Priority, and likewise for Should Have and Could Have); each pair is declared equivalent.
9. **Automation candidates.** The v5.2 example offers an operation as an automation candidate while the range is a process. The domain and range were widened to work item, the common super-class of process, operation, activity and task.
10. **Self-description left out.** The 37 individuals with which v5.2 describes itself (versions, change logs, test suites, benchmarks, deployment, migration) were not taken over; the classes and properties for that vocabulary were, as the part *Ontology lifecycle, testing and deployment*, because they can describe the lifecycle of any ontology, this one included.
11. **Definitions.** v5.2 defines 29 of its classes and 9 of those definitions were measurements such as "1-9 employees"; they were replaced by sentences. 445 class definitions were written for this release; 44 kept from v5.2. Property definitions were generated from label, domain and range ("Links a ... to a ... by the relation ..."): 962 of them, plus 5 kept from v5.2. These generated definitions are correct but plain; the owner may refine them.
12. **Axioms and the shapes.** The 112 restrictions of v5.2 are in the T-Box. The shapes do not turn them into data-entry rules: an organization would, for instance, have to carry at least three key performance indicators and every application system at least three layers, and when they were tried as rules the shapes reported dozens of gaps in the package's own examples. They remain OWL axioms for reasoners and for completeness queries. The 33 restrictions that 1.0.0 mirrored are still mirrored.
13. **Value partitions.** v5.2 states organization size, ownership type, lifecycle phase, asset condition and similar values as classes and points to them from individuals (the class is the value). The shapes accept this when the class is a subclass of the property range, and refuse a class from the wrong partition (a fixture shows it).
14. **Examples.** The 29 Fashion Retail individuals were taken over, with these changes: plain strings instead of language-tagged strings where the property range is text, the individuals' labels taken from their names, and one added example business role (Order Fulfillment Coordinator) because the shapes require a business role on every business process.

## Licence and provenance

The v5.2 header names the creator "Domain Engineering Consortium", the year 2025 and the licence Creative Commons Attribution 4.0. The note that came with the received material describes everything in it as the owner's own domain engineering material, and the repository licence is Apache License 2.0. v5.2 was therefore taken as the owner's own work: the creator and the earlier licence statement are kept as provenance on the module resource, and the module is licensed with the package. **If any part of v5.2 is third-party work, the owner should say so and it will be attributed.**

## What the owner may want to decide

- Whether all nineteen parts belong in a domain engineering ontology; they were all taken, as proposed in the fit-gap note. The on-chain governance classes and the lifecycle part are the likeliest to be moved out into a module of their own.
- Whether the plain generated definitions of properties should be refined.
- Whether the 18 properties with range owl:Thing, and the properties whose domain was supplied, should get a considered domain and range.

## Not done in this release

The AI4SE material in `vendored-received/` is not consolidated yet (it is planned for 1.2.0). The Enterprise Edition v4.5 of that material is outside the scope of this package.
