# import logging
# import sys
# from pathlib import Path

# from dotenv import load_dotenv

# from smart_contracts._helpers.build import build
# from smart_contracts._helpers.config import contracts
# from smart_contracts._helpers.deploy import deploy

# # Uncomment the following lines to enable auto generation of AVM Debugger compliant sourcemap and simulation trace file.
# # Learn more about using AlgoKit AVM Debugger to debug your TEAL source codes and inspect various kinds of
# # Algorand transactions in atomic groups -> https://github.com/algorandfoundation/algokit-avm-vscode-debugger
# # from algokit_utils.config import config
# # config.configure(debug=True, trace_all=True)
# logging.basicConfig(
#     level=logging.DEBUG, format="%(asctime)s %(levelname)-10s: %(message)s"
# )
# logger = logging.getLogger(__name__)
# logger.info("Loading .env")
# # For manual script execution (bypassing `algokit project deploy`) with a custom .env,
# # modify `load_dotenv()` accordingly. For example, `load_dotenv('.env.localnet')`.
# load_dotenv()
# root_path = Path(__file__).parent


# def main(action: str, contract_name: str | None = None) -> None:
#     artifact_path = root_path / "artifacts"

#     # Filter contracts if a specific contract name is provided
#     filtered_contracts = [
#         c for c in contracts if contract_name is None or c.name == contract_name
#     ]

#     match action:
#         case "build":
#             for contract in filtered_contracts:
#                 logger.info(f"Building app at {contract.path}")
#                 build(artifact_path / contract.name, contract.path)
#         case "deploy":
#             for contract in filtered_contracts:
#                 output_dir = artifact_path / contract.name
#                 app_spec_file_name = next(
#                     (
#                         file.name
#                         for file in output_dir.iterdir()
#                         if file.is_file() and file.suffixes == [".arc32", ".json"]
#                     ),
#                     None,
#                 )
#                 if app_spec_file_name is None:
#                     raise Exception("Could not deploy app, .arc32.json file not found")
#                 app_spec_path = output_dir / app_spec_file_name
#                 if contract.deploy:
#                     logger.info(f"Deploying app {contract.name}")
#                     deploy(app_spec_path, contract.deploy)
#         case "all":
#             for contract in filtered_contracts:
#                 logger.info(f"Building app at {contract.path}")
#                 app_spec_path = build(artifact_path / contract.name, contract.path)
#                 if contract.deploy:
#                     logger.info(f"Deploying {contract.path.name}")
#                     deploy(app_spec_path, contract.deploy)


# if __name__ == "__main__":
#     if len(sys.argv) > 2:
#         main(sys.argv[1], sys.argv[2])
#     elif len(sys.argv) > 1:
#         main(sys.argv[1])
#     else:
#         main("all")

from algosdk import algod
from .contracts.contract import NFTContract
from ._helpers.config import Config
from ._helpers.deploy import deploy_smart_contract, compile_smart_contract

def main():
    algod_client = algod.AlgodClient(Config.ALGOD_TOKEN, Config.ALGOD_ADDRESS)
    
    # Biên dịch smart contract
    source_code = "your_smart_contract_source_code"  # Thay bằng mã nguồn thực tế
    compiled_contract = compile_smart_contract(source_code)
    
    # Triển khai smart contract
    txid = deploy_smart_contract(compiled_contract)
    print(f"Smart contract deployed with transaction ID: {txid}")
    
    # Khởi tạo hợp đồng NFT
    nft_contract = NFTContract(algod_client)

    # Kiểm tra giao dịch
    user_address = "your_user_address"
    nft_id = 123456  # Hoặc ID thực tế của NFT
    try:
        txn_id = nft_contract.execute_transaction(nft_id, user_address)
        print(f"Transaction executed with ID: {txn_id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()