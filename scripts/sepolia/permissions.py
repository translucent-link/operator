from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    operator = Operator.at("0x2362A262148518Ce69600Cc5a6032aC8391233f5")
    operator.setAuthorizedSenders(
        ["0x1B4315a4F09733c19d6ff4fF7Eb3b7DD161f4E8b"], {'from': acct})
