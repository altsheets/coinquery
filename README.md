# coinquery
Work in progress - NOT READY.

### Problem: custom setup.py not working yet.

See [README-setupCustom.md](README-setupCustom.md).

---
---
---
---

from here onwards: **Not** ready.

### Examples
	coinq
	coinq --help
	 
	coinq price
	coinq --only price
	
	coinq price DOGE
	coinq price --exchange bittrex DOGE
	
	coinq --only price --exchange bittrex dash && coinq --only price --exchange bittrex doge
	
	coinq price --exchange bittrex doge && coinq cmc --param marketCap doge && coinq cmc --param volume24 doge
	
	coinq cmc --param marketCap doge && coinq cmc --param volume24 doge && coinq cmc --param change7h doge && coinq cmc --param position doge && coinq cmc --param price doge && coinq cmc --param name doge
