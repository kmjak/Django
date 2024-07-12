from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator,ValidationError
import re
# Create your models here.

def number_only(value):
    if re.match(r'^[0-9]*$', value) == None:
        raise ValidationError(
            '%(value)s is not number!!',
            params={'value':value}
        )


class Friend(models.Model):
    name = models.CharField(validators=[number_only] ,max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(150)] ,default=0)
    birthday = models.DateField()

    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'