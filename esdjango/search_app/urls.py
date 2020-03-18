from django.urls import path
import views

urlpatterns = [
    path('',views.SearchView.as_view())
]