from owlready2 import *


def get_ontology_from(path_to_ontology) -> Ontology:
    return get_ontology(path_to_ontology).load()


def get_tourism_ontology() -> Ontology:
    return get_ontology_from('../resources/TourismOntology.owl')


class TourismOntology:
    def __init__(self):
        self.__ontology = get_tourism_ontology()

    def get_ontology(self) -> Ontology:
        return self.__ontology

    def get_all_tours(self):
        return tuple(self.__ontology.Поездки.instances())

    def get_tour(self, tour: str = None):
        return self.__ontology.Поездки(tour) if tour else self.get_all_tours()

    def get_all_services(self):
        return tuple(self.__ontology.Услуги.instances())

    def get_service(self, service: str = None):
        return self.__ontology.Услуги(service) if service else self.get_all_services()


ontology = get_tourism_ontology()

print(list(ontology.classes()))
print(list(ontology.individuals()))
print(list(ontology.properties()))
print(list(ontology.object_properties()))

print()
for service in ontology.Услуги.instances():
    print(ontology.Услуги(service).входит_в)
