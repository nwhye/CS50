def main():
    text = input("Input: ")
    tweet = shorten(text)
    print(tweet)


def shorten(word):
    tweet = ""
    for t in word:
        tweet += t.strip("aeiouAEIOU")
    print(f"Output: {tweet}")


if __name__ == "__main__":
    main()
