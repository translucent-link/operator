from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0x326c977e6efc84e512bb9c30f76e30c160ed06fb"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
