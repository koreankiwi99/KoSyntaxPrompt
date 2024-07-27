# Methodology

## Corpus
### Collection
In this study, we aimed to investigate how inference performance in if-then relations varies due to the syntactic structure of prompts. To achieve this, we used the Atomic2020 dataset, which is designed for commonsense reasoning about everyday events, and translated it into Korean using machine translation. The Atomic2020 dataset is organized into triples: a Base Event (*Head*), a *Relation*, and an inferred Event (*Tail*). It includes 23 Relations set by researchers, with Heads automatically extracted from a corpus and Tails created through crowdsourcing, where workers generated the Tails based on given Heads and Relations. The dataset contains approximately 1.33M triples and is used to evaluate if machines can infer Tails similarly to humans and as training data for this purpose. Although the Heads in Atomic2020 include sentences and words like 'Apple,' this study focuses on if-then relations using only sentence-form Heads.

+---------------+---------------+--------------------+
| Fruit         | Price         | Advantages         |
+===============+===============+====================+
| Bananas       | $1.34         | - built-in wrapper |
|               |               | - bright color     |
+---------------+---------------+--------------------+
| Oranges       | $2.10         | - cures scurvy     |
|               |               | - tasty            |
+---------------+---------------+--------------------+

|Head|Relation|Tail|
|---|---|---|
|PersonX votes for PersonY|xIntent|to give support|
|^  |oEffect|receives praise|

A Korean version of Atomic2020 existed previously, but it had poor translation quality. Therefore, we created a new machine-translated dataset called KR-Atomic to improve quality. We randomly sampled 3,000 Heads from this dataset for our experiments. For more details on the dataset creation process, please refer to the [KR-Atomic Repository](https://github.com/koreankiwi99/KR-Atomic).

### Statistics


