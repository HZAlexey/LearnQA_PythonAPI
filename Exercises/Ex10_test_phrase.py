class TestPhrase:
    def test_phrase_len(self):
        phrase = input("Set a phrase: ")
        phrase_len = 15

        assert len(phrase) < phrase_len, f"This phrase is less than {phrase_len} characters"