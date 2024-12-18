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

    def get_services_and_tours(self):
        services_and_tours = ''
        services = self.get_all_services()
        for service in services:
            services_and_tours += f'Услуга {service.name} входит в туры:\n'
            for tour in self.__ontology.Услуги(service).входит_в:
                services_and_tours += f'- {tour.name}\n'
        return services_and_tours

    def get_tours_by_service(self, service_name: str = None):
        if not service_name:
            return self.get_services_and_tours()

        result = str()
        for service in self.get_all_services():
            print(service)
            if service_name == f'{service.name}':
                result += 'Рекомендованные Вам туры:\n'
                for tour in self.__ontology.Услуги(service).входит_в:
                    result += f'- {tour.name}\n'
        if not result:
            result = 'Ничего не найдено в базе'

        return result
