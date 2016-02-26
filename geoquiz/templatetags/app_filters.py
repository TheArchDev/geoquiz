from django import template

register = template.Library()

@register.filter(name='return_array_element_by_index')
def return_array_element_by_index(array, index):
	try:
		return array[index]
	except:
		return None