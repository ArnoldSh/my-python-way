from collections import defaultdict

def main() -> None:
    print(words_dict("hello goose hello mouse"))
    print(words_dict(""))

def words_dict(text: str) -> dict:
    result = defaultdict(int)
    for word in text.split():
        result[word.lower()] += 1
    return result

if __name__ == "__main__":
    main()