from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Backend.models import ModeDB, TypeDB, VideoDb, AddressDb, TeamDb, LocationDb
from Frontend.models import SignupDb, ShipDb, WarehouseDb, OrderStorage, WeightStorage, ClassStorage,\
    QuoteDb, ContactUsDb, MainbodyDb
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def backindex(request):
    footer = AddressDb.objects.all()
    return render(request, 'backindex.html', {'footer': footer})

# =================================== Admin_section_starts =====================================================

def adlogin(request):
    return render(request, 'admin/adlogin.html')

def loginAdmin(request):
    if request.method == 'POST':
        un = request.POST.get('usrnm')
        ps = request.POST.get('pswrd')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=ps)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = ps
                messages.success(request, 'Admin login successfull')
                return redirect(backindex)
            else:
                messages.error(request, 'Admin not recognised')
                return redirect(adlogin)
        else:
            messages.error(request, 'Admin not recognised')
            return redirect(adlogin)

def logoutadmin(request):
    del request.session['username']   
    del request.session['password']
    messages.success(request, 'Admin successfully logged off')
    return redirect(adlogin)    

# ========================== Admin_section_ends ==================================================================

# ========================== Mode_section_starts =================================================================

def modeAdd(a):
    return render(a, 'mode/modeAdd.html')

def saveMode(request):
    if request.method == 'POST':
        nm = request.POST.get('mname')
        ds = request.POST.get('mdesc')
        icn = request.FILES['micons']
        obj = ModeDB(ModeName=nm, ModeDesc=ds, ModeImage=icn)
        obj.save()
        messages.success(request, 'Mode added successfully')
        return redirect(modeAdd)

def modeDisplay(request):
    mode = ModeDB.objects.all()
    return render(request, 'mode/modeDisplay.html', {'mode': mode})

def modeEdit(request, ModeId):
    mode = ModeDB.objects.get(id=ModeId)
    return render(request, 'mode/modeEdit.html', {'mode': mode})

def modeUpdate(request, ModeId):
    if request.method == 'POST':
        nm = request.POST.get('uname')
        ds = request.POST.get('udesc')
        ds1 = request.POST.get('udesc1')
        ds2 = request.POST.get('udesc2')
        ds3 = request.POST.get('udesc3')
        ds4 = request.POST.get('udesc4')
        ds5 = request.POST.get('udesc5')
        try:
            img = request.FILES['micons']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ModeDB.objects.get(id=ModeId).ModeImage    
        ModeDB.objects.filter(id=ModeId).update(ModeName=nm, ModeDesc=ds, ModeDesc_P1=ds1, ModeDesc_P2=ds2,\
            ModeDesc_P3=ds3, ModeDesc_P4=ds4, ModeDesc_P5=ds5, ModeImage=file)
        messages.success(request, 'Mode updated successfully')
        return redirect(modeDisplay)

def modeDelete(request, ModeId):
    mode = ModeDB.objects.filter(id=ModeId)
    mode.delete()
    messages.error(request, 'Mode deleted successfully')
    return redirect(modeDisplay)
    
# ================================== Mode_section_ends ============================================================

# ================================== Type_section_starts ==========================================================

def typeadd(request):
    return render(request, 'type/addtype.html')

def typesave(request):
    if request.method == 'POST':
        tnm = request.POST.get('typename')
        tds = request.POST.get('typedesc')
        tds1 = request.POST.get('typedesc1')
        tds2 = request.POST.get('typedesc2')
        tds3 = request.POST.get('typedesc3')
        tds4 = request.POST.get('typedesc4')
        tds5 = request.POST.get('typedesc5')
        obj = TypeDB(TypeName=tnm, TypeDesc=tds,  TypeDesc_P1=tds1, TypeDesc_P2=tds2, TypeDesc_P3=tds3,\
            TypeDesc_P4=tds4, TypeDesc_P5=tds5)
        obj.save()
        messages.success(request, "Type added successfully..!")
        return redirect(typeadd)

def typedisplay(tdisp):
    type = TypeDB.objects.all()
    return render(tdisp, 'type/displaytype.html', {'type': type})

def type_edit(tedit, TypeId):
    type = TypeDB.objects.get(id=TypeId)
    return render(tedit, 'type/edit_type.html', {'type': type})
    

