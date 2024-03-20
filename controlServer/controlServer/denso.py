import rria_api_denso


class Denso:
    def __init__(self, ip):
        self.ip = ip
        self.robot_denso = rria_api_denso.DensoRobotAPI('', '', f'Server={self.ip}')
        self.robot_denso.connect()  # conecta ao robô
        self.receive_positions = []  # inicializa a variável que receberá as posições
        self.positions = None  # inicializa a variável que armazenará
        # as posições recebidas
        self.error = ''  # inicializa a variável que armazenará os erros
        self.condition_error = False  # inicializa a variável que armazenará a condição de erro

    def receive_positions_server(self):
        self.positions = rria_api_denso.RobotCartesianCommand(self.receive_positions[0], self.receive_positions[1],
                                                              self.receive_positions[2], self.receive_positions[3],
                                                              self.receive_positions[4], self.receive_positions[5],
                                                              self.receive_positions[6])
        # Carrega as posições recebidas para a classe que armazenará as posições
        self.receive_positions = ''  # Limpa a variável que armazena as posições recebidas

    def move_joints(self):
        if self.robot_denso.is_connected():  # verifica se o robô está conectado
            # if self.positions.joint_1 != 1000:  # verifica se as posições foram recebidas
            self.robot_denso.motor_on()  # liga os motores
            if self.robot_denso.motor_enabled():  # verifica se os motores estão ligados
                self.robot_denso.set_arm_speed(5, 5, 5)  # seta velocidade, aceleração, desaceleração
                self.robot_denso.move_cartesian(self.positions)  # move o robô para as posições recebidas
                self.condition_error = False  # seta a condição de erro como falsa
            else:
                self.error = "Motor off"
                self.condition_error = True  # seta a condição de erro como verdadeira
                return self.error  # caso os motores estejam desligados
            # else:
            #     self.error = "No positions received"
            #     self.condition_error = True  # seta a condição de erro como verdadeira
            #     return self.error  # caso as posições não tenham sido recebidas
        else:
            self.error = "Not connected"
            self.condition_error = True  # seta a condição de erro como verdadeira
            return self.error  # caso o robô não esteja conectado

    def motor_off(self):
        self.robot_denso.motor_off()  # desliga os motores


if __name__ == '__main__':
    from lists import *
    from time import sleep
    denso = Denso('192.168.160.226')
    for i in range(28):
        denso.receive_positions = globals()['p' + str(i)]
        print(i)
        if globals()['p' + str(i)] == 'pause':
            op = input('Pegou')
            if op == 's':
                pass
        else:
            denso.receive_positions_server()
            denso.move_joints()
