from django.urls import path

from familyapp.views import member_list, member_detail,index


urlpatterns=[
    path("members/", member_list, name="member_list"),
    # path("members/create", member_detail(), name="create_member"),
    
    
    path("members/<int:pk>/", member_detail, name="member_detail"),
    path("", index, name="index")
    
]