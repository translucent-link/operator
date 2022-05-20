from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0x01BE23585060835E02B77ef475b0Cc51aA1e0709"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
