def get_address_info(address):
    """
    Get address information from the blockchain.

    Args:
        address (str): The address to get information for.

    Returns:
        tuple: A tuple containing the address, the total number of transactions associated with the address, and the total amount of money spent from the address.
    """

    # Get the address information from the blockchain.
    address_info = blockchain.get_address_info(address)

    # Get the total number of transactions associated with the address.
    total_txs = len(address_info["transactions"])

    # Get the total amount of money spent from the address.
    total_spent = sum([tx["amount"] for tx in address_info["transactions"]])

    # Return the address, the total number of transactions associated with the address, and the total amount of money spent from the address.
    return address, str(total_txs), str(total_spent)
