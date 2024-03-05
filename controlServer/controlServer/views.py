from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def send_control_denso(request):
    if request.method == 'POST':
        control_denso = request.POST.get('positions')
        print(control_denso)
        return JsonResponse({'message': 'Received control_denso: ' + control_denso})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


def send_control_hand(request):
    if request.method == 'POST':
        control_hand = request.POST.get('move_hand')
        print(control_hand)
        return JsonResponse({'message': 'Received control_hand: ' + control_hand})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
