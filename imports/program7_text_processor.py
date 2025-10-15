"""
Program 7: Text Processing Suite
Practice: Multiple import styles with string, re (regex), and collections modules
This program demonstrates various import patterns for text processing.
"""

# Different import styles for different modules
import string  # Full module import
import re as regex  # Module with alias
from collections import Counter, defaultdict, namedtuple  # Specific imports
from textwrap import wrap, dedent, fill  # Multiple specific imports
from itertools import chain, combinations  # Utility functions
import unicodedata  # Unicode handling

# Create a named tuple for structured data
TextStats = namedtuple('TextStats', ['words', 'sentences', 'paragraphs', 'avg_word_length'])

class TextAnalyzer:
    """Comprehensive text analysis tool"""

    def __init__(self, text):
        self.original_text = text
        self.cleaned_text = self.clean_text(text)

    def clean_text(self, text):
        """Clean and normalize text"""
        # Remove extra whitespace
        text = regex.sub(r'\s+', ' ', text)
        # Remove leading/trailing whitespace
        text = text.strip()
        return text

    def word_frequency(self):
        """Calculate word frequency using Counter"""
        # Remove punctuation and convert to lowercase
        translator = str.maketrans('', '', string.punctuation)
        clean_words = self.cleaned_text.translate(translator).lower().split()

        # Use Counter for frequency
        word_freq = Counter(clean_words)
        return word_freq

    def character_analysis(self):
        """Analyze character types in the text"""
        char_types = defaultdict(int)

        for char in self.original_text:
            if char in string.ascii_letters:
                char_types['letters'] += 1
            elif char in string.digits:
                char_types['digits'] += 1
            elif char in string.punctuation:
                char_types['punctuation'] += 1
            elif char in string.whitespace:
                char_types['whitespace'] += 1
            else:
                char_types['other'] += 1

        return dict(char_types)

    def get_statistics(self):
        """Get comprehensive text statistics"""
        words = self.cleaned_text.split()
        sentences = regex.split(r'[.!?]+', self.cleaned_text)
        sentences = [s for s in sentences if s.strip()]
        paragraphs = self.original_text.split('\n\n')

        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0

        return TextStats(
            words=len(words),
            sentences=len(sentences),
            paragraphs=len(paragraphs),
            avg_word_length=round(avg_word_length, 2)
        )

def demonstrate_string_module():
    """Demonstrate string module constants and templates"""
    print("=== String Module Demo ===\n")

    # String constants
    print("String Constants:")
    print(f"  Lowercase letters: {string.ascii_lowercase}")
    print(f"  Uppercase letters: {string.ascii_uppercase}")
    print(f"  Digits: {string.digits}")
    print(f"  Hexdigits: {string.hexdigits}")
    print(f"  Punctuation: {string.punctuation}")
    print(f"  Printable characters: {string.printable[:50]}...")

    # String Template
    from string import Template

    template = Template("Hello, $name! Welcome to $place.")
    result = template.substitute(name="Alice", place="Python World")
    print(f"\nTemplate Substitution:")
    print(f"  Template: 'Hello, $name! Welcome to $place.'")
    print(f"  Result: {result}")

    # Safe substitute (doesn't raise error for missing values)
    template2 = Template("User: $username, Role: $role, Status: $status")
    result2 = template2.safe_substitute(username="admin", role="superuser")
    print(f"\nSafe Substitution (missing 'status'):")
    print(f"  Result: {result2}")

def demonstrate_regex_patterns():
    """Demonstrate regular expressions with re module (aliased as regex)"""
    print("\n=== Regular Expression Demo ===\n")

    sample_text = """
    Contact us at: john.doe@email.com or jane_smith@company.co.uk
    Phone numbers: +1-555-123-4567, (555) 987-6543, 555.246.8910
    URLs: https://www.example.com, http://test.org/page
    Dates: 2024-01-15, 01/15/2024, January 15, 2024
    """

    # Email pattern
    email_pattern = regex.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = email_pattern.findall(sample_text)
    print("Found Emails:", emails)

    # Phone number pattern
    phone_pattern = regex.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
    phones = phone_pattern.findall(sample_text)
    print("Found Phone Numbers:", phones)

    # URL pattern
    url_pattern = regex.compile(r'https?://[\w\-\.]+(\.[\w\-]+)+[^\s]*')
    urls = url_pattern.findall(sample_text)
    print("Found URLs:", urls)

    # Date patterns
    date_pattern = regex.compile(r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|[A-Z][a-z]+ \d{1,2}, \d{4}')
    dates = date_pattern.findall(sample_text)
    print("Found Dates:", dates)

    # Substitution example
    masked_text = email_pattern.sub('[EMAIL REDACTED]', sample_text)
    print("\nEmail Masking:")
    print(masked_text[:100] + "...")

def demonstrate_collections():
    """Demonstrate collections module utilities"""
    print("\n=== Collections Module Demo ===\n")

    # Counter for frequency analysis
    text = "the quick brown fox jumps over the lazy dog the fox was quick"
    word_counter = Counter(text.split())
    print("Word Frequency with Counter:")
    print(f"  All counts: {dict(word_counter)}")
    print(f"  Most common 3: {word_counter.most_common(3)}")

    # defaultdict for grouping
    words = ["apple", "banana", "apricot", "blueberry", "avocado", "cherry"]
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)

    print("\nGrouping with defaultdict:")
    for letter, word_list in sorted(grouped.items()):
        print(f"  {letter}: {word_list}")

    # Named tuple for structured data
    Person = namedtuple('Person', ['name', 'age', 'city'])
    people = [
        Person("Alice", 30, "New York"),
        Person("Bob", 25, "San Francisco"),
        Person("Charlie", 35, "Boston")
    ]

    print("\nNamed Tuples:")
    for person in people:
        print(f"  {person.name} is {person.age} years old from {person.city}")

