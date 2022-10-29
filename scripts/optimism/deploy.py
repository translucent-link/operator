from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0x350a791Bfc2C21F9Ed5d10980Dad2e2638ffa7f6"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
