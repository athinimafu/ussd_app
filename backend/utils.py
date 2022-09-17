import hashlib
import base64


def hash_pin(pin: str):
    hash = hashlib.sha256(pin.encode('utf-8')).digest()
    return base64.b64encode(hash).decode('utf-8')
