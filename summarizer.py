from transformers import pipeline

# Inizializza il summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def main():
    print("📄 Incolla il testo da riassumere (digita 'FINE' su una nuova riga per terminare):\n")
    lines = []
    while True:
        line = input()
        if line.strip().lower() == 'fine':
            break
        lines.append(line)
    full_text = ' '.join(lines)

    # Genera il riassunto
    summary = summarizer(full_text, max_length=130, min_length=30, do_sample=False)

    print("\n📝 Riassunto:")
    print(summary[0]['summary_text'])

if __name__ == "__main__":
    main()
