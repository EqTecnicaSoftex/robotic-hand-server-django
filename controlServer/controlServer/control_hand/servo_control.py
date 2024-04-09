import serial
import time


class HandAngles:
    def __init__(self):
        # Suponha que você tenha uma maneira de obter os ângulos dos dedos
        self.angles = [0, 0, 0, 0, 0, 0]
        self.ser = serial.Serial('COM6', 512000, timeout=1)

    # Atualiza o ângulo do dedão
    def update_thumb(self, angle):
        self.angles[0] = angle

    # Atualiza o ângulo do indicador
    def update_index(self, angle):
        self.angles[1] = angle

    # Atualiza o ângulo do médio
    def update_middle(self, angle):
        self.angles[2] = angle

    # Atualiza o ângulo do anelar
    def update_ring(self, angle):
        self.angles[3] = angle

    # Atualiza o ângulo do mínimo
    def update_pinky(self, angle):
        self.angles[4] = angle

    # Atualiza todos os ângulos de uma vez
    def update_angles(self, new_angles):
        self.angles = new_angles

    def send_hand_angles(self, angles):
        angles_str = ",".join(str(a) for a in angles)
        self.ser.write(angles_str.encode())
        self.ser.write(b'\n')  # Envia uma quebra de linha para indicar o fim da mensagem

# angle_servo = HandAngles()
# ser = serial.Serial('COM7', 512000, timeout=1)
#
# while True:
#     dedo = int(input("Angulo: "))
#     angle_servo.update_thumb(dedo)
#     send_hand_angles(ser, angle_servo.angles)
