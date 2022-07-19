// SPDX-License-Identifier: MIT
// Deployed Mainnet @ 0xBeCBf3ccC03592979dD032d7d60f77c409095e0A
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";

contract GetUint256Test is ChainlinkClient, ConfirmedOwner {
    using Chainlink for Chainlink.Request;

    uint256 public value;

    event RequestValue(bytes32 indexed requestId, uint256 indexed value);

    constructor(address linkTokenAddress) ConfirmedOwner(msg.sender) {
        setChainlinkToken(linkTokenAddress);
    }

    function requestValue(
        address _oracle,
        string memory _jobId,
        string memory _url,
        int256 _multiply,
        string memory _path,
        uint256 _payment
    ) public onlyOwner {
        Chainlink.Request memory req = buildChainlinkRequest(
            stringToBytes32(_jobId),
            address(this),
            this.fulfillValue.selector
        );
        req.add("get", _url);
        req.add("path", _path);
        req.addInt("multiply", _multiply);
        sendChainlinkRequestTo(_oracle, req, _payment);
    }

    function fulfillValue(bytes32 _requestId, uint256 _value)
        public
        recordChainlinkFulfillment(_requestId)
    {
        emit RequestValue(_requestId, _value);
        value = _value;
    }

    function stringToBytes32(string memory source)
        private
        pure
        returns (bytes32 result)
    {
        bytes memory tempEmptyStringTest = bytes(source);
        if (tempEmptyStringTest.length == 0) {
            return 0x0;
        }

        assembly {
            // solhint-disable-line no-inline-assembly
            result := mload(add(source, 32))
        }
    }
}
