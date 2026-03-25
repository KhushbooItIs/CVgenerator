from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import  HttpResponse
import io

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
        return redirect('dashboard')

    return render(request, 'CvgeneratorApp/modern_create_profile.html')

def resume(request,id):
    user_profile=Profile.objects.get(id=id)
    return render(request, 'CvgeneratorApp/resume.html',{'user_profile':user_profile})

def dashboard(request):
    resumes=Profile.objects.all()
    return render(request, 'CvgeneratorApp/modern-dashboard.html',{'resumes':resumes})

def download_resume(request,id):
    user_profile=get_object_or_404(Profile,id=id)
    template_path='CvgeneratorApp/download_resume.html'
    context={'profile':user_profile}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={user_profile.name}_CV.pdf'

    pisa_status = pisa.CreatePDF(io.BytesIO(html.encode('UTF-8')), dest=response,encoding='UTF-8')

    if pisa_status.err:
        return HttpResponse('Error generating PDF',status=500)

    return response

