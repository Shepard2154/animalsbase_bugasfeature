from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Animals


class AnimalsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "kind",
        "animal_name",
        "anamnesis",
        "accounting_card",
        "is_socialized",
        "issued",
        "get_photo",
    )

    search_fields = ("accounting_card", "animal_name",)
    list_filter = ("issued", "is_socialized", "kind", "sex", "shelter_address",)

    fields = ("get_photo", "photo", "kind", "age", "weight", "animal_name", "sex", "breed", "colour", "wool",
              "ears", "tail", "size", "features", "aviary", "id_label", "sterilization_date", "doctor_name",
              "is_socialized", "admission_info", "admission_date", "district", "capture_act", "capture_address",
              "entity", "guardian_name", "individual", "issued", "receipts_date", "act_number", "departure_date",
              "departure_reason", "contract_number", "shelter_address", "operating_organization",
              "shelter_director", "сare_person", "trearment_date", "preparation_name", "dose", "vaccination_info",
              "vaccination_date", "serie_number", "inspection_date", "anamnesis",
              )
    readonly_fields = ("get_photo",)
    admin.site.site_header = "Управление электронной базой животных"
    admin.site.site_title = "Управление электронной базой животных"

    def get_photo(self, animal):
        if animal.photo:
            return mark_safe(f'<img src={animal.photo.url} width="75px">')
        else:
            return '-'

    get_photo.short_description = "Фото"


admin.site.register(Animals, AnimalsAdmin)
