# UMLS CSV concept integration

Integrate concepts ontologies in csv format to the UMLS format for reuse concept extractors (e.g. cTakes, QuickUMLS).

## UMLS format

Details about the UMLS RRF files can be found in the [UMLS Reference Manual](https://www.ncbi.nlm.nih.gov/books/NBK9685/)

UMLS extractors cTakes, QuickUMLS are using the following files:
- [MRCONSO.RRF](https://www.ncbi.nlm.nih.gov/books/NBK9685/table/ch03.T.concept_names_and_sources_file_mr/?report=objectonly) Concept Names and Sources (3.3.4)
- MRSTY.RRF Semantic Types (3.3.7)
    

## Onotologies in csv format

Ontologies in csv format can be downloaded from [BioPortal](http://bioportal.bioontology.org).
 
- [RadLex](http://bioportal.bioontology.org/ontologies/RADLEX) Radiology Lexicon
- [ROO](https://bioportal.bioontology.org/ontologies/ROO) Radiation Oncology Ontology


    
## Configuration

### cTakes

The cTakes [Dictionary Creator GUI](https://cwiki.apache.org/confluence/display/CTAKES/Dictionary+Creator+GUI) extracts the following columns from UMLS RRF files.

MRCONSO.RRF

| CUI( 0 ) | LANGUAGE( 1 ) | STATUS( 2 ) | FORM( 4 ) | SOURCE( 11 ) | TERM_TYPE( 12 ) | SOURCE_CODE( 13 ) | TEXT( 14 ) |
|----------|---------------|-------------|-----------|--------------|-----------------|-------------------|------------|

MRSTY.RRF

| CUI( 0 ) | TUI( 1 ) |
|----------|----------|



### QuickUMLS

QuickUMLS extracts the following columns from UMLS RRF files.

MRCONSO.RRF

| str | cui | ispref | lat |
|-----|-----|--------|-----|
  
MRSTY.RRF

| CUI( 0 ) | TUI( 1 ) |
|----------|----------|

