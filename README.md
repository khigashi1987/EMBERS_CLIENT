# EMBERS Client

EMBERS Client is a Python package that provides an easy-to-use interface for the EMBERS Project API. It allows users to retrieve sample IDs based on metadata conditions and fetch taxonomic composition data for specified samples.

## Repository Structure

```
embers_client/
│
├── embers_client/
│   ├── __init__.py
│   └── client.py
│
├── tests/
│   └── test_client.py
│
├── setup.py
├── README.md
└── requirements.txt
```

## Installation

To install the EMBERS Client package, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/embers_client.git
   ```

2. Change to the project directory:
   ```
   cd embers_client
   ```

3. Install the package in editable mode:
   ```
   pip install -e .
   ```

This will install the package in "editable" mode, which means you can make changes to the source code and see the effects immediately without having to reinstall the package.

## Usage

Here's a quick example of how to use the EMBERS Client:

```python
from embers_client import EMBERSClient

# Initialize the client
client = EMBERSClient()

# Get sample IDs based on metadata conditions
conditions = {"age": {"min": 20, "max": 30}, "country": ["USA", "Japan"]}
sample_ids = client.get_samples(conditions)

# Get composition data for specific sample IDs
composition_df = client.get_composition_by_ids(sample_ids)

# Get composition data based on metadata conditions
composition_df = client.get_composition_by_metadata(conditions)
```

For more detailed usage instructions, please refer to the documentation in the `client.py` file.

## Development

To set up the development environment:

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

3. Install the development dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the tests:
   ```
   python -m unittest discover tests
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
