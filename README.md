# Virtual Assistant (Proof of Concept)

This project is a simple voice-driven virtual assistant built in Python.
It is a **proof of concept**, not a full conversational assistant.

Dominican University Assignment: MSSD-745 | Week 1

## What it can do

The assistant listens for a command and responds only to specific keyword patterns:

- **Tell a joke**
  - Trigger keyword: `joke`
  - Example: `tell me a joke`
- **Tell today’s date**
  - Trigger keywords: `date` or `day`
  - Example: `what day is today`
- **Wikipedia summary**
  - Trigger phrase: `who is ...`
  - Example: `who is alan turing`
  - Behavior: speaks a short (2-sentence) summary
- **Play a song/video on YouTube**
  - Trigger phrase: `play ...`
  - Example: `play shape of you`
  - Behavior: opens YouTube, then exits assistant loop
- **Exit assistant**
  - Trigger words: `quit`, `stop`, or `goodbye`

## What it cannot do

- No general conversation or chat memory
- No follow-up context handling
- No timer/alarm/reminder features
- No weather/news/email/task integrations
- No natural-language understanding beyond the keyword checks above

If spoken text does not match supported patterns, the assistant replies:
`Sorry, I didn't catch that. Can you repeat?`

## Requirements

- Python 3.12 (or compatible)
- Microphone
- Internet connection (speech recognition, Wikipedia, YouTube)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python Virtual_Assistant.py
```

## Known Issues

- Speech recognition may miss words or mishear commands, especially in noisy environments.
- Commands must closely match supported keywords/phrases; similar phrasing may not trigger an action.
- Wikipedia lookups can fail or return unexpected summaries for ambiguous names.
- `PyAudio` can be difficult to install on some systems (notably Windows) without platform-specific wheels.
- Text-to-speech behavior can vary by system audio/voice driver configuration.
- A stable internet connection is required for speech recognition, Wikipedia queries, and YouTube playback.

## Notes

- `PyAudio` installation can be platform-specific (especially on Windows).
- Background noise can affect recognition accuracy.
- This project is intended as a demo/prototype for voice-command flow.
