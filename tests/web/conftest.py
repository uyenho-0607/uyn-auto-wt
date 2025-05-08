from src.core.config_manager import Config
from src.data.enums import Client, Server


def pytest_generate_tests(metafunc):
    client = Config.get_value("client")
    if "server" in metafunc.fixturenames:
        servers = metafunc.config.getoption("server").split(",")
        if client == Client.TRANSACTION_CLOUD:
            servers = [Server.MT5]

        metafunc.parametrize("server", servers)

    if "account" in metafunc.fixturenames:
        accounts = metafunc.config.getoption("account").split(",")
        metafunc.parametrize("account", accounts)

    # if "client" in metafunc.fixturenames:
    #     clients = metafunc.config.getoption("client").split(",")
    #     metafunc.parametrize("client", clients)
