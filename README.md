
### Examples
	altcoin price
	altcoin --only price
	altcoin price DOGE
	altcoin price --exchange bittrex DOGE
	
	altcoin --only price --exchange bittrex dash && altcoin --only price --exchange bittrex doge
	
	altcoin price --exchange bittrex doge && altcoin cmc --param marketCap doge && altcoin cmc --param volume24 doge
	
	altcoin cmc --param marketCap doge && altcoin cmc --param volume24 doge && altcoin cmc --param change7h doge && altcoin cmc --param position doge && altcoin cmc --param price doge && altcoin cmc --param name doge
