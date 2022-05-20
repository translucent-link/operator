from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0xa36085F69e2889c224210F603D836748e7dC0088"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
