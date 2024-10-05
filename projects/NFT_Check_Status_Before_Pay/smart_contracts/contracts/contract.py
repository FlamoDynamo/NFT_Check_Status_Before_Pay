from algosdk import algod, transaction
from algosdk.future import transaction
from algosdk import encoding

class NFTContract:
    def __init__(self, algod_client):
        self.algod_client = algod_client

    def check_ownership(self, nft_id, user_address):
        # Kiểm tra quyền sở hữu NFT
        account_info = self.algod_client.account_info(user_address)
        return nft_id in account_info['assets']

    def check_nft_status(self, nft_id):
        # Kiểm tra trạng thái của NFT (có thể giao dịch hay không)
        # Giả sử trạng thái được lưu trữ trong smart contract
        # Lấy thông tin từ smart contract
        app_info = self.algod_client.application_info(nft_id)
        return app_info['params']['global-state']

    def log_transaction(self, txn_id):
        # Ghi lại giao dịch
        # Có thể lưu vào database hoặc blockchain
        print(f"Transaction {txn_id} logged.")
    
    def execute_transaction(self, nft_id, user_address):
        if not self.check_ownership(nft_id, user_address):
            raise Exception("User is not the owner of the NFT.")

        nft_status = self.check_nft_status(nft_id)
        if not nft_status:
            raise Exception("NFT is not available for transaction.")

        # Thực hiện giao dịch
        txn_id = self.send_transaction(user_address)
        self.log_transaction(txn_id)
        return txn_id

    def send_transaction(self, user_address):
        # Gửi giao dịch (chức năng giả định)
        txn = transaction.PaymentTxn(
            sender=user_address,
            receiver="recipient_address",
            amt=1000,
            sp=self.algod_client.suggested_params()
        )
        signed_txn = txn.sign("your_private_key")
        txid = self.algod_client.send_transaction(signed_txn)
        return txid