from hvac import Client
import base64

def base64ify(bytes_or_str): # From documentation
    if isinstance(bytes_or_str, str):
        input_bytes = bytes_or_str.encode('utf8')
    else:
        input_bytes = bytes_or_str

    output_bytes = base64.urlsafe_b64encode(input_bytes)
    return output_bytes.decode('ascii')

def debase64fi(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        input_bytes = bytes_or_str.decode("utf-8")
    else:
        input_bytes = bytes_or_str
    output_bytes = base64.b64decode(input_bytes)
    return output_bytes.decode('ascii')

def init_client():
	client = Client(url='http://localhost:8200/', token="")
	return client

def create_transit_key(client, name):
	client.secrets.transit.create_key(name=name)


def encrypt_string(client, transit_key, plaintext):
	encrypt_data_response = client.secrets.transit.encrypt_data(name=transit_key, plaintext=base64ify(plaintext.encode()),)
	cipher_text = encrypt_data_response.get("data").get("ciphertext")
	cipher_text_encoded = base64ify(encrypt_data_response.get("data").get("ciphertext"))
	return cipher_text

def decrypt_string(client, transit_key, cipher_text):
	decrypt_data_response = client.secrets.transit.decrypt_data(name=transit_key, ciphertext=cipher_text)
	plain_text = decrypt_data_response.get("data").get("plaintext")
	plain_text_decoded = debase64fi(plain_text)
	return plain_text_decoded

def rotate_key(client, transit_key):
	client.secrets.transit.rotate_key(name=transit_key)


def add_or_update_values_to_secret(client, path, key_value):
	client.secrets.kv.v2.create_or_update_secret(
    path=path,
    secret=key_value,)

def read_secret(client, path):
	read_secret_result = client.secrets.kv.v2.read_secret(path='test1',)
	return read_secret_result.get("data").get("data")


def main():
	transit_key = "test_key"
	string = "Hello World"
	path = "test"

	client = init_client()
	create_transit_key(client, transit_key)
	cipher_text = encrypt_string(client, transit_key, string)
	plain_text = decrypt_string(client, transit_key, cipher_text)
	rotate_key()

	add_or_update_values_to_secret(client, path, {"key": cipher_text})
	key = read_secret(client, path)


if __name__ == '__main__':
	main()
