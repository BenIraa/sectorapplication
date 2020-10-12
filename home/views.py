from django.shortcuts import render
import africastalking
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
username ="iradukundacyuzuzo50@gmail,com"
api_key = "fadcb6a9ccf85104850af3477cc74d46eb392efb4940ff37495b8db395fa2e14"
africastalking.initialize(username, api_key)
# Create your views here.
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