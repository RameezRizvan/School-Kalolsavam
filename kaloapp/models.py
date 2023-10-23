from django.db import models


# LOGIN
class login_model(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    def __str__(self):
        return self.username


#  ITEM
class item_model(models.Model):
    choice=(
        ('General LP','general_lp'),
        ('General UP','general_up'),
        ('General HS','general_hs'),
        ('General HSS','general_hss'),
        ('Arabic LP','arabic_lp'),
        ('Arabic UP','arabic_up'),
        ('Arabic HS','arabic_hs'),
        ('Sanskrit UP','sanskrit_up'),
        ('Sanskrit HS','sanskrit_hs')
    )
    itemcode=models.IntegerField()
    itemname=models.CharField(max_length=25)
    category=models.CharField(max_length=25,choices=choice)
    def __str__(self):
        return self.itemname


# SCHOOL
class school_model(models.Model):
    schoolcode=models.IntegerField()
    schoolname=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    mark=models.IntegerField()
    agrade=models.IntegerField()
    bgrade=models.IntegerField()
    cgrade=models.IntegerField()
    # place=models.CharField(max_length=50)
    def __str__(self):
        return self.schoolname


# ITEM_POINTS
class itempoints_model(models.Model):
    choice = (
        ('General LP', 'general_lp'),
        ('General UP', 'general_up'),
        ('General HS', 'general_hs'),
        ('General HSS', 'general_hss'),
        ('Arabic LP', 'arabic_lp'),
        ('Arabic UP', 'arabic_up'),
        ('Arabic HS', 'arabic_hs'),
        ('Sanskrit UP', 'sanskrit_up'),
        ('Sanskrit HS', 'sanskrit_hs')
    )
    category=models.CharField(max_length=25,choices=choice)
    item=models.CharField(max_length=25)
    file=models.FileField(upload_to='kaloapp/static/item_points')
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.item


# SCHOOL_POINTS
class schoolpoint_model(models.Model):
    text=models.CharField(max_length=25)
    file=models.FileField(upload_to='kaloapp/static/school_points')
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text

