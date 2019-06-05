from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def phones(self):
        return list(Phone.objects.filter(person=self).values_list('phone', flat=True))

    @property
    def emails(self):
        return list(Email.objects.filter(person=self).values_list('email', flat=True))


class Phone(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, null=True, max_length=50)


class Email(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70, blank=True)







