
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from.models import *

# Create your views here.


def start(request):
    return render(request, 'start.html')


def category(request):
    categories = Category.objects.all()
    print(category)
    contents = {'categories': categories}

    return render(request, 'category.html', contents)


def quiz(request, id):
    quiz_questions = Questions.objects.filter(category=id)[:10]
    questions = []
    datas = {'questions': questions}

    for quiz_question in quiz_questions:
        question = {}
        question['questions'] = quiz_question.question
        question['answers'] = quiz_question.answer
        question['id'] = quiz_question.id
        options = []
        options.append(quiz_question.first_option)
        options.append(quiz_question.second_option)
        options.append(quiz_question.third_option)
        options.append(quiz_question.fourth_option)

        question['options'] = options

        questions.append(question)

    return render(request, 'quiz.html', datas)
# Signup


def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    else:
        first_name = request.POST.get('frstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('psswd')
    # validation resubmission after error message
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email

        }
    # validation
        error_message = None

        student = Student(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password)

        error_message = validate_student(student)

    # saving after the validation
        if not error_message:
            student.password = make_password(student.password)
            student.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'value': values
            }
            return render(request, "signup.html", data)

# validating Customer Signup form :


def validate_student(student):
    error_message = None
    if(not student.first_name):
        error_message = "First Name Required !"
    elif len(student.first_name) < 4:
        error_message = "First Name Must Be 4 Characters Or More !"
    elif(not student.last_name):
        error_message = "Lase Name Required !"
    elif len(student.last_name) < 4:
        error_message = "Last Name Must Be 4 Characters Or More !"
    elif(not student.phone):
        error_message = "Phone Number Required !!"
    elif len(student.phone) < 10:
        error_message = "Phone Number must Be 10 Characters Long "
    elif(not student.email):
        error_message = "Email Is Required"
    elif len(student.email) < 5:
        error_message = "Email Must Be 5 Characters Long"
    elif(not student.password):
        error_message = "Password Field Is Required !"
    elif len(student.password) < 6:
        error_message = "Password Must Be 6 Character Long"
    elif student.is_exist():
        error_message = "E-mail Is Already Registered !"
    return error_message


# Login

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    else:
        email = request.POST.get("email")
        password = request.POST.get("psswd")

        error_message = None
        student = Student.get_student_by_email(email)

        if student:
            user_password = check_password(password, student.password)
            if user_password:
                request.session["student_id"] = student.id
                request.session["email"] = student.email
                return redirect("category")
            else:
                error_message = "E-Mail or Password Is Invalid !"
        else:
            error_message = "E-Mail or Password Is Invalid !"

        return render(request, "login.html", {"error": error_message})


def logout(request):
    request.session.clear()
    return redirect("login")
