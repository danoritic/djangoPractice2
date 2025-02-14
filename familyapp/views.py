from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from familyapp.models import Member
def member_list(request): 
    MAX_OBJECTS = 20
    member = Member.objects.all()[:MAX_OBJECTS]
    data = {"results": list(member.values("name", "alias", "date_of_birth"))}
    return JsonResponse(data)


def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk) 
    data = {"results": {
            "name": member.name,
            "alias": member.alias,
            "date_of_birth": member.date_of_birth
    }}
    return JsonResponse(data)