class Denso:
    def __init__(self):
        self.ip = ''
        self.port = 0
        self.receive_positions = ''
        self.positions = ''

    def receive_positions_server(self):
        self.positions = self.receive_positions

    def clear_receive_positions(self):
        self.receive_positions = ''
