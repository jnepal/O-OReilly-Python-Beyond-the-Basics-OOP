import timeit

print(
    'By Index:',
    timeit.timeit(stmt="mydict['c']",
                  setup="mydict = {'a': 5, 'b': 6, 'c': 7}",
                  number=1000000
                  )
      )
print(
    'By Get:',
    timeit.timeit(stmt="mydict.get('c')",
                  setup="mydict = {'a': 5, 'b': 6, 'c': 7}",
                  number=1000000
                  )
      )

def test(mydict, key):
    return mydict[key]

print(
    'test(mydict, key)',
    timeit.timeit(
                  setup="from __main__ import test;"
                        "mydict={'a': 1, 'b': 2, 'c': 3};"
                        "key='c'",
                  number=1000000
                  )
      )