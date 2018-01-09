from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return render(request, 'queryScore/index.html')


def register(request):
    return render(request, "queryScore/register.html")


def showpage(request, user_number, examtype):
    user = get_object_or_404(User, pk=user_number)
    exam_number = ''
    if(examtype == "cet"):
        exam_number = user.CET46exam
    elif(examtype == "psc"):
        exam_number = user.PSCexam
    elif(examtype == "neep"):
        exam_number = user.NEEPexam
    else:
        raise Http404("非法访问")

    #查无此项
    if(exam_number==''):
        return render(request, "queryScore/index.html",{"errorMessage": "查询内容为空"})
    return render(request, "queryScore/showpage.html", {"user_number": user.number, "exam_number": exam_number})


# 查询提交
@csrf_exempt
def onQuery(request):
    user_number = request.POST["username"] #由于html设定的提交是username，但实际是提交的学号所以做出处理
    examtype = request.POST["selProvince"]

    #一级排错
    if(examtype==""):
        render(request, "queryScore/index.html",{"errorMessage":"请选择考试"})

    #user = get_object_or_404(User, pk=user_number)
    try:
        uesr = User.objects.get(pk=user_number)
    except User.DoesNotExist:
        return render(request,"queryScore/index.html", {"errorMessage":"学号没注册"})
    '''
    exam_number = ''
    if(examtype == "cet"):
        exam_number = user.CET46exam
    elif(examtype == "psc"):
        exam_number = user.PSCexam
    elif(examtype == "neep"):
        exam_number = user.NEEPexam
    else:
        raise Http404("非法访问")
    '''
    return HttpResponseRedirect(reverse('queryScore:showpage', args=(user_number, examtype,)))


#提交注册
@csrf_exempt
def onRegister(request):
    user_name = request.POST["username"]
    user_number = request.POST["password"]  #原html文件中此项name为password，为防止混淆故重命名为user_name
    examtype = request.POST["selProvince"]
    exam_number = request.POST["phone_number"]  #同上 为保持一致性

    # 一级排查:检查学号,准考证长度长度
    if(len(user_number)!=10):
        return render(request, "queryScore/register.html", {"errorMessage":"学号有误，请检查"})
    elif(examtype=='cet' and len(exam_number)!=15):
        return render(request, "queryScore/register.html", {"errorMessage":"四六级准考证长度为15位，请核准"})
    elif(examtype=='psc' and len(exam_number)!=13):
        return render(request, "queryScore/register.html",{"errorMessage":"普通话考试准考证长度为13位，请核准"})
    elif(examtype=='neep' and len(exam_number)!=15):
        return render(request, "queryScore/register.html",{"errorMessage":"研究生考试准考证长度为15位，请检查"})
    elif(examtype==""):
        return render(request, "queryScore/register.html",{"errorMessage":"未选择考试"})



    try:
        user = User.objects.get(pk=user_number)
    except User.DoesNotExist:
        user = User.objects.create(number=user_number, name=user_name)
    if(examtype=='cet'):
        user.CET46exam = exam_number
    elif(examtype=='psc'):
        user.PSCexam = exam_number
    elif(examtype=='neep'):
        user.NEEPexam = exam_number
    user.save()
    return HttpResponseRedirect(reverse('queryScore:index'))



