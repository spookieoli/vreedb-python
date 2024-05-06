
import urllib.parse
import httpx
from typing import Optional, Any


class BaseClient:
    def __init__(self, host: Optional[str] = None, timeout: Any = None) -> None:
        """
        Creates a httpx client
        :param host:
        :param timeout:
        """

    def _parse_host(self, host: Optional[str]) -> str:
        """
        Parses a given host
        :param host: str
        :return: parsed host
        """

        host, port = host or '', 8080
        schema, _, hostandport = host.partition('://')
        if not hostandport:
            schema, hostandport = 'http', host
        elif schema == 'http':
            port = 8080
        elif schema == 'https':
            port = 443

        split = urllib.parse.urlsplit('://'.join([schema, hostandport]))
        host = split.hostname or '127.0.0.1'
        port = split.port or port

        return f'{schema}://{host}:{port}'

