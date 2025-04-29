import streamlit as st
from textblob import TextBlob
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def sumy_summarizer(doc_text):
    parser = PlaintextParser.from_string(doc_text, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


@st.cache
def text_analyzer(input_text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(input_text)
    all_data = [('"Token":{},\n"Lemma":{}'.format(token.text, token.lemma_)) for token in doc]
    return all_data


@st.cache
def entity_analyzer(input_text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(input_text)
    tokens = [token.text for token in doc]
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    all_data = ['"Token":{},\n"Entities":{}'.format(tokens, entities)]
    return all_data


def main():
    st.write("###Natural Language Processing On the Go..")
    st.title("NLPify")

    # Tokenization
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize Your Text")

        message = st.text_area("", "Enter text..")
        if st.button("Analyze"):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)

    # Entity Extraction
    if st.checkbox("Show Named Entities"):
        st.subheader("Analyze Your Text")

        message = st.text_area("", "Enter text..")
        if st.button("Extract"):
            entity_result = entity_analyzer(message)
            st.json(entity_result)

    # Sentiment Analysis
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Analyze Your Text")

        message = st.text_area("", "Enter text..")
        if st.button("Analyze"):
            blob = TextBlob(message)
            result_sentiment = blob.sentiment
            polarity = result_sentiment.polarity

            if polarity > 0:
                sentiment_word = "Positive"
                color = "#c6f7c6"
            elif polarity < 0:
                sentiment_word = "Negative"
                color = "#f7c6c6"
            else:
                sentiment_word = "Neutral"
                color = "#fff7c6"

            st.markdown(f"<h3 style='color:{color};'>{sentiment_word}</h3>", unsafe_allow_html=True)
            st.json(result_sentiment)

    # Summarization
    if st.checkbox("Show Text Summarization"):
        st.subheader("Summarize Your Text")

        message = st.text_area("Enter Text", "Type Here ..")
        if st.button("Summarize"):
            st.text("Using Sumy Summarizer ..")
            summary_result = sumy_summarizer(message)
            st.success(summary_result)


if __name__ == '__main__':
    main()
