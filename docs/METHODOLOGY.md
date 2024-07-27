# Methodology

## Corpus
### Collection
In this study, we aimed to investigate how inference performance in if-then relations varies due to the syntactic structure of prompts. To achieve this, we used [the Atomic dataset](https://arxiv.org/abs/1811.00146), which is designed for commonsense reasoning about everyday events, and translated it into Korean using machine translation. The Atomic dataset is organized into triples: a Base Event (*Head*), a *Relation*, and an inferred Event (*Tail*). It includes 9 Relations set by researchers, 24K Heads automatically extracted from a corpus, and 309K Tails created through crowdsourcing, where workers generated the Tails based on given Heads and Relations. The dataset contains 877K triples. Atomic is used to evaluate if machines can infer Tails similarly to humans and also as training data for this purpose.

A Korean version of Atomic existed previously, but it had poor translation quality. Therefore, we created a new machine-translated dataset called KR-Atomic to improve quality. We randomly sampled 3,000 Heads from this dataset for our experiments. For more details on the dataset creation process, please refer to the [KR-Atomic Repository](https://github.com/koreankiwi99/KR-Atomic).

### Statistics


