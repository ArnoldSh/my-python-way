def main() -> None:
    is_palindrome("heleh")
    is_palindrome("helleh")
    is_palindrome("he")
    is_palindrome("hh")
    is_palindrome("h")
    is_palindrome("")

def is_palindrome(x: str) -> bool:
    palindrome = True
    x_len = len(x)
    for a in range(x_len // 2):
        b = x_len - a - 1
        palindrome = x[a] == x[b]
        if not palindrome:
            break
    print(f'{x} is palindrome - {palindrome}')
    return palindrome

if __name__ == "__main__":
    main()

