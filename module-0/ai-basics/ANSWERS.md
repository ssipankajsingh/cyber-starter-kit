# Answers: AI basics

## Part 1

1. The bundle of patterns a computer learned from lots of examples. You feed it something new, and it uses those patterns to give an answer or a guess.
2. Predict the next word, based on all the words so far.
3. It only looks at the one word before, and it's only seen a few sentences. It has no idea what the whole sentence means. It just knows which words have followed which.
4. It wouldn't know. It might say so, or it might make up an answer that sounds right. (Some chatbots can search the web to fill the gap, but the model itself only knows its training text.)
5. Because it's predicting words that *sound* like a good answer, not checking facts. A confident tone is just a pattern it learned from text, and it says nothing about whether the answer is true. This is often called a **hallucination**.

## Part 2

1. The hidden instructions a company gives the chatbot before you start talking. The company (the people building the bot) writes it.
2. The model sees the system prompt and your message as one big block of text. It has no reliable way to tell "rules from the company" apart from "words from the user", so instructions in your message can override the real ones.
3. In prompt injection, *you* type the sneaky instruction into the chat. In indirect prompt injection, the instruction is hidden in something the chatbot reads, like a web page, email or file, so the person using the bot might not know it's there.
4. Don't give the chatbot the addresses. If it doesn't have them, no trick can make it leak them. Give it only what it needs to do its job.
5. Lots of right answers. Scripts are great at: checking thousands of links, counting failed logins, scanning files for known malware. People are still needed for: deciding if an odd login is a real attack or just someone who forgot their password, talking to a worried user, deciding how to respond to an incident.
