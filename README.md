# Code Tokenizer

A language-agnostic code tokenizer that splits code into meaningful chunks while preserving the integrity of code structures like methods and classes. This tool is particularly useful for preparing code for RAG (Retrieval-Augmented Generation) systems and code understanding tasks.

## Features

- Language-agnostic code tokenization
- Preserves code structure integrity
- Configurable breaking points
- Comment detection across multiple languages
- Easy to extend and customize

## Installation

Clone the repository and include it in your project:

```bash
git clone https://github.com/yourusername/code-tokenizer.git
cd code-tokenizer
```

## Usage

Basic usage example:

```python
from code_tokenizer import CodeTokenizer

# Create a tokenizer instance
tokenizer = CodeTokenizer()

# Tokenize some code
code = """
def example_function():
    print("Hello")
    return True

class ExampleClass:
    def method(self):
        pass
"""

# Get tokens
tokens = tokenizer.tokenize(code)
for token in tokens:
    print("=== Token ===")
    print(token)

# Get symbols
symbols = tokenizer.get_symbols(code)
print("Symbols:", symbols)
```

## Customization

You can customize the natural and closing breakpoints by providing your own lists:

```python
custom_natural_breakpoints = ["function", "class", "method"]
custom_closing_breakpoints = ["end", "}"]

tokenizer = CodeTokenizer(
    custom_natural_breakpoints=custom_natural_breakpoints,
    custom_closing_breakpoints=custom_closing_breakpoints
)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
