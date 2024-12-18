from owlready2 import *


def get_ontology_from(path_to_ontology) -> Ontology:
    return get_ontology(path_to_ontology).load()


def get_tourism_ontology() -> Ontology:
    return get_ontology_from('../resources/TourismOntology.owl')


class TourismOntology:
    def __init__(self):
        self.__ontology = get_tourism_ontology()


ontology = get_tourism_ontology()

print(list(ontology.classes()))
print(list(ontology.individuals()))
print(list(ontology.properties()))
print(list(ontology.object_properties()))

print()
for service in ontology.Услуги.instances():
    print(ontology.Поездки(service).входит_в)