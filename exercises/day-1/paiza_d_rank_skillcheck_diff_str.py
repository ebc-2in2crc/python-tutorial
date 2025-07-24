def diff_str(a: str, b: str):
    if a == b:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    diff_str("abc", "def") # NG
    diff_str("abc", "abc") # OK