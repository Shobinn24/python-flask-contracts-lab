#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>')
def get_contract(id):
    """
    Retrieve contract information by ID.
    
    Returns:
        200: Contract information as plain text if found
        404: Not found if the contract ID does not exist
    """
    # Search through contracts list to find matching ID
    for contract in contracts:
        if contract["id"] == id:
            # Return just the contract_information string with 200 status
            return contract["contract_information"], 200
    # If no matching contract is found, return 404
    return "Contract not found", 404

@app.route('/customer/<string:customer_name>')
def get_customer(customer_name):
    """
    Retrieve customer information by name.
    
    Returns:
        204: Customer name as plain text if found
        404: Not found if the customer name does not exist
    """
    # Check if the customer name exists in the customers list
    if customer_name in customers:
        return customer_name, 204
    else:
        return "Customer not found", 404
   
if __name__ == '__main__':
    app.run(port=5555, debug=True)
