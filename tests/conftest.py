import pytest

from src.core.config_manager import Config
from src.data.enums import Client, Server, AccountType


def pytest_generate_tests(metafunc):
    client = Config.get_value("client")

    if "server" in metafunc.fixturenames:
        servers = metafunc.config.getoption("server").split(",")
        if client == Client.TRANSACTION_CLOUD:
            servers = [Server.MT5]

        metafunc.parametrize("server", servers)

    accounts = Config.get_value("account").split(",")

    if "account" in metafunc.fixturenames:
        # Check for account type markers
        if metafunc.definition.get_closest_marker("not_demo"):
            AccountType.DEMO not in accounts or accounts.remove(AccountType.DEMO)

        if metafunc.definition.get_closest_marker("not_live"):
            AccountType.LIVE not in accounts or accounts.remove(AccountType.LIVE)

        if metafunc.definition.get_closest_marker("not_crm"):
            AccountType.CRM not in accounts or accounts.remove(AccountType.CRM)

        else:
            # If no specific marker, use the accounts from config
            accounts = Config.get_value("account").split(",")

        if client == Client.TRANSACTION_CLOUD:
            AccountType.CRM not in accounts or accounts.remove(AccountType.CRM)

        metafunc.parametrize("account", accounts)


@pytest.fixture(autouse=True)
def server(server):
    return server


@pytest.fixture(autouse=True)
def account(account):
    return account
