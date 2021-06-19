from hashtable.hashtable import *

# Adding a key/value to your hashtable results in the value being in the data structure
def test_add_to_hash_table():
    hash_table=HashTable()
    actual = hash_table.add('Noura','she is dressed in strength')
    expected="{['Noura', 'she is dressed in strength']} -> None"
    assert actual == expected

# Retrieving based on a key returns the value stored
def test_get_hash_table():
    hash_map=HashTable()
    hash_map.add('Noura','love python')
    expected='love python'
    actual=hash_map.get('Noura')
    assert actual == expected


# Successfully returns null for a key that does not exist in the hashtable
def test_not_exist_key():
    hash_map=HashTable()
    hash_map.add('Noura','love python')
    expected=None
    actual=hash_map.get('Manar')
    assert actual == expected


# Successfully handle a collision within the hashtable
def test_handle_collisons():
    expected = "{['Noura', 'Faten']} -> {['ouraN', 'Tala']} -> None"
    hashtable = HashTable()
    hashtable.add('Noura','Faten')
    hashtable.add('ouraN','Tala')
    actual = hashtable.__str__()
    assert actual == expected


# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_get_value_for_collisons_bucket():
    expected = ['Faten','Tala']
    hashtable = HashTable()
    hashtable.add('Noura','Faten')
    hashtable.add('ouraN','Tala')
    actual = [hashtable.get('Noura'),hashtable.get('ouraN')]
    assert actual == expected

# Successfully hash a key to an in-range value
def test_hash():
    hash=HashTable()
    expected=435
    actual=hash.hash('Noura')
    assert actual == expected






