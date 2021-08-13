from django.db import models

class coursemodel(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)
    course_fee = models.FloatField()


class studentmodel(models.Model):
    student_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    course = models.ManyToManyField(coursemodel)

