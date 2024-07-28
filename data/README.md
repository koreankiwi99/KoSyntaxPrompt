# Data

**Note**: The results of LLM-based evaluations will be updated.

## Input

### test.csv
- **Source**: Derived from KR-Atomic and Atomic2020, containing 122,526 triples.
- **Notes**:
  - `Head_Ko` is used as the input data for generation.
  - `Tail_Ko` is used as the target label for assessment.
- **Columns**:
  - `Head_Eng`: Head events in English (from Atomic2020).
  - `Head_raw`: Machine-translated head events in Korean, which may contain translation errors.
  - `lemma_revised`: Head events with verbs lemmatized.
  - `Head_Ko`: Final revised version of the head events in Korean, with verbs changed to past tense (Input).
  - `Rel`: Relation between head and tail events (from Atomic2020).
  - `Tail_Eng`: Tail events in English (from Atomic2020).
  - `Tail_raw`: Machine-translated tail events in Korean.
  - `Tail_Ko`: Final revised version of the tail events in Korean, with verbs changed to past tense (Label).

## Outcome

### Zero-shot & Few-shot
These folders contain generated outcomes named according to the type of relation (e.g., `isAfter.csv`, `isBefore.csv`).
