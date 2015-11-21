from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
import json
from models import StatusObject
import dtw
import cosine
import numpy as np


def checkSync(request):
	if request.method != 'POST':
		return HttpResponseBadRequest("Use a POST request to send data")

	
	body = json.loads(request.body);
	
	phoneData = body["phone"]
	watchData = body["watch"]	
	
	cosine_score = cosine.similarity_score(phoneData,watchData)

	d = dtw.DynamicTimeWarping()
	pX = phoneData['x'][10:]
	pY = phoneData['y'][10:]
	pZ = phoneData['z'][10:]
	wX = watchData['x'][10:]
	wY = watchData['y'][10:]
	wZ = watchData['z'][10:]

	d1 = d.distance(pX,wX) 
	d2 = d.distance(pY,wY) 
	d3 = d.distance(pZ,wZ) 

	failureDict = {"status":"0"}
	successDict = {"status":"1"}

	
	result = successDict;

	
	failCount =0
	for s in cosine_score:
		if s<0.95:
			failCount+=1

	if failCount==0:
		result= successDict

	elif(failCount==1):
	 	if(d1>8.0 or d2>8.0 or d3>8.0  ):
		 	result = failureDict;

	else:
	 	if(d1>5.0 or d2>5.0 or d3>5.0  ):
		 	result = failureDict;		

	return JsonResponse(result)


