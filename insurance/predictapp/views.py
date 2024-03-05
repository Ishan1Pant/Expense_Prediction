from django.shortcuts import render
import pickle 
import numpy as np 
import pandas as pd 

model_path='D:/netsmartz/Projects/Insurance/insurance.pkl'

with open (model_path,'rb') as file:
    model=pickle.load(file)

region_data={
    
}

# Create your views here.
def home(request):
    if request.method =='POST':
        age=request.POST['age']
        sex=request.POST['sex']
        bmi=request.POST['bmi']
        children=request.POST['children']
        smoker=request.POST['smoker']
        region=request.POST['region']

        final_data=[age,sex,bmi,children,smoker,region]


        prediction=model.predict([final_data])
        return render(request,'predictapp/home.html',{'prediction':prediction})


    return render(request,'predictapp/home.html')