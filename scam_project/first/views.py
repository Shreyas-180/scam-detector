from django.shortcuts import render
from django.http import HttpResponse
from ml_model.tryingout_model import checker
from .forms import MessageForm
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.abspath(os.path.join(BASE_DIR, '../ml_model/bayes_model.pkl'))
print("Loading model from:", MODEL_PATH)  

with open(MODEL_PATH, 'rb') as f:
    bayes_model = pickle.load(f)
    
def home(request):
    return render(request,'first/home.html')

def message(request):
    form = MessageForm()

    if request.method == "POST":
        msg = request.POST.get("message")
        form = MessageForm(request.POST)
        pred_confidence = checker([msg], bayes_model)

        return render(request,'first/message.html',{
            'form': form,
            'prediction': pred_confidence[0],
            'confidence': 100*pred_confidence[1]
        })

    return render(request,'first/message.html',{'form': form})

def website(request):
    return HttpResponse("Website Detection coming soon!!!")
def about(request):
    return HttpResponse("About !")
# Create your views here.
