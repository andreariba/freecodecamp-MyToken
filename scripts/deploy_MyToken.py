from brownie import MyToken, network, config

from scripts.utility import get_account


def deploy_MyToken():

    account = get_account()

    active_network = network.show_active()

    my_token = MyToken.deploy(
        {"from": account},
        publish_source=config["networks"][active_network].get("verify", False),
    )

    print(my_token)


def main():
    deploy_MyToken()
    return
