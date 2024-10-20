import math
from django.shortcuts import render

def index(request):
    result = None
    factorial_result = None

    # Handle the ODD/EVEN checker
    if request.method == 'POST' and 'check_number' in request.POST:
        number = int(request.POST.get('number', ''))
        if number % 2 == 0:
            result = f"{number} is an even number"
        else:
            result = f"{number} is an odd number"

    # Handle the Factorial Calculation
    if request.method == 'POST' and 'factorial' in request.POST:
        num = int(request.POST.get('number_factorial', ''))
        factorial_result = math.factorial(num)

    return render(request, 'tempconn/index.html', {
        'result': result,
        'factorial_result': factorial_result,
    })
    