from brownie import GetUint256Test, LinkToken, accounts
from web3 import Web3


def main():

    # customise this section to match your environment
    linkAddress = "0x326C977E6efc84E512bB9C30f76E30c160eD06FB"
    testContractAddress = "0xfAff5705DBD291Fb2b9cE2E5deb4e295E66595F3"
    payment = 50000000000000000
    oracleAddress = "0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434"
    jobId = "7599d3c8f31e4ce78ad2b790cbcfc673"

    acct = accounts.load('deployer')
    linkToken = LinkToken.at(linkAddress)
    linkToken.transfer(testContractAddress, payment, {'from': acct})

    test = GetUint256Test.at(testContractAddress)
    test.requestValue(
        oracleAddress,
        jobId,
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD",
        1000,
        "RAW,ETH,USD,PRICE",
        payment,
        {'from': acct})
