from django.shortcuts import render,redirect
from ShopApp.models import Category_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from ShopApp.models  import Product_Db
import datetime
from WebApp.models import Contact_Db
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages



# Create your views here.
def furniture_page(request):
    date = datetime.datetime.now()
    x = Category_Db.objects.count()
    y = Product_Db.objects.count()
    return render(request,"index.html",{'date':date,'x':x,'y':y})

def add_categories(request):
    return render(request,"Add_Category.html")

def save_category(request):
    if request.method == "POST":
        cn    = request.POST.get('cname')
        desc  = request.POST.get('desc')
        cm    = request.FILES['img']
        obj=Category_Db(Category_Name=cn,Description=desc,Images=cm)
        obj.save()
        messages.success(request,"Successfully Saved")
        return redirect(add_categories)

def display_category(request):
    cat = Category_Db.objects.all
    return render(request,"Display_Category.html",{'cat':cat})

def edit_category(request,cat_id):
    cat = Category_Db.objects.get(id=cat_id)
    return render(request,"Edit_Category.html",{'cat':cat})

def update_category(request,cat_id):
    if request.method=="POST":
        cn = request.POST.get('cname')
        desc = request.POST.get('desc')
    try:
        cm   = request.FILES['img']
        fs = FileSystemStorage()
        file = fs.save(cm.name,cm)
    except MultiValueDictKeyError:
         file = Category_Db.objects.get(id=cat_id).Images
         Category_Db.objects.filter(id=cat_id).update(Category_Name=cn,
                                                      Description=desc,Images=file)
         messages.success(request, "Successfully Updated")
         return redirect(display_category)

def delete_student(request,cat_id):
    stud = Category_Db.objects.filter(id=cat_id)
    stud.delete()
    messages.success(request, "Data Deleted ")
    return redirect(display_category)

def add_product(request):
    prod = Category_Db.objects.all()
    return render(request,"Add_Products.html",{'prod':prod})

def save_product(request):
     if request.method =="POST":
         a = request.POST.get('pcat')
         b = request.POST.get('pname')
         c = request.POST.get('pquant')
         d = request.POST.get('price')
         e = request.POST.get('orgin')
         f = request.POST.get('manuf')
         g = request.POST.get('desc')
         h = request.FILES['img']
         i = request.FILES['img2']
         j = request.FILES['img3']
         obj = Product_Db(Product_Category=a,Product_Name=b,Quality=c,MRP=d,
                          Orgin=e,Manufacture=f,Description=g,img1=h,img2=i,img3=j)
         obj.save()
         messages.success(request,"Product Saved..")
         return redirect(add_product)

def display_products(request):
    prod = Product_Db.objects.all
    return render(request,"Display_Products.html",{'prod':prod})

def edit_products(request,prod_id):
    prod = Product_Db.objects.get(id=prod_id)
    cat = Category_Db.objects.all()
    return render(request,"Edit_Products.html",{'prod':prod,'cat':cat})

def update_products(request,prod_id):
    if request.method=="POST":
        a = request.POST.get('pcat')
        b = request.POST.get('pname')
        c = request.POST.get('pquant')
        d = request.POST.get('price')
        e = request.POST.get('orgin')
        f = request.POST.get('manuf')
        g = request.POST.get('desc')
    try:
        h = request.FILES['img']
        fs = FileSystemStorage()
        file = fs.save(h.name,h)

    except MultiValueDictKeyError:
        file = Product_Db.objects.get(id=prod_id).img1

    try :
        i = request.FILES['img2']
        fs = FileSystemStorage()
        file2  = fs.save(i.name,i)

    except MultiValueDictKeyError:
        file2 = Product_Db.objects.get(id=prod_id).img2

    try:
        j = request.FILES['img3']
        fs = FileSystemStorage()
        file3  = fs.save(j.name,j)

    except MultiValueDictKeyError:
        file3 = Product_Db.objects.get(id=prod_id).img3
    Product_Db.objects.filter(id=prod_id).update(Product_Category=a,Product_Name=b,Quality=c,MRP=d,
                          Orgin=e,Manufacture=f,Description=g,img1=file,img2=file2,img3=file3)
    messages.success(request, "Successfully Updated")
    return redirect(display_products)

def delete_products(request,prod_id):
    prod = Product_Db.objects.filter(id=prod_id)
    prod.delete()
    messages.success(request, "Data Deleted..")
    return redirect(display_products)

def login_page(request):
    return render(request,"Admin.html")

def admin_login(request):
    if request.method=="POST":
        un     = request.POST.get('username')
        pswd   = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pswd)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = pswd
                messages.success(request,"Welcome..")
                return redirect(furniture_page)
            else:
                messages.warning(request,"Invalid Password")
                return redirect(login_page)
        else:
            messages.warning(request,"Invalid Username")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)

def contact_details(request):
    contact = Contact_Db.objects.all()
    return render(request,"Contact_details.html",{'contact':contact})

def delete_contact(request,d_id):
    dc = Contact_Db.objects.filter(id=d_id)
    dc.delete()
    return redirect(contact_details)