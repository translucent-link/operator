//SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract RequestGetBytes is ChainlinkClient {
  using Chainlink for Chainlink.Request;

  // variable bytes returned in a single oracle response
  bytes public data;
  string public image_url;

  constructor(
  ) {
    setChainlinkToken(LINK_TOKEN_ADDRESS);
    setChainlinkOracle(OPERATOR_ADDRESS);
  }

  function requestBytes(
  )
    public
  {
    bytes32 specId = "JOB_ID";
    uint256 payment = 0;
    Chainlink.Request memory req = buildChainlinkRequest(specId, address(this), this.fulfillBytes.selector);
    req.add("get","https://ipfs.io/ipfs/QmZgsvrA1o1C8BGCrx6mHTqR1Ui1XqbCrtbMVrRLHtuPVD?filename=big-api-response.json");
    req.add("path", "image");
    sendOperatorRequest(req, payment);
  }

  event RequestFulfilled(
    bytes32 indexed requestId,
    bytes indexed data
  );

  function fulfillBytes(
    bytes32 requestId,
    bytes memory bytesData
  )
    public
    recordChainlinkFulfillment(requestId)
  {
    emit RequestFulfilled(requestId, bytesData);
    data = bytesData;
    image_url = string(data);
  }

}
