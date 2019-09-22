def is_list(l):
  return isinstance(l, list)

def is_dict(d):
  return isinstance(d, dict)

class FilterModule(object):
  def filters(self):
    return {
      'is_list': is_list,
      'is_dict': is_dict
    }
