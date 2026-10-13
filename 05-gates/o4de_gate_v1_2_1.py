#!/usr/bin/env python3
# Copyright 2026 Yusuf Altunel. Licensed under the Apache License, Version 2.0 (https://www.apache.org/licenses/LICENSE-2.0).
"""o4de_gate_v1_2_1.py -- the release gate of the O4DE package.

Run from the package root:   python3 05-gates/o4de_gate_v1_2_1.py .

It reads the package, never trusts a count written in a document, and fails with exit 1 on the first broken property:
  1. file structure: exactly one T-Box, one A-Box and one SHACL file (highest version of each), named <name>_<role>_v<M>_<m>_<p>.ttl
  2. role purity: the T-Box holds no individuals; the A-Box declares no class or property
  3. every O4DE term used anywhere is declared (no undeclared class, property or individual)
  4. the SHACL shapes accept the T-Box and A-Box together (SHACL advanced features on)
  5. every competency question in the highest-version question file returns at least one row
  6. each negative fixture is REFUSED by the shapes with the message it announces (a gate that cannot fail verifies nothing)
Needs: rdflib, pyshacl.
"""
import glob, os, re, sys
import rdflib
from rdflib import RDF, RDFS, OWL, SKOS, URIRef
from pyshacl import validate

root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
NS = "http://www.zt4swe.io/o4de#"
SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")
fails = []

def semver(f):
    m = re.search(r"_v(\d+)_(\d+)_(\d+)\.", f)
    return tuple(int(x) for x in m.groups()) if m else (0, 0, 0)

def newest(pattern):
    fs = sorted(glob.glob(os.path.join(root, pattern)), key=semver)
    return fs[-1] if fs else None

def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + (f"  {detail}" if detail else ""))
    if not ok:
        fails.append(name)

# 1 structure
def live(f):
    """a Turtle file of the package itself: not a fixture, an archive, a vendored copy or the publish record"""
    parts = os.path.relpath(f, root).split(os.sep)[:-1]
    return not any(p in ("fixtures", "archive") or p.startswith("vendored") or p.endswith("-snapshot") for p in parts) and os.path.basename(f) != "PUBLISH_RECORD.ttl"
ttl = [f for f in glob.glob(os.path.join(root, "**", "*.ttl"), recursive=True) if live(f)]
roles = {r: [f for f in ttl if re.search(rf"_{r}_v\d+_\d+_\d+\.ttl$", os.path.basename(f))] for r in ("tbox", "abox", "shacl")}
print("1. file structure")
for r, fs in roles.items():
    check(f"exactly one {r} file", len(fs) == 1, ", ".join(os.path.basename(f) for f in fs))
check("no other Turtle file", len(ttl) == sum(len(v) for v in roles.values()), f"{len(ttl)} found")
if fails:
    print("VERDICT: FAIL"); sys.exit(1)
tf, af, sf = roles["tbox"][0], roles["abox"][0], roles["shacl"][0]
t, a, s = rdflib.Graph(), rdflib.Graph(), rdflib.Graph()
t.parse(tf); a.parse(af); s.parse(sf)
print(f"   parsed: T-Box {len(t)} triples, A-Box {len(a)} triples, SHACL {len(s)} triples")

