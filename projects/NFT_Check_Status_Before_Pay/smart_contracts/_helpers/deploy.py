from algosdk import algod, transaction, mnemonic
from algosdk.kmd import KMDClient
from algosdk.future import transaction
from .config import Config

def get_algod_client():
    algod_token = Config.ALGOD_TOKEN
    algod_address = Config.ALGOD_ADDRESS
    return algod.AlgodClient(algod_token, algod_address)

def deploy_smart_contract(compiled_contract):
    algod_client = get_algod_client()
    
    # Thực hiện các bước triển khai
    params = algod_client.suggested_params()
    txn = transaction.ApplicationCreateTxn(
        sender="your_sender_address",
        sp=params,
        on_complete=transaction.OnComplete.NoOpOC,
        approval_program=compiled_contract,
        clear_program=compiled_contract,  # Có thể thay đổi thành clear program khác
        global_schema=transaction.StateSchema(num_uints=1, num_byte_slices=0),
        local_schema=transaction.StateSchema(num_uints=1, num_byte_slices=0)
    )
    
    # Ký và gửi giao dịch
    signed_txn = txn.sign("your_private_key")
    txid = algod_client.send_transaction(signed_txn)
    return txid