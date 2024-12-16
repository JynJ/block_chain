from datetime import datetime
import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount, blockchain_hash=""):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.now()
        # ID dépendant du hash si disponible
        base_string = f"{blockchain_hash}{sender}{receiver}{amount}{self.timestamp}"
        self.id = hashlib.sha256(base_string.encode()).hexdigest()
    
    def __str__(self):
        return f"ID: {self.id[:10]} | {self.sender} -> {self.receiver} : {self.amount}€ | {self.timestamp}"
