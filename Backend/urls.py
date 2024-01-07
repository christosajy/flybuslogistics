# ____________________________________________________________________________________________________________________
#                                          BACKEND
# ____________________________________________________________________________________________________________________

from django.urls import path
from Backend import views

urlpatterns = [

    # ADMIN
    path('adlogin/', views.adlogin, name='adlogin'),

    path('loginAdmin/', views.loginAdmin, name='loginAdmin'),

    path('logoutadmin/', views.logoutadmin, name='logoutadmin'),
    
    # HOMEPAGE
    path('backindex/', views.backindex, name='backindex'),
    
    # MODE
    path('modeAdd/', views.modeAdd, name='modeAdd'),

    path('saveMode/', views.saveMode, name='saveMode'),

    path('modeDisplay/', views.modeDisplay, name='modeDisplay'),

    path('modeEdit/<int:ModeId>/', views.modeEdit, name='modeEdit'),

    path('modeUpdate/<int:ModeId>/', views.modeUpdate, name='modeUpdate'),

    path('modeDelete/<int:ModeId>/', views.modeDelete, name='modeDelete'),
    
    # TYPE
    path('typeadd/', views.typeadd, name='typeadd'),

    path('typesave/', views.typesave, name='typesave'),

    path('typedisplay/', views.typedisplay, name='typedisplay'),

    path('type_edit/<int:TypeId>/', views.type_edit, name='type_edit'),

    path('typeUpdate/<int:TypeId>/', views.typeUpdate, name='typeUpdate'),

    path('typedelete/<int:TypeId>/', views.typedelete, name='typedelete'),
    
    # VIDEO
    path('addvideo/', views.addvideo, name='addvideo'),

    path('savevideo/', views.savevideo, name='savevideo'),

    path('displayvideo/', views.displayvideo, name='displayvideo'),

    path('deletevideo/<int:videoid>/', views.deletevideo, name='deletevideo'),
    
    # ADDRESS
    path('addressadd/', views.addressadd, name='addressadd'),

    path('saveaddress/', views.saveaddress, name='saveaddress'),

    path('displayaddress/', views.displayaddress, name='displayaddress'),

    path('editaddress/<int:addressId>/', views.editaddress, name='editaddress'),

    path('updateaddress/<int:addressId>/', views.updateaddress, name='updateaddress'),

    path('deleteaddress/<int:delId>/', views.deleteaddress, name='deleteaddress'),
    
    # USER
    path('displayuser/', views.displayuser, name='displayuser'),

    path('deleteuser/<int:userid>/', views.deleteuser, name='deleteuser'),

    # USER_FEEDBACK
    path('displayuserfeedback/', views.displayuserfeedback, name='displayuserfeedback'),

    path('deleteuserfeedback/<feedId>/', views.deleteuserfeedback, name='deleteuserfeedback'),
    
    # TEAM
    path('teamadd/', views.teamadd, name='teamadd'),

    path('saveteam/', views.saveteam, name='saveteam'),

    path('displayteam/', views.displayteam, name='displayteam'),

    path('teamedit/<int:teamid>/', views.teamedit, name='teamedit'),

    path('teamupdate/<int:teamid>/', views.teamupdate, name='teamupdate'),

    path('deleteteam/<int:teamid>/', views.deleteteam, name='deleteteam'),

    # LOCATION
    path('locationdb/', views.locationdb, name='locationdb'),

    path('locationsave/', views.locationsave, name='locationsave'),

    path('displaylocation/', views.displaylocation, name='displaylocation'), 

    path('editlocation/<int:locId>/', views.editlocation, name='editlocation'),  

    path('updatelocation/<int:locId>/', views.updatelocation, name='updatelocation'),  

    path('locationdelete/<int:locId>/', views.locationdelete, name='locationdelete'),

    # SHIPPING
    path('display_pending_tracking/', views.display_pending_tracking, name='display_pending_tracking'),

    path('edit_pending_tracking/<int:shipId>/', views.edit_pending_tracking, name='edit_pending_tracking'),

    path('update_pending_tracking/<int:shipId>/', views.update_pending_tracking, name='update_pending_tracking'),

    path('delete_pending_tracking/<int:shipId>/', views.delete_pending_tracking, name='delete_pending_tracking'),

    path('mail_page_for_shipping/<int:mailId>/', views.mail_page_for_shipping, name='mail_page_for_shipping'),

    path('send_mail_for_shipping/', views.send_mail_for_shipping, name='send_mail_for_shipping'),
    
    
    # TRACKING
    path('display_pending_warehouse/', views.display_pending_warehouse, name='display_pending_warehouse'),

    path('edit_pending_warehouse/<int:wareId>/', views.edit_pending_warehouse, name='edit_pending_warehouse'),

    path('update_pending_warehouse/<int:wareId>/', views.update_pending_warehouse, name='update_pending_warehouse'),

    path('delete_pending_warehouse/<int:wareId>/', views.delete_pending_warehouse, name='delete_pending_warehouse'),

    path('mail_page_for_warehouse/<int:wareId>/', views.mail_page_for_warehouse, name='mail_page_for_warehouse'),

    path('send_mail_for_warehouse/', views.send_mail_for_warehouse, name='send_mail_for_warehouse'),


    # OTHER_DATAS
    path('datastore_add/', views.datastore_add, name='datastore_add'),

    path('datastore_save/', views.datastore_save, name='datastore_save'),

    path('view_datastore/', views.view_datastore, name='view_datastore'),

    path('delete_datastore/<int:dataid>/', views.delete_datastore, name='delete_datastore'),

    path('weight_save/', views.weight_save, name='weight_save'),

    path('delete_weight/<int:weightid>/', views.delete_weight, name='delete_weight'),

    path('class_save/', views.class_save, name='class_save'),

    path('delete_cls/<int:clsid>/', views.delete_cls, name='delete_cls'),


    # QUOTE
    path('quotedisplay/', views.quotedisplay, name='quotedisplay'),

    path('quotemail/<int:quoteId>/', views.quotemail, name='quotemail'),

    path('quote_send_mail/', views.quote_send_mail, name='quote_send_mail'),

    path('quotedelete/<int:quoteId>/', views.quotedelete, name='quotedelete'),


    # MAIN_SLIDER
    path('mainslider/', views.mainslider, name='mainslider'),

    path('mainslidersave/', views.mainslidersave, name='mainslidersave'),

    path('displaymainslider/', views.displaymainslider, name='displaymainslider'),

    path('editslider/<int:SlId>/', views.editslider, name='editslider'),

    path('updateslider/<int:SlId>/', views.updateslider, name='updateslider'),
    
    path('deletemainslider/<int:SlId>/', views.deletemainslider, name='deletemainslider'),


]
