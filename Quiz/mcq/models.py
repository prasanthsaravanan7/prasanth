from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    joined_on = models.DateTimeField(auto_now_add=True)

    def register(self):
        self.save()

    def is_exist(self):
        if Student.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_student_by_email(email):
        return Student.objects.get(email=email)


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.category_name


class Questions(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.IntegerField()
    first_option = models.CharField(max_length=100)
    second_option = models.CharField(max_length=100)
    third_option = models.CharField(max_length=100, blank=True)
    fourth_option = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.question
