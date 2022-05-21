from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    operator = Operator.at("0xf71775b3640D7034466e0321E35c5CFB78fd212F")
    operator.setAuthorizedSenders(
        ["0xfAec569aF320661E150ae1A2a669F2A04aB9Fd3A"], {'from': acct})