def typeUpdate(request, TypeId):
    if request.method == 'POST':
        tnm = request.POST.get('typename')
        tds = request.POST.get('typedesc')
        tds1 = request.POST.get('typedesc1')
        tds2 = request.POST.get('typedesc2')
        tds3 = request.POST.get('typedesc3')
        tds4 = request.POST.get('typedesc4')
        tds5 = request.POST.get('typedesc5')
        TypeDB.objects.filter(id=TypeId).update(TypeName=tnm, TypeDesc=tds, TypeDesc_P1=tds1, TypeDesc_P2=tds2,\
            TypeDesc_P3=tds3, TypeDesc_P4=tds4, TypeDesc_P5=tds5)
        messages.success(request, "Type updated successfully..!")
        return redirect(typedisplay)

def typedelete(request, TypeId):
    type = TypeDB.objects.filter(id=TypeId)
    type.delete()
    messages.error(request, "Type deleted successfully..!")
    return redirect(typedisplay)

# ======================================== Type_section_ends ================================================

# ======================================== Video _section_starts ============================================

def addvideo(v):
    video = VideoDb.objects.all()
    return render(v, 'video/addvideo.html', {'video': video})

def savevideo(request):
    if request.method == 'POST':
        vid = request.FILES['svideo']
        obj = VideoDb(HomeVideo=vid)
        if VideoDb.objects.exists():
            messages.error(request, 'Cover video exists')
            return redirect(addvideo)
        else:
            obj.save()
            messages.success(request, 'Cover video added')
            return redirect(addvideo)

def displayvideo(vd):
    video = VideoDb.objects.all()
    return render(vd, 'video/displayvideo.html', {'video': video})

def deletevideo(request, videoid):
    video = VideoDb.objects.filter(id=videoid)
    video.delete()
    return redirect(displayvideo)

# ======================================== Video _section_ends ================================================

# ======================================== Address _section_starts ============================================

def addressadd(request):
    return render(request, 'address/addaddress.html')

def saveaddress(request):
    if request.method == 'POST':
        eml = request.POST.get('amail')
        web = request.POST.get('aweb')
        cpy = request.POST.get('acopy')
        add = request.POST.get('adesc')
        cnt = request.POST.get('afone')
        obj = AddressDb(Email=eml, Website=web, Copy_right=cpy, Address=add, ContactNum=cnt)
        if AddressDb.objects.exists():
            messages.error(request, "Address already exists")
            return redirect(addressadd)
        else:
            obj.save()
            messages.success(request, "Address uploaded successfully")
            return redirect(addressadd)

def displayaddress(request):
    address = AddressDb.objects.all()
    return render(request, 'address/displayaddress.html', {'address': address})

def editaddress(request, addressId):
    address = AddressDb.objects.get(id=addressId)
    return render(request, 'address/editaddress.html', {'address': address})

def updateaddress(request, addressId):
    if request.method == 'POST':
        eml = request.POST.get('email')
        web = request.POST.get('eweb')
        cpy = request.POST.get('acopy')
        efn = request.POST.get('efone')
        add = request.POST.get('edesc')
        AddressDb.objects.filter(id=addressId).update(Email=eml, Website=web, Copy_right=cpy, Address=add,\
            ContactNum=efn)
        messages.success(request, "Address updated successfully..!")
        return redirect(displayaddress)

def deleteaddress(request, delId):
    address = AddressDb.objects.filter(id=delId)
    address.delete()
    messages.error(request, 'Address deleted successfully..!')
    return redirect(displayaddress)

# ======================================== Address _section_ends ================================================

# ======================================== User _section_starts ==================================================

def displayuser(request):
    users = SignupDb.objects.all()
    return render(request, 'users/displayuser.html', {'users': users})

def deleteuser(request, userid):
    users = SignupDb.objects.filter(id=userid)
    users.delete()
    messages.warning(request, 'User Deleted')
    return redirect(displayuser)

def displayuserfeedback(request):
    feed = ContactUsDb.objects.all()
    return render(request, 'users/userfeedback.html', {'feed': feed})

def deleteuserfeedback(request, feedId):
    feed = ContactUsDb.objects.filter(id=feedId)
    feed.delete()
    messages.warning(request, 'Feedback Deleted')
    return redirect(displayuserfeedback)

# ======================================== User _section_ends ================================================

# ======================================== Team _section_starts ==============================================

def teamadd(request):
    return render(request, 'team/teamadd.html')

def saveteam(request):
    if request.method == 'POST':
        nm = request.POST.get('tname')
        ds = request.POST.get('dtion')
        im = request.FILES['timg']
        li1 = request.POST.get('link1')
        li2 = request.POST.get('link2')
        li3 = request.POST.get('link3')
        li4 = request.POST.get('link4')
        obj = TeamDb(Name=nm, Designation=ds, Image=im, Social_1=li1, Social_2=li2, Social_3=li3, Social_4=li4)
        obj.save()
        messages.success(request, 'Board member details uploaded successfully')
        return redirect(teamadd)
    
