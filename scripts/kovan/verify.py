
from brownie import Operator


def main():
    operator = Operator.at(
        "0xf71775b3640D7034466e0321E35c5CFB78fd212F")
    Operator.publish_source(operator)
