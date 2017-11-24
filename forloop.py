from itertools import imap
from operator import itemgetter



l=[{'m':1},{'m':11},{'m':12},{'m':13},{'m':14}]


v=list(imap(itemgetter('m'), l))

print v