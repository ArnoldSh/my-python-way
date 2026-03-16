from collections import defaultdict
from collections import deque
from collections import Counter

## O(n) time & O(1) extra memory solution: classic 2-phases algorithm
def first_unique_word(text: str) -> str | None:
    words_dict = defaultdict(int)
    for word in text.split():
        words_dict[word.lower()] += 1
    for word, count in words_dict.items():
        if count == 1:
            return word
    return None

## O(n) time & O(n) extra memory solution: using deque underhood allow to solve with single phase
def first_unique_word_deque(text: str) -> str | None:
    words_dict = {}
    candidates = deque()
    for word in text.split():
        words_dict[word] = words_dict.get(word, 0) + 1
        if words_dict[word] == 1:
            candidates.append(word)
        while candidates and words_dict[candidates[0]] > 1:
            candidates.popleft()
    return candidates[0] if candidates else None

## regular solution using counter and generator
def first_unique_word_counter(text: str):
    counts = Counter(text.split())
    return next((w for w in text.split() if counts[w] == 1), None)

def main() -> None:
    print(first_unique_word("apple banana apple orange banana pear"))
    print(first_unique_word_deque("apple banana apple orange banana pear"))
    print(first_unique_word_counter("apple banana apple orange banana pear"))
    print(first_unique_word("orange"))
    print(first_unique_word_deque("orange"))
    print(first_unique_word_counter("orange"))

if __name__ == "__main__":
    main()