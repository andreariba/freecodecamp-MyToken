from brownie import network, accounts, config


DEVELOPMENT_BLOCKCHAINS = ["mainnet-fork", "development"]


def get_account(index=0):

    active_network = network.show_active()

    if active_network not in DEVELOPMENT_BLOCKCHAINS:
        return accounts.load(config["networks"][active_network]["account"])

    return accounts[index]
