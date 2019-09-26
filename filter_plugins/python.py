import functools

def python_filter(data, exp):
  return eval(exp)

def dict2tuples(d):
  return [ (k, d[k]) for k in d.keys() ]

class FilterModule(object):
  def filters(self):
    return {
      'python': python_filter,
      'dict2tuples': dict2tuples
    }
