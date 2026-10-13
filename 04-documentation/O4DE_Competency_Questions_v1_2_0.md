# O4DE competency questions, version 1.2.0

Each question is paired with a SPARQL query. Every query declares the prefix `PREFIX : <http://www.zt4swe.io/o4de#>` (with the usual rdf, rdfs, owl, skos and xsd prefixes; shown once here, left out of the blocks below) and must return at least one row when run against the T-Box and A-Box together; the gate script in `05-gates` runs them all.
The questions are grouped by the part of the ontology they test. A longer list drafted in an earlier working session could not be recovered; the first 27 questions are those of version 1.0.0, the next 13 were added in version 1.1.0 for the enterprise domain structure and the last group in version 1.2.0.

## Domain engineering core

**CQ1. What assets are produced by domain analysis activities?**

```sparql
SELECT ?analysis ?asset WHERE { ?analysis a :DomainAnalysis ; :producesAsset ?asset . }
```

**CQ2. Which features are mandatory in a given feature model?**

```sparql
SELECT ?model ?feature WHERE { ?model :hasFeature ?feature . ?feature a :MandatoryFeature . }
```

**CQ3. What is the reuse rate of components?**

```sparql
SELECT ?component ?reuseRate WHERE { ?component a :Component ; :hasReuseRate ?reuseRate . }
```

**CQ4. Which activities precede domain implementation?**

```sparql
SELECT ?activity WHERE { ?activity :precedes ?impl . ?impl a :DomainImplementation . }
```

**CQ5. What tools are used in domain analysis activities?**

```sparql
SELECT ?activity ?tool WHERE { ?activity a :DomainAnalysis ; :usesTool ?tool . }
```

**CQ6. Which assets have variation points, and which mechanisms implement them?**

```sparql
SELECT ?asset ?vp ?mechanism WHERE { ?asset :hasVariationPoint ?vp . ?vp :implementsVariability ?mechanism . }
```

**CQ7. What is the maturity level distribution of domain engineering processes?**

```sparql
SELECT ?maturity (COUNT(?process) AS ?count) WHERE { ?process :hasMaturityLevel ?maturity . } GROUP BY ?maturity
```

**CQ8. Which stakeholders are involved in domain analysis?**

```sparql
SELECT ?stakeholder WHERE { ?analysis a :DomainAnalysis ; :involvesStakeholder ?stakeholder . }
```

## Business context, data collection, vendors

**CQ9. What business problems are addressed by domain engineering activities?**

```sparql
SELECT ?problem ?activity WHERE { ?activity :addressesProblem ?problem . }
```

**CQ10. Which vendor solutions support which system capabilities?**

```sparql
SELECT ?solution ?capability WHERE { ?solution :supportsCapability ?capability . }
```

**CQ11. What data was collected in a given period, and by which method?**

```sparql
SELECT ?log ?method ?date WHERE { ?log :collectionDate ?date ; :collectionMethod ?method . FILTER(?date >= "2024-06-01"^^xsd:date && ?date <= "2024-06-30"^^xsd:date) }
```

**CQ12. Which business processes are governed by which business rules?**

```sparql
SELECT ?process ?rule WHERE { ?process :governedByRule ?rule . }
```

**CQ13. What are the alternatives of a vendor solution?**

```sparql
SELECT ?solution ?alternative WHERE { ?solution :hasAlternative ?alternative . }
```

**CQ14. Which stakeholders were interviewed, and when?**

```sparql
SELECT ?stakeholder ?interview ?date WHERE { ?interview a :InterviewList ; :documentsInterview ?stakeholder ; :collectionDate ?date . }
```

**CQ15. What business benefits do domain assets deliver, and what are they worth?**

```sparql
SELECT ?asset ?benefit ?value WHERE { ?asset :deliversBenefit ?benefit . ?benefit :businessValue ?value . }
```

**CQ16. Which applications are included in an application portfolio?**

```sparql
SELECT ?portfolio ?application WHERE { ?portfolio :includesApplication ?application . }
```

**CQ17. How do vendor solutions compare by cost?**

