import redis

PREFIX = 'trie'
TERMINAL = '+'
r = redis.Redis(db=4)


def add_word(word):
    """This is to be loaded during initial dump and CRUD operations"""
    key = PREFIX + ':'
    pipeline = r.pipeline(True)
    for c in word:
        r.zadd(key, c, ord(c))
        key += c
    r.zadd(key, TERMINAL, 0)
    pipeline.execute()


def suggest(text):
    """this is for typeahead/autocomplete feature in search. Yet to be implemented."""
    for c in r.zrange(PREFIX + ":" + text, 0, -1):
        if c == TERMINAL:
            yield text
        else:
            for t in suggest(text + c):
                yield t
