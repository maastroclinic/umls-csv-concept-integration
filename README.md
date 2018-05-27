# UMLS Radlex concepts integration

Integrate Radlex concept ids with UMLS to reuse concept extractors (cTakes, QuickUMLS).

[UMLS® Reference Manual - 3 Metathesaurus - Rich Release Format (RRF)](https://www.ncbi.nlm.nih.gov/books/NBK9685/)

The cTakes dictionary creator and QuickUMLS are using the following files:
- 3.3.4. Concept Names and Sources (File = [MRCONSO.RRF](https://www.ncbi.nlm.nih.gov/books/NBK9685/table/ch03.T.concept_names_and_sources_file_mr/?report=objectonly))
    - cTakes ['CUI( 0 )', 'LANGUAGE( 1 )', 'STATUS( 2 )', 'FORM( 4 )', 'SOURCE( 11 )', 'TERM_TYPE( 12 )', 'SOURCE_CODE( 13 )', 'TEXT( 14 )']
    - QuickUMLS ['str','cui','ispref','lat']  
- 3.3.7. Semantic Types (File = MRSTY.RRF)
    - cTakes ['CUI( 0 )', 'TUI( 1 )']
    - QuickUMLS ['cui','sty']