from cryptography.fernet import Fernet

class ZeKoder:
    
    """
    Class de cryptage & decryptage
    source : https://github.com/pyca/cryptography
    cf. https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
    """
    
    def __init__(self, key=None) -> None:
        self.key = key
    
    def make_key(self) -> str:
        """
        retourne une clé pour l'encodage et le décodage
        """
        key = Fernet.generate_key()
        return key.decode()
   
    def set_key(self, key) -> None:
        self.key = key
    
    def get_key(self) -> str:
        return self.key
    
    def encrypt(self, message: str) -> str:
        """
        Méthode de cryptage d'un message
        """
        key = self.key
        if key:
            message = message.encode()
            key = key.encode()
            return Fernet(key).encrypt(message).decode()
        else:
            return 'no key provided'           
    
    def decrypt(self, token: str) -> str:
        """
        Méthode de decryptage du token
        """
        key = self.key
        if key:
            key = key.encode()
            token = token.encode()
            return Fernet(key).decrypt(token).decode()
        else:
            return 'no key provided'