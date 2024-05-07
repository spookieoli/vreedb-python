# vreedb-python

**Short description**: This project is a Python library that provides a `Client` class for managing operations with VreeDB. Python 3.10.12, as well as several other packages, are used in the project.

## Classes and Functions

### Class `Client`

The `Client` class is the main class in this project, which comprises several methods to add, delete, and manage data via an API.

It contains the following methods:

- **search**: Allows searching in the data.

- **create_collection**: Creates a new data collection.

- **list_collections**: Lists all the existing data collections.

- **delete_collection**: Deletes a specific data collection identified by a unique name.

- **add_point**: Adds a data point to a specific collection.

- **add_point_batch**: Allows batch insertion of data points into a specific collection.

- **classify**: Classifies the provided data based on the existing collections.

It also has the following instance attributes:

- `_api_key`: Stores the API key for connecting to the API. 

- `_client`: Stores the client instance for performing API operations.

### Function `_parse_host`

This helper function is used for parsing the host information.


## Installation

git clone https://github.com/spookieoli/vreedb-python

pip install .
