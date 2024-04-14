# Text Analysis with HGCT

This repository showcases the [HGCT (Hanzi Glyph Corpus Toolkit)](https://yongfu.name/hgct/index.html), a tool designed for advanced analysis and querying of Chinese text data, demonstrated through a textbook-derived corpus.

## Installation
To use this package, clone the repository and install the required dependencies.

1. Python version
```bash
3.11 > Python >= 3.0
```

2. Clone repository

```bash
git clone git@github.com:lopentu/HanziAnalysisKit.git
```

3. Install Requirement

```bash
cd HanziAnalysisKit && pip install -r requirements.txt
```

## Quick Start

### Building the Corpus
To prepare your data for use with the HGCT tool, build your corpus from the provided textbook data:

```python
from textbook import build_corpus

# Specify your CSV data file and desired output folder
csv_file = './data/教科書課文.csv'
folder = "textbook_corpus"

# Build the corpus
build_corpus(csv_file, folder)
```

This will create a `textbook_corpus` folder in your project directory, containing the processed data ready for analysis with HGCT.

### Directory Structure
After building the corpus, your project directory will include:

```
|--- data/
|    |--- 教科書課文.csv
|--- textbook/
|--- textbook_corpus/ # Newly generated
|--- ...
```

### Advanced HGCT Features
Explore the powerful querying capabilities of HGCT with the prepared textbook corpus. For comprehensive examples and detailed usage instructions, visit our [GitHub project page](https://lopentu.github.io/HanziAnalysisKit/) .

