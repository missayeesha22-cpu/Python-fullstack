from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student_table
from .serializers import StudentSerializer
# Create your views here.
def home(request):
    data={
          'name':"xyz",
          'age':18,
         'department':"bca"
    }
    marks=[100,96,97]
    return render(request,'home.html',{'data':data,'marks':marks})
def about(request):
        return render(request, 'about.html')
def contact(request):
       return render(request,'contact.html')   
def form(request):
      return render(request,' student_from.html')


from django.shortcuts import render

def student_form(request):

    if request.method == "POST":

        reg_no = request.POST.get('reg_no')
        name = request.POST.get('name')
        email = request.POST.get('email')
        marks = request.POST.get('marks')
        dob = request.POST.get('dob')

        student = {
            'reg_no': reg_no,
            'name': name,
            'email': email,
            'marks': marks,
            'dob': dob
        }

        return render(request, 'student_form.html', {
            'student': student
        })

    return render(request, 'student_form.html')

def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            return render(request, 'login.html', {
                'success': True,
                'username': username
            })

        else:
            return render(request, 'login.html', {
                'error': 'Please enter username and password'
            })

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    return render(request, 'logout.html')

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import student_table
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_api(request):

    if request.method == 'GET':
        students = student_table.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )