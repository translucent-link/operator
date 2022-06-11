import time
from brownie import RequestGetBytes, accounts

def main():
    account = accounts.load("deployer")
    requestGetBytes = RequestGetBytes.at("testBytesJobSpec_smart_contract_address")
    requestGetBytes.requestBytes({"from": account})

    #wait for the direct request to be processed by the chainlink node
    sleepSeconds = int(60)
    print("Waiting {} seconds for the request to be fulfilled by the associated Chainlink node".format(sleepSeconds))
    time.sleep(sleepSeconds)

    returnedBytes = requestGetBytes.data()
    returnedString = requestGetBytes.image_url()
    print("data: {}".format(returnedBytes))
    print("image_url: {}".format(returnedString))
