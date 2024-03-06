from django.http import JsonResponse
from .denso import Denso

denso = Denso()


def send_control_denso(request):
    if request.method == 'POST':
        control_denso = request.POST.get('positions')
        denso.receive_positions = control_denso
        denso.receive_positions_server()
        denso.clear_receive_positions()
        print('Received control_denso: ' + control_denso)
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


def move_denso(request):
    if request.method == 'POST':
        print(denso.positions)
        if denso.positions == '':
            return JsonResponse({'message': 'No positions received'}, status=400)
        else:
            print('Moving DENSO to positions: ' + denso.positions)
            return JsonResponse({'message': 'Received positions: ' + denso.positions})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


def finalize_denso(request):
    if request.method == 'POST':
        final_position = '0,0,0,0,0,0'
        print(f'Final position Denso: {final_position}')
        return JsonResponse({'message': 'Finalizing DENSO'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
