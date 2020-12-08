from django.shortcuts import render
from .models import Car
import pandas as pd
# Create your views here.
def main_view(request):
    qs=Car.objects.all().values()
    data=pd.DataFrame(qs)
    # data=pd.DataFrame(qs)
    print(data)
    
    #
    context={
        'df':data.to_html(),
        'describe':data.describe().to_html(),

    }
    return render(request,'cars/main.html',context)
