# Methodology

## Corpus
### Collection
In this study, we aimed to investigate how inference performance in if-then relations varies due to the syntactic structure of prompts. To achieve this, we used the [Atomic2020](https://github.com/allenai/comet-atomic-2020) dataset, which is designed for commonsense reasoning about everyday events, and translated it into Korean using machine translation. The Atomic2020 dataset is organized into triples: a Base Event (*Head*), a *Relation*, and an inferred Event (*Tail*). It includes 23 Relations set by researchers, with Heads automatically extracted from a corpus and Tails created through crowdsourcing, where workers generated the Tails based on given Heads and Relations. The dataset contains approximately 1.33M triples and is used to evaluate if machines can infer Tails similarly to humans and as training data for this purpose. Although the Heads in Atomic2020 include sentences and words like 'Apple,' this study focuses on if-then relations using only sentence-form Heads.

|Head|Relation|Tail|
|:---|:---:|:---|
|PersonX votes for PersonY|xIntent|to give support|
|PersonX runs out of steam|isBefore|PersonX hits the showers|
+ **Table 1. Examples from the Atomic2020 Dataset**

A Korean version of Atomic2020 existed previously, but it had poor translation quality. Therefore, we created a new machine-translated dataset called KR-Atomic to improve quality. We randomly sampled 3,000 Heads from this dataset for our experiments. For more details on the dataset creation process, please refer to the [KR-Atomic Repository](https://github.com/koreankiwi99/KR-Atomic).

### Statistics
From the 3,000 Heads extracted through random sampling, we selected 2,528 Heads for the experimental corpus after excluding those with redundant meanings, grammatical errors, or interpretative issues. Table 2 provides the detailed statistics for this experimental corpus. The dataset contains a total of 122,526 triples, which reduces to 102,999 when excluding entries with empty Tails. On average, each Head consists of 7.40 morphemes, while each Tail is shorter, with an average of 4.88 morphemes.

||Count|Words|Morphemes|
|--|-----|-----|---------|
|Triples|122,526|-|-|
|w/o Empty Tails|102,999|-|-|
|Heads|2,528|3.71|7.40|
|Tails|53,355|2.39|4.88|
+ **Table 2. Statistics for the Experimental Corpus.** *Words* and *Morphemes* represent the average counts. Morphemes were counted using the [Mecab Tokenizer](https://github.com/Pusnow/mecab-ko-msvc).

A key observation, as shown in Figure 1, is that not all Head-Relation combinations lead to effective commonsense inference. Consequently, the distribution of Tails is biased depending on the Relation, indicating that some Relations are more likely to produce meaningful Tails than others.

![Figure 01](figure01.png)

## Experiment Setup
