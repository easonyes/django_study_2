from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, QueryDict
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

# undone
# not test
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

# undone
# not test
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

# undone
# not test
def register(request):
    return

# done
# not test
"""
gifts
返回仓库中的礼品信息，如果是仓库管理员，就返回自己仓库的信息，如果是普通员工，就返回所有礼品信息
method: GET
"""
def gifts(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    context = {
        'error': 0
    }
    if(not employee) or ('EMPLOYEE_ID' not in request.session) or ('IS_LOGIN' not in request.session) \
        or (request.session['EMPLOYEE_ID' != employee_id]):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'GET':
        employee = employee[0]
        if employee.emporder == 1:
            presents = Present.objects.all()
            '''
            presents = []
            for p in present:
                presents.append(p)
            '''
            conx = serializers.serialize("json", presents)
            return HttpResponse(conx, content_type="application/json")
        elif employee.emporder == 2:
            depots = Depot.objects.filter(manager=employee.id)
            presents = []
            for depot in depots:
                present = Present.objects.filter(pdepot=depot.id)
                presents.append(present)
            conx = serializers.serialize("json", presents)
            return HttpResponse(conx, content_type="application/json")
            # present = Present.objects.filter(pdepot=)
        else:
            context['error'] = 2
            return HttpResponse(json.dumps(context), content_type="application")
    return

# undone
# not test
"""
add
添加一个礼品，仓库管理员可操作，但添加时其默认状态值为0，即待审核状态
method：POST
"""
def add(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    context = {
        'error': 0
    }
    if (not employee) or ('EMPLOYEE_ID' not in request.session) or ('IS_LOGIN' not in request.session) \
        or (request.session['EMPLOYEE_ID'] != employee_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'POST':
        pname = request.POST['name']
        introduction = request.POST['introduction']
        on_date = request.POST['on_date']
        store_num = request.POST['store_num']
        status = 0
        cost = request.POST['cost']
        hot = request.POST['hot']
        off = request.POST['off']
        off_cost = request.POST['off_cost']
        url = request.POST['url']
        pdepot = request.POST['pdepot']
        depots = Depot.objects.all()
        pdepots = []
        for depot in depots:
            did = depot.id
            pdepots.append(did)
        if pdepot not in pdepots:
            context['error'] = 3
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            obj = Present(name=pname, introduction=introduction, on_date=on_date, store_num=store_num,
                          status=status, cost=cost, hot=hot, off=off, off_cost=off_cost, url=url, pdepot=pdepot)
            obj.save()
            return redirect(reverse('index'))
    return

# undone
# not test
"""
modify
修改一个礼品的信息，仓库管理员可操作，但不可修改其状态值
method：PUT
"""

# undone
# not test
"""
delete
删除一个礼品，仅仓库管理员可操作
method：DELETE
"""

# undone
# not test
"""
sell
修改一个礼品的状态值，即上架或下架该礼品，仅普通员工可操作
method：PUT
"""

