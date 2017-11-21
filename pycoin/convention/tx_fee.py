
TX_FEE_PER_THOUSAND_BYTES = 10000


def recommended_fee_for_tx(tx):
    """
    Return the recommended transaction fee in satoshis.
    """

    size = tx.estimated_size()
    tx_fee = int(TX_FEE_PER_THOUSAND_BYTES * size//1000)

    return tx_fee
