TalentScout Hiring Assistant 🤖

An AI-powered hiring assistant chatbot built with Streamlit and Google’s Gemini API. It helps recruitment agencies like TalentScout conduct initial candidate screenings in a structured, conversational, and friendly way.


✨ Features

   •	👋 Warm Greetings & Clear Purpose – chatbot introduces itself and explains the process.
   •	📝 Step-by-Step Candidate Screening – collects details in order: Full Name, Email Address, Phone Number, Years of Experience, Desired Position(s), Current Location, Tech Stack (programming languages,  frameworks, databases, tools).
   •	❓ Dynamic Technical Questions – automatically generates 3–5 questions tailored to the candidate’s declared skills.
   •	🔄 Context-Aware Conversation – remembers history, steers back if off-topic, and ends gracefully when asked.
   •	⚡ Real-Time Streaming Responses – thanks to Gemini’s streaming API, users see a smooth “typing” effect.

   
🛠️ Tech Stack


•	Streamlit – for the web UI
•	Google Gemini API – for natural language generation
•	Python – backend logic
•	.env – secure API key handling


🚀 Getting Started
 1. Clone the repo
git clone https://github.com/ATIKWEBD/AI-TALENTSCOUT-HIRING-CHATBOT.git
cd AI-TALENTSCOUT-HIRING-CHATBOT
 2. Install dependencies
pip install -r requirements.txt
 3. Add your Google API Key
Create a .env file in the project root:
GOOGLE_API_KEY=your_api_key_here
 4. Run the app
streamlit run app.py


🎥 Demo Walkthrough
  •	Chatbot greets and begins structured screening.
  •	Candidate provides details step by step.
  •	Technical questions are generated based on the candidate’s stack.
  •	Conversation ends with a polite closing message.


🤝 Contribution
  Want to improve the assistant? Contributions are welcome!
  - Add more screening fields
  - Enhance tech question generation
  - Improve UI/UX
📜 License
  This project is licensed under the MIT License – feel free to use, modify, and share.
