from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    operator = Operator.at("0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    operator.setAuthorizedSenders(
        ["0x2d8fD575FD19d2d2ca453d4B3A69160F89eb1346"], {'from': acct})
