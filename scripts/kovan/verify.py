
from brownie import Operator


def main():
    operator = Operator.at(
        "0x188b71C9d27cDeE01B9b0dfF5C1aff62E8D6F434")
    Operator.publish_source(operator)
