def is_list(l):
  return isinstance(l, list)

class FilterModule(object):
  def filters(self):
    return {
      'is_list': is_list
    }
