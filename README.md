# Flask Contract and Customer API

A simple Flask REST API for managing contracts and customers with basic lookup functionality.

## Description

This application provides two RESTful endpoints to retrieve contract information and verify customer existence. Built as a learning project to demonstrate Flask routing, HTTP status codes, and RESTful API design principles.

## Features

- **Contract Lookup**: Retrieve contract information by ID
- **Customer Verification**: Check if a customer exists in the system
- **RESTful Design**: Proper HTTP status codes (200, 204, 404)
- **Test Coverage**: Comprehensive pytest test suite

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Shobinn24/python-flask-contracts-lab.git
cd python-flask-contracts-lab
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask pytest
```

## Usage

### Running the Application
```bash
python app.py
```

The server will start on `http://localhost:5555`

### API Endpoints

#### Get Contract by ID
```http
GET /contract/<id>
```

**Parameters:**
- `id` (integer): Contract ID

**Responses:**
- `200 OK`: Returns contract information as plain text
- `404 Not Found`: Contract does not exist

**Example:**
```bash
curl http://localhost:5555/contract/1
# Response: "This contract is for John and building a shed"
```

#### Check Customer Exists
```http
GET /customer/<customer_name>
```

**Parameters:**
- `customer_name` (string): Customer name to verify

**Responses:**
- `204 No Content`: Customer exists (empty response body)
- `404 Not Found`: Customer does not exist

**Example:**
```bash
curl -i http://localhost:5555/customer/bob
# Response: HTTP/1.1 204 NO CONTENT
```

## Running Tests

Execute the test suite using pytest:
```bash
pytest -v
```

### Test Coverage

- ✅ Contract route returns 200 for valid ID
- ✅ Contract route returns correct data
- ✅ Contract route returns 404 for invalid ID
- ✅ Customer route returns 204 for valid name
- ✅ Customer route returns empty body
- ✅ Customer route returns 404 for invalid name

## Project Structure
```
.
├── app.py              # Main Flask application
├── app_test.py         # Pytest test suite
├── conftest.py         # Pytest configuration
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Technologies Used

- **Flask**: Web framework for Python
- **pytest**: Testing framework

## Sample Data

### Contracts
```python
[
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]
```

### Customers
```python
["bob", "bill", "john", "sarah"]
```


### Code Standards

- Add comments for complex logic
- Follow PEP 8 style guidelines
- Write tests for new features
- Update README for new endpoints

## Future Enhancements

- [ ] Add POST endpoints for creating contracts/customers
- [ ] Implement database persistence (SQLite/PostgreSQL)
- [ ] Add authentication and authorization
- [ ] Implement pagination for large datasets
- [ ] Add input validation and error handling
- [ ] Create API documentation with Swagger/OpenAPI

## Author

Shobinn Clark - Full-Stack Software Engineering Student at Flatiron School

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Flatiron School for the curriculum and project structure
- Flask documentation for excellent API reference