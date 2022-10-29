
from brownie import Operator


def main():
    operator = Operator.at(
        "0x2362A262148518Ce69600Cc5a6032aC8391233f5")
    Operator.publish_source(operator)
