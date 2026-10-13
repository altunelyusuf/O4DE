#!/usr/bin/env python3
# Copyright 2026 Yusuf Altunel. Licensed under the Apache License, Version 2.0 (https://www.apache.org/licenses/LICENSE-2.0).
"""o4de_hermit_check_v1_2_1.py -- OWL consistency check of O4DE with the HermiT reasoner.

  python3 03-tooling/o4de_hermit_check_v1_2_1.py <package-root> [--with <extra-turtle-file>]

Needs: rdflib, owlready2 and a Java runtime. HermiT implements the OWL 2 datatype map, which has no xsd:date and no
xsd:duration, so the check runs on a COPY of the T-Box and A-Box in which those two datatypes are replaced by xsd:string.
The shipped files keep the real datatypes. Prints the reasoner verdict and the unsatisfiable classes (there must be none).
"""
import glob, os, re, sys, tempfile
import rdflib
from rdflib import XSD, Literal, RDF, RDFS, OWL

root = sys.argv[1] if len(sys.argv) > 1 else "."
extra = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--with" else None   # a fixture added to the data, to show the check can fail
def newest(p):
    fs = glob.glob(os.path.join(root, p))
    return sorted(fs, key=lambda f: tuple(int(x) for x in re.search(r"_v(\d+)_(\d+)_(\d+)\.", f).groups()))[-1]
g = rdflib.Graph()
for p in ("01-ontologies/o4de_tbox_v*.ttl", "01-ontologies/o4de_abox_v*.ttl"):
    g.parse(newest(p))
swap = {XSD.date: XSD.string, XSD.duration: XSD.string}
n = 0
for s, p, o in list(g):
    if isinstance(o, Literal) and o.datatype in swap:
        g.remove((s, p, o)); g.add((s, p, Literal(str(o), datatype=XSD.string))); n += 1
    if p in (RDFS.range, RDFS.domain, OWL.onDatatype) and o in swap:
        g.remove((s, p, o)); g.add((s, p, swap[o])); n += 1
if extra:
    g.parse(extra)
# the imports line would make owlready2 look for the T-Box on the web; both files are already merged
for s, o in list(g.subject_objects(OWL.imports)):
    g.remove((s, OWL.imports, o))
tmp = tempfile.mkdtemp()
path = os.path.join(tmp, "o4de.owl")
g.serialize(path, format="xml")
print(f"merged graph: {len(g)} triples; {n} date/duration items mapped to xsd:string for the reasoner")
from owlready2 import get_ontology, sync_reasoner_hermit, default_world, owl
onto = get_ontology("file://" + path).load()
from owlready2 import OwlReadyInconsistentOntologyError
try:
    with onto:
        sync_reasoner_hermit([onto], infer_property_values=False)
except OwlReadyInconsistentOntologyError:
    print("HermiT: ontology INCONSISTENT"); sys.exit(1)
bad = list(default_world.inconsistent_classes())
print("HermiT: ontology consistent")
print("unsatisfiable classes:", [str(c) for c in bad] if bad else "none")
sys.exit(1 if bad else 0)
