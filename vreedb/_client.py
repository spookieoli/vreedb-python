import urllib.parse
import httpx
from typing import Optional, Any, List, Union, Dict


class Client:
    def __init__(self, host: Optional[str] = None, timeout: Any = None, api_key: str = None) -> None:
        """
        Creates a httpx client
        :param host: a host [optional]
        :param timeout: None
        """

        # create client
        self._client = httpx.AsyncClient(base_url=_parse_host(host), timeout=timeout)
        self._api_key = api_key

    async def search(self, limit: Optional[int] = None, vector: List[Union[int, float]] = None,
                     filter: List[Optional[Dict]] = None, index: Optional[Dict] = None) -> Any:
        """
        Search for nearest neighbour in the Database
        :param limit: limit returned vectors
        :param vector: a vector as List
        :param filter: a filter
        :param index: a index
        :return: nearest neighbour
        """
        return await self._client.post('search', json={'api_key': self._api_key, 'limit': limit, 'vector': vector,
                                                       'filter': filter, 'index': index})

    async def create_collection(self, collection_name: str, dist_func: str, dimensions: int) -> Any:
        """
        Create a collection
        :param collection_name: a name for the collection
        :param dist_func: distance function
        :param dimensions: number of dimensions
        :return: collection dict
        """
        return await self._client.post('create_collection',
                                       json={'api_key': self._api_key, 'name': collection_name,
                                             dist_func: dist_func,
                                             dimensions: dimensions})

    async def list_collections(self, collection_name: str) -> Any:
        """
        Gets a collection info object
        :param collection_name: name of the collection
        :return: collection dict
        """
        return await self._client.post('listcollections', json={'api_key': self._api_key})

    async def delete_collection(self, collection_name: str) -> Any:
        """
        Delete a collection
        :param collection_name: name of the collection
        :return: collection dict
        """
        return await self._client.post('deletecollection',
                                       json={'api_key': self._api_key, 'collection_name': collection_name})

    async def add_point(self, collection_name: str, vector: List[Union[int, float]], payload: Optional[Dict],
                        wait: bool) -> Any:
        """
         Add a point to the collection
        :param collection_name: name of the collection
        :param vector: a vector as List
        :param payload: the optional payload
        :param wait: wait for reply or not
        :return: collection dict
        """
        return await self._client.post('addpoint', json={'api_key': self._api_key, 'collection_name': collection_name,
                                                         'vector': vector, 'payload': payload, 'wait': wait})

    async def add_point_batch(self, collection_name: str, vectors: List[Union[int, float]],
                              payloads: Optional[List[Dict]], ids: Optional[List[str]]) -> Any:
        """
        :param collection_name: A string representing the name of the collection where the points will be added.
        :param vectors: A list of integers or floats representing the vectors of the points to be added.
        :param payloads: An optional list of dictionaries representing the payloads associated with each point.
        :param ids: An optional list of strings representing the IDs for each point.
        :return: Returns the result of the API call.

        """
        points = []
        for idx, v in enumerate(vectors):
            points.append({'vector': v, 'id': ids[idx], 'payload': payloads[idx]})

        return await self._client.post('addpointbatch',
                                       json={'api_key': self._api_key, 'collection_name': collection_name,
                                             'points': points})

    async def classify(self, collection_name: str, classifier_name: str, vector: List[Union[int, float]]) -> Any:
        """
        :param collection_name: The name of the collection.
        :param classifier_name: The name of the classifier.
        :param vector: A list of numerical values representing the input vector to be classified.
        :return: The result of the classification.
        """
        return await self._client.post('classify', json={'api_key': self._api_key, 'collection_name': collection_name,
                                                         'classifier_name': classifier_name, 'vector': vector})


def _parse_host(host: Optional[str]) -> str:
    """
        Parses the given host URL and returns the formatted URL string.
        :param host: The host URL to parse.
        :type host: Optional[str]
        :return: The formatted URL string.
        :rtype: str
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