def displayteam(request):
    team = TeamDb.objects.all()
    return render(request, 'team/teamdisplay.html', {'team': team})

def teamedit(request, teamid):
    team = TeamDb.objects.get(id=teamid)
    return render(request, 'team/teamedit.html', {'team': team})

def teamupdate(request, teamid):
    if request.method == 'POST':
        nm = request.POST.get('tname')
        ds = request.POST.get('dtion')
        li1 = request.POST.get('link1')
        li2 = request.POST.get('link2')
        li3 = request.POST.get('link3')
        li4 = request.POST.get('link4')
        try:
            im = request.FILES['timg']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = TeamDb.objects.get(id=teamid).Image
        TeamDb.objects.filter(id=teamid).update(Name=nm, Designation=ds, Social_1=li1, Social_2=li2,\
            Social_3=li3, Social_4=li4,  Image=file)
        messages.success(request, 'Updation successfull')
        return redirect(displayteam)

def deleteteam(request, teamid):
    team = TeamDb.objects.filter(id=teamid)
    team.delete()
    messages.error(request, 'Member deleted successfully')
    return redirect(displayteam)

# ======================================== Team _section_ends ======================================================

# ======================================== Location _section_starts ================================================

def locationdb(request):
    return render(request, 'location/addlocations.html')

def locationsave(request):
    if request.method == 'POST':
        hnm = request.POST.get('hubname')
        loc = request.POST.get('hubaddress')
        obj = LocationDb(Hub=hnm, Location=loc)
        obj.save()
        messages.success(request, 'Location added successfully')
        return redirect(locationdb)
    
def displaylocation(request):
    location = LocationDb.objects.all()
    return render(request, 'location/displaylocation.html', {'location': location})    

def editlocation(request, locId):
    location = LocationDb.objects.get(id=locId)
    return render(request, 'location/editlocation.html', {'location': location})

def updatelocation(request, locId):
    if request.method == 'POST':
        hnm = request.POST.get('hubname')
        loc = request.POST.get('hubaddress')
        if LocationDb.objects.filter(Hub=hnm, Location=loc).exists():
            messages.warning(request, 'Location address same')
            return redirect(displaylocation)
        else:
            LocationDb.objects.filter(id=locId).update(Hub=hnm, Location=loc)
            messages.success(request, 'Location address successfull')
            return redirect(displaylocation)

def locationdelete(request, locId):
    location = LocationDb.objects.filter(id=locId)
    location.delete()
    messages.error(request, 'Location deleted successfully')
    return redirect(displaylocation)

# ======================================== Location _section_ends ================================================

# ======================================== Display_Tracking  _section_starts =====================================

def display_pending_tracking(request):
    ship = ShipDb.objects.all()
    return render(request, 'users/display_track.html', {'ship': ship})

def edit_pending_tracking(request, shipId):
    ship = ShipDb.objects.get(id=shipId)
    type = TypeDB.objects.all()
    cls = ClassStorage.objects.all()
    weight = WeightStorage.objects.all()
    data = OrderStorage.objects.all()
    context = {'ship': ship, 'type': type, 'cls': cls, 'weight': weight, 'data': data}
    return render(request, 'users/edit_track.html', context)

def update_pending_tracking(request, shipId):
    if request.method == 'POST':
        gd = request.POST.get('genid')
        fr = request.POST.get('from')
        to = request.POST.get('to')
        dp = request.POST.get('depar')
        est = request.POST.get('estdel')
        cl = request.POST.get('class')
        vl = request.POST.get('vol')
        ty = request.POST.get('type')
        st = request.POST.get('status')
        if ShipDb.objects.filter(Shipping_ID=gd).exists():
            ShipDb.objects.filter(id=shipId).update(From_Address=fr, To_Address=to, Dep_Date=dp,\
                Est_Del_Date=est, Class=cl, Volume=vl, Type=ty, Order_Status=st)
            messages.error(request, 'Tracking ID already given')
            return redirect(display_pending_tracking)
        else:
            ShipDb.objects.filter(id=shipId).update(Shipping_ID=gd, From_Address=fr, To_Address=to, Dep_Date=dp,\
                Est_Del_Date=est, Class=cl, Volume=vl, Type=ty, Order_Status=st)
            messages.success(request, 'Shipping updated successfully')
            return redirect(display_pending_tracking)

def delete_pending_tracking(request, shipId):
    ship = ShipDb.objects.filter(id=shipId)
    ship.delete()
    messages.error(request, 'Request deleted successfully')
    return redirect(display_pending_tracking)

