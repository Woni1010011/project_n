from django.shortcuts import render, redirect, get_object_or_404
from account_app.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from account_app.forms import UserEditForm
from django.contrib import messages


@csrf_exempt
def login_view(request):
    template = "registration/login.html"
    if request.session.get("user_id"):
        # 이미 로그인된 사용자는 메인 페이지로 리디렉션
        return redirect("main")
    else:
        if request.method == "POST":
            inputId = request.POST.get("id", "")  # 사용자가 입력한 ID
            inputPassword = request.POST.get("password", "")  # 사용자가 입력한 비밀번호

            try:
                user = User.objects.get(user_id=inputId)  # 입력한 ID로 사용자 조회
                if user.user_password == inputPassword:
                    # 로그인에 성공하면 세션에 사용자 ID 저장
                    request.session["user_id"] = user.user_id
                    return redirect("main")  # 로그인 성공 시 리디렉션할 페이지로 이동
                else:
                    context = {"result": "비밀번호가 틀렸습니다"}
            except User.DoesNotExist:
                context = {"result": "존재하지 않는 id입니다"}
        else:
            context = {}  # GET 요청일 경우, 빈 컨텍스트 전달

        return render(request, template, context)


def social_login_view(request):
    return render(request, "registration/login.html")


@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        user_password = request.POST["user_password"]
        password_check = request.POST["password_check"]
        user_name = request.POST["user_name"]
        user_email = request.POST["user_email"]
        user_nick = request.POST["user_nick"]
        user_phone = request.POST["user_phone"]
        user_address = request.POST["user_address"]

        if user_password == password_check:
            user = User.objects.create(
                user_id=user_id,
                user_password=user_password,
                user_name=user_name,
                user_email=user_email,
                user_nick=user_nick,
                user_phone=user_phone,
                user_address=user_address,
            )
            context = {"result": "가입이 완료되었습니다. 로그인해주세요."}
            return redirect("main")
        else:
            context = {"result": "비밀번호가 일치하지 않습니다."}
            return render(request, context)

    return render(request, "registration/signup.html")


def home_page(request):
    return render(request, "home_page.html")


def logout_view(request):
    if request.session.get("user_id"):
        del request.session["user_id"]

    # 로그아웃 후 리디렉션할 페이지로 이동
    return redirect("main")


@login_required
def my_page(request):
    users = User.objects.all()
    print(users)  # 이 줄을 추가하여 콘솔에서 users를 확인해보세요.
    context = {
        "users": users,
    }
    return render(request, "my_page.html", context)


def profile_edit(request):
    if request.method == "POST":
        # 현재 로그인된 사용자의 정보를 가져옵니다.
        form = User(request.POST, request.FILES, instance=users)

        if form.is_valid():
            form.save()
            messages.success(request, "프로필 변경이 완료되었습니다.")
        else:
            messages.error(request, "프로필 입력란을 다시 확인해주세요.")
    else:
        form = User(instance=users)

    context = {
        "form": form,
        "users": users,
    }
    return render(request, "profile_edit.html", context)
