# -*- coding: utf-8 -*-
import unittest

from csscolor.color import Color

class TestColor(unittest.TestCase):
	def test_from_hsl(self):
		self.assertEqual(
			Color.from_hsl(0.5, 0.5, 0.4).as_int_triple(),
			Color(0.2, 0.6, 0.6).as_int_triple())

	def test_from_hsl_percent(self):
		self.assertEqual(
			Color.from_hsl_percent_triple(50, 50, 40).as_int_triple(),
			Color(0.2, 0.6, 0.6).as_int_triple())

	def test_from_hsl_integer(self):
		self.assertEqual(
			Color.from_hsl_int_triple(0, 255, 102).as_int_triple(),
			Color(0.8, 0.0, 0.0).as_int_triple())

	def test_from_int_triple(self):
		self.assertEqual(
			Color.from_int_triple(0xcc, 0x99, 0x33).as_int_triple(),
			(204, 153, 51))
		self.assertEqual(
			Color.from_int_triple(0xcc, 0x99, 0x33, 0.5).as_int_triple(),
			(204, 153, 51))

	def test_from_rgb24(self):
		self.assertEqual(Color.from_rgb24(0xcc9933).as_rgb24(), 0xcc9933)
		self.assertEqual(Color.from_rgb24(0xcc9933, 0.5).as_rgb24(), 0xcc9933)

	def test_int_triple(self):
		self.assertEqual(
			Color(0.8, 0.6, 0.2).as_int_triple(), (204, 153, 51))
		self.assertEqual(
			Color(0.8, 0.6, 0.2, 0.5).as_int_triple(), (204, 153, 51))

	def test_hex_string(self):
		self.assertEqual(Color(0.8, 0.6, 0.2).as_hex_string(), '#cc9933')
		self.assertEqual(Color(0.8, 0.6, 0.2, 0.5).as_hex_string(), '#cc9933')

	def test_rgb_string(self):
		self.assertEqual(
			Color(0.8, 0.6, 0.2).as_rgb_string(),
			'rgb(204, 153, 51)')
		self.assertEqual(
			Color(0.8, 0.6, 0.2, 0.5).as_rgb_string(),
			'rgb(204, 153, 51)')

	def test_rgba_string(self):
		self.assertEqual(
			Color(0.8, 0.6, 0.2).as_rgba_string(),
			'rgba(204, 153, 51, 1.0)')
		self.assertEqual(
			Color(0.8, 0.6, 0.2, 0.5).as_rgba_string(),
			'rgba(204, 153, 51, 0.5)')
		self.assertEqual(
			Color(0.8, 0.6, 0.2, 0.0).as_rgba_string(),
			'rgba(204, 153, 51, 0.0)')

	def test_rgb_percent_string(self):
		self.assertEqual(
			Color(0.8, 0.6, 0.2).as_rgb_percent_string(),
			'rgb(80%, 60%, 20%)')
		self.assertEqual(
			Color(0.8, 0.6, 0.2, 0.5).as_rgb_percent_string(),
			'rgb(80%, 60%, 20%)')

	def test_rgba_percent_string(self):
		self.assertEqual(
			Color(0.8, 0.6, 0.2).as_rgba_percent_string(),
			'rgba(80%, 60%, 20%, 1.0)')
		self.assertEqual(
			Color(0.8, 0.6, 0.2, 0.5).as_rgba_percent_string(),
			'rgba(80%, 60%, 20%, 0.5)')
		self.assertEqual(
			Color(0.8, 0.6, 0.2, 0.0).as_rgba_percent_string(),
			'rgba(80%, 60%, 20%, 0.0)')

	def test_hsl_string(self):
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2).as_hsl_string(),
			'hsl(204, 153, 51)')
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2, 0.5).as_hsl_string(),
			'hsl(204, 153, 51)')

	def test_hsla_string(self):
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2).as_hsla_string(),
			'hsla(204, 153, 51, 1.0)')
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2, 0.5).as_hsla_string(),
			'hsla(204, 153, 51, 0.5)')
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2, 0.0).as_hsla_string(),
			'hsla(204, 153, 51, 0.0)')

	def test_hsl_percent_string(self):
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2).as_hsl_percent_string(),
			'hsl(80%, 60%, 20%)')
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2, 0.5).as_hsl_percent_string(),
			'hsl(80%, 60%, 20%)')

	def test_hsla_percent_string(self):
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2).as_hsla_percent_string(),
			'hsla(80%, 60%, 20%, 1.0)')
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2, 0.5).as_hsla_percent_string(),
			'hsla(80%, 60%, 20%, 0.5)')
		self.assertEqual(
			Color.from_hsla(0.8, 0.6, 0.2, 0.0).as_hsla_percent_string(),
			'hsla(80%, 60%, 20%, 0.0)')