def mail_page_for_shipping(request, mailId):
    ship = ShipDb.objects.get(id=mailId)
    return render(request, 'sendmail/shippingmail.html', {'ship': ship})

def send_mail_for_shipping(request):
    if request.method == 'POST':
        tom = request.POST.get('mailto')
        sbj = request.POST.get('subject')
        msg = request.POST.get('content')
        send_mail(sbj, msg, settings.EMAIL_HOST_USER, [tom], fail_silently=False)
        messages.success(request, 'Tracking ID Mail send successfully')    
        return redirect(display_pending_tracking)
    else:
        messages.error(request, 'Tracking ID Mail send Failed')    
        return redirect(display_pending_tracking)


# ======================================== Display_Tracking _section_ends ==========================================

# ======================================== Display_Warehouse _section_starts =======================================

def display_pending_warehouse(request):
    ware = WarehouseDb.objects.all()
    return render(request, 'users/display_ware.html', {'ware': ware})

def edit_pending_warehouse(request, wareId):
    type = TypeDB.objects.all()
    order = OrderStorage.objects.all()
    ware = WarehouseDb.objects.get(id=wareId)
    location = LocationDb.objects.all()
    context = {'order': order, 'type': type, 'ware': ware, 'location': location}
    return render(request, 'users/edit_ware.html', context)

def update_pending_warehouse(request, wareId):
    if request.method == 'POST':
        gd = request.POST.get('genid')
        sr = request.POST.get('start')
        ed = request.POST.get('end')
        ty = request.POST.get('type')
        hub = request.POST.get('hub')
        st = request.POST.get('status')
        if WarehouseDb.objects.filter(Warehouse_ID=gd).exists():
            WarehouseDb.objects.filter(id=wareId).update(StartDate=sr, EndDate=ed, Type=ty, Hub=hub, Order_Status=st)
            messages.error(request, 'Tracking ID already given')
            return redirect(display_pending_warehouse)
        else:
            WarehouseDb.objects.filter(id=wareId).update(Warehouse_ID=gd, StartDate=sr, EndDate=ed, Type=ty,\
                Hub=hub, Order_Status=st)
            messages.success(request, 'Shipping updated successfully')
            return redirect(display_pending_warehouse)

def delete_pending_warehouse(request, wareId):
    ware = WarehouseDb.objects.filter(id=wareId)
    ware.delete()
    messages.error(request, 'Request deleted successfully')
    return redirect(display_pending_warehouse)

def mail_page_for_warehouse(request, wareId):
    ware = WarehouseDb.objects.get(id=wareId)
    return render(request, 'sendmail/warehousemail.html', {'ware': ware})

def send_mail_for_warehouse(request):
    if request.method == 'POST':
        toml = request.POST.get('mailto')
        subt = request.POST.get('subject')
        cntd = request.POST.get('content')
        send_mail(subt, cntd, settings.EMAIL_HOST_USER, [toml], fail_silently=False)
        messages.success(request, 'Warehouse ID Mail send successfully')    
        return redirect(display_pending_warehouse)
    else:
        messages.error(request, 'Warehouse ID Mail send Failed')    
        return redirect(display_pending_warehouse)

# ======================================== Display_Warehouse _section_ends =========================================

# ======================================== Store _section_starts ===================================================

def datastore_add(request):
    return render(request, 'store/storedata.html')

def datastore_save(request):
    if request.method == 'POST':
        str = request.POST.get('status')
        obj = OrderStorage(Order_Status=str)
        if OrderStorage.objects.filter(Order_Status=str).exists():
            messages.error(request, 'Data already exists')
            return redirect(datastore_add)
        else:
            obj.save()
            messages.success(request, 'Data added successfully')
            return redirect(datastore_add)

def view_datastore(request):
    data = OrderStorage.objects.all()
    weight = WeightStorage.objects.all()
    cls = ClassStorage.objects.all()
    return render(request, 'store/view_storedata.html', {'data': data, 'weight': weight, 'cls': cls})

def delete_datastore(request, dataid):
    data = OrderStorage.objects.filter(id=dataid)
    data.delete()
    messages.error(request, 'Data deleted successfully')
    return redirect(view_datastore)

# <=== WEIGHT ADD ===> ---------------------------------------------------------------------------------------- #

def weight_save(request):
    if request.method == 'POST':
        wgt = request.POST.get('weight')
        obj = WeightStorage(Weightage=wgt)
        if WeightStorage.objects.filter(Weightage=wgt).exists():
            messages.error(request, 'Weight already exists')
            return redirect(datastore_add)
        else:
            obj.save()
            messages.success(request, 'Weight added successfully')
            return redirect(datastore_add)

