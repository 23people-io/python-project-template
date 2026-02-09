def my_sum(a: int, b: int) -> int:
    return a + b


def exclaim_phrases(phrases: list[str]) -> list[str]:
    return [f"¡{phrase}!" for phrase in phrases]


def test_function():
    assert my_sum(1, 2) == 3
    assert my_sum(-1, 1) == 0
    assert my_sum(0, 0) == 0


def test_exclaim_phrases():
    input_phrases = ["hello", "world"]
    expected_output = ["¡hello!", "¡world!"]
    assert exclaim_phrases(input_phrases) == expected_output
