# Introduction

## Background 
Recent advancements in large language models (LLMs) have significantly transformed natural language processing (NLP). A notable development in this field is the technique of prompting, which involves incorporating contextual information into input sentences. The efficacy of this approach is contingent upon both the format and content of the prompt. While extensive research has been conducted on English prompts, there is comparatively less exploration of prompting techniques in Korean.

## Research Motivation
This study investigates the challenges associated with translating completion-type prompts from English to Korean, with a focus on the distinct syntactic and structural differences between the two languages. The following examples illustrate these differences:

- (A) English Prompt: "PersonX’s face gets red because he feels ___"
- (B) Korean (Direct Translation): "그의 얼굴은 빨개졌는데, 왜냐하면 그는 ___ 느꼈기 때문이다."
- (C) Korean (Verb-Moved): "그의 얼굴은 빨개졌는데, 왜냐하면 그가 느꼈던 것은 ___" (PersonX's face gets red because what he feels is)
- (D) Korean (Clause-Moved): "그는 ___ 느끼기에, 그의 얼굴은 빨개졌다" (PersonX feels ___, so his face gets red.)

### 1. Syntactic Order Difference and Prompt Adaptation
Korean language structure follows a subject-object-verb (SOV) order, which means that verbs typically appear at the end of clauses. 
This structure complicates the direct translation of English open-ended prompts, particularly those designed for completion tasks. For instance, in the direct translation (example B), positioning the verb after the blank disrupts the intended format of the open-ended prompt. To address these syntactic challenges, two primary strategies can be employed:

- Switching to a Fill-in-the-Blank Format: Reformulating the prompt into a fill-in-the-blank format can address this issue. However, this approach may not align well with the pretraining methodologies used for autoregressive models.
- Integrating Verbs into Relative Clauses: Another strategy involves incorporating verbs into relative clauses, as demonstrated in example D. This approach can maintain the open-ended nature of the prompt but may not always be applicable. For instance, in the sentence "그는 매일 술을 마신다. 그는 __한 사람이다" (He drinks alcohol every day. He is a ___ person), the main verb cannot be effectively incorporated into the relative clause, presenting a challenge for this adaptation strategy.

### 2. Differences in Natural Clause Structure
There is also a distinction in natural clause structures. According to Dissel et al. (2011), English typically employs a main clause followed by a causal clause, whereas languages with OV structures, such as Korean, generally prefer a causal clause preceding a main clause. This structural difference makes example D more appropriate than example B for Korean. Given that models pre-trained on Korean texts may have encountered more examples of the causal clause-main clause sequence, it is important to investigate whether these structural differences affect inference performance.
