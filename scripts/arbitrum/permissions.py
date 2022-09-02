from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')

    operator = Operator.at("0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    operator.setAuthorizedSenders(
        ["0xe8Dc0b9023B32be568b6E6e26A2Eaaa8Cc89C5C2"], {'from': acct})
