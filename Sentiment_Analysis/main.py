from transformers import pipeline

def main():
    # Load a pretrained sentiment-analysis pipeline
    sentiment_analyzer = pipeline("sentiment-analysis")

    print("=== Sentiment Analysis Tool ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_text = input("Enter text to analyze: ")

        if user_text.lower() == "exit":
            print("Goodbye!")
            break

        # Run sentiment analysis
        result = sentiment_analyzer(user_text)[0]

        label = result["label"]
        score = result["score"]

        print(f"\nSentiment: {label}")
        print(f"Confidence: {score:.4f}\n")


if __name__ == "__main__":
    main()
