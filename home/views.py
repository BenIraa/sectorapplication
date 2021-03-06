import africastalking
from django.shortcuts import render
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
#login
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

username ="iradukundacyuzuzo50@gmail,com"
api_key = "fadcb6a9ccf85104850af3477cc74d46eb392efb4940ff37495b8db395fa2e14"
africastalking.initialize(username, api_key)
# Create your views here.
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username':user.username,
            'first_name':user.first_name,
        })
def welcome(request):
    return render(request, 'index.html')

@csrf_exempt
def proussd(request):
    
    if request.method == 'POST':
            ## mandatory
        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST.get("text")
        level = text.split('*')
        response =""
        numb = text[:3]
        if text =='':
            response = "CON Welcome to transport USSD app \n "
            response +="1. ikinyarwandaa \n"
            response +="2. English"
        elif text =='1':
            response ="CON Welcome to Sector App "+str(len(level))+"\n"
            response +="1. Iyandikishe \n"
            response +="2. Usanzwe wanditswe \n"
            
           #=
        elif text == '1*1':
            response ="CON Izina ryawe "+str(len(level))+"\n"
        elif numb =='1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Nimero yindangamuntu "
        elif numb =='1*1' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Nimero ya telefone"
        elif numb =='1*1' and  int(len(level))==5 and str(level[4]) in str(level):
            response ="CON Akarere\n"
        elif numb =='1*1' and  int(len(level))==6 and str(level[5]) in str(level):
            response ="CON Umurenge"
        elif numb =='1*1' and  int(len(level))==7 and str(level[6]) in str(level):
                response ="CON Akagali"
        elif numb =='1*1' and  int(len(level))==8 and str(level[5]) in str(level):
            response ="CON Umudugudu"
        elif numb =='1*1' and  int(len(level))==9 and str(level[6]) in str(level):
                response ="CON Ijambo banga"
          #===========Girls in
        elif text == '1*2':
            response ="CON Ijambo Banga "+str(len(level))+"\n"
        elif numb =='1*2' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Ikaze Kurubuga \n "
            response +="1. Kanda *147# Kumva Ibyavuzwe \n  "
            response +="2. kanda *148# Ubone Ubutumwa \n"

        


        
            

        


        elif text =='2':
            response ="CON Welcome to sector app "+str(level[0])+"\n"
            response +="1. Register \n"
            response +="2. Login \n"
            
            #==============transp out

        elif text =='2*1':
            response ="CON enter your name "+str(len(level))+"\n"
        elif numb =='2*1' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON I.d number "
        elif numb =='2*1' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Enter Your Phone Number "
        elif numb =='2*1' and  int(len(level))==5 and str(level[4]) in str(level):
            response ="CON Enter District"
        elif numb =='2*1' and  int(len(level))==6 and str(level[5]) in str(level):
            response ="CON Enter Sector"
        elif numb =='2*1' and  int(len(level))==7 and str(level[6]) in str(level):
            response ="CON Enter Cell"
        elif numb =='2*1' and  int(len(level))==8 and str(level[7]) in str(level):
            response ="CON Enter Village"
        elif numb =='2*1' and  int(len(level))==9 and str(level[8]) in str(level):
            response ="CON Enter PinCode"
           
        


        elif text =='2*2':
            response ="CON enter your PinCode "+str(len(level))+"\n"
        elif numb =='2*2' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Welcome To Chatbox \n"
            response +="CON Press *147#  For Insta Voice \n"
            response +="CON Press *148#  For Recieve Announcement \n"


        #=========== transp eng

        elif text == '1*3':
          response ="CON Izina ryawe"+str(len(level))+"\n"
        elif numb =='1*3' and int(len(level))==3 and str(level[2]) in str(level):
          response ="CON Nimero yindangamuntu "
        elif numb =='1*3' and int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Icyerekezo uganamo"


        elif text == '2*3':
          response ="CON Enter your name"+str(len(level))+"\n"
        elif numb =='2*3' and int(len(level))==3 and str(level[2]) in str(level):
          response ="CON I.d Number "
        elif numb =='2*3' and int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Location"
        elif numb =='2*3' and int(len(level))==4 and str(level[3]) in str(level):
            response ="Enter Amount"


        else:
            response ="END INvalid choice"

    return HttpResponse(response)
def registration (request):
    select =Registration.objects.all().order_by('id')
    if request.method =='POST':
        phone = request.POST['phone']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        insert = Registration(phone=phone,firstname=firstname,lastname=firstname)
        insert.save()
        try:
            insert.save()
            return render(request, 'register.html',{'message':'data has been inserted succesful','data':select})
        except:
            return render(request, 'register.html',{'message':'Failed to Insert','data':select})

        
    

    return render(request, 'register.html',{'data':select})
def delreg(request,id):
    select = Registration.objects.all().order_by('id')
    deleteinfos = Registration.objects.get(id=id).delete()
    return render(request, 'register.html',{'delmsg':'data has been inserted succesful','data':select})
def updatereg(request,id):
    select = Registration.objects.all().order_by('id')
    update = Registration.objects.get(id=id)
    if request.method=='POST':
        
        
        update.phone = request.POST['phone']
        update.phone = request.POST['firstname']
        update.phone = request.POST['lastname']
        try:
            update.save()
            return render(request, 'updateregister.html',{'message':'Data have been updated','data':select,'update':update})
        except:
            return render(request, 'updateregister.html',{'message':'Data does not  updated','data':select,'update':update})
                        



    return render(request, 'updateregister.html',{'delmsg':'data has been inserted succesful','data':select,'update':update})
#Biulidng our End point 
@csrf_exempt
def registerEndpoint(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reg = Registration.objects.all()
        serializer = RegisterSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mesage':'sent','data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)
#delete/put/get
    
#delete and update
@csrf_exempt
def deleteEndpoint(request,id):
 
    if request.method == 'GET':
        reg=Registration .objects.get(id=id)
        serializer = RegisterSerializer(reg, many=False)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='DELETE':
        delt=Registration .objects.get(id=id).delete()
        return JsonResponse({'message':'Data has been Deleted'}, status=490)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)#or request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':"Sent success",'data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)

# creating endpoint
class Posts(APIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes =(MultiPartParser, FormParser)
    # creating post method
    def post(self,request, *args, **kwargs):
        serializers= PostsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse({'message':'successfull','data':serializers.data},status=201)
        else:
            return JsonResponse({'message':'byanze','data':serializers.error}, status=400)

@csrf_exempt
def Sendemail(request):
   
    if request.method == 'GET':
        reg = Sendemail.objects.all()
        serializer = SendemailSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

 #request.data
        serializer = SendemailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400)  
  