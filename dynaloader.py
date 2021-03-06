"""
import sys
import requests
"""

def dynaload(path):
  url = "https://raw.githubusercontent.com/{path}".format(**locals())
  req = requests.get(url)
  if req.status_code != 200:
    sys.stderr.write("Error loading {url}:\n".format(**locals()))
    for name in vars(req):
      value = getattr(req, name)
      sys.stderr.write("  {name}: {value}\n".format(**locals()))
    exit(1)
  return req.text.replace('"__main__"', '"__static_main__"')