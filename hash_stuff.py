def hash_string(keyword,buckets):
    hash = 0
    for c in keyword:
        hash = (hash + ord(c)) % buckets
    return hash

def make_hashtable(nbuckets):
	table = []
	for n in range(0, nbuckets):
		table.append([])
	return table

def hashtable_getbucket(table, keyword):
	return table[hash_string(keyword, len(table))]

#add was replaced by update, i think
def hashtable_add(table, key, value):
		hashtable_getbucket(table, key).append([key, value])

#def hashtable_update(table, key, value):

def hashtable_lookup(htable, key):
	bucket = hashtable_getbucket(htable, key)
	for entry in bucket:
		if entry[0] == key:
			return entry[1]
	return None


def hashtable_update(htable, key, value):
	bucket = hashtable_getbucket(htable, key)
	for entry in bucket:
		if entry[0] == key:
			entry[1] = value
			return
	bucket.append([key, value])

