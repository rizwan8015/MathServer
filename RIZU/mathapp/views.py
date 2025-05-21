from django.shortcuts import render # type: ignore


def power_calculator(request):
    power = None 
    intensity = None
    resistance = None 

    if request.method == 'POST':
        print("POST method is used")
        
        intensity = request.POST.get('intensity','0')
        resistance = request.POST.get('resistance','0')

        
        if intensity and resistance:
            try:
            
                I = float(intensity)
                R = float(resistance)
                power = I**2 * R
                print('request=',request)
                print('intensity=',I)
                print('resistance=',R)
                print('power=',power)  

            except ValueError:
                power = "Invalid input. Please enter numerical values."

    
    return render(request, 'mathapp/math.html', {'power': power, 'intensity': intensity, 'resistance': resistance})