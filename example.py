from code_tokenizer import CodeTokenizer

# Example code to tokenize
example_code = """
class ExampleClass:
    def __init__(self):
        self.value = 0

    def method1(self):
        # This is a comment
        print("Hello")
        return True

    def method2(self):
        '''
        This is a docstring
        '''
        if True:
            return "World"

def standalone_function():
    return 42

class AnotherClass:
    def another_method(self):
        pass
"""

# Create tokenizer instance
tokenizer = CodeTokenizer()

# Tokenize the code
tokens = tokenizer.tokenize(example_code)

# Print each token with a separator
print("=== Tokenized Code ===")
for i, token in enumerate(tokens, 1):
    print(f"\n--- Token {i} ---")
    print(token)

# Get symbols
symbols = tokenizer.get_symbols(example_code)
print("\n=== Symbols ===")
for symbol in symbols:
    print(symbol)
