from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from .models import User


def home(request):
    userid = request.session.get('user_id')
    userinfo = User.objects.filter(pk=userid)
    context = {
        'info': userinfo
    }

    return render(request, 'home.html', context)


def login(request):
    if request.method == "POST":
        postdata = request.POST
        email = postdata.get('email')
        password = postdata.get('password')
        user = User.get_id_by_mail(email)
        massege = None

        if user:
            flag = check_password(password, user.password)
            if flag:
                request.session['user_id'] = user.id
                print(request.session.get('user_id'))
                userid = request.session.get('user_id')
                userinfo = User.objects.filter(id=userid)
                context = {
                    'info': userinfo
                }
                return render(request, 'home.html',context)
            else:
                massege = "password incorrect"
            return render(request, 'login.html', {'mg': massege})
    return render(request, 'login.html')


def registration(request):
    print(request.method)
    if request.method=='POST':
        postdata=request.POST
        f_name=postdata.get('Fname')
        l_name=postdata.get('Lname')
        email=postdata.get('email')
        company_name=postdata.get('Cname')
        phone=postdata.get('phone')
        password=make_password(postdata.get('password'))
        massege = None

        user=User(first_name=f_name,last_name=l_name,email=email,company_name=company_name,phone=phone,password=password)
        if User.objects.filter(email=email).exists():
            massege="you have already register"
            return render(request,'signup.html',{'mg':massege})
        user.save()
        return render(request,'signup.html')

    return render(request,'signup.html')

def search(request):
    if request.method == 'POST':
        postdata = request.POST
        searchvalue = postdata.get('searchvalue')
    userid = request.session.get('user_id')
    userinfo = User.objects.filter(pk=userid)
    context = {
        'info': userinfo,
        'mg': searchvalue
    }

    return render(request, 'home.html', context)


from django.http import JsonResponse
from datetime import timedelta

def index(request):
    return render(request, 'index.html')

# ajax_posting function
def ajax_posting(request):
    if request.is_ajax():
        all_keywords = request.POST.get('all_keywords', None) # getting data from first_name input 
        all_users = request.POST.get('all_users', None)  # getting data from last_name input
        time_range = request.POST.get('time_range', None) 
        if all_keywords and all_users: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON  


