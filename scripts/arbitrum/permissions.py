from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')

    operator = Operator.at("0x78075387A6ef71FE0F036f22f1Dc6Ea68C9c3FA1")
    operator.setAuthorizedSenders(
        ["0xe8Dc0b9023B32be568b6E6e26A2Eaaa8Cc89C5C2"], {'from': acct})
