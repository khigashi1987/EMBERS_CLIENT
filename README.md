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
   git clone https://github.com/khigashi1987/EMBERS_CLIENT.git
   ```

2. Change to the project directory:
   ```
   cd embers_client
   ```

3. Install the package in editable mode:
   ```
   pip install -e .
   ```

## Usage

Here's a quick example of how to use the EMBERS Client:

```python
from embers_client import EMBERSClient

# Initialize the client
client = EMBERSClient()

# Get sample IDs based on metadata conditions
conditions = {"Age": {"min": 45, "max": 55},
              "BiologicalSex": ["Male"],
              "BMI": {"min":25.0, "max":30.0},
              "GeographicLocation": ["United States", "Japan"]}
sample_ids = client.get_samples(conditions)

# Get composition data for specific sample IDs
composition_df = client.get_composition_by_ids(sample_ids)

# Get composition data based on metadata conditions
composition_df = client.get_composition_by_metadata(conditions)
```

## License

This project is licensed under the MIT License.
