from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')

    operator = Operator.at("0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    operator.setAuthorizedSenders(
        ["0x806b703FDa1c8F524D574CEb6C25C62D4442ab97"], {'from': acct})
