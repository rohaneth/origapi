from django.shortcuts import render
from student.models import Country, City, Student, Company
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CountrySerializer, CitySerializer, StudentSerializer, CompanySerializer

class CountryAPIView(APIView):
    def get(self, request,format = None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

class CityAPIView(APIView):
    def get(self, request,format = None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
class StudentAPIView(APIView):
    def get(self, request,format = None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
class CompanyAPIView(APIView):
    def get(self, request,format = None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
    




def view_django(request):

    return render(request,'django.html',{})



def view_hello(request):

    return render(request,'hello.html',{})




def view_hello_20(request):   

    return render(request,'hello-20.html',{})



def view_record(request):

    stud_record = Student.objects.all()
    city_record = City.objects.all()

    # return render(request,'record.html',{'stud12':stud_record})
    return render(request,'record.html',{'stud12':stud_record,'city12':city_record})


       # return render_to_response('courtcase/report_display.html', {'entry_list': q, 'entry_list1': q1,})


    # return render_to_response('hello.html', {'entry_list': q, 'entry_list1': q1,})





# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# Note that once we’ve done this in all these views, we no longer need to import loader and Ht




# Create your views here.
