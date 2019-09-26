import functools

def python_filter(data, exp):
  return eval(exp)

def dict2tuples(d):
  return d.items()

class FilterModule(object):
  def filters(self):
    return {
      'python': python_filter,
      'dict2tuples': dict2tuples
    }