def delete_weight(request, weightid):
    weight = WeightStorage.objects.filter(id=weightid)
    weight.delete()
    messages.error(request, 'Weight deleted successfully')
    return redirect(view_datastore)

# <=== CLASS ADD ===> ---------------------------------------------------------------------------------------- #

def class_save(request):
    if request.method == 'POST':
        cls = request.POST.get('class')
        obj = ClassStorage(Class=cls)
        if ClassStorage.objects.filter(Class=cls).exists():
            messages.error(request, 'Class already exists')
            return redirect(datastore_add)
        else:
            obj.save()
            messages.success(request, 'Class added successfully')
            return redirect(datastore_add)
        
def delete_cls(request, clsid):
    cls = ClassStorage.objects.filter(id=clsid)
    cls.delete()
    messages.error(request, 'Class deleted successfully')
    return redirect(view_datastore)

# ======================================== Store section Ends  =====================================================

# ======================================== Quote section Starts  ===================================================

def quotedisplay(request):
    quote = QuoteDb.objects.all()
    return render(request, 'quote/quotedisplay.html', {'quote': quote})

def quotemail(request, quoteId):
    quote = QuoteDb.objects.get(id=quoteId)
    return render(request, 'quote/mail.html', {'quote': quote})

def quote_send_mail(request):
    if request.method == 'POST':
        toml = request.POST.get('mailto')
        subt = request.POST.get('subject')
        cntd = request.POST.get('content')
        send_mail(subt, cntd, settings.EMAIL_HOST_USER, [toml], fail_silently=False)
        messages.success(request, 'Mail send successfully')    
        return redirect(quotedisplay)
    else:
        messages.error(request, 'Mail send Failed')    
        return redirect(quotedisplay)

def quotedelete(request, quoteId):
    quote = QuoteDb.objects.filter(id=quoteId)
    quote.delete()
    messages.error(request, 'Quote request deleted successfully')
    return redirect(quotedisplay)

# ======================================== Quote section Ends  =====================================================

# ======================================== Slider section Starts  ==================================================

def mainslider(request):
    return render(request, 'store/mainsec.html')

def mainslidersave(request):
    if request.method == 'POST':
        tphd = request.POST.get('tophead')
        mnhd = request.POST.get('mainhead')
        sbhd = request.POST.get('subhead')
        ctp1 = request.POST.get('ctp1')
        ctp2 = request.POST.get('ctp2')
        ctp3 = request.POST.get('ctp3')
        ctp4 = request.POST.get('ctp4')
        ctp5 = request.POST.get('ctp5')
        if MainbodyDb.objects.exists():
            messages.error(request, 'Data Existing, please edit')
            return redirect(mainslider)
        else:
            obj = MainbodyDb(Top_Heading=tphd, Main_Heading=mnhd, Sub_Heading=sbhd, Content_P1=ctp1,\
                Content_P2=ctp2, Content_P3=ctp3, Content_P4=ctp4, Content_P5=ctp5)
            obj.save()
            messages.success(request, 'Main Slider added successfully')
            return redirect(mainslider)
    
def displaymainslider(request):
    slider = MainbodyDb.objects.all()
    return render(request, 'store/dispmainsec.html', {'slider': slider})

def editslider(request, SlId):
    slider = MainbodyDb.objects.get(id=SlId)
    return render(request, 'store/editmainsec.html', {'slider': slider})

def updateslider(request, SlId):
    if request.method == 'POST':
        tphd = request.POST.get('tophead')
        mnhd = request.POST.get('mainhead')
        sbhd = request.POST.get('subhead')
        ctp1 = request.POST.get('ctp1')
        ctp2 = request.POST.get('ctp2')
        ctp3 = request.POST.get('ctp3')
        ctp4 = request.POST.get('ctp4')
        ctp5 = request.POST.get('ctp5')
        MainbodyDb.objects.filter(id=SlId).update(Top_Heading=tphd, Main_Heading=mnhd, Sub_Heading=sbhd,\
            Content_P1=ctp1, Content_P2=ctp2, Content_P3=ctp3, Content_P4=ctp4, Content_P5=ctp5)
        messages.success(request, 'Data updated successfully')
        return redirect(displaymainslider)

def deletemainslider(request, SlId):
    slider = MainbodyDb.objects.filter(id=SlId)
    slider.delete()
    messages.error(request, 'Main Slider deleted successfully')
    return redirect(displaymainslider)


# ======================================== Slider section Ends  =====================================================