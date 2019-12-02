from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from dateutil import parser
from . import models
import re
# Create your views here.
def is_number(num):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False

def index(request):
    pass
    return  HttpResponse("Hello, world. Fuck this database!")

def login(request):
    if request.session.get('is_login',None):
        message = "不允许重复登陆！"
        return HttpResponse({'message':message})
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        hobbies = request.POST.getlist('uhobbies')
        #return render(request, 'login/index.html', {'hobbies': hobbies})

        try:
            user = models.User.objects.get(username = username)
        except:
            message = "用户不存在"
            return HttpResponse({'message':message})

        if user.password == password:
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            request.session['permisson'] = user.permission
            return redirect('/index/')
        else:
            message = "密码错误"
            return HttpResponse({'message':message})
    return render(request,'login/login.html')

# def Bike_query(request):
#     if request.method == "POST":
#         bike_id = request.POST.get('BikeId')
#         company_name = request.POST.get('CompanyName')
#         try:
#             bikes = models.Bike.objects.filter(CompanyName=company_name)
#         except:
#             message = "数据不存在"
#             return render(request,'login/Bike_query.html',{'message': message})
#         num = len(bikes)
#         data = {}
#         data['bikes'] = bikes
#         data['num'] = num
#         return render(request, 'login/Bike_query.html', data)
#     return render(request,'login/Bike_query.html')

def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")


def Bike_query(request):
    if request.method == "POST":
        bike_id = request.POST.get('BikeId')
        company_name = request.POST.get('CompanyName')
        bikes = models.Bike.objects.filter(CompanyName=company_name)
        print(bikes)
        if bikes.exists():
            num = len(bikes)
            data = {}
            data['bikes'] = bikes
            data['num'] = num
            return render(request, 'login/Bike_query.html', data)
        else:
            message = "数据不存在"
            return render(request, 'login/Bike_query.html', {'message': message})
    bikes1 = models.Bike.objects.all()[:50]
    if bikes1.exists():
        data = {}
        data['bikes'] = bikes1
        return render(request, 'login/Bike_query.html', data)
    else:
        message = "无维修中心记录！"
        return render(request, 'login/Bike_query.html', {'message': message})


def Center_query(request):
    center = models.Center.objects.all()
    if center.exists():
        data = {}
        data['center'] = center
        return render(request, '', data)
    else:
        message = "无维修中心记录！"
        return render(request, '', {'message': message})


def Center_alter(request):
    if request.session.get('is_login',None):
        return redirect('/login/')
    else:
        if request.session.get('permisson') != 3:
            message = "无权限执行此操作！"
            return render(request,'',{'message':message})
    if request.method == "POST":
        center_id = request.POST.get('CenterId')
        location = request.POST.get('Location')
        brake_num = request.POST.get('BrakeNum')
        wheel_num = request.POST.get('WheelNum')
        pedal_num = request.POST.get('PedalNum')
        saddle_num = request.POST.get('SaddleNum')
        qrcode_num = request.POST.get('QRcodeNum')
        lock_num = request.POST.get('LockNum')
        models.Center.objects.filter(CenterId = center_id).update(BrakeNum=brake_num,WheelNum=wheel_num,PedalNum=pedal_num,SaddleNum=saddle_num,QRcodeNum=qrcode_num,LockNum=lock_num)
        data = {}
        data['Center'] = models.Center.objects.all()
        return render(request,'',data)


#------------------------------------------------------------------------------------------------


#增加骑行记录
def CyclingRecords_add(request):
    if request.method == "POST":
        data = {}
        data['BikeId'] = request.POST.get('bike_id')
        data['UserId'] = request.POST.get('user_id')
        data['StartTime'] = request.POST.get('start_time')
        data['EndTime'] = request.POST.get('end_time')
        data['LocationX'] = (request.POST.get('location_x'))
        data['LocationY'] = (request.POST.get('location_y'))
        try:
            data['StartTime'] = parser.parse(data['StartTime'])
            data['EndTime'] = parser.parse(data['EndTime'])
        except:
            message = "时间格式错误！"
            return render(request, 'login/CyclingR_add.html',{'message':message})
        if data['BikeId'].isdigit() and data['UserId'].isdigit() and is_number(data['LocationX']) and is_number(data['LocationY']):
            try:
                bike = models.Bike.objects.get(BikeId=data['BikeId'])
                models.CyclingRecords.objects.create(BikeId=bike,UserId=data['UserId'],LocationX=data['LocationX'],LocationY=data['LocationY'],StartTime=data['StartTime'],EndTime=data['EndTime'])
                return render(request, 'login/CyclingR_add.html',{'data':data})
            except:
                message = "不存在该编号的共享单车！"
                return HttpResponse({'message':message})
        else:
            message = "填写的数据格式有误！"
            return render(request, 'login/CyclingR_add.html', {'message': message})
    return render(request, 'login/CyclingR_add.html')


