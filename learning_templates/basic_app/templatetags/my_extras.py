from django import template

register=template.Library() # a library instance so that our filter is available in django template language

@register.filter(name='cutter')
def cutter(value, arg):
  """ This method cuts out all values of "arg" from the value """
  return value.replace(arg,'')

# # Now we are supposed to register our filter for django to be able to reference it.
# register.filter('cut',cut) # this goes as 'LibraryInstance.filter('Name of filter as string', actual function name)

