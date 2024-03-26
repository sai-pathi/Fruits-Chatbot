import streamlit as st
import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Fruit dataset with descriptions
fruits_data = {
    "apple": "Apples are a popular fruit. They come in various colors such as red, green, and yellow.",
    "banana": "Bananas are elongated, edible fruits – botanically berries – produced by several kinds of large herbaceous flowering plants in the genus Musa.",
    "orange": "Oranges are citrus fruits that are known for their high vitamin C content.",
    "grape": "Grapes are berries that grow on a vine. They come in various colors such as green, red, and purple.",
    "kiwi": "Kiwis, also known as kiwifruits, are small fruits with fuzzy brown skin and bright green flesh."
}

def respond_to_query(user_input):
    # Process user input using spaCy
    doc = nlp(user_input)

    # Extract fruit names from user input
    fruits_mentioned = [token.text.lower() for token in doc if token.text.lower() in fruits_data]

    if fruits_mentioned:
        response = ""
        for fruit in fruits_mentioned:
            response += f"{fruits_data[fruit]}\n\n"
        return response

    elif any(token.text.lower() in ["hi", "hello", "hey"] for token in doc):
        return "Hello there! How can I help you today?"

    elif any(token.text.lower() in ["bye", "goodbye"] for token in doc):
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I don't understand that. Please ask me something else."

def fruit_chatbot():
    st.title("Fruit Chatbot")

    st.markdown("""
    Welcome to the Fruit Chatbot! Ask me anything about fruits.
    """)

    user_input = st.text_input("You: ", "")

    if st.button("Send"):
        bot_response = respond_to_query(user_input)
        st.text_area("Fruit Bot:", value=bot_response, height=200, max_chars=None)

if __name__ == "__main__":
    fruit_chatbot()