# 查询骑行记录
def CyclingRecords_query(request):
    if request.method == "POST":
        query_dict = {}
        BikeId = request.POST.get('bike_id')
        UserId = request.POST.get('user_id')
        StartTime = request.POST.get('start_time')
        EndTime = request.POST.get('end_time')
        LocationX = (request.POST.get('location_x'))
        LocationY = (request.POST.get('location_y'))
        if StartTime or EndTime != None :
            try:
                StartTime = parser.parse(StartTime)
                EndTime = parser.parse(EndTime)
                query_dict['StartTime'] = StartTime
                query_dict['EndTime'] = EndTime
            except:
                message = "时间格式错误！"
                return render(request, 'login/CyclingR_query.html',{'message':message})
        if BikeId != None:
            query_dict['BikeId'] = BikeId
            if not BikeId.isdigit():
                message = "填写的数据格式有误！"
                return render(request, 'login/CyclingR_query.html', {'message': message})
        if UserId != None:
            query_dict['UserId'] = UserId
            if not UserId.isdigit():
                message = "填写的数据格式有误！"
                return render(request, 'login/CyclingR_query.html', {'message': message})
        if LocationX != None:
            query_dict['LocationX'] = LocationX
            if not is_number(LocationX):
                message = "填写的数据格式有误！"
                return render(request, 'login/CyclingR_query.html', {'message': message})
        if LocationY != None:
            query_dict['LocationY'] = LocationY
            if not is_number(LocationY):
                message = "填写的数据格式有误！"
                return render(request, 'login/CyclingR_query.html', {'message': message})
        queryset = models.CyclingRecords.objects.filter(**query_dict)
        print(queryset)
        if len(queryset) == 0:
            message = "没有符合条件的数据！"
            return render(request,'login/CyclingR_query.html',{'message':message})
        else:
            data = {}
            data['queryset'] = queryset
            return render(request, 'login/CyclingR_query.html', data)
            # return render(request,'login/CyclingR_query.html',{'queryset':queryset})
    queryset = models.CyclingRecords.objects.all()
    if queryset.exists():
        data = {}
        data['queryset'] = queryset
        return render(request, 'login/CyclingR_query.html', data)
    else:
        message = "无维修中心记录！"
        return render(request, 'login/CyclingR_query.html', {'message': message})

#删除骑行记录
def CyclingRecords_del(request):
    if request.method == "POST":
        BikeId = request.POST.get('bike_id')
        UserId = request.POST.get('user_id')
        StartTime = request.POST.get('start_time')
        EndTime = request.POST.get('end_time')
        LocationX = (request.POST.get('location_x'))
        LocationY = (request.POST.get('location_y'))
        result = models.CyclingRecords.objects.filter(BikeId =BikeId,UserId =UserId,StartTime =StartTime,EndTime =EndTime,LocationX =LocationX, LocationY =LocationY)
        length = len(result)
        result.delete()
        message = "共删除数据：" + str(length)
        return render(request,'login/CyclingR_query.html',{'message':message})
    return render(request,'login/CyclingR_query.html')

#修改骑行记录
def CyclingRecords_update(request):
    if request.method == "POST":
        id = request.POST.get('id')
        BikeId = request.POST.get('bike_id')
        UserId = request.POST.get('user_id')
        StartTime = request.POST.get('start_time')
        EndTime = request.POST.get('end_time')
        LocationX = request.POST.get('location_x')
        LocationY = request.POST.get('location_y')
        StartTime = parser.parse(StartTime)
        EndTime = parser.parse(EndTime)
        try:
            bike = models.Bike.objects.get(BikeId=BikeId)
        except:
            message = "无对应共享单车编号!"
            return render(request,'login/CyclingR_update.html',{'message':message})
        try:
            models.CyclingRecords.objects.filter(id=id).update(BikeId =bike,UserId =UserId,StartTime =StartTime,EndTime =EndTime,LocationX =LocationX, LocationY =LocationY)
            message = "修改已完成!"
            return render(request, 'login/CyclingR_update.html', {'message': message})
        except:
            message = "修改失败！"
            return render(request, 'login/CyclingR_update.html', {'message': message})
    return render(request,'login/CyclingR_update.html')

