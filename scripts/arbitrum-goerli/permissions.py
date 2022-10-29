from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    operator = Operator.at("0x2362A262148518Ce69600Cc5a6032aC8391233f5")
    operator.setAuthorizedSenders(
        ["0xFABc896b7FB08EaB9680E69d2B994AB279d05b3C"], {'from': acct})