```sparql
SELECT ?solution ?cost WHERE { ?solution a :VendorSolution ; :solutionCost ?cost . } ORDER BY ?cost
```

**CQ18. Which business roles take part in which business processes?**

```sparql
SELECT ?process ?role WHERE { ?process :hasBusinessRole ?role . }
```

## Strategic, product, customer and quality

**CQ19. Which products meet a quality standard, with their quality score and defect rate?**

```sparql
SELECT ?product ?qualityScore ?defectRate WHERE { ?product :meetsStandard ?standard ; :qualityScore ?qualityScore . OPTIONAL { ?product :defectRate ?defectRate } FILTER(?qualityScore >= 8.0) } ORDER BY DESC(?qualityScore)
```

**CQ20. How do product quality scores relate to customer satisfaction scores?**

```sparql
SELECT ?product ?qualityScore ?satisfaction WHERE { ?product :qualityScore ?qualityScore ; :usesChannel ?channel . ?channel :servesCustomerThrough ?customer . ?customer :experiencesAtTouchpoint ?touchpoint . ?touchpoint :providesExperience ?experience . ?experience :satisfactionScore ?satisfaction . }
```

**CQ21. Which supporting processes enable the most core business processes?**

```sparql
SELECT ?supporting (COUNT(?core) AS ?coreCount) WHERE { ?supporting :supportsCoreProcess ?core . } GROUP BY ?supporting ORDER BY DESC(?coreCount)
```

**CQ22. What is the average maturity of core versus supporting processes?**

```sparql
SELECT ?processType (AVG(?maturity) AS ?avgMaturity) WHERE { ?process a ?processType ; :processMaturity ?maturity . FILTER(?processType IN (:CoreBusinessProcess, :SupportingProcess)) } GROUP BY ?processType
```

**CQ23. Which suppliers provide inputs that core business processes consume?**

```sparql
SELECT ?supplier ?input ?core WHERE { ?supplier :suppliesInput ?input . ?core a :CoreBusinessProcess ; :consumesInput ?input . }
```

**CQ24. Which strengths does a SWOT analysis leverage, and which weaknesses do threats exploit?**

```sparql
SELECT ?swot ?strength ?threat ?weakness WHERE { ?swot :leveragesStrength ?strength . OPTIONAL { ?threat :exploitsWeakness ?weakness } }
```

## Organization and agility

**CQ25. What is the average performance rating per team and the agile methodology it uses?**

```sparql
SELECT ?team ?methodology (AVG(?rating) AS ?avgPerformance) WHERE { ?team :implementsAgileMethodology ?methodology . ?employee :memberOfTeam ?team ; :performanceRating ?rating . } GROUP BY ?team ?methodology
```

**CQ26. Which sprints had a velocity above 20, and what activities did they include?**

```sparql
SELECT ?sprint ?velocity ?activity WHERE { ?sprint :sprintVelocity ?velocity . OPTIONAL { ?sprint :includesActivity ?activity } FILTER(?velocity > 20) } ORDER BY DESC(?velocity)
```

**CQ27. Who reports, directly or indirectly, to a given employee?**

```sparql
SELECT ?employee ?manager WHERE { ?employee :reportsTo+ ?manager . }
```

## Enterprise domain structure

**CQ28. Which sub-domains does a business domain contain?**

```sparql
SELECT ?domain ?sub WHERE { ?sub :subDomainOf ?domain . }
```

**CQ29. Which operations make up a business process, and which capability does the process realize?**

```sparql
SELECT ?process ?operation ?capability WHERE { ?operation :operationOf ?process . ?process :realizesCapability ?capability . }
```

**CQ30. What are the cycle time, lead time and throughput of a process?**

```sparql
SELECT ?process ?cycle ?lead ?throughput WHERE { ?process :cycleTime ?cycle ; :leadTime ?lead ; :throughput ?throughput . }
```

**CQ31. How is an organization classified by size, ownership, geographic scope and lifecycle phase?**

