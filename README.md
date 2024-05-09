# vreedb-python

This Python code defines a `Client` class for creating an HTTP client for the VreeDB Vector Database and performing various operations on a server. 
This client can be used to manage specific collections and their data. The operations include creating collections, adding points, searching, listing, and deleting collections. 

## Methods Included

### `Client(self, host: Optional[str] = None, timeout: Any = None, api_key: str = None)`

This method is the constructor of the `Client` class. It creates an httpx client.

- `host`: An optional string representing the host's address.
- `timeout`: The HTTP request timeout limit.
- `api_key`: A string representing the API Key for the server.

### `search(self, collection_name: str, limit: Optional[int] = None, vector: List[Union[int, float]] = None, filter: List[Optional[Dict]] = None, index: Optional[Dict] = None)`

This method performs a search operation in the specified collection.

- `collection_name`: A string representing the collection's name to search in.
- `limit`: An optional integer representing the maximum number of results to return.
- `vector`: An input list of integers/floats representing the vector for similarity search.
- `filter`: An optional list of dictionaries representing the filter conditions to apply to the search.
- `index`: An optional dictionary to use for the search.

### `create_collection(self, collection_name: str, dist_func: str, dimensions: int)`

This method creates a new collection with the specified parameters.

- `collection_name`: A string representing the name for the new collection.
- `dist_func`: A string representing the distance function for the calculations in the new collection.
- `dimensions`: An integer representing the number of dimensions for the distance function.

### `list_collections(self, collection_name: str)`

This method retrieves a list of all the collections present on the server.

### `delete_collection(self, collection_name: str)`

This method deletes the specified collection from the server.

### `add_point(self, collection_name: str, vector: List[Union[int, float]], payload: Optional[Dict], wait: bool)`

This function adds a point to the specified collection.

- `collection_name`: A string representing the collection's name.
- `vector`: A list representing the point to be added.
- `payload`: An optional dictionary representing the additional data associated with the point.
- `wait`: A Boolean indicating whether the function should wait for the operation to complete before returning.

### `add_point_batch(self, collection_name: str, vectors: List[Union[int, float]], payloads: Optional[List[Dict]], ids: Optional[List[str]])`

This method adds a batch of points to the specified collection.

- `collection_name`: A string representing the collection's name.
- `vectors`: A list of points to be added.
- `payloads`: An optional list of dictionaries representing the data associated with each point.
- `ids`: An optional list of strings representing the IDs for each point.

### `classify(self, collection_name: str, classifier_name: str, vector: List[Union[int, float]])`

This method applies classification on the provided input vector.

- `collection_name`: A string representing the collection's name.
- `classifier_name`: A string representing the classifier's name.
- `vector`: A list of numerical values representing the input vector to be classified.

In addition to these methods, there is a helper function, `_parse_host(self, host: Optional[str])`, that parses the host URL and returns a formatted URL string.
