from django.db import models


class Animals(models.Model):
    accounting_card = models.CharField(max_length=300, blank=True, null=True,
                                       verbose_name="Карточка учета животного")  # Карточка учета животного №
    kind = models.CharField(max_length=30, blank=True, null=True, verbose_name="Вид")  # вид
    age = models.CharField(max_length=300, blank=True, null=True, verbose_name="Возраст, год")  # возраст, год
    weight = models.FloatField(blank=True, null=True, verbose_name="вес, кг")  # вес, кг
    animal_name = models.CharField(max_length=300, blank=True, null=True, verbose_name="Кличка")  # кличка
    sex = models.CharField(max_length=10, blank=True, null=True, verbose_name="Пол")  # пол
    breed = models.CharField(max_length=30, blank=True, null=True, verbose_name="Порода")  # порода
    colour = models.CharField(max_length=300, blank=True, null=True, verbose_name="Окрас")  # окрас
    wool = models.CharField(max_length=300, blank=True, null=True, verbose_name="Шерсть")  # шерсть
    ears = models.CharField(max_length=300, blank=True, null=True, verbose_name="Уши")  # уши
    tail = models.CharField(max_length=300, blank=True, null=True, verbose_name="Хвост")  # хвост
    size = models.CharField(max_length=300, blank=True, null=True, verbose_name="Размер")  # размер
    features = models.CharField(max_length=300, blank=True, null=True, verbose_name="Особые размеры")  # особые приметы
    aviary = models.CharField(max_length=300, blank=True, null=True, verbose_name="Вольтер №")  # вольер №
    id_label = models.CharField(max_length=300, blank=True, null=True,
                                verbose_name="Идентификационная метка")  # идентификационная метка
    sterilization_date = models.CharField(max_length=300, blank=True, null=True,
                                          verbose_name="Дата стерилизации")  # дата стерилизации
    doctor_name = models.CharField(max_length=300, blank=True, null=True,
                                   verbose_name="ф.и.о. ветеринарного врача")  # ф.и.о. ветеринарного врача
    is_socialized = models.BooleanField(blank=True, null=True, verbose_name="Социализировано")  # Социализировано
    admission_info = models.CharField(max_length=300, blank=True, null=True,
                                      verbose_name="Заказ-наряд / Акт о поступлении животного №")  # заказ-наряд / акт о поступлении животного №
    admission_date = models.CharField(max_length=300, blank=True, null=True,
                                      verbose_name="заказ-наряд дата/ акт о поступлении животного, дата")  # заказ-наряд дата/ акт о поступлении животного, дата
    district = models.CharField(max_length=10, blank=True, null=True,
                                verbose_name="Административный округ")  # административный округ
    capture_act = models.CharField(max_length=300, blank=True, null=True, verbose_name="акт отлова №")  # акт отлова №
    capture_address = models.CharField(max_length=1000, blank=True, null=True,
                                       verbose_name="Адрес места отлова")  # адрес места отлова
    entity = models.CharField(max_length=300, blank=True, null=True,
                              verbose_name="Юридическое лицо")  # юридическое лицо
    guardian_name = models.CharField(max_length=300, blank=True, null=True,
                                     verbose_name="ф.и.о. опекунов")  # ф.и.о. опекунов
    individual = models.CharField(max_length=300, blank=True, null=True,
                                  verbose_name="Физическое лицо ф.и.о.")  # физическое лицо ф.и.о.
    issued = models.BooleanField(default=None, blank=True, null=True, verbose_name="Выдано")  # выдано
    receipts_date = models.CharField(max_length=300, blank=True, null=True,
                                     verbose_name="Дата поступления в приют")  # дата поступления в приют
    act_number = models.CharField(max_length=300, blank=True, null=True, verbose_name="Акт №")  # акт №
    departure_date = models.CharField(max_length=300, blank=True, null=True,
                                      verbose_name="Дата убытия из приюта")  # дата убытия из приюта
    departure_reason = models.CharField(max_length=300, blank=True, null=True,
                                        verbose_name="Причина убытия")  # причина убытия
    contract_number = models.CharField(max_length=300, blank=True, null=True,
                                       verbose_name="Акт/Договор №")  # акт/договор №
    shelter_address = models.CharField(max_length=300, blank=True, null=True,
                                       verbose_name="Адрес приюта")  # адрес приюта
    operating_organization = models.CharField(max_length=300, blank=True, null=True,
                                              verbose_name="Эксплуатирующая организация")  # эксплуатирующая организация
    shelter_director = models.CharField(max_length=300, blank=True, null=True,
                                        verbose_name="ф.и.о. руководителя приюта")  # ф.и.о. руководителя приюта
    сare_person = models.CharField(max_length=300, blank=True, null=True,
                                   verbose_name="ф.и.о. сотрудника по уходу за животным")  # ф.и.о. сотрудника по уходу за животным
    trearment_date = models.CharField(max_length=300, blank=True, null=True, verbose_name="Дата обращения")  # дата
    preparation_name = models.CharField(max_length=300, blank=True, null=True,
                                        verbose_name="Название препарата")  # название препарата
    dose = models.CharField(max_length=300, blank=True, null=True, verbose_name="Доза")  # доза
    vaccination_info = models.CharField(max_length=300, blank=True, null=True,
                                        verbose_name="Вид вакцины")  # вид вакцины
    vaccination_date = models.CharField(max_length=300, blank=True, null=True,
                                        verbose_name="Дата вакцинации")  # Дата вакцинации
    serie_number = models.CharField(max_length=300, blank=True, null=True, verbose_name="№ серии")  # № серии
    inspection_date = models.CharField(max_length=300, blank=True, null=True,
                                       verbose_name="Дата осмотра")  # дата осмотра
    anamnesis = models.CharField(max_length=300, blank=True, null=True, verbose_name="Анамнез")  # анамнез
    photo = models.ImageField(upload_to="photo/%Y/%m/", blank=True)

    def __str__(self):
        return self.animal_name

    class Meta:
        verbose_name = 'животное'
        verbose_name_plural = "животные"
        ordering = ["-id"]

