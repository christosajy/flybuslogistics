# _____________________________________________________________________________________________________________________
#                                                     FRONTEND
# _____________________________________________________________________________________________________________________

from django.urls import path
from Frontend import views

urlpatterns = [

    # USER FORM
    path('userform/', views.userform, name='userform'),
    path('saveform/', views.saveform, name='saveform'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),

    # SAMPLE BLANK PAGE
    path('blank/', views.blank, name='blank'),

    # MAIN HOME
    path('frontindex/', views.frontindex, name='frontindex'),
    # path('trackrequest/', views.trackrequest, name='trackrequest'),
    path('aboutPage/', views.aboutPage, name='aboutPage'),
    path('servPage/', views.servPage, name='servPage'),
    # SCHEDULE
    path('schedulepage/', views.schedulepage, name='schedulepage'),
    path('shipping/', views.shipping, name='shipping'),
    path('warehouse/', views.warehouse, name='warehouse'),
    # LOGISTICS
    path('logistics/<int:valueId>/', views.logistics, name='logistics'),
    # CONTACT
    path('contactpage/', views.contactpage, name='contactpage'),
    path('savecontactus/', views.savecontactus, name='savecontactus'),
    path('requestquote/', views.requestquote, name='requestquote'),
    path('quotesave/', views.quotesave, name='quotesave'),
    # PROFILE
    path('profile/<user_mail>/', views.profile, name='profile'),
    path('profile_edit/<user_mail>/', views.profile_edit, name='profile_edit'),
    path('profilesave/<user_mail>/', views.profilesave, name='profilesave'),
    # LOCATION
    path('location/', views.location, name='location'),
    # ORDER_STATUS
    path('shipment_status_page/<unique_id>/', views.shipment_status_page, name='shipment_status_page'),
]
