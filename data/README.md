# Data

**Note**: The results of LLM-based evaluations will be updated.

## Input
Derived from [Atomic2020](https://github.com/allenai/comet-atomic-2020) and [KR-Atomic](https://github.com/koreankiwi99/KR-Atomic),

### test.csv
- **Description**: Containing 122,526 triples.
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

### samples.csv
- **Description**: Used for few-shot learning, containing 240 rows (12 relations with 20 samples each).
- **Notes**:
  - `Head_Ko` and `Tail_Ko` are used as a pair for few-shot learning tasks.
- **Columns**: Same as `test.csv`, with an additional column:
  - `gleu_score`: Measures the similarity between the samples in `samples.csv` and the data in `test.csv`.

## Outcome

### Zero-shot & Few-shot
These folders contain generated outcomes named according to the type of relation (e.g., `isAfter.csv`, `isBefore.csv`).
