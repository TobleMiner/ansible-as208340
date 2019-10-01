from copy import deepcopy

class FilterModule(object):
  def filters(self):
    return {
      'deepcopy': deepcopy
    }
