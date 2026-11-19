from django.shortcuts import render
from django.http import HttpResponse
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