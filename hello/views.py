from django.shortcuts import render
from django.http import HttpResponse
import requests
import pandas as pd
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')


def titanic_json(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'static/titanic_data_set.xls')
    dataset = pd.read_excel(file_path)
    print(dataset)
    return HttpResponse(dataset.to_json(orient="records"), content_type="application/json")
