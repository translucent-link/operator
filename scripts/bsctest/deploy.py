from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0x84b9b910527ad5c03a9ca831909e21e236ea7b06"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
