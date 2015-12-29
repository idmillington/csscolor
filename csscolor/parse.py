# -*- coding: utf-8 -*-
"""Parsing color values."""

import re
from .color import Color
from . import colors as names

def color(color_string):
	"""Parse colors conforming to the CSS 3 color specification.

	The CSS 3 Color module supports the following formats:

	- papayawhip
	- #369
	- #336699
	- rgb(153, 102, 51)
	- rgba(153, 102, 51, 0.5)
	- rgb(60%, 40%, 20%)
	- rgba(60%, 40%, 20%, 0.5)
	- hsl(128, 128, 102)
	- hsla(128, 128, 102, 0.5)
	- hsl(50%, 50%, 40%)
	- hsla(50%, 50%, 40%, 0.5)

	The following additional formats are supported:

	- 0x336699 # Python style hex values
	- rgb(0.6, 0.4, 0.2)
	- rgba(0.6, 0.4, 0.2, 0.5)
	- hsl(0.5, 0.5, 0.4)
	- hsla(0.5, 0.5, 0.4, 0.5)

	where the decimal is required, so

	- rgb(1.0, 1.0, 1.0) # white
	- rgb(1, 1, 1) # almost black
	"""
	color_string = color_string.strip()

	# Try hexes
	if color_string.startswith('#'):
		result = __from_hex(color_string[1:])
	elif color_string.startswith('0x'):
		result = __from_hex(color_string[2:])
	else:
		# Try component style values.
		result = __from_components(color_string)
		if not result:
			# Try color names.
			result = getattr(names, color_string.lower(), None)

	if result is None:
		raise ValueError("Unknown color.")
	return result

# -----------------------------------------------------------------------
# Internals
# -----------------------------------------------------------------------

def __from_components(color_string):
	match = __csscolor_component_re.match(color_string)
	if match:
		# Try to break apart the components.
		components = match.group(3).split(',')
		num_components = len(components)
		required = 4 if match.group(2) else 3
		if num_components != required:
			raise ValueError("Wrong number of components in the definition.")

		# Convert each component into a 0-1 value.
		component_values = [
			__get_component_value(components[0]),
			__get_component_value(components[1]),
			__get_component_value(components[2])
			]
		if num_components == 4:
			# Alpha can't be a 256 integer.
			component_values.append(__get_component_value(components[3], True))

		# Build the color
		if match.group(1) == 'rgb':
			return Color(*component_values)
		else:
			return Color.from_hsla(*component_values)
	return None

def __get_component_value(component_string, force_decimal=False):
	component_string = component_string.strip()
	if component_string.endswith('%'):
		factor = 100.0
		component_string = component_string[:-1].strip()
	elif force_decimal or '.' in component_string:
		factor = 1.0
	else:
		factor = 255.0
	return float(component_string) / factor

def __from_hex(color_string):
	color_length = len(color_string)
	if color_length == 3:
		return Color(
			int(color_string[0]*2, 16) / 255.0,
			int(color_string[1]*2, 16) / 255.0,
			int(color_string[2]*2, 16) / 255.0,
			)
	else:
		if color_length != 6:
			raise ValueError("Hex color value of an unknown form.")
		return Color(
			int(color_string[0:2], 16) / 255.0,
			int(color_string[2:4], 16) / 255.0,
			int(color_string[4:6], 16) / 255.0,
			)

__csscolor_component_re = re.compile(r'(hsl|rgb)(a)?\s*\((.*)\)')
