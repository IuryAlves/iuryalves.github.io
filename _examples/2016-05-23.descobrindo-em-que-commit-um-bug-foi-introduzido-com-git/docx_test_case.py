# coding: utf-8

import unittest

from pydocx import PyDocX


class DocxToHtmlTestCase(unittest.TestCase):
	
	def test_paragraph(self):

		html = PyDocX.to_html('file.docx').encode("utf-8")

		self.assertIn('<p>Exercício 08. 80', html)


if __name__ == '__main__':
	unittest.main()

