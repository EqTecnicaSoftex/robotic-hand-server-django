from django.http import JsonResponse
from .denso import Denso
from .lists import *
from time import sleep

denso = Denso('192.168.160.226')


def send_control_denso(request):
    if request.method == 'POST':
        control_denso = request.POST.get('positions')
        if control_denso == 0:
            denso.objeto = 1
            return JsonResponse({'message': f'Objeto {denso.objeto} selecionado!'})
        elif control_denso == 1:
            denso.objeto = 2
            return JsonResponse({'message': f'Objeto {denso.objeto} selecionado!'})
        else:
            return JsonResponse({'message': 'Erro ao selecionar objeto'})
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
        denso.objeto = request.POST.get('positions')
        if denso.objeto == '1':
            for i in range(0, 3):
                print(globals()['p' + str(i)])
                denso.receive_positions = globals()['p' + str(i)]
                denso.receive_positions_server()
                denso.move_joints()
            return JsonResponse({'message': f'O denso foi para as posições referentes ao objeto {denso.objeto}!'})
        elif denso.objeto == '2':
            for i in range(13, 17):
                denso.receive_positions = globals()['p' + str(i)]
                denso.receive_positions_server()
                denso.move_joints()
            return JsonResponse({'message': f'O denso foi para as posições referentes ao objeto {denso.objeto}!'})
        else:
            return JsonResponse({'message': 'Erro ao enviar as posições do objeto!'})
    else:
        return JsonResponse({'message': 'Método de solicitação inválido'}, status=400)


def captured(request):
    if request.method == 'POST':
        if denso.objeto == 1:
            for i in range(4, 8):
                denso.receive_positions = globals()['p' + str(i)]
                denso.receive_positions_server()
                denso.move_joints()
            return JsonResponse({'message': 'Realizou o movimento com sucesso!'})
        elif denso.objeto == 2:
            for i in range(19, 23):
                denso.receive_positions = globals()['p' + str(i)]
                denso.receive_positions_server()
                denso.move_joints()
            return JsonResponse({'message': 'Realizou o movimento com sucesso!'})
        else:
            return JsonResponse({'message': 'Não realizou o movimento com sucesso!'})
        
        # final_position = '0,0,0,0,0,0'
        # denso.receive_positions = final_position
        # denso.receive_positions_server()
        # denso.move_joints()
        # if denso.condition_error:
        #     return JsonResponse({'message': 'Erro: ' + denso.error}, status=400)
        # else:
        #     return JsonResponse({'message': 'Movendo o denso para a posição: ' + final_position})
    else:
        return JsonResponse({'message': 'Método de solicitação inválido'}, status=400)


def released(request):
    if denso.objeto == 1:
        for i in range(10, 12):
            denso.receive_positions = globals()['p' + str(i)]
            denso.receive_positions_server()
            denso.move_joints()
        return JsonResponse({'message': 'Realizou o movimento com sucesso!'})
    elif denso.objeto == 2:
        for i in range(25, 27):
            denso.receive_positions = globals()['p' + str(i)]
            denso.receive_positions_server()
            denso.move_joints()
        return JsonResponse({'message': 'Realizou o movimento com sucesso!'})
    else:
        return JsonResponse({'message': 'Método de solicitação inválido'}, status=400)
    
def finalize(request):
    if request.method == 'POST':
        for i in range(28, 30):
            denso.receive_positions = globals()['p' + str(i)]
            denso.receive_positions_server()
            denso.move_joints()
        return JsonResponse({'message': 'Realizou o movimento com sucesso!'})
    else:
        return JsonResponse({'message': 'Método de solicitação inválido'}, status=400)

def server_status(request):
    return JsonResponse({'message': 'Servidor em execução'})
