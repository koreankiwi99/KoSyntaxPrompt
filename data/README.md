# Data
This directory contains all data files used in this project, organized for both zero-shot and few-shot learning settings.

**Note**: The results of LLM-based evaluations will be updated.

## Folder Structure

```plaintext
data/
├── test.csv
├── samples.csv
├── zeroshot/
│   ├── raw/
│   │   ├── isAfter.csv
│   │   ├── isBefore.csv
│   │   └── ... (other relation files)
│   ├── processed/
│   │   ├── isAfter.csv
│   │   ├── isBefore.csv
│   │   └── ... (other relation files)
├── fewshot_outcome/
│   ├── raw/
│   │   ├── isAfter.csv
│   │   ├── isBefore.csv
│   │   └── ... (other relation files)
│   ├── processed/
│   │   ├── isAfter.csv
│   │   ├── isBefore.csv
│   │   └── ... (other relation files)
└── README.md
```

## Input
Derived from [Atomic2020](https://github.com/allenai/comet-atomic-2020) and [KR-Atomic](https://github.com/koreankiwi99/KR-Atomic).

### test.csv
- **Description**: Contains 122,526 triples.
- **Notes**:
  - `Head_Ko` serves as the input data for generation.
  - `Tail_Ko` serves as the target label for assessment.
- **Columns**:
  - `Head_Eng`: Head events in English (sourced from Atomic2020).
  - `Head_raw`: Machine-translated head events in Korean, which may include translation errors.
  - `lemma_revised`: Head events with lemmatized verbs.
  - `Head_Ko`: Final revised version of the head events in Korean, with verbs converted to past tense (input).
  - `Rel`: Relation between head and tail events (sourced from Atomic2020).
  - `Tail_Eng`: Tail events in English (sourced from Atomic2020).
  - `Tail_raw`: Machine-translated tail events in Korean.
  - `Tail_Ko`: Final revised version of the tail events in Korean, with verbs converted to past tense (label).

### samples.csv
- **Description**: Used for few-shot learning, containing 240 rows (12 relations with 20 samples each).
- **Notes**:
  - `Head_Ko` and `Tail_Ko` are used as pairs for few-shot learning tasks.
- **Columns**: Same as `test.csv`, with an additional column:
  - `gleu_score`: Measures the similarity between the samples in `samples.csv` and the data in `test.csv`.

## Outcome
### Zero-shot & Few-shot
## Outcome

### Zero-shot & Few-shot
These folders contain `raw` and `processed` subfolders. Each subfolder contains generated outcomes named according to the type of relation (e.g., `isAfter.csv`, `isBefore.csv`).

###raw
Contains raw, unprocessed generated outcomes directly produced by the model without any further modifications or cleaning.

###processed
Contains generated outcomes that have been cleaned and processed to correct errors and improve quality.

- **Columns**:
  - `input`: Head events used as input.
  - `A`: Generated output with prompt type A.
  - `B`: Generated output with prompt type B1.
  - `B2`: Generated output with prompt type B2 (optional).
  - `B3`: Generated output with prompt type B3 (optional).
