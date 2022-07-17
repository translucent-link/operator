from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0x514910771AF9Ca656af840dff83E8264EcF986CA"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
