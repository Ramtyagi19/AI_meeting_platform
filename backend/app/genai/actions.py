from transformers import pipeline

# Zero-shot classifier
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

ACTION_LABELS = [
    "task assignment",
    "follow up",
    "deadline",
    "meeting action item"
]


def extract_actions(text: str):

    results = []

    sentences = text.split(".")

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        prediction = classifier(
            sentence,
            ACTION_LABELS
        )

        label = prediction["labels"][0]
        score = prediction["scores"][0]

        if score > 0.4:
            results.append({
                "text": sentence,
                "label": label,
                "score": round(score, 2)
            })

    return results