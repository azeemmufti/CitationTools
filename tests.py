__author__ = 'azeem'

import unittest
from nose.tools import *
from CitationParser import *
import os


#sample item to be cited
sample = {
"id": "ITEM-5",
"title":"Boundaries of Dissent: Protest and State Power in the Media Age",
"author": [
{
"family": "D'Arcus",
"given": "Bruce",
"static-ordering": False
}
],
"publisher": "Routledge",
"publisher-place": "New York",
"issued": {
"date-parts":[[2006]]
},
"type": "book",
"URL": "website.com"
}


class TestConversion(unittest.TestCase):

    def test_JSON_to_harvard1_plain(self):
        expected_output = open("/home/azeem/PycharmProjects/Citations/fixtures/harvard1_plaintext_output.txt").read()
        bibtex_intermediate = to_CSL(sample,os.path.join(CSL_PATH, 'harvard1.csl'), formatter.plain)
        self.assertEqual(bibtex_intermediate, expected_output)

    def test_JSON_to_harvard1_html(self):
        expected_output = open("/home/azeem/PycharmProjects/Citations/fixtures/harvard1_html_output.txt").read()
        bibtex_intermediate = to_CSL(sample,os.path.join(CSL_PATH, 'harvard1.csl'), formatter.html)
        self.assertEqual(bibtex_intermediate, expected_output)

    def test_JSON_to_bibtex(self):
        expected_output = open("/home/azeem/PycharmProjects/Citations/fixtures/bibtex_intermediate_output.txt").read()
        bibtex_intermediate = to_CSL(sample,os.path.join(CSL_PATH, 'bibtex.csl'), formatter.plain)
        self.assertEqual(bibtex_intermediate, expected_output)

    def test_bibtex_to_endnote(self): #fails due to unicode 'u' at beginning
        expected_output = open("/home/azeem/PycharmProjects/Citations/fixtures/endnote_output.txt").read()
        endnote_final = to_final('xml2end', sample)
        self.assertEqual(endnote_final.strip(), expected_output.strip())

    def test_bibtex_to_ris(self):
        expected_output = open("/home/azeem/PycharmProjects/Citations/fixtures/ris_output.txt").read()
        ris_final = to_final('xml2ris', sample)
        self.assertEqual(ris_final.strip(), expected_output.strip())


#print (sample)

if __name__ == '__main__':
    unittest.main()

