from django.shortcuts import render, redirect
from ShopApp.models import Product_Db, Category_Db
from WebApp.models import Contact_Db
from WebApp.models import SignUp_Db
from WebApp.models import Cart_Db
from django.contrib import messages
from WebApp.models import CheckOut_Db
import razorpay


# Create your views here.

def home_page(request):
    categories = Category_Db.objects.all()
    cart_data = Cart_Db.objects.filter(Name=request.session['Name'])
    x = cart_data.count()
    return render(request, "Home.html", {'categories': categories, 'x': x})


def products_page(request):
    product = Product_Db.objects.all()
    return render(request, "Products.html", {'product': product})


def about_page(request):
    return render(request, "About Us.html")


def contact_page(request):
    return render(request, "Contact.html")


def save_contact(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('cont')
        c = request.POST.get('email')
        d = request.POST.get('desc')
        obj = Contact_Db(Name=a, Contact=b, Email=c, Description=d)
        obj.save()
        return redirect(contact_page)


def filtered_product(request, cat_name):
    data = Product_Db.objects.filter(Product_Category=cat_name)
    return render(request, "Products_Filtered.html", {'data': data})


def single_product(request, prod_id):
    data = Product_Db.objects.get(id=prod_id)
    return render(request, "Single_Product.html", {'data': data})


def sign_up(request):
    return render(request, "Sign_Up.html")


def sign_in(request):
    return render(request, "Sign_In.html")


def save_signup(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('number')
        d = request.POST.get('pass')
        e = request.POST.get('re_pass')
        obj = SignUp_Db(Name=a, Email=b, Mobile=c, Password=d, Confirm_Password=e)
        if SignUp_Db.objects.filter(Name=a).exists():
            messages.warning(request, "User already exist..")
            return redirect(sign_up)
        elif SignUp_Db.objects.filter(Email=b).exists():
            messages.warning(request, "Email already exist..")
            return redirect(sign_up)
        obj.save()
        messages.success(request, "Successfully Registered..")
        return redirect(sign_up)


def user_login(request):
    if request.method == "POST":
        un = request.POST.get('your_name')
        pwd = request.POST.get('your_pass')
        if SignUp_Db.objects.filter(Name=un, Password=pwd).exists():
            request.session['Name'] = un
            request.session['Password'] = pwd
            messages.success(request, "Welcome")
            return redirect(home_page)
        else:
            messages.warning(request, "Invalid Password")
            return redirect(sign_in)
    else:
        messages.warning(request, "Invalid Username")
        return redirect(sign_in)


def save_cart(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        pname = request.POST.get('pro_name')
        quant = request.POST.get('quantity')
        price = request.POST.get('mrp')
        tprice = request.POST.get('total')

        try:
            x = Product_Db.objects.get(Product_Name=pname)
            img = x.img1
        except Product_Db.DoesNotExist:
            img = None
        obj = Cart_Db(Name=name, Product_Name=pname, Quantity=quant, Price=price, Total_Price=tprice, Prod_Image=img)
        obj.save()
        return redirect(cart_page)


def cart_page(request):
    cart_data = Cart_Db.objects.filter(Name=request.session['Name'])
    Subtotal = 0
    Shipping_amt = 0
    Total = 0
    for i in cart_data:
        Subtotal += i.Total_Price
        if Subtotal > 50000:
            Shipping_amt = 100
        else:
            Shipping_amt = 250
        Total = Subtotal + Shipping_amt
    return render(request, "Cart.html", {'cart_data': cart_data, 'Subtotal': Subtotal,
                                             'Shipping_amt': Shipping_amt, 'Total': Total})


def delete_cart(request, cart_id):
    a = Cart_Db.objects.filter(id=cart_id)
    a.delete()
    return redirect(cart_page)


def check_out(request):
    cdata = Cart_Db.objects.filter(Name=request.session['Name'])
    Subtotal = 0
    Shipping_amt = 0
    Total = 0
    for i in cdata:
        Subtotal += i.Total_Price
        if Subtotal > 50000:
            Shipping_amt = 100
        else:
            Shipping_amt = 250
        Total = Subtotal + Shipping_amt
    return render(request, "CheckOut.html", {'cdata': cdata, 'Subtotal': Subtotal,
                                             'Shipping_amt': Shipping_amt, 'Total': Total})


def save_checkout(request):
    if request.method == "POST":
        a = request.POST.get('count')
        b = request.POST.get('name')
        c = request.POST.get('email')
        d = request.POST.get('place')
        e = request.POST.get('c_address')
        f = request.POST.get('zip')
        g = request.POST.get('state')
        h = request.POST.get('c_phone')
        i = request.POST.get('total')
        j = request.POST.get('msg')
        obj = CheckOut_Db(Country=a, Name=b, Email=c, Place=d, Address=e, Zip=f, State=g, Mobile_Number=h,
                          Total_Price=i, Messages=j)
        obj.save()
        return redirect(check_out)


def payment_page(request):
    # Retrieve the data from CheckOut_Db with the specific ID
    customer = CheckOut_Db.objects.order_by('-id').first()

    # Get the payment amount of the specified customer
    payy = customer.Total_Price

    # Convert the amount into Paisa(Smallest currency unit)
    amount = int(payy * 100)  # Assuming the payment amount in rupees

    payy_str = str(amount)

    for i in payy_str:
        print(i)
        if request.method == "POST":
            order_currency = 'INR'
            client = razorpay.Client(auth=('rzp_test_A7vwIAzI1n64cC', '2IrIHYOdrgy3eCYVczrvmYjT'))
            payment = client.order.create({'amount': amount, 'currency': order_currency})

    return render(request, "Payment_page.html", {'customer': customer, 'payy_str': payy_str})


def service_page(request):
    return render(request, "Service.html")

def blog_page(request):
    return render(request,"Blog.html")