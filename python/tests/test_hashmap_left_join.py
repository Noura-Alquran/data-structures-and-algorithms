from code_challenges.hashmap_left_join.hashmap_left_join import *
import pytest


def test():
  ht_one = HashTable()
  ht_one.add('fond', 'enamored')
  ht_one.add('wrath', 'anger')
  ht_one.add('diligent', 'employed')
  ht_one.add('guide', 'garp')
  ht_one.add('outfit', 'usher')
  ht_two = HashTable()
  ht_two.add('fond', 'averse')
  ht_two.add('wrath', 'delight')
  ht_two.add('diligent', 'idle')
  ht_two.add('guide', 'follow')
  ht_two.add('flow', 'jam')
  assert left_join_hash(ht_one,ht_two).__str__() =="{['diligent', ['employed', 'idle']]} -> None{['outfit', ['usher', None]]} -> None{['fond', ['enamored', 'averse']]} -> None{['guide', ['garp', 'follow']]} -> None{['wrath', ['anger', 'delight']]} -> None"

