from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def hello(request):
    return HttpResponse("<h1>Salom, Dunyo</h1>")
def talabalar(request):
    if request.method == 'POST':
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            Talaba.objects.create(
                ism = forma.cleaned_data.get('name'),
                kurs = forma.cleaned_data.get('nums_of_books'),
                kitob_soni = forma.cleaned_data.get('course')
            )
        return redirect('/talabalar/')
    soz = request.GET.get('qidirish')
    if soz is None:
       t = Talaba.objects.all()
    else:
        t = Talaba.objects.filter(ism__contains=soz)
    data = { 'talabalar_ismlar':t,
             'forma':TalabaForm()}
    return render(request, 'talabalar.html',data)

def salomlash(request):
    return render(request, 'hello.html')
def recordlar(request):
    if request.method == 'POST':
        form = recordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/recordlar/')
    soz = request.GET.get('qidirish')
    if soz is None:
        rec = Record.objects.all()
    else:
        rec = Record.objects.filter(talaba__ism__contains=soz)
    data = {'recordlar': rec,
            'talabalar':Talaba.objects.all(),
            'kitob':kitob.objects.all(),
            'admin':Admin.objects.all(),
            'forma':recordForm()

            }
    return render(request, 'record.html',data)

def kitobla(request,son):
    data = {'kitoblar':kitob.objects.get(id=son)}
    return render(request, 'kitobi.html', data)
def boshsahifa(request):
    return render(request,'boshsahifa.html')
def ismlar(request):
    data = {'ism':Talaba.objects.filter(ism__contains='a')}
    return render(request,'ismida.html',data)
def bitta_talaba(request,son):
    if request.method == 'POST':
        if request.POST.get('b') == 'on':

            qiymat = True
        else:
            qiymat = False
        Talaba.objects.filter(id=son).update(
           ism = request.POST.get('i'),
           kurs = request.POST.get('k'),
           kitob_soni = request.POST.get('k_s'),
           bitiruvchi= qiymat


        )
        return redirect('/talabalar/')
    data = {'talaba':Talaba.objects.get(id=son)}
    return render(request, 'bitta_talaba.html', data)
def mualliflarr(request):
    if request.method == 'POST':
        qidiruv_soz = request.POST.get('qidirish')
        mualliflar = Muallif.objects.filter(ism__contains=qidiruv_soz) | Muallif.objects.filter(jins=qidiruv_soz)
        data = {
            'mualliflar':mualliflar
        }
        return render(request,'muallif_hamma.html',data)
    else:
        data = {'mualliflar': Muallif.objects.all()}
        return render(request, 'muallif_hamma.html',data)


def bitta_muallif(request,son):
    if request.method == 'POST':
        if request.POST.get('t') == 'on':

            qiymat = True
        else:
            qiymat = False
        Muallif.objects.filter(id=son).update(
            ism = request.POST.get('i'),
            jins = request.POST.get('jins'),
            kitob_soni = request.POST.get('k_s'),
            tugilgan_yil = request.POST.get('yil'),
            tirik =qiymat

        )
        return redirect('/mualliflar/')
    data = {'muallif':Muallif.objects.get(id=son),
            'm':Muallif.objects.all()
            }

    return render(request, 'tanlangan_muallif.html', data)
def kitoblari(request):
    soz = request.GET.get('qidirish')
    if request.method == 'POST':



        form = kitobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/kitoblar/')

    if soz is None:
        kt = kitob.objects.all()
    else:
        kt = kitob.objects.filter(nom__contains=soz)

    data = {'kitoblar': kt,
            'mualliflar':Muallif.objects.all(),
            'forma': kitobForm()
            }
    return render(request,  'kitob.html', data)
def talaba_ochir(request, son):
    talaba = Talaba.objects.get(id=son)
    talaba.delete()

    return redirect('/talabalar/')
def muallif_ochir(request, son):
    muallif = Muallif.objects.get(id=son)
    muallif.delete()

    return redirect('/mualliflar/')
def record_ochir(request,son):
    record = Record.objects.get(id=son)
    record.delete()

    return redirect('/recordlar/')
def kitob_ochir(request,son):
    kitobla = kitob.objects.get(id=son)
    kitobla.delete()
    return redirect('/kitoblar/')



def tanlangan_record(request,son):
    if request.method =='POST':
        if request.POST.get('q') == 'on':

            qiymat = True
        else:
            qiymat = False
        Record.objects.filter(id=son).update(
            qaytardi = qiymat,
            qaytargan_sana = request.POST.get('q_s')
        )
        return redirect('/recordlar/')

    data = {'record':Record.objects.get(id=son)}

    return render(request, 'tanlangan_record.html', data )
def tanlangan_admin(request, son):
    if request.method == 'POST':

        return redirect('/adminlar/')
    data = {
        'admin':Admin.objects.get(id=son),

    }
    return render(request,'tanlangan_admin.html', data)
def tanlangan_kitobla(request,son):
    if request.method =='POST':
        kitob.objects.filter(id=son).update(
            nom =request.POST.get('n'),
            sahifa =request.POST.get('s'),
            janr =request.POST.get('j'),
            muallif = Muallif.objects.get(id=request.POST.get('m'))
        )
        return redirect('/kitoblar/')

    data = {'kitob':kitob.objects.get(id=son),
            'mualliff':Muallif.objects.all()
            }
    return render(request, 'tanlangan_kitob.html',data)

def muallif_qosh(request):
    data = {'forma':muallifForm()}
    if request.method == 'POST':
        form = muallifForm(request.POST)
        print(form)
        if form.is_valid():
            print('valid')
            form.save()
        return redirect('/mualliflar/')
    else:

        return render(request,'muallif_qoshish.html',data)

def adminlar(request):
    if request.method == 'POST':
        form = adminForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/adminlar/')
    soz = request.GET.get('qidirish')
    if soz is None:
        ad = Admin.objects.all()
    else:
        ad= Admin.objects.filter(ism__contains=soz)
    data = {'adminlar':ad,
            'forma':adminForm}
    return render(request,'admin.html',data)
def adminlar_ochir(request,son):
    Admin.objects.filter(id=son).delete()
    return redirect('/adminlar/')




