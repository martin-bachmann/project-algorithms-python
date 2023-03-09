from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises

VALID_MESSAGE = "String"


def test_encrypt_message():
    with raises(TypeError, match="tipo inválido para key"):
        encrypt_message(VALID_MESSAGE, "1")
    with raises(TypeError, match="tipo inválido para message"):
        encrypt_message(12, 1)

    assert encrypt_message(VALID_MESSAGE, 3) == "rtS_gni"
    assert encrypt_message(VALID_MESSAGE, 2) == "gnir_tS"
    assert encrypt_message(VALID_MESSAGE, 20) == "gnirtS"
