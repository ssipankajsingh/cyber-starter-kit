# A tiny next-word predictor.
#
# It's nowhere near as clever as a real chatbot, but it works on the
# same basic idea: learn which words tend to follow which, then keep
# guessing the next word. You don't need to change anything here. Just
# run it, and then try changing training_text.txt instead.

import random
from pathlib import Path

folder = Path(__file__).parent
text = (folder / "training_text.txt").read_text()

# Treat full stops as their own "word", so the predictor knows where
# sentences end.
words = text.lower().replace(".", " .").split()

# Learning: for every word, write down every word that came straight after it.
next_words = {}
for i in range(len(words) - 1):
    word = words[i]
    following = words[i + 1]
    if word not in next_words:
        next_words[word] = []
    next_words[word].append(following)

print("=== Tiny next-word predictor ===")
print("I read", len(words), "words and learned", len(next_words), "different ones.")
print()

start = input("Give me a word to start with: ").strip().lower()
if start not in next_words:
    # Pick a word that started one of the training sentences.
    start = random.choice(next_words["."])
    print("I've never seen that word, so I'll start with '" + start + "' instead.")

print()
for attempt in range(3):
    word = start
    sentence = [word]
    # Keep predicting until we hit a full stop (or 15 words, so it can't run forever).
    for step in range(15):
        if word not in next_words:
            break
        word = random.choice(next_words[word])
        if word == ".":
            break
        sentence.append(word)
    print("  " + " ".join(sentence) + ".")