# 2 role purity
print("2. role purity")
decl = (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
check("T-Box holds no named individual", not any(True for _ in t.subjects(RDF.type, OWL.NamedIndividual)))
check("T-Box holds no taxonomy concept", not any(True for _ in t.subjects(RDF.type, SKOS.Concept)))
check("A-Box declares no class or property", not any(isinstance(x, URIRef) for d in decl for x in a.subjects(RDF.type, d)))
check("SHACL file declares no class or property", not any(isinstance(x, URIRef) for d in decl for x in s.subjects(RDF.type, d)))
for g, n in ((t, "T-Box"), (a, "A-Box"), (s, "SHACL")):
    check(f"{n} has one ontology header", len(list(g.subjects(RDF.type, OWL.Ontology))) == 1)

# 3 declared terms
print("3. declared terms")
d = rdflib.Graph(); [d.parse(f) for f in (tf, af)]
declared = set()
for ty in decl + (OWL.NamedIndividual, SKOS.Concept, SKOS.ConceptScheme):
    declared |= {x for x in d.subjects(RDF.type, ty) if isinstance(x, URIRef)}
used = set()
for g in (t, a):
    for sub, p, o in g:
        for x in (sub, p, o):
            if isinstance(x, URIRef) and str(x).startswith(NS):
                used.add(x)
undeclared = sorted(str(x).replace(NS, "o4de:") for x in used - declared)
check("every O4DE term used is declared", not undeclared, ", ".join(undeclared[:8]))
nC = len([x for x in t.subjects(RDF.type, OWL.Class) if isinstance(x, URIRef)])
nO = len([x for x in t.subjects(RDF.type, OWL.ObjectProperty)])
nD = len([x for x in t.subjects(RDF.type, OWL.DatatypeProperty)])
nS = len(list(a.subjects(RDF.type, SKOS.ConceptScheme))); nK = len(list(a.subjects(RDF.type, SKOS.Concept)))
nI = len(list(a.subjects(RDF.type, OWL.NamedIndividual)))
print(f"   counts: {nC} classes, {nO} object properties, {nD} datatype properties, {nS} taxonomies, {nK} concepts, {nI} example individuals")

# 4 SHACL
print("4. SHACL conformance")
def run_shapes(data):
    ok, rg, _ = validate(data, shacl_graph=s, advanced=True, inference="none", allow_warnings=False)
    msgs = [str(m) for m in rg.objects(None, SH.resultMessage)]
    return ok, msgs
ok, msgs = run_shapes(d)
check("T-Box and A-Box conform to the shapes", ok, f"{len(msgs)} violation(s)" if not ok else f"{len(list(s.subjects(RDF.type, SH.NodeShape)))} shapes")

# 5 competency questions
print("5. competency questions")
cq = newest("04-documentation/O4DE_Competency_Questions_v*.md")
check("a competency question file exists", cq is not None)
if cq:
    text = open(cq, encoding="utf-8").read()
    blocks = re.findall(r"```sparql\n(.*?)```", text, re.S)
    prefix = f"PREFIX : <{NS}>\nPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\nPREFIX skos: <http://www.w3.org/2004/02/skos/core#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
    empty = []
    for i, q in enumerate(blocks, 1):
        try:
            rows = len(list(d.query(prefix + q)))
        except Exception as e:
            rows = 0
        if rows == 0: empty.append(i)
    check("every competency question returns rows", blocks and not empty, f"{len(blocks)} questions" + (f"; empty: {empty}" if empty else ""))

# 6 negative fixtures
print("6. negative fixtures (the gate must be able to fail)")
fx = sorted(glob.glob(os.path.join(root, "fixtures", "negative_*.ttl")))
check("negative fixtures present", len(fx) >= 5, f"{len(fx)} found")
for f in fx:
    head = open(f, encoding="utf-8").read().splitlines()[0]
    m = re.match(r"# EXPECT: (.*)", head)
    g = rdflib.Graph(); g.parse(f)
    data = d + g
    ok, msgs = run_shapes(data)
    hit = bool(m) and any(m.group(1) in x for x in msgs)
    check(f"{os.path.basename(f)} is refused", (not ok) and hit, f"expected '{m.group(1) if m else '?'}'")

# 7 licence (BP-D24; the same arrangement as the OE Method and the other public repositories of the owner)
print("7. licence: CC BY 4.0 for ontologies, shapes and documentation; Apache-2.0 for tooling and gates")
CCURL = "http://creativecommons.org/licenses/by/4.0/"
def licence_problems(onto_licences, onto_banners, tool_texts, licence_md):
    bad = []
    bad += [f"ontology licence {x}" for x in onto_licences if x != CCURL]
    bad += [f"ontology banner {b[:40]}" for b in onto_banners if "CC BY 4.0" not in b]
    bad += [f"tool {n}" for n, t in tool_texts.items() if "Apache License, Version 2.0" not in t]
    if not ("CC BY 4.0" in licence_md and "Apache License 2.0" in licence_md): bad.append("LICENSE.md terms")
    return bad
lic_md = open(os.path.join(root, "LICENSE.md"), encoding="utf-8").read() if os.path.exists(os.path.join(root, "LICENSE.md")) else ""
onto_files = [f for f in ttl if live(f)]
lic_vals, banners = [], []
for f in onto_files:
    gg = rdflib.Graph(); gg.parse(f)
    lic_vals += [str(o) for o in gg.objects(None, rdflib.URIRef("http://purl.org/dc/terms/license"))]
    banners.append(open(f, encoding="utf-8").readline() + open(f, encoding="utf-8").readlines()[1])
tool_files = glob.glob(os.path.join(root, "03-tooling", "*.py")) + glob.glob(os.path.join(root, "05-gates", "*.py"))
tool_texts = {os.path.basename(f): open(f, encoding="utf-8").read() for f in tool_files}
probs = licence_problems(lic_vals, banners, tool_texts, lic_md)
check("licences match the arrangement", not probs, "; ".join(probs[:4]))
check("the licence check can fail: Apache on an ontology is refused", bool(licence_problems([APACHE_URL := "http://www.apache.org/licenses/LICENSE-2.0"], banners, tool_texts, lic_md)))
check("the licence check can fail: a tool without its Apache statement is refused", bool(licence_problems(lic_vals, banners, {"x.py": "no statement"}, lic_md)))
check("the licence check can fail: missing LICENSE.md is refused", bool(licence_problems(lic_vals, banners, tool_texts, "")))

print("VERDICT: PASS" if not fails else f"VERDICT: FAIL ({len(fails)} check(s): {'; '.join(fails)})")
sys.exit(0 if not fails else 1)
