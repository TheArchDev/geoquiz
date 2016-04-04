from django import template

register = template.Library()

@register.filter(name='array_index')
def return_array_element_by_index(array, index):
	try:
		return array[index]
	except:
		return 2

@register.filter(name='dot_parameter')
def dot_parameter(variable, parameter):
	try:
		return getattr(variable,parameter)
	except:
		return None