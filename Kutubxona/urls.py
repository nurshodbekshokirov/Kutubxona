
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', hello),
    path('salomlash/', salomlash),
    path('', boshsahifa),
    path('kitob/<int:son>', kitobla),
    path('tanlangan_kitob/<int:son>/', tanlangan_kitobla),
    path('tanlangan_admin/<int:son>/', tanlangan_admin),
    path('talabalar/', talabalar),
    path('ismlar/', ismlar),
    path('talaba/<int:son>/',bitta_talaba),
    path('mualliflar/', mualliflarr),
    path('muallif/<int:son>/', bitta_muallif),
    path('kitoblar/', kitoblari),
    path('recordlar/', recordlar),
    path('talaba_ochirish/<int:son>/',talaba_ochir),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('muallif_qosh/', muallif_qosh),
    path('record_ochir/<int:son>/', record_ochir),
    path('tanlangan_record/<int:son>/',tanlangan_record),
    path('kitob_ochir/<int:son>/',kitob_ochir),
    path('adminlar/',adminlar),
    path('adminlar_delete/<int:son>/',adminlar_ochir),











]
