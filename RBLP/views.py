from django.shortcuts import redirect, render
from .models import Gender, User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.

def index_gender(request):
    genders = Gender.objects.all() #SELECT * FRom genders
    
    context = {
        'genders': genders
    }
    
    return render(request, 'gender/index.html', context)

def create_gender(request):
    return render(request, 'gender/create.html')

def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender) # INSERT INTO genders(gender) VALUES(gender)
    messages.success(request, 'Gender successfully saved!')
    
    return redirect('/genders')

def show_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)# SELECT *FROM genders WHERE gender_id = gender_id
    
    context = {
        'gender': gender,
    }
    
    return render(request, 'gender/show.html', context)

def edit_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)# SELECT *FROM genders WHERE gender_id = gender_id
    
    context = {
        'gender': gender,
    }
    return render(request, 'gender/edit.html', context)

def update_gender(request, gender_id):
    gender = request.POST.get('gender')
    
    
    Gender.objects.filter(pk=gender_id).update(gender=gender) #UPDATE genders SET gender = gender WHERE gender)id = gender_id
    messages.success(request, 'Gender succesfully updated')
    return redirect('/genders')


def delete_gender(request,gender_id):
    gender = Gender.objects.get(pk=gender_id)# SELECT *FROM genders WHERE gender_id = gender_id
    
    context = {
        'gender': gender,
    }
    return render(request, 'gender/delete.html', context)

def destroy_gender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete()# DELETE FROM gender WHERE gender_id = gender_id
    messages.success(request,"Gender successfully deleted.")
    
    return redirect('/genders')

def index_user(request):
    user = User.objects.select_related()
    
    context = {
        'users': user,
    }
    
    return render(request, 'user/index.html', context)


def create_user(request):
    genders = Gender.objects.all() #SELECT * FROM genders
    
    context = {
        'genders': genders
    }
    
    return render(request, 'user/create.html', context)
def show_user(request, user_id):
    users = User.objects.select_related('gender').get(pk=user_id)
    
    context = {
        'user': users
    }
    
    return render(request, 'user/show.html', context)

def edit_user(request, user_id):
    users = User.objects.select_related('gender').get(pk=user_id)
    genders = Gender.objects.all()
    
    context = {
        'user': users,
        'genders':genders,
    }
    
    return render(request, 'user/edit.html', context)

def update_user(request, user_id):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    address = request.POST.get('address')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    username = request.POST.get('username')
    genderId = request.POST.get('gender_id')
    
    User.objects.filter(pk=user_id).update(first_name=firstName, middle_name=middleName, last_name=lastName, address=address, age=age, birth_date=birthDate, username=username, gender_id=genderId) 
    return redirect("/users")

def delete_user(request,user_id):
    users = User.objects.select_related('gender').get(pk=user_id)
    
    context = {
        'user': users
    }

    return render(request, 'user/delete.html', context)

def destroy_user(request, user_id):
    User.objects.filter(pk=user_id).delete()
    messages.success(request,"User successfully deleted.")
    
    return redirect('/users')

def store_user(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    address = request.POST.get('address')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    genderId = request.POST.get('gender_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirm_password')
    
    if password == confirmPassword:
        encryptedPassword = make_password(password)
        
        User.objects.create(first_name=firstName, middle_name=middleName, last_name=lastName, address=address, age=age, birth_date=birthDate, 
        gender_id=genderId, username=username, password=encryptedPassword)
        
        messages.success(request, 'User successfully saved.')
        
        return redirect('/users')
    else:
        messages.error(request, 'Password do not match.')
        return redirect('/user/create')
    