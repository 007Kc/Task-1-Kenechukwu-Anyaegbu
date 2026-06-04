# 🎓 Kc's Learning Platform

A beginner-friendly command-line application that recommends personalised
courses to users based on their selected interests.

---

## 📋 Description

Kc's Learning Platform is a Python-based recommendation system that collects
a user's personal details and interests, then suggests the most relevant
courses from the course catalogue using a tag-based similarity algorithm.

---

## 🚀 Features

- User onboarding — collects name, username and age
- Interest selection — displays all available topics for the user to choose from
- Smart recommendations — matches user interests to courses and ranks them by relevance
- Animated loading sequences for a polished user experience

---

## 📁 Project Structure
Kc-Learning-Platform/
│
├── main.py                # Entry point — handles user input and program flow
└── Recommendation.py      # Core logic — User class, courses catalogue and recommendation system


---

## ⚙️ How It Works

1. User enters their name, username and age
2. User selects their interests from a list of available tags
3. The recommendation system compares selected interests against course tags
4. Courses are scored based on the number of matching tags
5. Results are displayed ranked from most to least relevant

---

## 🗂️ Available Courses

| Course | Tags |
|---|---|
| Python Basics | Python, Programming, Coding, Beginner, Automation |
| AI Fundamentals | AI, Machine Learning, Python, Data, Automation |
| Web Development | HTML, CSS, JavaScript, Web Design, Frontend |
| UI / UX Design | Design, Figma, UI, UX, Creativity |
| Data Science | Data, Python, Analytics, Statistics, Machine Learning |

---


---

## ▶️ How To Run

1. Clone or download the project files
2. Open your terminal and navigate to the project folder
```bash
   cd path/to/project
```
3. Run the program
```bash
   python main.py
```

---

## 📌 Known Limitations

- Course catalogue is currently static — new courses require manual updates to `Recommendation.py`
- Interest index input does not yet support multi-digit indexes robustly
- Recommendation algorithm is tag-based only — no machine learning involved

---



---

## 👤 Author

**Kenechukwu Ronaldo Anyaegbu**