```sparql
SELECT ?org ?size ?ownership ?scope ?phase WHERE { ?org :hasOrganizationSize ?size ; :hasOwnershipType ?ownership ; :hasGeographicScope ?scope ; :inLifecyclePhase ?phase . }
```

**CQ32. Which capabilities does an organization have?**

```sparql
SELECT ?capability ?org WHERE { ?capability :capabilityOf ?org . }
```

**CQ33. What priority and status does a requirement have?**

```sparql
SELECT ?requirement ?priority ?status WHERE { ?requirement :hasPriority ?priority ; :hasRequirementStatus ?status . }
```

**CQ34. Which attributes does a data entity have, and how is the data classified?**

```sparql
SELECT ?entity ?attribute ?class WHERE { ?attribute :attributeOf ?entity . ?entity :hasDataClassification ?class . }
```

**CQ35. Which candidates for automation exist, and by which technique could they be automated?**

```sparql
SELECT ?candidate ?work ?technique WHERE { ?candidate :automationCandidateOf ?work ; :usesAutomationTechnique ?technique . }
```

**CQ36. In what condition are the physical assets of an organization?**

```sparql
SELECT ?asset ?condition WHERE { ?asset :hasCondition ?condition . }
```

**CQ37. Which change requests exist, and what impact do they have?**

```sparql
SELECT ?request ?impact WHERE { ?request a :ChangeRequest . ?impact a :ChangeImpact . }
```

**CQ38. Which parts is the enterprise domain structure divided into, and how many classes does each part hold?**

```sparql
SELECT ?part (COUNT(?class) AS ?classes) WHERE { ?part skos:inScheme :EnterpriseDomainStructureTaxonomy ; rdfs:seeAlso ?class . } GROUP BY ?part ORDER BY DESC(?classes)
```

**CQ39. Which classes were taken over from the earlier domain engineering ontology, and what is their original term?**

```sparql
SELECT ?class ?original WHERE { ?class rdfs:seeAlso ?original . FILTER(STRSTARTS(STR(?original), "http://domainengineering.org/ontology#")) }
```

**CQ40. Which classes of different parts of the ontology are declared equivalent?**

```sparql
SELECT ?class ?twin WHERE { ?class owl:equivalentClass ?twin . }
```

## AI-assisted practice, business analysis and variation

**CQ41. Which techniques of domain analysis are defined, and which are kinds of another technique?**

```sparql
SELECT ?technique ?kindOf WHERE { ?technique rdfs:subClassOf ?kindOf . ?kindOf rdfs:subClassOf* :DomainAnalysisTechnique . }
```

**CQ42. Which example domain ontologies are in the package?**

```sparql
SELECT ?ontology ?label WHERE { ?ontology a :DomainOntology ; rdfs:label ?label . }
```

**CQ43. Which key processes and artifacts belong to the domain engineering phase?**

```sparql
SELECT ?relation ?part WHERE { :DomainEngineeringPhase rdfs:subClassOf [ a owl:Restriction ; owl:onProperty ?relation ; owl:someValuesFrom ?part ] . }
```

**CQ44. Which quality attributes make up the variation capacity of a component?**

```sparql
SELECT ?attribute WHERE { ?attribute rdfs:subClassOf :VariationCapacityProperty . }
```

**CQ45. In what order are the steps of the variant generation process?**

```sparql
SELECT ?notation ?step WHERE { ?concept skos:broader :VariantGenerationProcessConcept ; skos:notation ?notation ; skos:prefLabel ?step . } ORDER BY ?notation
```

**CQ46. Which OWL reasoners and which methods of validating a domain model does the AI-assisted taxonomy list?**

```sparql
SELECT ?kind ?item WHERE { ?concept skos:broader ?group ; skos:prefLabel ?item . ?group skos:prefLabel ?kind . FILTER(?kind IN ("OWL Reasoners"@en, "Domain Model Validation Methods"@en)) }
```

**CQ47. Which conceptual entity-relationship diagrams are a basis for which domain ontology?**

```sparql
SELECT ?erd ?ontology WHERE { ?erd :isBasisForOntology ?ontology . }
```
