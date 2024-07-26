# Introduction

## Background 
Recent advancements in large language models (LLMs) have revolutionized natural language processing (NLP). A notable development is the use of prompting, which involves integrating contextual information into input sentences to guide the model’s output. The success of this technique depends on both the format and content of the prompt. While much research has focused on English prompts, there is comparatively less exploration of prompts in Korean.

## Research Motivation
This paper examines the challenges of translating completion-type prompts from English to Korean, highlighting the unique syntactic and structural differences between the two languages:

(A) English Prompt: "PersonX’s face gets red because he feels ___"
(B) Korean (Direct Translation): "그의 얼굴은 빨개졌는데, 왜냐하면 그는 ___ 느꼈기 때문이다."
(C) Korean (Into Relative Clause): "그의 얼굴은 빨개졌는데, 왜냐하면 그가 느꼈던 것은 ___"
(D) Korean (): "그는 ___ 느꼈기에, 그의 얼굴은 빨개졌다"

### Key Challenges

#### Syntactic Order Difference and Prompt Adaptation
Korean uses a subject-object-verb (SOV) order, meaning verbs typically appear at the end of clauses. This syntactic structure can complicate the direct translation of English open-ended prompts, especially those designed for completion tasks. For example, in a direct translation (see example B), placing the verb after the blank space disrupts the intended form of the open-ended sentence.

To address these syntactic challenges, two main strategies can be employed:
1. Switching to a Fill-in-the-Blank Format: Reformulating the prompt into a fill-in-the-blank style can better accommodate Korean syntax. However, this approach may not align well with the pretraining methods of autoregressive models.
2. Incorporating Verbs into Relative Clauses: Another strategy is to integrate verbs into relative clauses, as shown in example D. This method can maintain the original format but may not always be applicable. For instance, in the sentence "그는 매일 술을 마신다. 그는 __한 사람이다" (He drinks alcohol every day. He is a ___ person), integrating verbs into relative clauses might not fit smoothly.

#### Natural Clause Difference
