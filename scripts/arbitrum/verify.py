
from brownie import Operator


def main():
    operator = Operator.at(
        "0x78075387A6ef71FE0F036f22f1Dc6Ea68C9c3FA1")
    Operator.publish_source(operator)
