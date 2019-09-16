from time import sleep

from stem.control import Controller
from stem import SocketError
from stem.connection import AuthenticationFailure

def attempt_connect(password='password'):
    response = None
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password)
        response = controller.get_info("status/bootstrap-phase")

    return response

def is_ready(response):
    if "PROGRESS=100" in response:
        return True
    else:
        return False

ready = False
while not ready:
    try:
        response = attempt_connect
        ready = is_ready(response)
        print(response)
        if ready:
            print("READY!")
        else:
            sleep(1)
    except (SocketError, ConnectionRefusedError, AuthenticationFailure):
        print("connection refused")
        sleep(1)
