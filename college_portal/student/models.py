from django.db import models

# Create your models here.
class student_table(models.Model):
    reg_no=models.IntegerField(),
    name=models.CharField(max_length=20),
    email=models.EmailField(default='example@gmail.com'),
    dob=models.DateField()

    def __str__(self):
        return super().__str__()


