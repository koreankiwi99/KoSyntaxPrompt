from konlpy.tag import Mecab
import pandas as pd
import numpy as np
from typing import Union, Dict, List

RELS = ['xWant', 'oWant', 'xEffect', 'oEffect', 'xReact', 'oReact', 
        'xNeed', 'xIntent', 'HinderedBy', 'isAfter', 'isBefore', 'xAttr']
PROMPTS = ['A', 'B', 'B2', 'B3']

class Tokenizer:
    """
    A tokenizer class that uses either morpheme analysis (using Mecab) or a simple split based on spaces.
    """
    def __init__(self, use_morphemes: bool = True):
        self.use_morphemes = use_morphemes
        try:
            self.tokenizer = Mecab().morphs if use_morphemes else lambda text: text.split()
        except Exception as e:
            raise RuntimeError(f"Error initializing Mecab: {e}")

    def tokenize(self, text: Union[str, bool]) -> List[str]:
        """
        Tokenizes the input text. If the input is not a string or is empty, it returns a default message '응답 없음'.
        """
        if not isinstance(text, str):
            text = '응답 없음'
        return self.tokenizer(text.strip())


class TokenStats:
    """
    A class to compute statistics for different relation types using tokenization.
    """
    def __init__(self, data_dict: Dict[str, Dict[str, pd.DataFrame]], use_morphemes: bool = True):
        self.tokenizer = Tokenizer(use_morphemes)
        self.data_dict = data_dict

    def compute_stats(self, num_shot: str) -> pd.DataFrame:
        """
        Computes statistics for all relation types within a specified setting and returns the results as a DataFrame.
        """
        metrics_list = [self.relation_metrics(num_shot, relation) for relation in RELS]
        return pd.DataFrame(metrics_list, index=RELS)

    def relation_metrics(self, num_shot: str, relation: str) -> Dict[str, float]:
        """
        Computes metrics for a specific relation.
        """
        df = self.data_dict[num_shot][relation]
        columns = [p for p in PROMPTS if p in df.columns]
        metrics = {}
        for col in columns:
            token_lists = df[col].apply(lambda x: self.tokenizer.tokenize(x))
            metrics[f'{col}_mean'] = self._average_token_count(token_lists)
            metrics[f'{col}_unique'] = self._unique_token_count(token_lists)
        return metrics

    def _unique_token_count(self, token_lists: List[List[str]]) -> int:
        """
        Calculates the number of unique tokens in a list of token lists.
        """
        return len({token for sublist in token_lists for token in sublist})

    def _average_token_count(self, token_lists: List[List[str]]) -> float:
        """
        Calculates the average number of tokens per entry in the list of token lists.
        """
        return round(np.mean([len(tokens) for tokens in token_lists]), 2)
