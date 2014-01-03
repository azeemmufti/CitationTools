from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import subprocess
import os

os.chdir('/home/azeem/PycharmProjects/Citations')

from citeproc.py2compat import *

# We'll use json.loads for parsing the JSON data.
import json


# Import the citeproc-py classes we'll use below.
from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import Citation, CitationItem
from citeproc import formatter
from citeproc.source.json import CiteProcJSON

__author__ = 'azeem'

CSL_PATH = '/home/azeem/PycharmProjects/Citations/styles'

def to_CSL(project_data, citation_style, formatter_Style):
    """Format an OSF project as a citation.

    :param project_data: JSON-style dictionary of project information
    :param citation_style: File name of citation xml document
    :param formatter: Citeproc formatter (e.g. formatter.plain, formatter.html)
    """
    bib_source = CiteProcJSON([project_data])
    bib_style = CitationStylesStyle(citation_style)

    bibliography = CitationStylesBibliography(bib_style, bib_source, formatter_Style)

    citation1 = Citation([CitationItem(project_data['id'])])
    bibliography.register(citation1)

    return bibliography.bibliography()


def to_final(utilname, csl_input):
    """following conversion from JSON to CSLformat (bibtex in this case), this method converts that to XMLintermediary
    and then to final user specified format"""

    texText = to_CSL(csl_input, os.path.join(CSL_PATH, 'bibtex.csl'), formatter.plain)

    bibtexTerminal = subprocess.Popen(["echo", texText], stdout = subprocess.PIPE)
    xmlTerminal = subprocess.Popen(["bib2xml"], stdin = bibtexTerminal.stdout, stdout = subprocess.PIPE)
    finalForm = subprocess.check_output([utilname], stdin = xmlTerminal.stdout)
    return finalForm



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



#print (to_CSL(sample,os.path.join(CSL_PATH, 'harvard1.csl'), formatter.rst))
#print (to_CSL(sample,os.path.join(CSL_PATH, 'harvard1.csl'), formatter.plain))

print(to_final('xml2bib', sample))




