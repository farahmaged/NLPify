## Overview

**NLPify** is a Streamlit web application that provides a suite of natural language processing (NLP) tools for text analysis. It includes functionalities such as text tokenization, named entity recognition (NER), sentiment analysis, and text summarization. The app leverages popular NLP libraries like **spaCy**, **TextBlob**, and **Sumy** to process and analyze text in an intuitive, user-friendly interface.

## Usage Instructions

1. **Install Dependencies:**
   Install the required dependencies by running the following command:

    ```shell
    pip install -r requirements.txt
    ```

2. **Download spaCy Model:**
   After installing the dependencies, download the spaCy English language model:

    ```shell
    python -m spacy download en_core_web_sm
    ```

3. **Run the Application:**
   Start the Streamlit app using this command:

    ```shell
    streamlit run app.py
    ```

4. **Access the Application:**
   Open your browser and navigate to [http://localhost:8501/](http://localhost:8501/) to access the frontend.

5. **Text Analysis:**
   - **Tokenization and Lemmatization:** Enter any text, and the app will show you the tokenized text along with their lemmatized forms.
   - **Named Entity Recognition (NER):** Extract named entities such as names, dates, and locations from your text.
   - **Sentiment Analysis:** Analyze the sentiment of the text (positive, negative, or neutral).
   - **Text Summarization:** Generate concise summaries of long texts using the LexRank algorithm.

## Key Features

- **Tokenization and Lemmatization:** Breaks down text into tokens and returns their base forms (lemmas) for easier analysis.
- **Named Entity Recognition (NER):** Identifies and categorizes entities like people, organizations, and dates within the text.
- **Sentiment Analysis:** Analyzes the sentiment of the input text, categorizing it as positive, negative, or neutral.
- **Text Summarization:** Summarizes large chunks of text into concise, readable summaries using LexRank.
- **Interactive UI:** Built with [Streamlit](https://streamlit.io/), providing an easy-to-use interface for text analysis.
- **Efficient Processing:** Utilizes spaCy, TextBlob, and Sumy for fast and accurate NLP tasks.
