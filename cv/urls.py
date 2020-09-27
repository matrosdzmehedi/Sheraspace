
from django.urls import path
from .views import Home,CvDetailView,CvCreateView,CvListView,CvDeleteView,ChartData,ChartDataAge

urlpatterns = [
   
    path('',Home.as_view(),name='home'),
    path('cv-create/',CvCreateView.as_view(),name='createcv'),
    path('cv-list/',CvListView.as_view(),name='cvlist'),
    path('cv-details/<str:slug>/', CvDetailView.as_view(), name='cv_details'),
    path('cv-delete/<str:slug>/delete/', CvDeleteView.as_view(), name='cvdelete'),
    path('api/data/',ChartData.as_view(),name='apidata'),
    path('api/data/age',ChartDataAge.as_view(),name='apidataage'),

]
