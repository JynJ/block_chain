from blockchain import Blockchain

def main():
    blockchain = Blockchain()
    
    while True:
        print("\n=== Menu Blockchain ===")
        print("1. Ajouter une transaction")
        print("2. Vérifier une transaction")
        print("3. Afficher les 10 dernières transactions")
        print("4. Créer un bloc")
        print("5. Altérer un bloc")
        print("6. Valider la blockchain")
        print("7. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            sender = input("Expéditeur : ")
            receiver = input("Destinataire : ")
            amount = float(input("Montant : "))
            blockchain.add_transaction(sender, receiver, amount)
        elif choice == "2":
            tx_id = input("ID de la transaction (premiers caractères) : ")
            blockchain.check_transaction(tx_id)
        elif choice == "3":
            blockchain.show_last_transactions()
        elif choice == "4":
            blockchain.create_block()
        elif choice == "5":
            index = int(input("Index du bloc à altérer : "))
            blockchain.tamper_block(index)
        elif choice == "6":
            blockchain.validate_blockchain()
        elif choice == "7":
            print("Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
