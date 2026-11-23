# TravelMate AI Chatbot

TravelMate is a chatbot that provides basic travel and tourism information about Malaysia.

## Team Members

| Name |
|---|
| MOHAMAD SYAKIR BIN NOR AZMI |
| MUHAMAD DAHNIAL BIN MOHD TAHIR |

## Destinations
- Kuala Lumpur
- Melaka
- Penang
- Langkawi
- Cameron Highlands

## Features
- Answers travel questions using a custom Q&A dataset.
- Uses TF-IDF to find relevant information.
- Uses Google Gemini API to generate responses.
- Includes a dataset-only demo mode.

## Technologies
- Python
- Streamlit
- Google Gemini API
- scikit-learn
- pandas

## Run locally

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the application:
   ```bash
   streamlit run app/streamlit_app.py
   ```

3. To use Gemini, configure your `GEMINI_API_KEY` in the environment. Otherwise, use dataset-only demo mode.

## Dataset
The custom dataset is available at `data/travel_dataset.csv`.

## Note
TravelMate is an academic prototype. It does not provide live booking, ticket prices or real-time travel updates.
