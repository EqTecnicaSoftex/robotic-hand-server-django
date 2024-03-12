from django.http import JsonResponse
from .denso import Denso

denso = Denso('192.168.0.1')  # exemplo de IP do robô


def send_control_denso(request):
    if request.method == 'POST':
        control_denso = request.POST.get('positions')
        denso.receive_positions = control_denso
        denso.receive_positions_server()
        if denso.condition_error:
            return JsonResponse({'message': 'Erro: ' + denso.error}, status=400)
        else:
            return JsonResponse({'message': 'Posições ' + control_denso + ' recebidas com sucesso'})
    else:
        return JsonResponse({'message': 'Método de solicitação inválido'}, status=400)


def send_control_hand(request):
    if request.method == 'POST':
        control_hand = request.POST.get('move_hand')
        return JsonResponse({'message': 'Abertura: ' + control_hand + ' da mão recebida com sucesso'})
    else:
        return JsonResponse({'message': 'Método de solicitação inválido'}, status=400)


def move_denso(request):
    if request.method == 'POST':
        pass
        if denso.positions == '':
            return JsonResponse({'message': 'Posições não recebidas'}, status=400)
        else:
            denso.move_joints()
            if denso.condition_error:
                return JsonResponse({'message': 'Erro: ' + denso.error}, status=400)
            else:
                return JsonResponse({'message': 'Movendo o denso para a posição: ' + denso.positions})
    else:
        return JsonResponse({'message': 'Método de solicitação inválido'}, status=400)


def finalize_denso(request):
    if request.method == 'POST':
        final_position = '0,0,0,0,0,0'
        denso.receive_positions = final_position
        denso.receive_positions_server()
        denso.move_joints()
        if denso.condition_error:
            return JsonResponse({'message': 'Erro: ' + denso.error}, status=400)
        else:
            return JsonResponse({'message': 'Movendo o denso para a posição: ' + final_position})
    else:
        return JsonResponse({'message': 'Método de solicitação inválido'}, status=400)


def server_status():
    return JsonResponse({'message': 'Servidor em execução'})
