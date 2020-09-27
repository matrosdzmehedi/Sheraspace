from .models import PersonCv
from django.views.generic import TemplateView,DetailView,ListView,DeleteView,CreateView
from django.urls import reverse_lazy
from.forms import MyCvForm
from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response




class Home(TemplateView):
    template_name = 'cv/dashboard.html'

  


class CvCreateView(CreateView):
    model = PersonCv
    template_name = 'cv/cvnew.html'
    form_class=MyCvForm


    def post(self,request,*args, **kwargs):
        form = MyCvForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('cvlist')
    


class CvDetailView(DetailView):
    model = PersonCv
    template_name = 'cv/cvdetails.html'


class CvListView(ListView):
    model = PersonCv
    template_name = 'cv/listview.html'

class CvDeleteView(DeleteView):
    model = PersonCv
    template_name = 'cv/cvdelete.html'
    success_url = reverse_lazy('cvlist')





class ChartData(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self,request):
       
        dk=PersonCv.objects.filter(district='Dhaka').count()
        brs=PersonCv.objects.filter(district='Barisal').count()
        ctg=PersonCv.objects.filter(district='Chittagong').count()
        kh=PersonCv.objects.filter(district='Khulna').count()
        msh=PersonCv.objects.filter(district='Mymensingh').count()
        rj=PersonCv.objects.filter(district='Rajshahi').count()
        rp=PersonCv.objects.filter(district='Rangpur').count()
        sy=PersonCv.objects.filter(district='Sylhet').count()

        labels = ['Barisal','Chittagong','Dhaka','Khulna','Mymensingh','Rajshahi','Rangpur','Sylhet']
        data = [brs,ctg,dk,kh,msh,rj,rp,sy]

        datas = {
                "labels": labels,
                "data": data,
        }

        return Response(datas)


class ChartDataAge(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self,request):
       
        mtf=PersonCv.objects.filter(gender='Male',age__lte=25 ).count()
        ftf=PersonCv.objects.filter(gender='Female',age__lte=25).count()
        mtr=PersonCv.objects.filter(gender='Male',age__gte=26 ).count()
        ftr=PersonCv.objects.filter(gender='Female',age__gte=26).count()
       
        labels = ['21-25','26-30']
        data = [[mtf,ftf],[mtr,ftr]]
     
        datas = {
                "labels": labels,
                "data": data,
        }

        return Response(datas)

