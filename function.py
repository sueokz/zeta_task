from abi import (
    pool_abi,
    approve_abi,
    encoding_contract_abi,
    multicall_abi,
)

from config import (
    bnb_to_approve,
    pool_zeta_value,  
    zeta_value_bnb , 
    zeta_value_eth ,
    zeta_value_bnb ,
    wallet_A,
    wallet_B,…
    wallet…,
    key_A,
    key_B,
    key_wallet…,
)

#パッケージ管理
!pip freeze > requirements.txt

#install
#!pip install -r requirements.txt


#RPCの設定
RPC_URL = "https://zetachain-evm.blockpi.network/v1/rpc/public"
web3 = Web3(HTTPProvider(RPC_URL))
proxy_info = None

#Networkの確認
print(web3.is_connected())
print(web3.eth.chain_id) 


#Send_Task
def create_transaction(
)


#send_token
abi=
btc_address=""
btcContract = web3.eth.contract(address=btc_address, abi=btc_abi)

def transfer_tokens(
)


#Swap_Task
def eth_task(
)
def bnb_task(
)


#LP_Task_approve
def approve(
)

#pool
def pool_tx(
)


#一括送金
def create_transaction()
