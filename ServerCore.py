STATE_INIT = 0
STATE_STANDBY = 1
STATE_CONNECTED_TO_NETWORK = 2
STATE_SHUTTING_DOWN =3

class ServerCore:
    def __init__(self):
        print('Initializing server ...')

    def start(self):
        self.server_state = STATE_STANDBY

    def join_network(self):
        #接続していないがCONNECTEDとここでは使う
        self.server_state = STATE_CONNECTED_TO_NETWORK

    def shutdown(self):
        self.server_state = STATE_SHUTTING_DOWN
        print('Shutdown server ...')

    def get_my_current_state(self):
        return self.server_state


