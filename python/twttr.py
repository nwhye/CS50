def main():
    text = input("Input: ")
    tweet = ""
    for t in text:
        tweet += t.strip("aeiouAEIOU")
    print("Output: " + tweet)
main()
