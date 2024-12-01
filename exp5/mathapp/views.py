from django.shortcuts import render
def calculate_power(request):
    context={}
    context['power']="0"
    context["intensity"]="0"
    context["resistance"]="0"
    if request.method == "POST":
        print("POST method is used")
        intensity = float(request.POST.get("intensity", '0'))
        resistance = float(request.POST.get("resistance", '0'))
        print('request=',request)
        print('intensity =',intensity)
        print('resistance =',resistance)
        power = (intensity ** 2) * resistance
        context['power']= power
        context["intensity"]= intensity
        context["resistance"]= resistance
        print('power =',power)
    return render(request,'mathapp\math.html',context)
