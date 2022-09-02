# operator
Repository for deploying Operator.sol to various EVM-based blockchains

## Environment Variables

You need to setup a .env file in this folder to support the indidual scripts.

    WEB3_INFURA_PROJECT_ID=...
    ETHERSCAN_TOKEN=...
    POLYGONSCAN_TOKEN=...

## Before you start

To see a list support networks

    brownie networks list

You need to setup a "deployer" account

    brownie accounts new deployer
    <you'll now be asked for the private key>

## Step 1. Deploy

To deploy run:

    brownie run scripts/mumbai/deploy.py --network polygon-test
    brownie run scripts/arbitrum/deploy.py --network arbitrum-main

## Step 2. Verify

To verify the contract:

    brownie run scripts/mumbai/verify.py --network polygon-test
    brownie run scripts/arbitrum/verify.py --network arbitrum-main

## Step 3. Permissions

To grant your node access to submit transactions through this Oracle:

    brownie run scripts/mumbai/permissions.py --network polygon-test
    brownie run scripts/arbitrum/permissions.py --network arbitrum-main

## Testing your node with Get > Uint256

Assuming you've got a Get > Uint256 job deployed to the node you can run the test contract and script to test the job execution.

First deploy the test client contract:

    brownie run scripts/mumbai/test_deploy.py --network polygon-test

Then customise the test_run.py script to match your environment, before running run it:

    brownie run scripts/mumbai/test_run.py --network polygon-test


## Support & Help

Feel free to open a [Github Issue](https://github.com/translucent-link/stonechat/issues) or come find us in the [Translucent Discord](https://discord.gg/JxKT6R9Xpz).