def demonstrate_text_wrapping():
    """Demonstrate text wrapping with textwrap module"""
    print("\n=== Text Wrapping Demo ===\n")

    long_text = """
    Python is a high-level, interpreted programming language with dynamic semantics.
    Its high-level built-in data structures, combined with dynamic typing and dynamic binding,
    make it very attractive for Rapid Application Development, as well as for use as a
    scripting or glue language to connect existing components together.
    """

    # Clean up the text
    cleaned = dedent(long_text).strip()

    # Wrap text to different widths
    print("Original Text (cleaned):")
    print(cleaned)

    print("\nWrapped to 40 characters:")
    wrapped_40 = wrap(cleaned, width=40)
    for line in wrapped_40[:3]:  # Show first 3 lines
        print(f"  {line}")

    print("\nFilled with 50 character width:")
    filled_50 = fill(cleaned, width=50)
    print(filled_50[:150] + "...")

def demonstrate_unicode_handling():
    """Demonstrate Unicode text handling"""
    print("\n=== Unicode Handling Demo ===\n")

    # Unicode text samples
    texts = [
        "Café",
        "Москва",  # Moscow in Cyrillic
        "東京",     # Tokyo in Japanese
        "مرحبا",    # Hello in Arabic
        "Zürich"
    ]

    print("Unicode Normalization:")
    for text in texts:
        # Normalize to NFC (Canonical Composition)
        nfc = unicodedata.normalize('NFC', text)
        # Get Unicode name for first character
        try:
            char_name = unicodedata.name(text[0])
        except ValueError:
            char_name = "Unknown"

        print(f"  '{text}' -> First char: '{text[0]}' ({char_name})")

    # Remove accents example
    def remove_accents(text):
        """Remove accents from Unicode text"""
        nfd = unicodedata.normalize('NFD', text)
        return ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')

    accented_text = "Héllö Wörld! Çà và?"
    clean = remove_accents(accented_text)
    print(f"\nAccent Removal:")
    print(f"  Original: {accented_text}")
    print(f"  Cleaned: {clean}")

def analyze_sample_text():
    """Analyze a sample text using the TextAnalyzer class"""
    print("\n=== Complete Text Analysis ===\n")

    sample = """
    Python is an interpreted, high-level programming language.
    Python's design philosophy emphasizes code readability!
    It supports multiple programming paradigms.

    Python is dynamically typed and garbage-collected.
    It has a large and comprehensive standard library.
    """

    analyzer = TextAnalyzer(sample)

    # Get word frequency
    word_freq = analyzer.word_frequency()
    print("Top 5 Most Frequent Words:")
    for word, count in word_freq.most_common(5):
        print(f"  '{word}': {count} times")

    # Character analysis
    char_analysis = analyzer.character_analysis()
    print("\nCharacter Type Analysis:")
    for char_type, count in char_analysis.items():
        print(f"  {char_type}: {count}")

    # Text statistics
    stats = analyzer.get_statistics()
    print("\nText Statistics:")
    print(f"  Words: {stats.words}")
    print(f"  Sentences: {stats.sentences}")
    print(f"  Paragraphs: {stats.paragraphs}")
    print(f"  Avg Word Length: {stats.avg_word_length}")

def main():
    """Main function to run all demonstrations"""
    print("=" * 60)
    print("TEXT PROCESSING WITH MULTIPLE IMPORT STYLES")
    print("=" * 60)

    # Run all demonstrations
    demonstrate_string_module()
    demonstrate_regex_patterns()
    demonstrate_collections()
    demonstrate_text_wrapping()
    demonstrate_unicode_handling()
    analyze_sample_text()

    print("\n" + "=" * 60)
    print("Text processing demonstration completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()