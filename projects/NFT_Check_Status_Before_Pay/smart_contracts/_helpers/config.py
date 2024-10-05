import os

class Config:
    ALGOD_ADDRESS = os.getenv("ALGOD_ADDRESS", "http://localhost:4001")
    ALGOD_TOKEN = os.getenv("ALGOD_TOKEN", "your_algod_token")
    NETWORK = os.getenv("NETWORK", "testnet")