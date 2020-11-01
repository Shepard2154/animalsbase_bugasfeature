from django.shortcuts import render, HttpResponse
from .models import Animals
import json


def animal_json(animal, is_admin=False):
    if not is_admin:
        data_for_user = {
            "kind": animal.kind,
            "age": animal.age,
            "weight": animal.weight,
            "animal_name": animal.animal_name,
            "sex": animal.sex,
            "breed": animal.breed,
            "colour": animal.colour,
            "wool": animal.wool,
            "ears": animal.ears,
            "tail": animal.tail,
            "size": animal.size
        }

        return json.dumps(data_for_user)
    else:
        data_for_admin = {
            "accounting_card": animal.accounting_card,
            "kind": animal.kind,
            "age": animal.age,
            "weight": animal.weight,
            "animal_name": animal.animal_name,
            "sex": animal.sex,
            "breed": animal.breed,
            "colour": animal.colour,
            "wool": animal.wool,
            "ears": animal.ears,
            "tail": animal.tail,
            "size": animal.size,
            "features": animal.features,
            "aviary": animal.aviary,
            "id_label": animal.id_label,
            "sterilization_date": animal.sterilization_date,
            "doctor_name": animal.doctor_name,
            "is_socialized": animal.is_socialized,
            "admission_info": animal.admission_info,
            "admission_date": animal.admission_date,
            "district": animal.district,
            "capture_act": animal.capture_act,
            "capture_address": animal.capture_address,
            "entity": animal.entity,
            "guardian_name": animal.guardian_name,
            "individual": animal.individual,
            "issued": animal.issued,
            "receipts_date": animal.receipts_date,
            "act_number": animal.act_number,
            "departure_date": animal.departure_date,
            "departure_reason": animal.departure_reason,
            "contract_number": animal.contract_number,
            "shelter_address": animal.shelter_address,
            "operating_organization": animal.operating_organization,
            "shelter_director": animal.shelter_director,
            "сare_person": animal.сare_person,
            "trearment_date": animal.trearment_date,
            "preparation_name": animal.preparation_name,
            "dose": animal.dose,
            "vaccination_info": animal.vaccination_info,
            "vaccination_date": animal.vaccination_date,
            "serie_number": animal.serie_number,
            "inspection_date": animal.inspection_date,
            "anamnesis": animal.anamnesis
        }

        return json.dumps(data_for_admin)


def index(request):
    animals = Animals.objects.filter(is_socialized=True, issued=False)

    context = {"animals": animals}
    return render(request, template_name="index.html", context=context)


def get_animal(request, animal_id):
    animal = Animals.objects.get(pk=animal_id)
    context = {"animal": animal}
    return render(request, template_name='card_pet.html', context=context)

