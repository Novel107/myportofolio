from django.urls import path
from main.views import (
    show_main, show_experience, show_education, 
    create_education, delete_education, 
    show_xml, show_json, show_xml_by_id, show_json_by_id,
    create_experience, update_experience, delete_experience, show_json_experience # Tambahan buat Experience
) 

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('education/', show_education, name='show_education'),
    
    path('create-education/', create_education, name='create_education'),
    path('delete-education/<uuid:id>/', delete_education, name='delete_education'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    
    path('create-experience/', create_experience, name='create_experience'),
    path('update-experience/<uuid:id>/', update_experience, name='update_experience'),
    path('delete-experience/<uuid:id>/', delete_experience, name='delete_experience'),
    path('json-experience/', show_json_experience, name='show_json_experience'),
]