# Animals.objects.create(
#     accounting_card = one_animal.get("карточка учета животного №"),
#     kind = one_animal.get("вид"),
#     age = one_animal.get("возраст, год"),
#     weight = one_animal.get("вес, кг"),
#     animal_name = one_animal.get("кличка"),
#     sex = one_animal.get("пол"),
#     breed = one_animal.get("порода"),
#     colour = one_animal.get("окрас"),
#     wool = one_animal.get("шерсть"),
#     ears = one_animal.get("уши"),
#     tail = one_animal.get("хвост"),
#     size = one_animal.get("размер"),
#     features = one_animal.get("особые приметы"),
#     aviary = one_animal.get("Вольер №"),
#     id_label = one_animal.get("идентификационная метка"),
#     sterilization_date = one_animal.get("дата стерилизации"),
#     doctor_name = one_animal.get("ф.и.о. ветеринарного врача"),
#     is_socialized = one_animal.get("Социализировано (да/нет)"),
#     admission_info = one_animal.get("заказ-наряд / акт о поступлении животного №"),
#     admission_date = one_animal.get("заказ-наряд дата/ акт о поступлении животного, дата"),
#     district = one_animal.get("административный округ"),
#     capture_act = one_animal.get("акт отлова №"),
#     capture_address = one_animal.get("адрес места отлова"),
#     entity = one_animal.get("юридическое лицо"),
#     entity_address = one_animal.get("адрес"),
#     phone_number = one_animal.get("телефон"),
#     guardian_name = one_animal.get("ф.и.о. опекунов"),
#     individual = one_animal.get("физическое лицо ф.и.о."),
#     passport_series_number = one_animal.get("паспорт РФ серия номер"),
#     issued = one_animal.get("выдан"),
#     issued_date = one_animal.get("дата выдачи"),
#     registration_address = one_animal.get("адрес регистрации"),
#     receipts_date = one_animal.get("дата поступления в приют"),
#     act_number = one_animal.get("акт №"),
#     departure_date = one_animal.get("дата выбытия из приюта"),
#     departure_reason = one_animal.get("причина выбытия"),
#     contract_number = one_animal.get("акт/договор №"),
#     shelter_address = one_animal.get("адрес приюта"),
#     operating_organization = one_animal.get("эксплуатирующая организация"),
#     shelter_director = one_animal.get("ф.и.о. руководителя приюта"),
#     сare_person = one_animal.get("ф.и.о. сотрудника по уходу за животным"),
#     trearment_date = one_animal.get("дата"),
#     preparation_name = one_animal.get("название препарата"),
#     dose = one_animal.get("доза"),
#     vaccination_info = one_animal.get("вид вакцины"),
#     vaccination_date = one_animal.get("№ серии"),
#     serie_number = one_animal.get("дата осмотра"),
#     inspection_date = None,
#     anamnesis = one_animal.get("анамнез")
# )
