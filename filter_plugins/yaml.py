import yaml

def dump_yaml(d):
  return yaml.dump(d)

class FilterModule(object):
  def filters(self):
    return {
      'yaml': dump_yaml
    }
