from django.db import models

STATUS = ((0, "IN_ACTIVE"), (1, "ACTIVE"))


class Role(models.Model):
    name = models.CharField(max_length=60)
    role_alias = models.CharField(max_length=60)

    def get_alias(self):
        return self.role_alias

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=60)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def get_email(self):
        return self.email

    def __str__(self):
        return self.name


# Create your models here.
