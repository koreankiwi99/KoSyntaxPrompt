# Data Description
This directory contains all data files used in this project. 

**Note**: The results of LLM-based evaluations will be updated

## Input
`test.csv`
  - Source : Derived from KR-Atomic and Atomic2020, containing 122,526 triples.
  - Columns:
    - `Head_Eng`: Head events in English (from Atomic2020).
    - `Head_raw`: Machine-translated head events in Korean. It may contain translation errors.
    - `lemma_revised`: Head events with verbs lemmatized.
    - `Head_Ko`: Final revised version of the head events in Korean, with verbs changed to past tense. (Input)
    - `Rel`: Relation between head and tail events (from Atomic2020).
    - `Tail_Eng`: Tail events in English (from Atomic2020).
    - `Tail_raw`: Machine-translated tail events in Korean.
    - `Tail_Ko`: Final revised version of the tail events in Korean, with verbs changed to past tense. (Label)

## Output
