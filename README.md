# GIET AI Assistant & Student Dashboard

A comprehensive, AI-powered interactive dashboard built for the **Godavari Institute of Engineering and Technology (GIET)**, Rajahmundry. This application uses an AI bot integrated with voice recognition to answer student and visitor queries regarding college academics, placements, facilities, and events.

## 🚀 Features

- **🗣️ AI Voice Assistant:** Speak or type your questions to the GIET AI Bot! Powered by a custom RAG (Retrieval-Augmented Generation) pipeline, it uses the institution's real data to answer queries about fees, placements, faculty, and syllabi.
- **📊 Interactive Dashboard:** A quick summary of the university's core statistics, including total students, faculty, and recent placement highlights.
- **🗺️ Campus Map:** Integrated with Folium maps, providing the exact geolocation of the GIET campus on NH-16.
- **🗂️ Branch Explorer:** Deep dive into every undergraduate, postgraduate, and diploma program offered at the institution, detailing intake, duration, and tuition fees.
- **🏢 Facilities & Infrastructure:** Navigate through the hostel capacities, library details, multiple canteens, sports complexes, and more.
- **💼 Placements & Careers:** View year-over-year placement highlights (from 2021 to 2024), top visiting companies, and highest packages offered.

## 🛠️ Technology Stack

- **Frontend / UI:** [Streamlit](https://streamlit.io/)
- **Voice Recognition:** `SpeechRecognition` and `PyAudio`
- **AI / NLP Backend:** Custom RAG Agent (`rag_agent.py`) using document vector search (`vector_store.py`).
- **Mapping:** `folium` and `streamlit-folium`
- **Data:** Structured JSON (`giet_data.json`) containing +2,000 lines of highly descriptive college details.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/GIET-AI-Bot.git
   cd GIET-AI-Bot
   ```

2. **Set up a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   Ensure you have the required packages.
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: For the Voice AI feature to work, the `PyAudio` package is required. If running on Windows, standard `pip install pyaudio` should suffice. For macOS/Linux, you might need to install `portaudio` system dependencies first).*

4. **Environment Variables:**
   If the RAG agent relies on an LLM API (like Hugging Face or OpenAI), provide the required tokens in the `.env` file:
   ```env
   HF_TOKEN=your_huggingface_token
   # or
   OPENAI_API_KEY=your_openai_key
   ```

## 🏃 Running the Application

To launch the Streamlit dashboard locally, run:

```bash
streamlit run app.py
```

The application will be accessible in your web browser at `http://localhost:8501`.

## 📂 Project Structure

- `app.py`: The main entry point for the Streamlit application.
- `ui/`: Contains modular UI files for various pages (e.g., `dashboard.py`, `map.py`, `facilities.py`, `placements.py`, `voice_ai.py`).
- `rag_agent.py` & `vector_store.py`: Logic for the Retrieval-Augmented Generation model, allowing the bot to parse the massive text mappings and context efficiently.
- `giet_data.json`: The core knowledge base data dictionary loaded with extensive details utilized by the AI.
- `requirements.txt`: Project Python dependencies.
