# operator
Repository for deploying Operator.sol to various EVM-based blockchains

## Environment Variables

You need to setup a .env file in this folder to support the individual scripts.

    export WEB3_INFURA_PROJECT_ID=...
    export ETHERSCAN_TOKEN=...
    export POLYGONSCAN_TOKEN=...

## Before you start

To see a list support networks

    brownie networks list

You need to setup a "deployer" account

    brownie accounts new deployer
    <you'll now be asked for the private key>

## Step 1. Deploy

To deploy run:

    brownie run scripts/mumbai/deploy.py --network polygon-test

## Step 2. Verify

To verify the contract:

    brownie run scripts/mumbai/verify.py --network polygon-test

## Step 3. Permissions

To grant your node access to submit transactions through this Oracle:

    brownie run scripts/mumbai/permissions.py --network polygon-test
    
## Step 4. Deploy test requesting smart contract to interact with operator.sol

    brownie run scripts/deploy.py --network polygon-test
    
## Step 5. Send request to operator.sol

    brownie run scripts/requestBytes.py --network polygon-test
