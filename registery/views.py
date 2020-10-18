from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib import messages
from .forms import DataForm
from .models import DemographicInfo

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'نام کاربری یا کلمه عبور صحیح نیست.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def index(request):
    if request.user.is_authenticated:

        data = DemographicInfo.objects.all()

        if request.method == 'POST':
            form = DataForm(request.POST)
            if form.is_valid():
                if DemographicInfo.objects.filter(national_code=form.cleaned_data['national_code']):
                    messages.error(request, 'رکوردی با این کد ملی موجود است')
                    return redirect('index')
                else:
                    DemographicInfo.objects.create(**form.cleaned_data)
                    messages.success(request, 'اطلاعات با موفقیت ثبت شد.')
                    return redirect('index')

        else:
            form = DataForm()

        context = {
            'form': form,
            'data': data,
        }

        return render(request, 'index.html', context)
    else:
        return redirect('login')

def delete(request, id):
    if request.user.is_authenticated:
        DemographicInfo.objects.get(pk=id).delete()
        messages.success(request, f'رکورد با آیدی {id} حذف شد.')
        return redirect('index')

def edit(request, id):
    if request.user.is_authenticated:
        data = DemographicInfo.objects.all()
        dataRecordToUpdate = DemographicInfo.objects.get(pk=id)

        if request.method == 'POST':
            form = DataForm(request.POST)

            if form.is_valid():
                dataRecordToUpdate.first_name = form.cleaned_data['first_name']
                dataRecordToUpdate.last_name = form.cleaned_data['last_name']
                dataRecordToUpdate.national_code = form.cleaned_data['national_code']
                dataRecordToUpdate.phone_number = form.cleaned_data['phone_number']
                dataRecordToUpdate.cell_number = form.cleaned_data['cell_number']
                dataRecordToUpdate.education_degree = form.cleaned_data['education_degree']

                dataRecordToUpdate.save()

                messages.success(request, f'رکورد با آیدی {dataRecordToUpdate.id} تغییر یافت')
                return redirect('index')
        else:
            form = DataForm(initial = dataRecordToUpdate.__dict__)
            form.edit = True

        return render(request, 'index.html', {
            'form': form,
            'data': data,
            'id': id
        })
