import functools

def python_filter(data, exp):
  return eval(exp)

class FilterModule(object):
  def filters(self):
    return {
      'python': python_filter
    }
