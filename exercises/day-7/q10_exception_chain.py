# 問題: raise from を使って例外の連鎖を起こしてください。

if __name__ == '__main__':
    try:
        try:
            raise ValueError("何か値エラー")
        except ValueError as e:
            raise RuntimeError("何かエラー") from e
    except RuntimeError as e:
        print(f"捕捉したエラー: {e}")
        print(f"元のエラー: {e.__cause__}")