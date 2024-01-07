from django.shortcuts import render, redirect
from Backend.models import ModeDB, TypeDB, VideoDb, AddressDb, TeamDb, LocationDb
from Frontend.models import QuoteDb, ContactUsDb, SignupDb, ShipDb, WarehouseDb, WeightStorage, ClassStorage,\
    ContactUsDb, MainbodyDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from Frontend import mail
from django.contrib.auth.decorators import login_required
import re as RegEx

# =========================================== ADMIN STARTS ===============================================

def userform(request):
    return render(request, 'forms/form.html')

def saveform(request):
    if request.method == 'POST':
        fnm = request.POST.get('fullname')
        ph = request.POST.get('phone')
        em = request.POST.get('email')
        ps = request.POST.get('pass')
        pp = request.FILES['profile']
        check_mail = '^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w'
        if SignupDb.objects.filter(Email=em).exists():
            messages.error(request, 'Username already exists. Try with another Email ID')
            return redirect(userform)
        else:
            if RegEx.search(check_mail, em):
                obj = SignupDb(Full_Name=fnm, Phone=ph, Email=em, Password=ps, ProImg=pp)
                obj.save()
                send_mail(mail.reg_sub, mail.reg_msg, settings.EMAIL_HOST_USER, [em], fail_silently=False)
                messages.success(request, 'User registered successfully. Now you can Login.')
                return redirect(userform)
            else:
                messages.warning(request, 'Enter valid mail')
                return redirect(userform)
           
def userlogin(request):
    if request.method == 'POST':
        em = request.POST.get('email')
        ps = request.POST.get('pass')
        if SignupDb.objects.filter(Email=em, Password=ps).exists():
            request.session['Email'] = em
            request.session['Password'] = ps
            messages.success(request, 'Login successfull.')
            return redirect(frontindex)
        else:
            messages.error(request, 'Login error...!')
            return redirect(userform)
    messages.error(request, 'Login error...!')
    return redirect(userform)

def logoutuser(request):
    del request.session['Email']
    del request.session['Password']
    messages.warning(request, 'User logged off..!')
    return redirect(frontindex)

# =========================================== ADMIN ENDS ===============================================
# blank_starts

def blank(request):
    mode = ModeDB.objects.all()
    type = TypeDB.objects.all()
    address = AddressDb.objects.all()
    return render(request, 'blank/blank.html', {'address': address, 'type': type, 'mode': mode})

# blank_ends
# =========================================== HOME STARTS ===============================================

def frontindex(request):
    mode = ModeDB.objects.all()
    type = TypeDB.objects.all()
    address = AddressDb.objects.all()
    team = TeamDb.objects.all()
    slider = MainbodyDb.objects.all()
    feed = ContactUsDb.objects.all()
    context = {'address': address, 'type': type, 'mode': mode, 'team': team, 'slider': slider, 'feed': feed}
    return render(request, 'home/frontindex.html', context)


# =========================================== HOME ENDS ===================================================
# =========================================== ABOUT STARTS ================================================

def aboutPage(request):
    video = VideoDb.objects.all()
    type = TypeDB.objects.all()
    address = AddressDb.objects.all()
    team = TeamDb.objects.all()
    feed = ContactUsDb.objects.all()
    slider = MainbodyDb.objects.all()
    context = {'address': address,  'type': type, 'video': video, 'team': team, 'feed': feed, 'slider': slider }
    return render(request, 'home/about.html', context)


# =========================================== ABOUT ENDS ====================================================
# =========================================== SERVICES STARTS ===============================================

def servPage(request):
    mode = ModeDB.objects.all()
    type = TypeDB.objects.all()
    address = AddressDb.objects.all()
    slider = MainbodyDb.objects.all()
    return render(request, 'home/services.html', {'address': address, 'type': type, 'mode': mode, 'slider': slider })


# =========================================== SIDEBAR ENDS ===================================================
# =========================================== SCHEDULES STARTS ===============================================

def schedulepage(request):
    type = TypeDB.objects.all()
    address = AddressDb.objects.all()
    cls = ClassStorage.objects.all()
    weight = WeightStorage.objects.all()
    location = LocationDb.objects.all()
    slider = MainbodyDb.objects.all()
    context = {'address': address, 'type': type, 'cls': cls, 'weight': weight, 'location': location,\
        'slider': slider }
    return render(request, 'home/schedule.html', context)

# _______________________________________ SHIPPING SECTION ________________________________________________________

def shipping(request):
    if request.method == 'POST':
        to = request.POST.get('shfr')
        fr = request.POST.get('shto')
        dp = request.POST.get('depar')
        cl = request.POST.get('class')
        vl = request.POST.get('volume')
        ty = request.POST.get('type')
        eml = request.POST.get('email')
        obj = ShipDb(From_Address=to, To_Address=fr, Dep_Date=dp, Class=cl, Volume=vl, Type=ty, Email=eml)
        if SignupDb.objects.filter(Email=eml).exists():
            obj.save()
            messages.success(request, 'Shipping booked successfully')
            return redirect(schedulepage)
        else:
            messages.warning(request, 'Please login first to continue')
            return redirect(schedulepage)

# _________________________________________ WAREHOUSE SECTION ______________________________________________________

def warehouse(request):
    if request.method == 'POST':
        str = request.POST.get('start')
        end = request.POST.get('end')
        typ = request.POST.get('type')
        hub = request.POST.get('hub')
        eml = request.POST.get('email')
        obj = WarehouseDb(StartDate=str, EndDate=end, Type=typ, Hub=hub, Email=eml)
        if SignupDb.objects.filter(Email=eml).exists():
            obj.save()
            messages.success(request, 'Storage booked successfully')
            return redirect(schedulepage)
        else:
            messages.warning(request, 'Please login first to continue')
            return redirect(schedulepage)


