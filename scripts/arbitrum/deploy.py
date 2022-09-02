from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0xf97f4df75117a78c1A5a0DBb814Af92458539FB4"

    operator = Operator.deploy(
        linkAddress,
        acct,
        {'from': acct}
    )
