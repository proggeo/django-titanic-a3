from django.shortcuts import render
from django.http import HttpResponse
import requests
import pandas as pd
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')

def googlemapstrees(request):
    return render(request, 'googlemaptrees.html')

def cars(request):
    return render(request, 'cars.html')

def titanic_json(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'static/titanic_data_set.xls')
    dataset = pd.read_excel(file_path)
    print(dataset)
    return HttpResponse(dataset.to_json(orient="records"), content_type="application/json")


def trees_json(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'static/trees_GeoCoo.json')
    with open(file_path) as json_file:
        json_trees = json_file.read()
    return HttpResponse(json_trees, content_type="application/json")

def cars_json(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'static/cars_GeoCoo.json')
    with open(file_path) as json_file:
        json_cars = json_file.read()
    return HttpResponse(json_cars, content_type="application/json")