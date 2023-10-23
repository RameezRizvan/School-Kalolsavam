from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib import messages



# Create your views here.



# LOGIN------------------------------------------------------------
def login(request):
    if request.method=='POST':
        a=login_form(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['password']
            b = login_model.objects.all()
            for i in b:
                if i.username == username and i.password == password:
                    return redirect(school_points)
            else:
                return HttpResponse('incorrect email/password')
        else:
            return HttpResponse('Failed')
    return render(request,'login.html')



# ITEM ADD---------------------------------------------------------
def item(request):
    c=item_model.objects.all()
    if request.method=='POST':
        a=item_form(request.POST)
        if a.is_valid():
            itemcode=a.cleaned_data['itemcode']
            itemname=a.cleaned_data['itemname']
            category=a.cleaned_data['category']
            for i in c:
                if i.itemcode==itemcode:
                    messages.error(request,'*item code already exist')
                    return redirect(item)
            else:
                b = item_model(itemcode=itemcode, itemname=itemname, category=category)
                b.save()
                return redirect(item_display)
    return render(request,'items.html')



# ITEM DISPLAY---------------------------------------------------------
def item_display(request):
    a=item_model.objects.all()
    return render(request,'item_display.html',{'k':a})



# ITEM EDIT---------------------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404



def item_edit(request, id):
    a = get_object_or_404(item_model, id=id)

    if request.method == 'POST':
        new_itemcode = request.POST.get('itcode')
        new_itemname = request.POST.get('itname')
        new_category = request.POST.get('cat')

        # Check if the new itemcode already exists
        if item_model.objects.filter(itemcode=new_itemcode).exclude(id=id).exists():
            messages.error(request, '*Item code already exists')
        else:
            # Update the item fields
            a.itemcode = new_itemcode
            a.itemname = new_itemname
            a.category = new_category
            a.save()
            return redirect(item_display)  # Assuming 'item_display' is the name of your display view

    return render(request, 'item_edit.html', {'datas': a})


# ITEM DELETE---------------------------------------------------------
def item_delete(request,id):
    a=item_model.objects.get(id=id)
    a.delete()
    return redirect(item_display)



# ITEM_POINTS ADD---------------------------------------------------------
def item_points(request):
    a=item_model.objects.all()
    if request.method=='POST':
        b = itempoints_form(request.POST,request.FILES)
        if b.is_valid():
            category = b.cleaned_data['category']
            item = b.cleaned_data['item']
            file = b.cleaned_data['file']
            c = itempoints_model(category=category,item=item,file=file)
            c.save()
            return redirect(itempoints_display)
        else:
            return HttpResponse('Failed')
    return render(request,'item_points.html',{'k':a})



# ITEM_POINTS DISPLAY---------------------------------------------------------
def itempoints_display(request):
    a=itempoints_model.objects.all()
    cat=[]
    it=[]
    fil=[]
    up=[]
    id1=[]
    for i in a:
        ca=i.category
        cat.append(ca)
        ite=i.item
        it.append(ite)
        fi=str(i.file).split('/')[-1]
        fil.append(fi)
        up1=i.updated_at
        up.append(up1)
        id2=i.id
        id1.append(id2)
    pair=zip(cat,it,fil,up,id1)
    return render(request,'itempoints_display.html',{'a':pair})



# ITEM_POINTS EDIT---------------------------------------------------------
from django.utils import timezone
def itempoints_edit(request,id):
    a=itempoints_model.objects.get(id=id)
    b=item_model.objects.all()
    if request.method=='POST':
        a.category=request.POST.get('cat')
        a.item=request.POST.get('it')
        if 'fil' in request.FILES:
            a.file = request.FILES['fil']
        a.save()
        return redirect(itempoints_display)
    return render(request,'itempoints_edit.html',{'datas':a,'k':b})



# ITEM_POINTS DELETE---------------------------------------------------------
def itempoints_delete(request,id):
    a=itempoints_model.objects.get(id=id)
    a.delete()
    return redirect(itempoints_display)



# SCHOOL ADD---------------------------------------------------------
def school(request):
    c=school_model.objects.all()
    if request.method=='POST':
        a=school_form(request.POST)
        if a.is_valid():
            schoolcode=a.cleaned_data['schoolcode']
            schoolname=a.cleaned_data['schoolname']
            category=a.cleaned_data['category']
            mark=a.cleaned_data['mark']
            agrade=a.cleaned_data['agrade']
            bgrade=a.cleaned_data['bgrade']
            cgrade=a.cleaned_data['cgrade']
            for i in c:
                if i.schoolcode==schoolcode and i.category==category:
                    messages.error(request, '*school code already exist')
                    return redirect(school)
            else:
                b = school_model(schoolcode=schoolcode, schoolname=schoolname, category=category, mark=mark, agrade=agrade, bgrade=bgrade, cgrade=cgrade)
                b.save()
                return redirect(school_display)
    return render(request,'schools.html')



# SCHOOL DISPLAY---------------------------------------------------------
def school_display(request):
    schools = school_model.objects.all()
    return render(request, 'school_display.html', {'k': schools})



# SCHOOL EDIT---------------------------------------------------------
def school_edit(request,id):
    a=school_model.objects.get(id=id)
    b=school_model.objects.all()
    if request.method=='POST':
        a.mark=request.POST.get('mark1')
        a.agrade=request.POST.get('agrade1')
        a.bgrade = request.POST.get('bgrade1')
        a.cgrade = request.POST.get('cgrade1')
        a.save()
        return redirect(school_display)
    return render(request,'school_edit.html',{'datas':a,'k':b})



# SCHOOL DELETE---------------------------------------------------------
def school_delete(request,id):
    a=school_model.objects.get(id=id)
    a.delete()
    return redirect(school_display)



# SCHOOL_POINTS ADD---------------------------------------------------------
def school_points(request):
    if request.method == 'POST':
        b = schoolpoints_form(request.POST, request.FILES)
        if b.is_valid():
            txt = b.cleaned_data['text']
            fil = b.cleaned_data['file']
            c = schoolpoint_model(text=txt,file=fil)
            c.save()
            return redirect(schoolpoints_display)
        else:
            return HttpResponse('Failed')
    return render(request,'school_points.html')



def schoolpoints_display(request):
    a=schoolpoint_model.objects.all()
    txt=[]
    fil=[]
    up=[]
    id1=[]
    for i in a:
        txt1=i.text
        txt.append(txt1)
        fil1=str(i.file).split('/'[-1])
        fil.append(fil1)
        up1=i.updated_at
        up.append(up1)
        id2=i.id
        id1.append(id2)
    pair=zip(txt,fil,up,id1)
    return render(request,'schoolpoints_display.html',{'a':pair})


# SCHOOL_POINTS EDIT---------------------------------------------------------
def schoolpoints_edit(request,id):
    a=schoolpoint_model.objects.get(id=id)
    if request.method=='POST':
        a.text=request.POST.get('txt')
        if 'fil' in request.FILES:
            a.file = request.FILES['fil']
        a.save()
        return redirect(schoolpoints_display)
    return render(request,'schoolpoints_edit.html',{'datas':a})



# SCHOOL_POINTS DELETE---------------------------------------------------------
def schoolpoints_delete(request,id):
    a=schoolpoint_model.objects.get(id=id)
    a.delete()
    return redirect(schoolpoints_display)


