from block import Block
from transaction import Transaction

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)
    
    def add_transaction(self, sender, receiver, amount):
        blockchain_hash = self.chain[-1].hash if len(self.chain) >= 2 else ""
        transaction = Transaction(sender, receiver, amount, blockchain_hash)
        self.pending_transactions.append(transaction)
        print(f"Transaction ajoutée : {transaction}")
    
    def create_block(self):
        if len(self.pending_transactions) == 0:
            print("Aucune transaction à valider.")
            return
        new_block = Block(len(self.chain), self.pending_transactions[:10], self.chain[-1].hash)
        self.chain.append(new_block)
        self.pending_transactions = self.pending_transactions[10:]
        print(f"Nouveau bloc créé : {new_block}")
    
    def check_transaction(self, transaction_id):
        for block in self.chain:
            for tx in block.transactions:
                if tx.id.startswith(transaction_id):
                    print(f"Transaction trouvée : {tx}")
                    return
        print("Transaction introuvable.")
    
    def show_last_transactions(self):
        print("\n=== Dernières 10 transactions ===")
        recent = self.pending_transactions[-10:] if self.pending_transactions else []
        for tx in recent:
            print(tx)
    
    def tamper_block(self, block_index):
        if 0 <= block_index < len(self.chain):
            self.chain[block_index].transactions = []
            print(f"Bloc {block_index} altéré !")
        else:
            print("Bloc invalide.")
    
    def validate_blockchain(self):
        print("\n=== Validation de la Blockchain ===")
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].hash:
                print("La blockchain est invalide.")
                return
        print("La blockchain est valide.")