# =========================================== SCHEDULES ENDS ===================================================
# =========================================== CONTACTS STARTS ==================================================

def contactpage(request):
    type = TypeDB.objects.all()
    address = AddressDb.objects.all()
    slider = MainbodyDb.objects.all()
    return render(request, 'home/contact.html', {'address': address, 'type': type, 'slider': slider})

def savecontactus(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pf = request.POST.get('prfsn')
        mg = request.POST.get('message')
        obj = ContactUsDb(Name=nm, Email=em, Proffession=pf, Message=mg)
        obj.save()
        messages.success(request, "Feedback submitted successfully. We will look on to it. Thank You..!")
        return redirect(contactpage)


# =========================================== CONTACTS ENDS ====================================================
# =========================================== QUOTE REQUEST STARTS =============================================

def requestquote(request):
    address = AddressDb.objects.all()
    type = TypeDB.objects.all()
    slider = MainbodyDb.objects.all()
    return render(request, 'home/freequote.html', {'address': address, 'type': type, 'slider': slider})

def quotesave(request):
    if request.method == 'POST':
        nm = request.POST.get('qname')
        em = request.POST.get('qmail')
        check_mail = '^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w'
        if RegEx.search(check_mail, em):
            if QuoteDb.objects.filter(Email=em).exists():
                messages.error(request, 'Request pending, unable to process')
                return redirect(requestquote)
            else:
                obj = QuoteDb(Name=nm, Email=em)
                obj.save()
                send_mail(mail.qt_sub, mail.qt_msg, settings.EMAIL_HOST_USER, [em], fail_silently=False)
                messages.success(request, "Request submitted successfully..!")
                return redirect(requestquote)
        else:
            messages.error(request, "Enter valid Email..!")
            return redirect(requestquote)

# =========================================== REQUEST ENDS ===================================================
# =========================================== PROFILE STARTS =================================================

def profile(request, user_mail):
    address = AddressDb.objects.all()
    type = TypeDB.objects.all()
    slider = MainbodyDb.objects.all()
    email = SignupDb.objects.filter(Email=user_mail).first()   
    context = {'address': address, 'type': type, 'email': email, 'slider': slider }
    return render(request, 'profile/profile.html', context)

def profile_edit(request, user_mail):
    address = AddressDb.objects.all()
    type = TypeDB.objects.all()
    slider = MainbodyDb.objects.all()
    location = LocationDb.objects.all()
    email = SignupDb.objects.filter(Email=user_mail).first() 
    context = {'address': address, 'type': type, 'email': email, 'slider': slider, 'location': location }
    return render(request, 'profile/profile_edit.html', context)

def profilesave(request, user_mail):
    if request.method == 'POST':
        fnm = request.POST.get('fullname')
        phn = request.POST.get('mobile')
        add = request.POST.get('address')
        loc = request.POST.get('locality')
        prof = request.POST.get('prof')
        pin = request.POST.get('pincode')
        sta = request.POST.get('state')
        cty = request.POST.get('country')
        eml = request.POST.get('email')
        pwd = request.POST.get('pass')
        try:
            img = request.FILES['profile']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = SignupDb.objects.get(Email=user_mail).ProImg 
        SignupDb.objects.filter(Email=user_mail).update(Full_Name=fnm, Email=eml, Phone=phn, Address=add,\
            Locality=loc, Proffession=prof, Pincode=pin, State=sta, Country=cty, Password=pwd, ProImg=file)
        messages.success(request, 'Details inserted successfully..!')
        return redirect(frontindex)

# =========================================== PROFILE ENDS ===================================================
# =========================================== SIDEBAR STARTS ===============================================    

def logistics(request, valueId):
    address = AddressDb.objects.all()
    type = TypeDB.objects.all()
    slider = MainbodyDb.objects.all()
    value = TypeDB.objects.get(id=valueId)
    context = {'address': address, 'type': type, 'value': value, 'slider': slider}
    return render(request, 'home/logistics.html', context)


# =========================================== SIDEBAR ENDS ===================================================
# =========================================== LOCATION STARTS ================================================

def location(request):
    type = TypeDB.objects.all()
    address = AddressDb.objects.all()
    location = LocationDb.objects.all()
    slider = MainbodyDb.objects.all()
    context = {'address': address, 'type': type, 'location': location, 'slider': slider}
    return render(request, 'location/location.html', context)


# =========================================== LOCATION ENDS ===================================================
# =========================================== STATUS PAGE STARTS ==============================================

def shipment_status_page(request, unique_id):
    type = TypeDB.objects.all()
    address = AddressDb.objects.all()
    if request.method == 'POST':
        unique_id = request.POST.get('reqid')

        if ShipDb.objects.filter(Shipping_ID=unique_id).exists():
            email = ShipDb.objects.filter(Shipping_ID=unique_id).first()    # filter using input [i.e; Tracking ID]
            context = {'address': address, 'type': type, 'email': email}
            return render(request, 'status/shipment_status.html', context) 
        
        elif WarehouseDb.objects.filter(Warehouse_ID=unique_id).exists():
            email = WarehouseDb.objects.filter(Warehouse_ID=unique_id).first()  # first() returns first item
            context = {'address': address, 'type': type, 'email': email}
            return render(request, 'status/warehouse_status.html', context)
        
        else:
            messages.warning(request, 'Shipping ID not found')  
            return redirect(frontindex)

        