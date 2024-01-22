from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from interviewer.models import Question, Category, Test, Contact
from django.http import HttpResponse
from openpyxl import Workbook
from django.utils import timezone
from bs4 import BeautifulSoup
from django.core.mail import send_mail
from djangoProject.settings import EMAIL_HOST_USER


# Create your views here.
def index(request):
    context = {
        "questions": Question.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "homePage/index.html", context)


"""
def questions(request):
    context = {
        "questions": Question.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "questionsPage/questions.html", context)
"""


class PostListView(ListView):
    model = Question
    template_name = 'questionsPage/questions.html'
    context_object_name = 'questions'
    extra_context = {'categories': Category.objects.all()}
    ordering = ['-date_posted']


class PostCreateView(CreateView):
    model = Question
    extra_context = {'categories': Category.objects.all()}
    template_name = 'questionsPage/question_form.html'
    fields = ['title', 'description', 'question_title', 'test_name',
              'department_name', 'question_description', 'correct_answer']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def question_details(request, slug):
    questions = Question.objects.get(slug=slug)
    categories = Category.objects.all()
    tests = Test.objects.all()

    return render(request, "questionDetailPage/questionDetails.html", {
        "question": questions,
        "categories": categories,
        "tests": tests,
    })


def questions_by_category(request, slug):
    context = {
        "questions": Question.objects.filter(is_active=True, category__slug=slug).order_by('-date_posted'),
        "categories": Category.objects.all(),
        "selected_category": slug,


    }
    return render(request, "questionsPage/questions.html", context)


# def userprofile(request):
#     context = {
#
#         "questions": Question.objects.all()
#     }
#     return render(request, "profile.html", context)

#     path("export_to_csv", views.export_to_csv, name="export_to_csv"),
"""
def export_to_csv(request):
    questions = Question.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachement; filename=question_export.csv'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Title', 'Description', 'Date_posted', 'Category', 'Question Title',
                     'Test Name', 'Department Name', 'Question Description', 'Question Number'])
    question_fields = questions.values_list('id', 'title', 'description', 'date_posted', 'category', 'question_title',
                                            'test_name', 'department_name', 'question_description', 'question_number')
    for question in question_fields:
        writer.writerow(question)
    return response
    """

def export_questions_to_xlsx(request):
    questions = Question.objects.all().values(
        'id', 'title', 'description', 'date_posted', 'category',
        'question_title', 'test_name', 'department_name',
        'question_description', 'question_number'
    )

    wb = Workbook()
    ws = wb.active

    headers = [
        'id', 'title', 'description', 'date_posted', 'category',
        'question_title', 'test_name', 'department_name',
        'question_description', 'question_number'
    ]
    ws.append(headers)

    for question in questions:
        # Remove HTML tags from the 'description' field
        description_cleaned = BeautifulSoup(question['description'], "html.parser").get_text()

        # Convert datetime fields to the appropriate format
        row_data = []
        for field in headers:
            if field == 'description':
                row_data.append(description_cleaned)
            elif isinstance(question[field], timezone.datetime):
                row_data.append(question[field].replace(tzinfo=None))
            else:
                row_data.append(question[field])
        ws.append(row_data)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="questions.xlsx"'
    wb.save(response)

    return response

def completetest(request):
    context = {
        "categories": Category.objects.all(),
    }
    return render(request, "completeTest.html",context)

class QuestionSearchView(ListView):
    model = Question
    template_name = 'questionsPage/questions.html'
    context_object_name = 'questions'
    extra_context = {'categories': Category.objects.all()}

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Question.objects.filter(Q(title__icontains=query) | Q(department_name__icontains=query)).order_by(
            '-date_posted')



def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        send_mail(
            'interviewer Customer Support',
            'Dear ' + name + ', \nThank you for reaching out to us. We have received your request and are currently processing it. Our Customer Service Team will promptly update you on the status as soon as possible.' +
            '\n\n\nBest Regards,' +
            '\ninterviewer Customer Support Team',
            EMAIL_HOST_USER,
            [email],
        )

        return render(request, 'homePage/index.html', {})
    else:
        return render(request, 'homePage/index.html', {})

