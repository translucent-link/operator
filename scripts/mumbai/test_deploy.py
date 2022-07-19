from brownie import GetUint256Test,  accounts
from web3 import Web3


def main():
    acct = accounts.load('deployer')
    linkAddress = "0x326C977E6efc84E512bB9C30f76E30c160eD06FB"

    test = GetUint256Test.deploy(
        linkAddress,
        {'from': acct}
    )
