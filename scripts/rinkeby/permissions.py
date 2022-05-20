from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    operator = Operator.at("0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    operator.setAuthorizedSenders(
        ["0x24E7c03F2b8f50543BC711b334AA12a94D0BE5C6"], {'from': acct})
