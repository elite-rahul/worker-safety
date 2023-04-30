from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializer import SerializerClass
from .models import *
from django.http import Http404,HttpResponse,StreamingHttpResponse
from rest_framework.response import Response
import requests
import json
import cv2
from django.views.decorators import gzip
from django.views.decorators.csrf import csrf_exempt

class Crud(APIView):
    def post(self,request):
        serialized_data = SerializerClass(data = request.POST)
        print(serialized_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return HttpResponse('Success')
        else:
            return HttpResponse('Something went wrong')
    def get(self,request):
        allData = WorkerDetails.objects.all()
        serialized_data = SerializerClass(allData, many = True)
        return Response(serialized_data.data)

def showData(request):
    data = requests.get('http://localhost:8000/crud')
    data = data.json()
    context = {
        'data':data
    }
    template ='home.html'
    return render(request, template, context)

def Form(request):
    if(request.method == 'POST'):
        Name = request.POST.get('Name')
        age = request.POST.get('Age')
        address = request.POST.get('Address')
        Contact = request.POST.get('Contact')
        Medical_History = request.POST.get('Medical_History')
        Safety_Breach = request.POST.get('safety_breach')
        BloodGroup = request.POST.get('blood_group')
        pulsate = request.POST.get('Pulsate')
        data = {
            'name':Name,
            'age':age,
            'address':address,
            'phn_num':Contact,
            'medical_history':Medical_History,
            'safety_breach':Safety_Breach
        }
        requests.post('http://localhost:8000/crud', data=data)
        return redirect('showdata')
       
    return render(request, 'form.html')



@csrf_exempt
def web_cam(request):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return HttpResponse("Failed to open webcam.")

    def generate():
        keep_streaming = True
        while keep_streaming:
            ret, frame = cap.read()

            if not ret:
                break

            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                keep_streaming = False

        cap.release()

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')


