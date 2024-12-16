import hashlib

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions  # Liste de transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = f"{self.index}{[str(tx) for tx in self.transactions]}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def __str__(self):
        return f"Block {self.index} | Hash: {self.hash[:10]} | Previous: {self.previous_hash[:10]}"
