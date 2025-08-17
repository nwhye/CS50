import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'<iframe src="https?://(www\.)?youtube\.com/embed/(\w+)"', s):
        video_id = match.group(2)
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()
