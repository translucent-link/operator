from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0xd14838a68e8afbade5efb411d5871ea0011afd28"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
