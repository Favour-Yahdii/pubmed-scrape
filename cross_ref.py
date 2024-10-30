from habanero import Crossref
cr = Crossref()

# get works that cite this DOI
cr.works(ids = "10.10.1111_1747-0080.12611")
