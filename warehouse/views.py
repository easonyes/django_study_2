from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from django.urls import reverse
from django.core import serializers
from django.forms.models import model_to_dict
import json
from warehouse.models import *

# Create your views here.

"""

def index(request):
    # 查看所有礼品信息
    #lists = warehouse.objects.all()
    # 返回主页，并将信息在主页显示
    #return render(request, 'index.html', {'presents':lists})


def login(request):
    if request.method == 'POST':
        name = request.POST['empname']
        psd = request.POST['emppassword']
        emploee = Emploee.objects.filter(empname=name, emppassword=psd )
        context = {
            'log_status': 0,
            'order': 0
        }
        request.session['IS_LOGIN'] = False
        if emploee:
            context['log_status'] = 1
            context['order'] = emploee.emporder
            request.session['IS_LOGIN'] = True
            return render(request, request.path, context)
        else:
            return render(request, request.path, context)
    else:
        return render(request, request.path, context='')

def add_page(request):
    return render(request, 'adddata.html', {'title': '添加', 'urlname': 'add_data', 'warehouse': ''})


def add_data(request):
    iname = request.POST['name']
    iintroduction = request.POST['introduction']
    iondate = request.POST['ondate']
    istorenum = request.POST['storenum']
    ioff = request.POST['off']
    offcost = request.POST['offcost']
    if offcost:
        ioffcost = float(offcost)
    else:
        ioffcost = 0
    hot = request.POST['hot']
    if hot:
        ihot = int(hot)
    else:
        ihot = 0
    iprice = request.POST['price']
    obj = warehouse(name=iname, introduction=iintroduction, ondate=iondate, storenum=int(istorenum), status=2, off=int(ioff),
                    offcost=ioffcost, hot=ihot, price=int(iprice))
    obj.save()
    return redirect(reverse('index'))
"""

#undone
def login(request):
    context = {
        'log_status': 0
    }
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        employee = Employee.objects.filter(empname=name , emppassword=password)

        if employee:
            request.session['IS_LOGIN'] = True
            request.session['EMPLOYEE_ID'] = employee[0].id
            request.session['ORDER'] = employee[0].emporder
            conx = serializers.serialize("json", employee)
            conx2 = '{"log_status":1, "employee": ' + conx + '}'
            return HttpResponse(conx2, content_type="application/json")
        else:
            return HttpResponse(json.dumps(context), content_type="application/json")

#undone
def logout(request):
    context={
        'IS_LOGOUT': 0
    }
    if('IS_LOGIN' in request.session and 'EMPLOYEE_ID' in request.session):
        del request.session['IS_LOGIN']
        del request.session['EMPLOYEE']
        context['IS_LOGOUT'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponse(json.dumps(context), content_type="application/json")

#undone
def register(request):
    return

#undone
"""
gifts
返回仓库中的礼品信息，如果是仓库管理员，就返回自己仓库的信息，如果是普通员工，就返回所有礼品信息
method: GET
"""
def gifts(request):
    return

#undone
"""
add
添加一个礼品，仓库管理员可操作，但添加时其默认状态值为0，即待审核状态
method：POST
"""
def add(request):
    return

#undone
"""
modify
修改一个礼品的信息，仓库管理员可操作，但不可修改其状态值
method：PUT
"""

#undone
"""
delete
删除一个礼品，仅仓库管理员可操作
method：DELETE
"""

#undone
"""
sell
修改一个礼品的状态值，即上架或下架该礼品，仅普通员工可操作
method：PUT
"""

