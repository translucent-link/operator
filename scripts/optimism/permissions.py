from brownie import Operator,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')

    operator = Operator.at("0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    operator.setAuthorizedSenders(
        ["0x433fd57c9C8e3750Fda5bDA85168a2dAaEFc79E1"], {'from': acct})
