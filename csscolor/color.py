# -*- coding: utf-8 -*-
"""The color class."""

import collections
import colorsys

class Color(collections.namedtuple('Color', ('r', 'g', 'b', 'a'))):
	"""An sRGB color.

	RGBA values should be in the range 0.0 - 1.0. CSS and some other
	graphics tools use values in the range 0-255 for RGB, these can
	be returned with the ``.as_int_triple()`` method."""
	__slots__ = ()

	def __new__(Class, r, g, b, a=1.0):
		return super().__new__(Class, r, g, b, a)

	@classmethod
	def from_rgb(Class, r, g, b):
		return Class(r, g, b, a=1.0)

	@classmethod
	def from_rgba(Class, r, g, b, a=1.0):
		return Class(r, g, b, a)

	@classmethod
	def from_int_triple(Class, r, g, b, a=1.0):
		return Class(r/255, g/255, b/255, a)

	@classmethod
	def from_percent_triple(Class, r, g, b, a=1.0):
		return Class(r/100, g/100, b/100, a)

	@classmethod
	def from_rgb24(Class, rgb24, a=1.0):
		return Class.from_int_triple(
			rgb24 // 65536, (rgb24 // 256) % 256, rgb24 % 256, a)

	@classmethod
	def from_hsl(Class, h, s, l):
		return Class.from_hsla(h, s, l, a=1.0)

	@classmethod
	def from_hsla(Class, h, s, l, a=1.0):
		r, g, b = colorsys.hls_to_rgb(h, l, s)
		return Class(r, g, b, a)

	@classmethod
	def from_hsl_int_triple(Class, h, s, l, a=1.0):
		return Class.from_hsla(h/255, s/255, l/255, a)

	@classmethod
	def from_hsl_percent_triple(Class, h, s, l, a=1.0):
		return Class.from_hsla(h/100, s/100, l/100, a)


	# Numeric formats

	def as_int_triple(self):
		"""Returns the r,g,b triple with each value in the range 0-255.

		Any transparency will be ignored.
		"""
		return round(self.r * 255), round(self.g * 255), round(self.b * 255)

	def as_percent_triple(self):
		"""Returns the r,g,b triple with each value an integer ≤ 100.

		Any transparency will be ignored.
		"""
		return round(self.r * 100), round(self.g * 100), round(self.b * 100)

	def as_rgb24(self):
		"""Returns the color as an RGB24 integer."""
		ints = self.as_int_triple()
		return (ints[0] * 256 + ints[1]) * 256 + ints[2]

	def as_hsl(self):
		"""Returns the color as a h,s,l,a tuple with components between 0 and 1.
		"""
		h, l, s = colorsys.rgb_to_hls(self.r, self.g, self.b)
		return h, s, l, self.a

	def as_hsl_int_triple(self):
		"""Returns the h, s, l triple with each value in the range 0-255.

		Any transparency will be ignored.
		"""
		h, s, l, _ = self.as_hsl()
		return round(h * 255), round(s * 255), round(l * 255)

	def as_hsl_percent_triple(self):
		"""Returns the h, s, l triple with each value in the range 0-100.

		Any transparency will be ignored.
		"""
		h, s, l, _ = self.as_hsl()
		return round(h * 100), round(s * 100), round(l * 100)


	# Text formats

	def as_hex_string(self):
		"""Returns the color in CSS hex formatr #xxxxxx.

		Any transparency will be ignored."""
		return '#{:02x}{:02x}{:02x}'.format(*self.as_int_triple())

	def as_rgb_string(self):
		"""Returns the color in CSS rgb format: rgb(r, g, b).

		Color channel values are in the range 0-255."""
		r, g, b = self.as_int_triple()
		return 'rgb({}, {}, {})'.format(r, g, b)

	def as_rgba_string(self):
		"""Returns the color in CSS rgb format: rgba(r, g, b, a).

		Color channel values are in the range 0-255. Alpha is 0-1."""
		r, g, b = self.as_int_triple()
		return 'rgba({}, {}, {}, {})'.format(r, g, b, self.a)

	def as_rgb_percent_string(self):
		"""Returns the color in CSS rgb format: rgb(r%, g%, b%).

		Color channel values are in the range 0-100."""
		r, g, b = self.as_percent_triple()
		return 'rgb({:.0f}%, {:.0f}%, {:.0f}%)'.format(r, g, b)

	def as_rgba_percent_string(self):
		"""Returns the color in CSS rgb format: rgba(r%, g%, b%, a).

		Color channel values are in the range 0-100. Alpha is 0-1."""
		r, g, b = self.as_percent_triple()
		return 'rgba({:.0f}%, {:.0f}%, {:.0f}%, {})'.format(r, g, b, self.a)

	def as_hsl_string(self):
		"""Returns the color in CSS hsl format: hsl(h, s, l).

		Color channel values are in the range 0-255."""
		h, s, l = self.as_hsl_int_triple()
		return 'hsl({}, {}, {})'.format(h, s, l)

	def as_hsla_string(self):
		"""Returns the color in CSS hsl format: hsla(h, s, l, a).

		Color channel values are in the range 0-255. Alpha is 0-1."""
		h, s, l = self.as_hsl_int_triple()
		return 'hsla({}, {}, {}, {})'.format(h, s, l, self.a)

	def as_hsl_percent_string(self):
		"""Returns the color in CSS hsl format: hsl(h%, s%, l%).

		Color channel values are in the range 0-100."""
		h, s, l = self.as_hsl_percent_triple()
		return 'hsl({:.0f}%, {:.0f}%, {:.0f}%)'.format(h, s, l)

	def as_hsla_percent_string(self):
		"""Returns the color in CSS hsl format: hsla(h%, s%, l%, a).

		Color channel values are in the range 0-100. Alpha is 0-1."""
		h, s, l = self.as_hsl_percent_triple()
		return 'hsla({:.0f}%, {:.0f}%, {:.0f}%, {})'.format(h, s, l, self.a)
