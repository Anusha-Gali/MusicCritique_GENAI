# MusicCritique

## Introduction

**MusicCritique** is a revolutionary application that harnesses the power of audio transcription and Language Model (LLM) technology to provide artists and music managers with valuable insights into their recorded songs. By offering data-driven understanding and analysis, MusicCritique empowers creators to make more informed and strategic decisions before releasing their musical masterpieces to the world.

## Tools Used

The following non-trivial tools were used in this application:

- `Python` (^3.9)
- `Streamlit`: For the UI
- `Assembly AI`: For Audio transcription
- `LangChain`: For generating critical analyses and recommendations using `OpenAI`'s LLM
- `Hugging Face`: For generating cover image ideas
- `Plotly`: For visualizations
- `Pytest` and `SeleniumBase`: For testing

## Features

The application provides the following features:

**MusicCritique** offers a range of powerful features to enhance your music creation and decision-making process:

- **Audio Transcription**: It automatically transcribes audio/video files of song recordings into text, making it easier to analyze and understand the lyrics and song structure.
- **Summarization**: It summarizes the song recording.
- **Sentiment Analysis**: It utilizes sentiment analysis to gain insights into the emotional tone of the song.
- **Lyrical Content Analysis**: It analyzes the lyrical content of the songs using visualizations to identify themes, keywords that can inform creative direction.
- **Content Moderation**: It detects and reports sensitive content in the song
- **Topic Detection**: It detects topics discussed in the song.

## Installation

To get started with **MusicCritique**, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone the repository
cd music-critique
```

2. Initialize [**Poetry**](https://python-poetry.org/)

This project uses **Poetry** for package management, you can alternatively run the next steps using your virtual environment.

```bash
poetry init
```

3. Install the required dependencies using **Poetry** (or your preferred package manager)

To install the project's dependencies listed in pyproject.toml, run:

```bash
poetry install
```

4. Run the app

```bash
poetry run streamlit run app/1_Music_Critique.py
```

Access the app in your web browser at `http://localhost:8501`
