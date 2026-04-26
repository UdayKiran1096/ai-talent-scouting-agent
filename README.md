# AI-Powered Talent Scouting & Engagement Agent

## Overview
This project simulates an AI recruiter agent that:
- Parses a job description
- Matches candidates based on skills and experience
- Simulates conversational outreach to assess interest
- Produces a ranked shortlist with explainability

## How it Works
1. Job Description is analyzed to extract key skills
2. Candidates are matched based on skill overlap and experience
3. A simulated conversation evaluates candidate interest
4. Candidates are ranked using:
   Final Score = Match Score + Interest Score

## Scoring Logic
- Match Score:
  - 20 points per matching skill
  - 5 points per year of experience
- Interest Score:
  - High = 40
  - Medium = 25
  - Low = 10

## How to Run
pip install streamlit pandas openai
streamlit run app.py

## Future Improvements
- LLM-based JD parsing
- Real candidate data integration
- Live conversational agents
