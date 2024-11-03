import json
import os
from typing import List, Dict

class CodeTokenizer:
    """
    A language-agnostic code tokenizer that splits code into meaningful chunks
    while preserving the integrity of code structures like methods and classes.
    """

    def __init__(self, custom_natural_breakpoints: List[str] = None, custom_closing_breakpoints: List[str] = None):
        """
        Initialize the CodeTokenizer with optional custom breakpoints.

        Args:
            custom_natural_breakpoints (List[str], optional): Custom natural breakpoints to use instead of defaults
            custom_closing_breakpoints (List[str], optional): Custom closing breakpoints to use instead of defaults
        """
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        
        if custom_natural_breakpoints is not None:
            self.natural_breakpoints = custom_natural_breakpoints
        else:
            with open(os.path.join(data_dir, "natural_breakpoints.json"), 'r') as f:
                self.natural_breakpoints = json.load(f)

        if custom_closing_breakpoints is not None:
            self.closing_breakpoints = custom_closing_breakpoints
        else:
            with open(os.path.join(data_dir, "closing_breakpoints.json"), 'r') as f:
                self.closing_breakpoints = json.load(f)

    def tokenize(self, code: str) -> List[str]:
        """
        Tokenize the given code into meaningful chunks.

        Args:
            code (str): The source code to tokenize

        Returns:
            List[str]: List of code chunks
        """
        tokenized_code = []
        current_chunk = []
        token_index = 0

        for line in code.split('\n'):
            line_check = line.strip()
            
            # Start a new chunk if we hit a natural breakpoint
            if self.is_line_symbol(line_check):
                if current_chunk:
                    tokenized_code.append('\n'.join(current_chunk))
                    current_chunk = []
                token_index += 1
            
            current_chunk.append(line)

        # Add the last chunk if there's anything remaining
        if current_chunk:
            tokenized_code.append('\n'.join(current_chunk))

        return tokenized_code

    def get_symbols(self, code: str) -> List[str]:
        """
        Extract symbols (significant code markers) from the code.

        Args:
            code (str): The source code to analyze

        Returns:
            List[str]: List of symbols found in the code
        """
        symbols = []
        for line in code.split('\n'):
            line = line.strip()
            if self.is_line_symbol(line):
                symbols.append(line)
        return symbols

    def is_line_symbol(self, line: str) -> bool:
        """
        Determine if a line contains a symbol that should start a new chunk.

        Args:
            line (str): The line to check

        Returns:
            bool: True if the line contains a symbol, False otherwise
        """
        line = line.strip()
        return (
            self.line_contains(line, self.natural_breakpoints) and
            not self.line_contains(line, self.closing_breakpoints) and
            not self.is_comment(line)
        )

    def line_contains(self, line: str, tokens: List[str]) -> bool:
        """
        Check if a line contains any of the given tokens.

        Args:
            line (str): The line to check
            tokens (List[str]): List of tokens to look for

        Returns:
            bool: True if the line contains any of the tokens, False otherwise
        """
        # Add spaces around line to ensure we match whole words
        line = f" {line} "
        return any(f" {token} " in line for token in tokens)

    def is_comment(self, line: str) -> bool:
        """
        Determine if a line is a comment.

        Args:
            line (str): The line to check

        Returns:
            bool: True if the line is a comment, False otherwise
        """
        line = line.strip()
        if not line:
            return False
            
        # Common comment markers across different languages
        comment_markers = ['#', '//', '/*', '*', '\'\'\'', '"""', '--']
        return any(line.startswith(marker) for marker in comment_markers)
