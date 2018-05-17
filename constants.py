HEADERS_MRCONSO = [
    'cui', 'lat', 'ts', 'lui', 'stt', 'sui', 'ispref', 'aui', 'saui',
    'scui', 'sdui', 'sab', 'tty', 'code', 'str', 'srl', 'suppress', 'cvf'
]

HEADERS_RADLEX = [
    'Class ID', 'Preferred Label', 'Synonyms', 'Definitions', 'Obsolete', 'CUI',
    'Semantic Types', 'Parents', 'AAL', 'ACR_ID', 'ACR_Term', 'Acronym', 'Anatomical_Site',
    'Anterior_to,Attaches_to', 'Blood_Supply_of,Bounded_by', 'Bounds,Branch_Of', 'Branch_Part_of,Changes made to class',
    'CMA_Label', 'Comment,Constitutional_Part_Of', 'Contained_In,Contains,Continuous_With', 'Created mm/dd/yyyy',
    'Definition,Distal_to', 'Drains_Into,External_to', 'FMAID', 'Freesurfer,Has_Blood_Supply',
    'Has_Branch', 'Has_Branch_Part', 'Has_Constitutional_Part', 'Has_Entrapment_Site', 'Has_Innervation_Source',
    'Has_insertion', 'Has_Member,Has_origin', 'Has_Part', 'Has_Regional_Part', 'Has_Subtype',
    'http://data.bioontology.org/metadata/prefixIRI', 'id', 'Image_URL,Inferior_to', 'Innervates,Insertion_of',
    'Is_A', 'JHU_DTI-81', 'JHU_White-Matter_Tractography_Atlas', 'language', 'Left_Lateral_to,Lymphatic_Drainage',
    'Lymphatic_Drainage_Of,May_Be_Caused_By', 'May_Cause,Member_Of', 'Misspelling of term', 'name,Name,Neurolex_ID',
    'Neurolex_Term,Non-English_name', 'Origin_of', 'Part_Of', 'Posterior_to,Preferred_name', 'Preferred_Name_for_Obsolete',
    'Preferred_name_German', 'Projects_From,Projects_To', 'Proximal_to', 'Radlex version of class change',
    'Receives_attachment_from', 'Receives_Drainage_From', 'Receives_Input_From,Receives_Projection_From',
    'Regional_Part_Of,Related_modality', 'Replaced_by,Right_Lateral_to', 'Segment_Of', 'Sends_Output_To',
    'SNOMED_ID', 'SNOMED_Term', 'Source', 'Superior_to', 'Surrounded_by', 'Surrounds', 'Synonym', 'Synonym_German',
    'Talairach', 'Term type', 'Term_Status', 'Tributary_Of', 'UMLS_ID', 'UMLS_Term', 'Unsanctioned Term'
]

HEADERS_MRSTY = [
    'cui', 'sty', 'hier' 'desc', 'sid', 'num'
]

NEGATIONS = {'none', 'non', 'neither', 'nor', 'no', 'not'}

ACCEPTED_SEMTYPES = {
    'T029',     # Body Location or Region
    'T023',     # Body Part, Organ, or Organ Component
    'T031',     # Body Substance
    'T060',     # Diagnostic Procedure
    'T047',     # Disease or Syndrome
    'T074',     # Medical Device
    'T200',     # Clinical Drug
    'T203',     # Drug Delivery Device
    'T033',     # Finding
    'T184',     # Sign or Symptom
    'T034',     # Laboratory or Test Result
    'T058',     # Health Care Activity
    'T059',     # Laboratory Procedure
    'T037',     # Injury or Poisoning
    'T061',     # Therapeutic or Preventive Procedure
    'T048',     # Mental or Behavioral Dysfunction
    'T046',     # Pathologic Function
    'T121',     # Pharmacologic Substance
    'T201',     # Clinical Attribute
    'T130',     # Indicator, Reagent, or Diagnostic Aid
    'T195',     # Antibiotic
    'T039',     # Physiologic Function
    'T040',     # Organism Function
    'T041',     # Mental Process
    'T170',     # Intellectual Product
    'T191'      # Neoplastic Process
}

UNICODE_DASHES = {
    u'\u002d', u'\u007e', u'\u00ad', u'\u058a', u'\u05be', u'\u1400',
    u'\u1806', u'\u2010', u'\u2011', u'\u2010', u'\u2012', u'\u2013',
    u'\u2014', u'\u2015', u'\u2053', u'\u207b', u'\u2212', u'\u208b',
    u'\u2212', u'\u2212', u'\u2e17', u'\u2e3a', u'\u2e3b', u'\u301c',
    u'\u3030', u'\u30a0', u'\ufe31', u'\ufe32', u'\ufe58', u'\ufe63',
    u'\uff0d'
}

LANGUAGES = {
    'BAQ',  # Basque
    'CHI',  # Chinese
    'CZE',  # Czech
    'DAN',  # Danish
    'DUT',  # Dutch
    'ENG',  # English
    'EST',  # Estonian
    'FIN',  # Finnish
    'FRE',  # French
    'GER',  # German
    'GRE',  # Greek
    'HEB',  # Hebrew
    'HUN',  # Hungarian
    'ITA',  # Italian
    'JPN',  # Japanese
    'KOR',  # Korean
    'LAV',  # Latvian
    'NOR',  # Norwegian
    'POL',  # Polish
    'POR',  # Portuguese
    'RUS',  # Russian
    'SCR',  # Croatian
    'SPA',  # Spanish
    'SWE',  # Swedish
    'TUR',  # Turkish
}

