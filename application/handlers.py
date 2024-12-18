from ontology.ontology import TourismOntology
from application.tours import ToursDialog
from application.services import ServicesDialog

tourism_ontology = TourismOntology()


def open_tours():
    tours = tourism_ontology.get_all_tours()
    result = 'Туры:\n'

    if not tours:
        result = 'Ничего не найдено в базе'
        dialog = ToursDialog(result)
        dialog.exec_()
        return

    for tour in tours:
        result += f'- {tour.name}\n'

    dialog = ToursDialog(result)
    dialog.exec_()


def open_services():
    services = tourism_ontology.get_all_services()
    result = 'Услуги:\n'

    if not services:
        result = 'Ничего не найдено в базе'
        dialog = ServicesDialog(result)
        dialog.exec_()
        return

    for service in services:
        result += f'- {service.name}\n'

    dialog = ServicesDialog(result)
    dialog.exec_()


def open_tours_and_services():
    services_and_tours = tourism_ontology.get_services_and_tours()
    result = ''

    if not services_and_tours:
        result = 'Ничего не найдено в базе'
        dialog = ServicesDialog(result)
        dialog.exec_()
        return

    result = services_and_tours
    dialog = ServicesDialog(result)
    dialog.exec_()
