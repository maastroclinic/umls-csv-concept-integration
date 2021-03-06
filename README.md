# UMLS CSV concept integration

Integrate concepts ontologies in csv format to the UMLS format for reuse concept extractors (e.g. cTakes, QuickUMLS).

TODO
-	Implement UMLS semantic types (currently everything is set to T021 Anatomical Site)
-	Find a system to prevent conflicts with UMLS CUI (cTakes changes id RID13437 to C100013437)
-	Make the implementation more generic so the ROO can be used next to the RadLex ontology


## 1. Formats 
### 1.1 UMLS

Details about the UMLS RRF files can be found in the [UMLS Reference Manual](https://www.ncbi.nlm.nih.gov/books/NBK9685/)

[Unique Identifiers in the Metathesaurus](https://www.nlm.nih.gov/research/umls/new_users/online_learning/Meta_005.html)

UMLS extractors cTakes, QuickUMLS are using the following files:
- [MRCONSO.RRF](https://www.ncbi.nlm.nih.gov/books/NBK9685/table/ch03.T.concept_names_and_sources_file_mr/?report=objectonly) Concept Names and Sources (3.3.4)
- MRSTY.RRF Semantic Types (3.3.7) Currently all semantic types are set to T021 as configured in [config.json](config.json)
    

### 1.2. Onotologies in csv

Ontologies in csv format can be downloaded from [BioPortal](http://bioportal.bioontology.org).
 
- [RadLex](http://bioportal.bioontology.org/ontologies/RADLEX) Radiology Lexicon
- [ROO](https://bioportal.bioontology.org/ontologies/ROO) Radiation Oncology Ontology



### 1.3 cTakes

cTakes [Dictionary Creator GUI](https://cwiki.apache.org/confluence/display/CTAKES/Dictionary+Creator+GUI) columns extracted from the UMLS RRF files.

MRCONSO.RRF

| CUI(0) | LANGUAGE(1) | STATUS(2) | FORM(4) | SOURCE(11) | TERM_TYPE(12) | SOURCE_CODE(13) | TEXT(14) |
|--------|-------------|-----------|---------|------------|---------------|-----------------|----------|

MRSTY.RRF

| CUI(0) | TUI(1) |
|--------|--------|


### 1.4 QuickUMLS

QuickUMLS extracts the following columns from UMLS RRF files.

MRCONSO.RRF

| str | cui | ispref | lat |
|-----|-----|--------|-----|
  
MRSTY.RRF

| CUI(0) | TUI(1) |
|----------|----------|


## 3. Usage

1. Download csv (TODO support for other formats than RadLex)
2. Configure output format in [config.json](config.json)
3. Run tests/umlscsv_test.py with correct parameters for in and output (TODO command line approach)
4. The output folder is in UMLS installation format, compatible with:  
    - cTakes Dictionary Creator
    - QuickUMLS initialization 

### 3.1 Configuration in config.json

- **convert_rid_to_cui:** when set to true, radlex RID is converted to UMLS CUI to be compatible with cTakes fast dictionary lookup. E.g. Radlex ontology entity "lungs" with label [RID13437](https://bioportal.bioontology.org/ontologies/RADLEX/?p=classes&conceptid=http%3A%2F%2Fwww.radlex.org%2FRID%2F%23RID13437) becomes C0013437.
    **Make sure u don't mix up concepts!**
    
    - In MRCONSO.RRF:

            C0013437|ENG|P|lui|PF|sui|ispref|aui|saui|scui|sdui|RADLEX_ENG|PT|71620000|lungs|srl|N|256
        
    - In cTakes dictionary <dictionary_name>.script

            INSERT INTO PREFTERM VALUES(13437,'lungs')     

    
## 4. Concept extractors

### 4.1 cTakes


#### 4.1.1 Create a cTakes dictionary

Follow the cTakes [dictionary creator manual](https://cwiki.apache.org/confluence/display/CTAKES/Dictionary+Creator+GUI)
- In step 3, configure the UMLS installation to the folder created by the script of this repository
- In step 6, currently semantic types are by default all T021

PS
To use the cTakes dictionary creator for another languages than English use the [trunk](https://svn.apache.org/repos/asf/ctakes/trunk/ctakes-gui/src/main/java/org/apache/ctakes/gui/dictionary/DictionaryCreator.java)

#### 4.1.2 Usage of the cTakes fast dictionary lookup

1. Locate the path of the created DictionaryName.xml (default org/apache/ctakes/dictionary/lookup/fast/DictionaryName.xml)
2. Set the DictionaryName.xml path as value for DictionaryDescriptor in <apache-ctakes-4.0.0>\desc\ctakes-dictionary-lookup-fast\desc\analysis_engine\UmlsLookupAnnotator.xml
3. Test extraction (e.g. Step 2 in [cTAKES+4.0+User+Install+Guide](https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+4.0+User+Install+Guide))
    
        bin\runctakesCVD.bat  desc\ctakes-clinical-pipeline\desc\analysis_engine\AggregatePlaintextFastUMLSProcessor.xml


More info:
- [Dependencies between modules](https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+4.0+Component+Use+Guide#cTAKES4.0ComponentUseGuide-ComponentDependencies)
- [Fast Dictionary lookup Implementation details](https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+4.0+-+Fast+Dictionary+Lookup)

### 4.2 QuickUMLS

https://github.com/Georgetown-IR-Lab/QuickUMLS

