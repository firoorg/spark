import address
from dumb25519 import random_point
from random import randrange
import mint_transaction
import unittest

class TestMint(unittest.TestCase):
	def test_mint(self):
		protocol_params = mint_transaction.ProtocolParameters(random_point(),random_point(),random_point(),4)
		address_params = address.AddressParameters(protocol_params.G,protocol_params.F)

		# Mint data
		_,_,_,_,public = address.generate(address_params)
		value = randrange(0,2**protocol_params.N)
		memo = 'Mint memo'

		# Generate the spend transaction
		transaction = mint_transaction.MintTransaction(
			protocol_params,
			public,
			value,
			memo
		)

		# Verify it
		transaction.verify(
			protocol_params
		)

if __name__ == '__main__':
	unittest.main()