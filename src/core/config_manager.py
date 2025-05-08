from typing import Any, Dict, Literal, Optional

import yaml

from src.data.consts import CONFIG_DIR
from src.data.enums import URLPaths, SiteURLs, Server, AccountType
from src.utils import DotDict


class ClientConfig:
    def __init__(self, config_data: Dict[str, Any]):
        self._config = DotDict(config_data)

    def credentials(
            self,
            server_type: Server = Server.MT4,
            account_type: AccountType = AccountType.LIVE,
            root=False
    ) -> Dict[str, str]:
        """Get credentials for a specific server type and account type."""

        if root:
            return DotDict(
                username=ConfigManager.config.get("user_root"),
                password=ConfigManager.config.get("password")
            )

        credentials = self._config.get("credentials", {}).get(server_type, {})
        return DotDict(
            username=credentials.get(f"user_{account_type}"),
            password=credentials.get(f"password_{account_type}")
        )

    def url(self, site: SiteURLs = SiteURLs.MEMBER_SITE) -> str:
        """Get URL for a specific site (memberSite, adminPortal, rootAdmin)."""

        if site == SiteURLs.ROOT_ADMIN:
            return ConfigManager.config.get("root_url")

        return self._config.get(f"{site}_url", "")

    def url_path(self, path: URLPaths) -> str:
        """Get full URL including path."""
        base_url = self._config.get("base_url", "")

        if path == URLPaths.TRADE:
            return base_url

        return f"{base_url}/{path}"

    @property
    def mobile_config(self):
        return DotDict(self._config.mobile)


class ConfigManager:
    config: Dict[str, Any] = {}
    _instance = None
    _loaded = False
    _client_config: Optional[ClientConfig] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance

    @classmethod
    def load_config(cls, env: str = "sit"):
        if cls._loaded:
            return cls

        config_file = CONFIG_DIR / f"{env}.yaml"
        with open(config_file, "r") as f:
            cls.config = DotDict(yaml.safe_load(f))
        cls._loaded = True

        # Initialize client config if client is set
        if "client" in cls.config:
            cls._client_config = cls.get_client_config(cls.config.client)

        return cls

    @classmethod
    def get_client_config(cls, client: Literal["lirunex", "transactionCloud"]) -> ClientConfig:
        """Get the configuration for a specific client."""
        if not cls._loaded:
            cls.load_config()
        return ClientConfig(cls.config.get(client, {}))

    @classmethod
    def get_credentials(cls, server_type: Server = Server.MT4, account_type: AccountType = AccountType.LIVE) -> Dict[
        str, str]:
        """Get credentials for the current client configuration."""
        if not cls._client_config:
            if not cls._loaded or "client" not in cls.config:
                raise ValueError("Client configuration not initialized. Call load_config() first.")
            cls._client_config = cls.get_client_config(cls.config.client)
        return cls._client_config.credentials(server_type, account_type)

    @classmethod
    def get_url_site(cls, site: SiteURLs = SiteURLs.MEMBER_SITE):
        if not cls._client_config:
            if not cls._loaded or "client" not in cls.config:
                raise ValueError("Client configuration not initialized. Call load_config() first.")

            cls._client_config = cls.get_client_config(cls.config.client)
        return cls._client_config.url(site)

    @classmethod
    def get_url_path(cls, url_path: URLPaths):
        if not cls._client_config:
            if not cls._loaded or "client" not in cls.config:
                raise ValueError("Client configuration not initialized. Call load_config() first.")

            cls._client_config = cls.get_client_config(cls.config.client)
        return cls._client_config.url_path(url_path)

    @classmethod
    def get_mobile_config(cls):
        if not cls._client_config:
            if not cls._loaded or "client" not in cls.config:
                raise ValueError("Client configuration not initialized. Call load_config() first.")

            cls._client_config = cls.get_client_config(cls.config.client)

        return cls._client_config.mobile_config

    @classmethod
    def set_value(cls, key: str, value):
        cls.config[key] = value
        # Update client config if client is changed
        if key == "client":
            cls._client_config = cls.get_client_config(value)

    @classmethod
    def get_value(cls, key: str):
        return cls.config.get(key, None)


# Create a global instance
Config = ConfigManager()
