from owlready2 import *


def get_ontology_from(path_to_ontology) -> Ontology:
    return get_ontology(path_to_ontology).load()


def get_tourism_ontology() -> Ontology:
    return get_ontology_from('../resources/TourismOntology.owl')



