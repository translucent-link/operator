from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0xb0897686c545045aFc77CF20eC7A532E3120E0F1"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
