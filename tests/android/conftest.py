

def pytest_generate_tests(metafunc):

    if "server" in metafunc.fixturenames:
        servers = metafunc.config.getoption("server").split(",")
        metafunc.parametrize("server", servers)

    if "account" in metafunc.fixturenames:
        accounts = metafunc.config.getoption("account").split(",")
        metafunc.parametrize("account", accounts)

    # if "client" in metafunc.fixturenames:
    #     clients = metafunc.config.getoption("client").split(",")
    #     metafunc.parametrize("client", clients)
