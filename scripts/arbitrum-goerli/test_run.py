from brownie import GetUint256Test, LinkToken, accounts, convert
from web3 import Web3


def main():

    # customise this section to match your environment
    testContractAddress = "0xdA1390f5bb86dC26D9A70CFCDd799719Cb93e1Ec"
    linkAddress = "0x326C977E6efc84E512bB9C30f76E30c160eD06FB"
    payment = 50000000000000000
    oracleAddress = "0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434"
    jobId = "7599d3c8f31e4ce78ad2b790cbcfc673"
    print(jobId)
    print(convert.to_bytes(jobId))

    acct = accounts.load('deployer')
    linkToken = LinkToken.at(linkAddress)
    linkToken.transfer(testContractAddress, payment, {'from': acct})

    test = GetUint256Test.at(testContractAddress)
    test.requestValue(
        oracleAddress,
        convert.to_bytes(jobId),
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD",
        1000,
        "RAW,ETH,USD,PRICE",
        payment,
        {'from': acct})
