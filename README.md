# UMLS CSV concept integration

Integrate concepts ontologies in csv format to the UMLS format for reuse concept extractors (e.g. cTakes, QuickUMLS).

## UMLS format

Details about the UMLS RRF files can be found in the [UMLS Reference Manual](https://www.ncbi.nlm.nih.gov/books/NBK9685/)

UMLS extractors cTakes, QuickUMLS are using the following files:
- [MRCONSO.RRF](https://www.ncbi.nlm.nih.gov/books/NBK9685/table/ch03.T.concept_names_and_sources_file_mr/?report=objectonly) Concept Names and Sources (3.3.4)
- MRSTY.RRF Semantic Types (3.3.7) Currently all semantic types are set to T021 as configured in [config.json](config.json)
    

## Onotologies in csv format

Ontologies in csv format can be downloaded from [BioPortal](http://bioportal.bioontology.org).
 
- [RadLex](http://bioportal.bioontology.org/ontologies/RADLEX) Radiology Lexicon
- [ROO](https://bioportal.bioontology.org/ontologies/ROO) Radiation Oncology Ontology


## Usage

1. Download csv (TODO support for other formats than RadLex)
2. Configure output format in config.json
3. Run tests/umlscsv_test.py with correct parameters for in and output (TODO command line approach)
4. The output folder is in UMLS installation format, compatible with:  
    - cTakes Dictionary Creator
    - QuickUMLS initialization 

    
## Configuration

### cTakes

cTakes [Dictionary Creator GUI](https://cwiki.apache.org/confluence/display/CTAKES/Dictionary+Creator+GUI) columns extracted from the UMLS RRF files.

MRCONSO.RRF

| CUI( 0 ) | LANGUAGE( 1 ) | STATUS( 2 ) | FORM( 4 ) | SOURCE( 11 ) | TERM_TYPE( 12 ) | SOURCE_CODE( 13 ) | TEXT( 14 ) |
|----------|---------------|-------------|-----------|--------------|-----------------|-------------------|------------|

MRSTY.RRF

| CUI( 0 ) | TUI( 1 ) |
|----------|----------|

#### Create the cTakes dictionary

1. Follow the cTakes dictionary creator [manual](https://cwiki.apache.org/confluence/display/CTAKES/Dictionary+Creator+GUI)
2. In step 3, configure the UMLS installation to the folder created by the script of this repository
    - Possibly MRCONSO.RRF and MRSTY.RRF can me merged with an existing UMLS installation (untested)
3. In step 6, currently semantic types are by default all T021

PS
To use the cTakes dictionary creator for another languages than English use the [trunk](https://svn.apache.org/repos/asf/ctakes/trunk/ctakes-gui/src/main/java/org/apache/ctakes/gui/dictionary/DictionaryCreator.java)

#### Usage of the cTakes fast dictionary lookup

[Implementation details](https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+4.0+-+Fast+Dictionary+Lookup)

1. Locate the created DictionaryName.xml (default org/apache/ctakes/dictionary/lookup/fast/DictionaryName.xml)
2. Set the DictionaryName.xml path as value for DictionaryDescriptor in <apache-ctakes-4.0.0>\desc\ctakes-dictionary-lookup-fast\desc\analysis_engine\UmlsLookupAnnotator.xml
3. Test cTakes extraction (e.g. Step 2 in [cTAKES+4.0+User+Install+Guide](https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+4.0+User+Install+Guide))
    
        bin\runctakesCVD.bat  desc\ctakes-clinical-pipeline\desc\analysis_engine\AggregatePlaintextFastUMLSProcessor.xml

In AggregatePlaintextFastUMLSProcessor.xml pipeline modules can be configured, see [here](https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+4.0+Component+Use+Guide#cTAKES4.0ComponentUseGuide-ComponentDependencies) for dependencies between modules

### QuickUMLS

[QuickUMLS](https://github.com/Georgetown-IR-Lab/QuickUMLS)

QuickUMLS extracts the following columns from UMLS RRF files.

MRCONSO.RRF

| str | cui | ispref | lat |
|-----|-----|--------|-----|
  
MRSTY.RRF

| CUI( 0 ) | TUI( 1 ) |
|----------|----------|

