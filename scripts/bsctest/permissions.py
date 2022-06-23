from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')

    operator = Operator.at("0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    operator.setAuthorizedSenders(
        ["0xbb97Ab9E4c334b68167667f93115B1fE19831f21"], {'from': acct})
