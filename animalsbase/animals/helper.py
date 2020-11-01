import pandas as pd
import math
import datetime

# from animalsbase.animals.models import Animals

file = '/home/john/Загрузки/hack/Dataset2.xlsx'

xl = pd.ExcelFile(file)

df1 = xl.parse('Лист')
all_data = df1.to_dict()

cnt = 1
db_objects = {}
for header in all_data.keys():
    for item in all_data.get(header):
        db_objects[cnt] = {}
        cnt += 1
    break

cnt = 1

headers = {'Unnamed: 0': '№ п/п', 'Unnamed: 1': 'карточка учета животного №', 'Unnamed: 2': 'вид ',
           'Unnamed: 3': 'возраст, год', 'Unnamed: 4': 'вес, кг', 'Unnamed: 5': 'кличка', 'Unnamed: 6': 'пол',
           'Unnamed: 7': 'порода', 'Unnamed: 8': 'окрас', 'Unnamed: 9': 'шерсть', 'Unnamed: 10': 'уши',
           'Unnamed: 11': 'хвост', 'Unnamed: 12': 'размер', 'Unnamed: 13': 'особые приметы', 'Unnamed: 14': 'Вольер №',
           'Unnamed: 15': 'идентификационная метка', 'Unnamed: 16': 'дата стерилизации',
           'Unnamed: 17': 'ф.и.о. ветеринарного врача', 'Unnamed: 18': 'Социализировано (да/нет)',
           'Unnamed: 19': 'заказ-наряд / акт о поступлении животного №',
           'Unnamed: 20': 'заказ-наряд дата/ акт о поступлении животного, дата',
           'Unnamed: 21': 'административный округ', 'Unnamed: 22': 'акт отлова №', 'Unnamed: 23': 'адрес места отлова',
           'Unnamed: 24': 'юридическое лицо ', 'Unnamed: 25': 'адрес', 'Unnamed: 26': 'телефон',
           'Unnamed: 27': 'ф.и.о. опекунов', 'Unnamed: 28': 'адрес', 'Unnamed: 29': 'телефон',
           'Unnamed: 30': 'физическое лицо ф.и.о.', 'Unnamed: 31': 'паспорт РФ серия номер', 'Unnamed: 32': 'выдан',
           'Unnamed: 33': 'дата выдачи', 'Unnamed: 34': 'адрес регистрации', 'Unnamed: 35': 'телефон',
           'Unnamed: 36': 'дата поступления в приют', 'Unnamed: 37': 'акт №', 'Unnamed: 38': 'дата выбытия из приюта',
           'Unnamed: 39': 'причина выбытия', 'Unnamed: 40': 'акт/договор №', 'Unnamed: 41': 'адрес приюта',
           'Unnamed: 42': 'эксплуатирующая организация', 'Unnamed: 43': 'ф.и.о. руководителя приюта',
           'Unnamed: 44': 'ф.и.о. сотрудника по уходу за животным', 'Unnamed: 45': '№ п/п', 'Unnamed: 46': 'дата',
           'Unnamed: 47': 'название препарата', 'Unnamed: 48': 'доза', 'Unnamed: 49': '№ п/п', 'Unnamed: 50': 'дата',
           'Unnamed: 51': 'вид вакцины', 'Unnamed: 52': '№ серии', 'Unnamed: 53': 'дата осмотра',
           'Unnamed: 54': 'анамнез '}

for header in all_data.keys():
    for item in all_data.get(header):
        db_objects[cnt].update({headers.get(header): all_data.get(header).get(item)})
        cnt += 1
    cnt = 1

db_objects.pop(1, None)

for i in db_objects:
    db_objects[i].pop("№ п/п", None)

for item in db_objects:
    for i in db_objects[item]:
        try:
            if math.isnan(db_objects[item][i]):
                db_objects[item][i] = None
        except:
            pass

        if i == "Социализировано (да/нет)":
            if db_objects[item][i] == "да":
                db_objects[item][i] = True
            else:
                db_objects[item][i] = False
    one_animal = db_objects[item]
    if item > 1:
        # try:
        #     problem_vac = one_animal.get("вид вакцины").split(" ")[0] + one_animal.get("вид вакцины").split(" ")[1]
        # except Exception:
        #     problem_vac = one_animal.get("вид вакцины").split(" ")[0]
        #
        # try:
        #     problem_data = one_animal.get("дата").split(" ")[0] + one_animal.get("дата").split(" ")[1]
        # except:
        #     pass

        # Animals.objects.create(accounting_card=one_animal.get("карточка учета животного №"), kind=one_animal.get("вид"),age=one_animal.get("возраст, год"), weight=one_animal.get("вес, кг"), animal_name=one_animal.get("кличка"), sex=one_animal.get("пол"), breed=one_animal.get("порода"), colour=one_animal.get("окрас"), wool=one_animal.get("шерсть"),            ears=one_animal.get("уши"), tail=one_animal.get("хвост"),size=one_animal.get("размер"),features=one_animal.get("особые приметы"),aviary=one_animal.get("Вольер №"), id_label=one_animal.get("идентификационная метка"), sterilization_date=one_animal.get("дата стерилизации"), doctor_name=one_animal.get("ф.и.о. ветеринарного врача"), is_socialized=one_animal.get("Социализировано (да/нет)"), admission_info=one_animal.get("заказ-наряд / акт о поступлении животного №"),admission_date=one_animal.get("заказ-наряд дата/ акт о поступлении животного, дата"),  district=one_animal.get("административный округ"),  capture_act=one_animal.get("акт отлова №"),  capture_address=one_animal.get("адрес места отлова"),  entity=one_animal.get("юридическое лицо"),  entity_address=one_animal.get("адрес"),  phone_number=one_animal.get("телефон"),  guardian_name=one_animal.get("ф.и.о. опекунов"),  individual=one_animal.get("физическое лицо ф.и.о."), passport_series_number=one_animal.get("паспорт РФ серия номер"), issued=one_animal.get("выдан"), issued_date=one_animal.get("дата выдачи"), registration_address=one_animal.get("адрес регистрации"),receipts_date=one_animal.get("дата поступления в приют"),act_number=one_animal.get("акт №"),departure_date=one_animal.get("дата выбытия из приюта"),departure_reason=one_animal.get("причина выбытия"), contract_number=one_animal.get("акт/договор №"),shelter_address=one_animal.get("адрес приюта"),operating_organization=one_animal.get("эксплуатирующая организация"), shelter_director=one_animal.get("ф.и.о. руководителя приюта"), сare_person=one_animal.get("ф.и.о. сотрудника по уходу за животным"),trearment_date=problem_data,preparation_name=one_animal.get("название препарата"), dose=one_animal.get("доза"),vaccination_info=problem_vac,vaccination_date=one_animal.get("№ серии"),serie_number=one_animal.get("дата осмотра"), inspection_date=None, anamnesis=one_animal.get("анамнез"))

        # print(one_animal.get("дата осмотра"))
        # print(one_animal.get("юридическое лицо "))

        # if 43 <= item - 1 <= 62:
        #     one_animal["название препарата"] = "Тронцил Инсектал"
        # if item-1 == 125 or (128 <= item-1 <= 131):
        #     one_animal["название препарата"] = "Рольф клуб 3D Прател"
        # print(" ".join(one_animal.get("название препарата").split()), item - 1)

        # try:
        #     print(" ".join(one_animal.get("вид вакцины").split()), item - 1)
        # except:
        #     print(one_animal.get("вид вакцины"), item - 1)


       print(one_animal.get("причина выбытия"))


