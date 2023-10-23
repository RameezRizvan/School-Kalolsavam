from django import forms
from .models import *


# LOGIN
class login_form(forms.Form):
    username=forms.CharField(max_length=25)
    password=forms.CharField(max_length=25)


# ITEM
class item_form(forms.Form):
    itemcode=forms.IntegerField()
    itemname=forms.CharField(max_length=25)
    category=forms.CharField(max_length=25)


# SCHOOL
class school_form(forms.Form):
    schoolcode=forms.IntegerField()
    schoolname=forms.CharField(max_length=100)
    category=forms.CharField(max_length=50)
    mark=forms.IntegerField()
    agrade=forms.IntegerField()
    bgrade=forms.IntegerField()
    cgrade=forms.IntegerField()


# ITEM_POINTS
class itempoints_form(forms.Form):
    category=forms.CharField(max_length=25)
    item=forms.CharField(max_length=25)
    file=forms.FileField()


# SCHOOL_POINTS
class schoolpoints_form(forms.Form):
    text=forms.CharField(max_length=25)
    file=forms.FileField()