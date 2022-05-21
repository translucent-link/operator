from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')

    operator = Operator.at("0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    operator.setAuthorizedSenders(
        ["0x1Abc1de91F50c7f4179E8DE292E9f5cD2b24c434"], {'from': acct})
