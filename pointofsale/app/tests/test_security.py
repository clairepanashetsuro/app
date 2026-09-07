from core.security import (
hash_password, 
verify_password, 
create_access_token,
decode_access_token
)

def test_hash_password_and_verify_password():
    password = "my_secure_password"
    hashed_password = hash_password(password)
    assert isinstance(hashed_password, str)

    # Ensure that the hashed password is not the same as the original password
    assert hashed_password != password

    # Verify that the original password matches the hashed password
    assert verify_password(password, hashed_password) is True

    # Verify that an incorrect password does not match the hashed password
    assert verify_password("wrong_password", hashed_password) is False

    #pytest tests/test_security.py

    def test_create_access_token():
        user_id = 1
        token = create_access_token(user_id)
        assert isinstance(token, str)


    def test_decode_access_token():
        user_id = 1
        token = create_access_token(user_id)
        payload = decode_access_token(token)
        assert payload.get("sub") == str(user_id)