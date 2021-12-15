from zipf.parse_text import count_words


def test_parse_text():
    with open("fake_text.txt") as f:
        results = count_words(f, True)
        assert len(results) == 5
        assert results["the"] == 5
        assert results["and"] == 4
        assert results["i"] == 3
        assert results["to"] == 2
        assert results["of"] == 1
