from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20, default=None, null=True)
    last_name = models.CharField(max_length=20, default=None, null=True)
    email = models.EmailField(max_length=20, default=None, null=True)
    company_name = models.CharField(max_length=20, default=None, null=True)
    phone = models.CharField(max_length=20, default=None, null=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

    @staticmethod
    def get_id_by_mail(email):
        return User.objects.get(email=email)

    @staticmethod
    def get_id_by_id(id):
        return User.objects.get(id=id)


class Search(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    keyword = models.CharField(max_length=200, default=None, null=True)
    search_date = models.DateTimeField(default=None, null=True)


class Search_data(models.Model):
    all_keywords = models.CharField(max_length=100, unique =  True)
    all_users = models.CharField(max_length=100)
    time_range = models.CharField(max_length=100)
    
