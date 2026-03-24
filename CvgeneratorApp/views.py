from django.shortcuts import render
from .models import Profile

def save_profile(request):

    if request.method == 'POST':   
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        school = request.POST.get('school')
        degree = request.POST.get('degree')
        university = request.POST.get('university')
        summary = request.POST.get('summary')
        previous_work = request.POST.get('previous_work')
        skil = request.POST.get('skil')  

        p = Profile(
            name=name,
            email=email,
            phone=phone,
            school=school,
            degree=degree,
            university=university,
            summary=summary,
            previous_work=previous_work,   
            skil= skil               
        )

        p.save()  

    return render(request, 'CvgeneratorApp/accept.html')
