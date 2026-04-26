import streamlit as st
import pandas as pd

st.title("AI Talent Scouting Agent")

# --- Candidate Data ---
candidates = [
    {"name": "Ravi", "skills": ["Python", "APIs"], "experience": 3, "interest": "high"},
    {"name": "Priya", "skills": ["Java", "SQL"], "experience": 2, "interest": "medium"},
    {"name": "Arjun", "skills": ["Python", "AI"], "experience": 4, "interest": "high"},
    {"name": "Sneha", "skills": ["React", "Node"], "experience": 2, "interest": "low"},
]

# --- Input JD ---
jd = st.text_area("Paste Job Description")

# --- Parse JD ---
def parse_jd(jd_text):
    jd_text = jd_text.lower()
    skills = []
    if "python" in jd_text:
        skills.append("Python")
    if "api" in jd_text:
        skills.append("APIs")
    if "ai" in jd_text:
        skills.append("AI")
    if "sql" in jd_text:
        skills.append("SQL")
    return skills

# --- Match Score ---
def calculate_match(candidate, jd_skills):
    score = 0
    matched = []
    for skill in jd_skills:
        if skill in candidate["skills"]:
            score += 20
            matched.append(skill)
    score += candidate["experience"] * 5
    return score, matched

# --- Interest Score ---
def calculate_interest(candidate):
    if candidate["interest"] == "high":
        return 40
    elif candidate["interest"] == "medium":
        return 25
    else:
        return 10

# --- Run Agent ---
if st.button("Run Agent"):

    jd_skills = parse_jd(jd)

    st.subheader("📌 Extracted Skills")
    st.write(jd_skills if jd_skills else "No skills detected")

    st.subheader("🧪 Candidate Evaluation & Conversation")

    results = []

    for c in candidates:

        match_score, matched_skills = calculate_match(c, jd_skills)
        interest_score = calculate_interest(c)
        final_score = match_score + interest_score

        # --- Conversation Simulation ---
        st.markdown(f"""
**Candidate:** {c['name']}  
**Agent:** Hi {c['name']}, we found a role matching your profile.  
**Agent:** Are you interested in this opportunity?  
**Candidate:** I am **{c['interest']}ly interested**  

**Agent:** When can you join?  
**Candidate:** {"Within 2 weeks" if c["interest"] == "high" else "Within 1 month"}  

**Agent:** Open to salary discussion?  
**Candidate:** Yes  
---
""")

        results.append({
            "Name": c["name"],
            "Match Score": match_score,
            "Interest Score": interest_score,
            "Matched Skills": ", ".join(matched_skills),
            "Why Match": f"{', '.join(matched_skills) if matched_skills else 'No skill match'}, Exp: {c['experience']} yrs",
            "Final Score": final_score
        })

    df = pd.DataFrame(results)
    df = df.sort_values(by="Final Score", ascending=False)

    st.subheader("🏆 Final Ranked Candidates")
    st.dataframe(df)