from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0x326C977E6efc84E512bB9C30f76E30c160eD06FB"

    operator = Operator.at("0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    operator.setAuthorizedSenders(
        ["0x67b65DDb04282668Cc2Cb85e9381Da0E249B7258"], {'from': acct})
