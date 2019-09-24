def list_format(l, fmt):
  return [ fmt.format(e) for e in l ]

class FilterModule(object):
  def filters(self):
    return {
      'list_format': list_format
    }
