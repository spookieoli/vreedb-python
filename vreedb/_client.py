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
        self._client = httpx.Client(base_url=_parse_host(host), timeout=timeout)
        self._api_key = api_key

    def search(self, collection_name: str, limit: Optional[int] = None, vector: List[Union[int, float]] = None,
               filter: List[Optional[Dict]] = None, index: Optional[Dict] = None) -> str:
        """
        Perform a search operation with the specified parameters.

        :param collection_name: The name of the collection to search in. (str)
        :param limit: The maximum number of results to return. (Optional[int])
        :param vector: The input vector for similarity search. (List[Union[int, float]])
        :param filter: The filter conditions to apply to the search. (List[Optional[Dict]])
        :param index: The index option to use for the search. (Optional[Dict])
        :return: The search results. (Any)

        """
        return self._client.post('search',
                                 json={'api_key': self._api_key, 'collection_name': collection_name, 'limit': limit,
                                       'vector': vector,
                                       'filter': filter, 'index': index}).text

    def create_collection(self, collection_name: str, dist_func: str, dimensions: int) -> str:
        """
        Create a collection
        :param collection_name: a name for the collection
        :param dist_func: distance function
        :param dimensions: number of dimensions
        :return: collection dict
        """
        return self._client.post('create_collection',
                                 json={'api_key': self._api_key, 'name': collection_name,
                                       dist_func: dist_func,
                                       dimensions: dimensions}).text

    def list_collections(self, collection_name: str) -> Any:
        """
        Gets a collection info object
        :param collection_name: name of the collection
        :return: collection dict
        """
        return self._client.post('listcollections', json={'api_key': self._api_key}).json()

    def delete_collection(self, collection_name: str) -> Any:
        """
        Delete a collection
        :param collection_name: name of the collection
        :return: collection dict
        """
        return self._client.post('deletecollection',
                                 json={'api_key': self._api_key, 'collection_name': collection_name}).json()

    def add_point(self, collection_name: str, vector: List[Union[int, float]], payload: Optional[Dict],
                  wait: bool) -> Any:
        """
         Add a point to the collection
        :param collection_name: name of the collection
        :param vector: a vector as List
        :param payload: the optional payload
        :param wait: wait for reply or not
        :return: collection dict
        """
        return self._client.post('addpoint', json={'api_key': self._api_key, 'collection_name': collection_name,
                                                   'vector': vector, 'payload': payload, 'wait': wait}).json()

    def add_point_batch(self, collection_name: str, vectors: List[Union[int, float]],
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

        return self._client.post('addpointbatch',
                                 json={'api_key': self._api_key, 'collection_name': collection_name,
                                       'points': points}).json()

    def classify(self, collection_name: str, classifier_name: str, vector: List[Union[int, float]]) -> Any:
        """
        :param collection_name: The name of the collection.
        :param classifier_name: The name of the classifier.
        :param vector: A list of numerical values representing the input vector to be classified.
        :return: The result of the classification.
        """
        return self._client.post('classify', json={'api_key': self._api_key, 'collection_name': collection_name,
                                                   'classifier_name': classifier_name, 'vector': vector}).json()


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
