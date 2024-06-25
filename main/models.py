from django.contrib.postgres.fields import ArrayField
from django.db import models


class CreatePatientModel(models.Model):
    GENDER_CHOICES = [
        (1, 'Female'),
        (2, 'Male'),
    ]

    company_code = models.BigIntegerField(null=True, blank=True,
                                          help_text="Уникальный код клиники (учитывается, если есть глобальный доступ к API)")
    name = models.CharField(max_length=255, help_text="Имя")
    lastname = models.CharField(max_length=255, help_text="Фамилия")
    middlename = models.CharField(max_length=255, help_text="Отчество")
    patient_email = models.EmailField(help_text="Электронная почта")
    birthday = models.CharField(max_length=10, help_text="Дата рождения (дд.мм.гггг)")
    gender = models.IntegerField(choices=GENDER_CHOICES, help_text="Пол (1 - женский; 2 - мужской)")

    patient_phone_country_code = models.CharField(max_length=10, help_text="Код страны")
    patient_phone_city_code = models.CharField(max_length=10, help_text="Код города")
    patient_phone_number = models.CharField(max_length=20, help_text="Номер")

    iin = models.CharField(max_length=12, help_text="ИИН")
    source_code = models.BigIntegerField(null=True, blank=True, help_text="Источник информации о клинике")

    def __str__(self):
        return f'{self.lastname} {self.name} {self.middlename}'

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"


class CreatePatientResponseModel(models.Model):
    GENDER_CHOICES = [
        (1, 'Female'),
        (2, 'Male'),
    ]


    patient_code = ArrayField(models.BigIntegerField(), help_text="Уникальные коды пациентов")
    email = ArrayField(models.EmailField(), help_text="Список адресов электронной почты")
    iin = ArrayField(models.CharField(max_length=12), help_text="Список ИИН-ов")
    name = models.CharField(max_length=255, help_text="Имя")
    lastname = models.CharField(max_length=255, help_text="Фамилия")
    middlename = models.CharField(max_length=255, help_text="Отчество")
    gender = models.IntegerField(choices=GENDER_CHOICES, help_text="Пол (1 - женский, 2 - мужской)")
    birthday = models.CharField(max_length=10, help_text="Дата рождения (дд.мм.гггг)")

    patient_phone_country_code = models.IntegerField(help_text="Код страны (7 или 998)")
    patient_phone_city_code = models.IntegerField(help_text="Код города (777)")
    patient_phone_number = models.IntegerField(help_text="Номер (1231212)")

    skip = models.IntegerField(help_text="Какое количество записей пропустить")

    def __str__(self):
        return f'{self.lastname} {self.name} {self.middlename}'

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"



class SearchPatientModel(models.Model):
    GENDER_CHOICES = [
        (1, 'Female'),
        (2, 'Male'),
    ]

    patient_code = models.JSONField(help_text="Уникальные коды пациентов")
    email = models.JSONField(help_text="Список адресов электронной почты")
    iin = models.JSONField(help_text="Список ИИН-ов")
    name = models.CharField(max_length=255, help_text="Имя")
    lastname = models.CharField(max_length=255, help_text="Фамилия")
    middlename = models.CharField(max_length=255, help_text="Отчество")
    gender = models.IntegerField(choices=GENDER_CHOICES, help_text="Пол (1 - женский, 2 - мужской)")
    birthday = models.CharField(max_length=10, help_text="Дата рождения (дд.мм.гггг)")

    patient_phone_country_code = models.IntegerField(help_text="Код страны (7 или 998)")
    patient_phone_city_code = models.IntegerField(help_text="Код города (777)")
    patient_phone_number = models.IntegerField(help_text="Номер (1231212)")

    skip = models.IntegerField(help_text="Какое количество записей пропустить")

    def __str__(self):
        return f'{self.lastname} {self.name} {self.middlename}'

    class Meta:
        verbose_name = "Поиск пациента"
        verbose_name_plural = "Поиск пациентов"


class SearchPatientResponseModel(models.Model):
    GENDER_CHOICES = [
        (1, 'Female'),
        (2, 'Male'),
    ]

    profile_code = models.CharField(max_length=255, unique=True, help_text="Уникальный код профиля")
    parent_code = models.CharField(max_length=255, help_text="Код родителя")
    name = models.CharField(max_length=255, help_text="Имя")
    lastname = models.CharField(max_length=255, help_text="Фамилия")
    middlename = models.CharField(max_length=255, help_text="Отчество")
    fullname = models.CharField(max_length=255, help_text="Полное имя")
    birthday = models.CharField(max_length=10, help_text="Дата рождения (дд.мм.гггг)")
    gender = models.IntegerField(choices=GENDER_CHOICES, help_text="Пол (1 - женский, 2 - мужской)")
    iin = models.CharField(max_length=12, help_text="ИИН")
    ambulatory_count = models.CharField(max_length=255, help_text="Количество амбулаторных посещений")
    created_date = models.DateTimeField(help_text="Дата создания")
    removed = models.BooleanField(default=False, help_text="Удален ли профиль")
    removed_date = models.DateTimeField(null=True, blank=True, help_text="Дата удаления")
    removed_reason = models.TextField(null=True, blank=True, help_text="Причина удаления")
    description = models.TextField(null=True, blank=True, help_text="Описание")
    status_code = models.CharField(max_length=255, null=True, blank=True, help_text="Код статуса")
    percentage_discount = models.FloatField(default=0, help_text="Процент скидки")
    patient_passport = models.TextField(null=True, blank=True, help_text="Паспорт пациента")
    patient_phone_1 = models.CharField(max_length=20, null=True, blank=True, help_text="Телефон пациента 1")
    patient_phone_2 = models.CharField(max_length=20, null=True, blank=True, help_text="Телефон пациента 2")
    patient_phone_3 = models.CharField(max_length=20, null=True, blank=True, help_text="Телефон пациента 3")
    patient_phone_4 = models.CharField(max_length=20, null=True, blank=True, help_text="Телефон пациента 4")
    phones_str = models.TextField(null=True, blank=True, help_text="Строка с телефонами")
    patient_address = models.TextField(null=True, blank=True, help_text="Адрес пациента")
    patient_email = models.EmailField(null=True, blank=True, help_text="Электронная почта пациента")
    patient_card_number = models.CharField(max_length=255, null=True, blank=True, help_text="Номер карты пациента")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

