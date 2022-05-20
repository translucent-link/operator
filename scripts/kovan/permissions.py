from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    operator = Operator.at("0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    operator.setAuthorizedSenders(
        ["0xfAec569aF320661E150ae1A2a669F2A04aB9Fd3A"], {'from': acct})
