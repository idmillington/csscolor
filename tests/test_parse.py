# -*- coding: utf-8 -*-
import unittest
from csscolor import parse
from csscolor.color import Color

class TestCSSParse(unittest.TestCase):
	def test_6_digit_hex(self):
		self.assertEqual(
			parse.color('#336699').as_int_triple(),
			Color(0.2, 0.4, 0.6).as_int_triple())

	def test_py_style_hex(self):
		self.assertEqual(
			parse.color('0x336699').as_int_triple(),
			Color(0.2, 0.4, 0.6).as_int_triple())

	def test_3_digit_hex(self):
		self.assertEqual(
			parse.color('#369').as_int_triple(),
			Color(0.2, 0.4, 0.6).as_int_triple())

	def test_name(self):
		self.assertEqual(
			parse.color('papayawhip').as_int_triple(),
			Color.from_int_triple(255, 239, 213).as_int_triple())
		self.assertEqual(parse.color('transparent'), Color(0, 0, 0, 0))

	def test_hsl(self):
		self.assertEqual(
			parse.color('hsl(50%, 50%, 40%)').as_int_triple(),
			Color(0.2, 0.6, 0.6).as_int_triple())
		self.assertEqual(
			parse.color('hsla(50%, 50%, 40%, 0.5)').as_int_triple(),
			Color(0.2, 0.6, 0.6, 0.5).as_int_triple())

	def test_rgb(self):
		self.assertEqual(
			parse.color('rgb(20%, 40%, 60%)'),
			Color(0.2, 0.4, 0.6))
		self.assertEqual(
			parse.color('rgba(20%, 40%, 60%, 0.5)'),
			Color(0.2, 0.4, 0.6, 0.5))

	def test_percent_alpha(self):
		self.assertEqual(
			parse.color('rgba(20%, 40%, 60%, 50%)'),
			Color(0.2, 0.4, 0.6, 0.5))

	def test_decimals(self):
		self.assertEqual(
			parse.color('rgb(1, 1, 1)'),
			Color(1 / 255, 1 / 255, 1 / 255))
		self.assertEqual(
			parse.color('rgb(1.0, 1.0, 1.0)'), Color(1.0, 1.0, 1.0))

	def test_rgba_with_integer_alpha(self):
		"""A non-decimal 1 in the alpha channel should be interpretd as 100%"""
		# Regression.
		self.assertEqual(
			parse.color('rgba(255, 255, 255, 1)'),
			Color(1.0, 1.0, 1.0, 1.0))
