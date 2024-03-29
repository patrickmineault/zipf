# Zipf's law project

This is an example project for the Good Research Code Handbook. It's a reinterpretation of the Zipf's law project from [Research Software Engineering in Python](https://merely-useful.tech/py-rse/). [It reuses and modifies some of the code from the original project](https://github.com/merely-useful/py-rse/tree/book/zipf), which was licensed under a CC-BY license. For this reason, this repo is under a CC-BY 4.0 license.

## Installation

Make a copy of this repo (e.g. with git clone), cd into the root folder of the repo, and run:

```
pip install -e .
```

## Organization

The project is organized into folders:

- `zipf` contains the main module code that runs the analysis
- `scripts` contains scripts to glue the module code
- `tests` contains tsts of the module code
- `data` contains the data for the analysis
- `results` will contain the output of the analysis

## Running the analysis

`cd` into the scripts folder and run `run_analysis.py` via:

`python run_analysis.py --in_folder ../data --out_folder ../results`

You can then load up `visualize_results.ipynb` in jupyter to visualize the results.

## Running tests

`cd` into the tests folder and run `pytest`.

## Adding data sources

I've pre-populated the data folder with these books from Project Gutenberg:

- [Dracula](https://www.gutenberg.org/files/345/345-0.txt) → `data/dracula.txt`
- [Frankenstein](https://www.gutenberg.org/ebooks/42324.txt.utf-8) → `data/frankenstein.txt`
- [Jane Eyre](https://www.gutenberg.org/files/1260/1260-0.txt) → `data/jane_eyre.txt`

You can add more documents to the folder as you wish.
