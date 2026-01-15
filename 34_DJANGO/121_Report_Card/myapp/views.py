from django.shortcuts import render,redirect
from myapp.models import *
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

# Paginator is a class that provides pagination functionality for a queryset, allowing you to split large datasets 
# into smaller, manageable pages.  link: https://docs.djangoproject.com/en/5.2/topics/pagination/
from django.core.paginator import Paginator

from django.db.models import Sum

# Create your views here.

def index(request):
    allstudent = Student.objects.all()
    # return render(request, 'index.html', {"students":allstudent})

    
    # Paginator takes two arguments: the queryset to paginate and the number of items per page.
    # In this case, we are paginating the 'allstudent' queryset and displaying 5 students per page.
    # The 'page_number' variable retrieves the current page number from the request's GET parameters    
    paginator = Paginator(allstudent, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {"students":page_obj})

def marksheet(request):
    studentid = int(request.GET['id'])
    # print(studentid)
    allstudent = Marks.objects.filter(student_id=studentid)
    # print(allstudent)
    # sum=0
    # for st in allstudent:
    #     # print(st.marks)
    #     sum += st.marks
    # # print(sum)


    
    sum = allstudent.aggregate(total = Sum("marks"))
    # print(sum)
    rankstudents = Student.objects.annotate(total = Sum('marks__marks')).order_by("-total")
    count = 0
    for ranks in rankstudents:
        count += 1
        if ranks.id == studentid:
            # print(ranks.total, ranks.id, count)
            break
            
    return render(request, 'marksheet.html', {"students":allstudent, "sum":sum, "count":count})


# Gmail sending code 
# link:- https://www.geeksforgeeks.org/python/setup-sending-email-in-django-project/
def send_mail_page(request):
    id = int(request.GET['id'])
    
    allstudent = Marks.objects.filter(student_id=id)
    # print(allstudent[0].student.email)

    sum = allstudent.aggregate(total = Sum("marks"))
    
    rankstudents = Student.objects.annotate(total = Sum('marks__marks')).order_by("-total")
    count = 0
    for ranks in rankstudents:
        count += 1
        if ranks.id == id:
            # print(ranks.total, ranks.id, count)
            break

    subject = "Report Card"
    from_email = settings.EMAIL_HOST_USER
    to_email = [allstudent[0].student.email] 

    html_content = render_to_string('marksheet.html', {"students":allstudent, "sum":sum, "count":count})

    email = EmailMultiAlternatives(subject, '', from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    email.send()

    return redirect("index")