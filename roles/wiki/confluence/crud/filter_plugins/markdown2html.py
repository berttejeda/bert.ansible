#!/usr/bin/python

import markdown2

def markdown2html(md):
  return markdown2.markdown(md)

class FilterModule(object):
    def filters(self):
      return {'markdown2html': markdown2html}