from django.db import models

class Value(models.Model): 
    value = models.TextField(max_length=60, null=True, blank=True)
    wartosc = models.TextField(max_length=60, null=True, blank=True)

    def __str__(self):
        return str(self.value)


class Map(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.ForeignKey(Value, null=True, blank=True, on_delete=models.SET_NULL) 
    wartosc = models.ForeignKey(Value, related_name="+", null=True, blank=True, on_delete=models.SET_NULL) 

    def __str__(self):
        return str(self.value)



