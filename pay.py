from web3 import Web3
import os

# KiteAI Testnet Settings
RPC_URL = "https://rpc-testnet.gokite.ai/"
CHAIN_ID = 2368

LITE_ADDR = '0x35A9b4E215c8Bf9b7bFF83Ac08aD32dEE8D19F64'
USDT_ADDR = "0x0fF5393387ad2f9f691FD6Fd28e07E3969e27e63"

# ERC20 Minimal ABI
ERC20_ABI = [
    {"constant": True, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"}
]

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(RPC_URL))

def connect_and_check():
    if w3.is_connected():
        print(f"✅ Connected to KiteAI Testnet")
        print(f"Network ID: {w3.eth.chain_id}")


        # Create USDT contract instance
        usdt_contract = w3.eth.contract(address=USDT_ADDR, abi=ERC20_ABI)

        try:
            # Query USDT balance of LITE contract
            balance_raw = usdt_contract.functions.balanceOf(LITE_ADDR).call()
            try:
                decimals = usdt_contract.functions.decimals().call()
            except:
                decimals = 6 # Default for USDT if call fails
            
            balance_formatted = balance_raw / (10 ** decimals)
            
            print(f"\n--- Balance Info ---")
            print(f"LITE Contract: {LITE_ADDR}")
            print(f"USDT Balance: {balance_formatted} USDT")
            print(f"--------------------\n")
        except Exception as e:
            print(f"❌ Error querying USDT balance: {e}")

    else:
        print("❌ Failed to connect to KiteAI Testnet")

if __name__ == "__main__":
    connect_and_check()
