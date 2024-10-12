from datetime import datetime


def debug_print(debug: bool, *args: str) -> None:
    """example: debug_print(debug, "Getting chat completion for...:", messages)"""
    if not debug:
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = " ".join(map(str, args))
    print(f"\033[97m[\033[90m{timestamp}\033[97m]\033[90m {message}\033[0m")


if __name__ == "__main__":
    message = "你好"
    debug_print(True, "getting chat completion for ...:", message)
