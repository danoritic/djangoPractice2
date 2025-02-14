import datetime
from django.http import HttpResponse, JsonResponse
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
def index(request):
    now = datetime.datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)