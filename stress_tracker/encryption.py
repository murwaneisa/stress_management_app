import base64


def encode(password):
    message_bytes = password.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")
    # print(base64_message)
    return base64_message

def decode(encrypted_password):
    try:
        base64_bytes = encrypted_password.encode("ascii")
        pass_bytes = base64.b64decode(base64_bytes)
        password = pass_bytes.decode("ascii")
    except:
        password = encrypted_password

    return password