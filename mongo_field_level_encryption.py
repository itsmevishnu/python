from mongoengine import Document, StringField, connect
from cryptography.fernet import Fernet
import base64

class EncryptFieldMixin:

    @staticmethod
    def _encrypt(value, encryption_key):
        f = Fernet(encryption_key)
        encrypted_value = f.encrypt(value.encode()) 
        return base64.b64encode(encrypted_value).decode("utf-8") 
    
    @staticmethod
    def _decrypt(value, encryption_key):
        try:
            decoded_value = base64.b64decode(value.encode("utf-8"))  # Base64 decode
            f = Fernet(encryption_key)
            decrypted_value = f.decrypt(decoded_value).decode()  # Decrypt and decode
            return decrypted_value
        except (base64.binascii.Error, ValueError):
            return None  # Handle potential decoding errors

    def _generate_encryption_key(self):
        key = getattr(self, "key", "")  # Retrieve base64-encoded key
        code_bytes = key.encode("utf-8")
        hash_key = base64.urlsafe_b64encode(code_bytes.ljust(32)[:32])
        return hash_key  # Use the hashed key for encryption/decryption

class EncryptedStringField(StringField, EncryptFieldMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.encrypted_fields = [self.name]

    def to_mongo(self, value):
        if value is not None:  # Check if value is provided
            encryption_key = self._generate_encryption_key()
            encrypted_value = self._encrypt(value, encryption_key)
            return encrypted_value
        return value

    def to_python(self, value):
        if value is not None:  # Check if value is provided
            encryption_key = self._generate_encryption_key()
            decrypted_value = self._decrypt(value, encryption_key)
            return decrypted_value
        return value

class MyDocument(Document, EncryptFieldMixin):
    key = "aTtGg3I8CVj3nQ0nKwlSENnxO_Dl-oz8hdyArVeGvOw=" 
    ssn = EncryptedStringField(required=True, key=key)
    name = StringField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'ssn' in kwargs:
            self.ssn = kwargs['ssn']

if __name__ == '__main__':
    # Example usage
    connect(host="mongodb://localhost:27017/test-db")
     # Replace with your actual base64-encoded key
    ssn_value = "12333-12323-1212"
    
    # Pass ssn directly to EncryptedStringField during instantiation
    my_doc = MyDocument(ssn=ssn_value, name="John Doe")
    
    try:  # Manually trigger validation
        my_doc.save()
        print("Object saved")
    except Exception as e:
        print(f"Error: {str(e)}")

    my_docs = MyDocument.objects
    for item in my_docs:
        print(f"ssn:{item.ssn} and name:{item.name}")
