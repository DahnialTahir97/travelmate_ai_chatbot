# TravelMate AI Chatbot

**AI-Powered Travel & Tourism Assistant for Malaysia**

TravelMate is a domain-specific conversational assistant for introductory travel information about five Malaysian destinations: Kuala Lumpur, Melaka, Penang, Langkawi and Cameron Highlands. It uses a custom question-and-answer dataset, TF-IDF retrieval, and Google Gemini to generate grounded responses.

> **Project status:** Initial working prototype. Dataset-only mode runs without an API key. Gemini mode requires a valid Google Gemini API key.

## Team
| Name | GitHub username | Role |
|---|---|---|
| To be completed by group | To be completed | Project Leader |
| To be completed by group | To be completed | Frontend Developer |
| To be completed by group | To be completed | Backend Developer / Model Integrator |
| To be completed by group | To be completed | Domain Specialist |

Replace these placeholders with the actual four group members. Add the lecturer as a repository collaborator as required by the course brief. Do not claim contributions that a member has not made.

## Domain and custom dataset
- **Domain:** Tourism and travel information
- **Geographic scope:** Malaysia
- **Destinations:** Kuala Lumpur, Melaka, Penang, Langkawi and Cameron Highlands
- **Dataset:** `data/travel_dataset.csv`, with 49 Q&A pairs and the required `Question` and `Answer` columns.
- The answers are concise educational summaries. The domain specialist must verify details against specific official source pages and record URLs and access dates in `data/SOURCES.md` before final submission.

## Features
- Streamlit conversational interface
- TF-IDF question retrieval from the custom CSV dataset
- Gemini LLM response generation using retrieved context
- Dataset-only demo mode requiring no API key
- Expandable display of retrieved knowledge-base references
- Unit tests for dataset size, retrieval and empty-input handling

## Architecture
`User -> Streamlit UI -> Python service -> TF-IDF retrieval from CSV -> retrieved context + user question -> Gemini API -> response`

In dataset-only mode, TravelMate returns the best matching dataset answer and does not call an LLM.

See [docs/architecture.md](docs/architecture.md).

## Technology
- Python 3.10+
- Streamlit
- Google Gen AI Python SDK
- scikit-learn TF-IDF and cosine similarity
- pandas
- pytest

## Model
- **Provider:** Google Gemini API
- **Default model ID:** `gemini-2.5-flash` (configurable with `GEMINI_MODEL`)
- **Integration:** Google Gen AI Python SDK
- **Prompting:** Domain-specific instructions and retrieved custom Q&A context
- **Fine-tuning:** Not used
- **Retrieval:** TF-IDF with unigrams and bigrams; cosine similarity ranks candidate questions

## Quick start

### 1. Create a virtual environment
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

### 2. Install packages
```bash
pip install -r requirements.txt
```

### 3. Configure Gemini (optional)
Copy `.env.example` to `.env` and set your own `GEMINI_API_KEY`. Never commit `.env`. The repository ignores it.

### 4. Run
```bash
streamlit run app/streamlit_app.py
```
When no key is configured, leave **Dataset-only demo mode** enabled in the sidebar.

### 5. Run tests
```bash
pytest -q
```

## Repository structure
```text
data/       Custom Q&A CSV and source-verification notes
src/        Retrieval, model integration and chatbot service
app/        Streamlit user interface
tests/      Automated tests and sample manual test questions
docs/       Architecture, scope and project documentation
.github/    Issue and pull request templates
README.md
requirements.txt
.env.example
.gitignore
```

## Testing
Run `pytest -q`. The sample prompts in `tests/test_questions.csv` support manual evaluation. The team should expand the tests with expected topics and record both successful and unsuccessful model responses for the presentation.

## Limitations
- No live ticket prices, bookings, hotel reservations, transport schedules, traffic or weather forecasts.
- Opening hours, access conditions and availability can change; confirm them with official providers.
- Coverage is limited to five destinations and the prepared dataset.
- Retrieval may return weak matches for ambiguous or out-of-domain questions.
- LLM output can be inaccurate; verify important travel decisions with official sources.
- TravelMate is informational and is not an emergency service.

## Data sources and verification
Starting points for source verification:
- Tourism Malaysia: https://www.malaysia.travel/
- Malaysia Immigration Department: https://www.imi.gov.my/
- Malaysian Meteorological Department: https://www.met.gov.my/
- Official websites of individual attractions, transport operators and local authorities.

These are starting points, not a claim that every answer has already been verified. Record the exact page URL, the related Q&A/topic and access date in [data/SOURCES.md](data/SOURCES.md).

## GitHub teamwork and academic integrity
The course brief requires meaningful commits from every member, issues and a project board, branches and reviewed pull requests. Each student must use their own GitHub account and commit their actual work. Do not fabricate contributor activity or share account credentials. Repository history should accurately represent the team's work.

## GenAI use
Disclose all GenAI tools used, the tasks they assisted with, and the code/data each member reviewed or modified. Complete the required FSKM GenAI declaration. Every member must understand and explain their own contribution.

## Licence
Academic coursework prototype. No open-source licence has been selected by the group.
