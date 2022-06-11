from brownie import RequestGetBytes, accounts

def main():
    account = accounts.load("deployer")
    requestGetBytes = RequestGetBytes.deploy({"from": account})
