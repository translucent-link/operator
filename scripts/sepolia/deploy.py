from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0x779877A7B0D9E8603169DdbD7836e478b4624789"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
