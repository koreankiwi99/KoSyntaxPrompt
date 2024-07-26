# Introduction

## Background 
Recent advancements in large language models (LLMs) have revolutionized natural language processing (NLP), with prompting techniques playing a significant role. Prompting involves integrating contextual information into input sentences to guide the model’s responses. The effectiveness of these techniques depends heavily on both the format and content of the prompt. While extensive research has focused on English prompts, there is comparatively less investigation into the application of prompting techniques in Korean.

## Research Motivation
This study addresses the challenges involved in translating completion-type prompts from English into Korean, particularly considering the syntactic and structural differences between the two languages. For example:

- (A) English Prompt: "PersonX’s face gets red because he feels ___"
- (B) Korean (Direct Translation): "그의 얼굴은 빨개졌는데, 왜냐하면 그는 ___ 느꼈기 때문이다."
- (C) Korean (Verb-Moved): "그의 얼굴은 빨개졌는데, 왜냐하면 그가 느꼈던 것은 ___" (PersonX's face gets red because what he feels is)
- (D) Korean (Clause-Moved): "그는 ___ 느끼기에, 그의 얼굴은 빨개졌다" (PersonX feels ___, so his face gets red.)

### 1. Syntactic Order Difference and Prompt Adaptation
Korean follows a subject-object-verb (SOV) structure, placing verbs at the end of clauses. This structural difference complicates the direct translation of English open-ended prompts, particularly those designed for completion tasks. For instance, in the direct translation (example B), the verb’s placement after the blank disrupts the intended format of the prompt. To address these syntactic challenges, two main strategies can be considered:

- **Switching to a Fill-in-the-Blank Format**: Reformulating the prompt into a fill-in-the-blank format can address this issue. However, this approach may not align well with the pretraining methodologies used for autoregressive models.
  
- **Integrating Verbs into Relative Clauses**: Incorporating verbs into relative clauses, as shown in example D, can preserve the open-ended nature of the prompt. However, this strategy may not be universally applicable. For instance, in "그는 매일 술을 마신다. 그는 __한 사람이다" (He drinks alcohol every day. He is a ___ person), integrating the main verb into the relative clause proves challenging.

### 2. Differences in Natural Clause Structure
The natural clause structures of English and Korean also differ. [Dissel et al. (2011)](https://www.semanticscholar.org/paper/Causal-clauses%3A-a-cross-linguistic-investigation-of-Diessel-Hetterle/d15a6b59855aceaba8a71d1d66601f14eadf118a) highlight that English typically employs a main clause followed by a causal clause, whereas languages with object-verb (OV) structures, such as Korean, generally prefer placing the causal clause before the main clause. This preference makes example D more suitable for Korean compared to example B. Given that models pre-trained on Korean texts may be more familiar with this clause order, it is important to explore how these structural differences impact inference performance.

## Objectives
This study aims to investigate how variations in verb placement and clause order in prompts affect the inference performance of large language models (LLMs). Specifically, we examine four different types of prompt syntax and their impact across twelve common-sense relational contexts.

To achieve this, we will use a Korean-translated version of the Atomic dataset and conduct experiments with the GPT-3.5 Turbo model. Our methodology involves inputting everyday events (Head) and their relationships (Relation) into the model using the different prompt syntaxes. We will analyze how these variations influence the model's ability to generate accurate inferences. Detailed information about the experimental design, data preparation, and analysis procedures is provided in the following section.


