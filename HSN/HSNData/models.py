from django.db import models

class System(models.Model):
    name = models.CharField("Название системы", max_length=256)
    
    class Meta:
        verbose_name = "Cистема"
        verbose_name_plural = "Cистемы"

    def __str__(self) -> str:
        return self.name
    
class Organ(models.Model):
    name = models.CharField("Название Органа", max_length=256)
    systems = models.ManyToManyField(System, verbose_name="Системы")
    
    class Meta:
        verbose_name = "Орган"
        verbose_name_plural = "Органы"

    def __str__(self) -> str:
        return self.name
    
class WeightData(models.Model):
    TYPES = {
        "KB": "Килобайты",
        "MB": "Мегабайты", 
        "GB": "Гигабайты"
    }
    name = models.CharField("Название", max_length=512)
    
    weight = models.FloatField("Объем занимаемой памяти")
    w_type = models.CharField("Тип веса", max_length=2, choices=TYPES, default="KB")

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        abstract=True

    
class Parametr(WeightData):
    class Meta:
        verbose_name = "Параметр"
        verbose_name_plural = "Параметры"
        
    is_research = models.BooleanField("Является исследованием?", default=True)
        
class Conclusion(WeightData):

    class Meta:
        verbose_name = "Заключение"
        verbose_name_plural = "Заключения"


class Research(WeightData):
    parametrs = models.ManyToManyField(Parametr, verbose_name="Список параметров")
    conclusion = models.ForeignKey(Conclusion, verbose_name="Заключение", on_delete=models.SET_NULL, null=True, default=None, blank=True)
    organs = models.ManyToManyField(Organ, verbose_name="Список огранов")
    
    class Meta:
        verbose_name = "Исследование"
        verbose_name_plural = "Исследования"
        


