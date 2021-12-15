import string
import collections


def count_words(f, clean_text=False):
    """
    Count words in a file.

    Arguments:
        f: an open file handle
        clean_text (optional): a Boolean, if true, filters out boilerplate typical of a Gutenberg book.

    Returns:
        A dict keyed by word, with word counts
    """
    text = f.read()
    if clean_text:
        text = _clean_gutenberg_text(text)

    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    word_list = [word.lower() for word in npunc if word]
    word_counts = collections.Counter(word_list)
    return dict(word_counts)


def _clean_gutenberg_text(text):
    """
    Find fences in a Gutenberg text and select the text between them.
    """
    start_fence = "start of the project gutenberg ebook"
    end_fence = "end of the project gutenberg ebook"
    text = text.lower()
    start_pos = text.find(start_fence) + len(start_fence) + 1
    end_pos = text.find(end_fence)

    # Check that the fences are at reasonable positions within the text.
    assert 0.000001 < start_pos / len(text) <= 0.1
    assert 0.9 < end_pos / len(text) <= 1.0

    return text[start_pos:end_pos]
