# 🔐 Password Strength Analyzer

A simple but powerful web app that checks password strength using [zxcvbn](https://github.com/dropbox/zxcvbn) — developed with Flask.

---

## 🚀 Features

- Real-time password strength scoring (0–4)
- Smart analysis using patterns and dictionary checks
- Clean dark-mode UI with cybersecurity theme
- Simple Flask backend — easy to expand

---

## 🛠️ Technologies Used

- Python 3.13
- Flask
- zxcvbn
- HTML/CSS (no JavaScript yet)

---

## 🧠 Password Strength Scale

| Score | Label         | Meaning                     |
|-------|---------------|-----------------------------|
| 0     | Very Weak     | Easily guessable            |
| 1     | Weak          | Slight improvement          |
| 2     | Medium        | Some resistance to guessing |
| 3     | Strong        | Good overall security       |
| 4     | Very Strong   | Excellent password          |

---

## 📸 Screenshots

![Strong Password Screenshot](Strong.png)

![Weak Password Screenshot](Weak.png)

---

## ⚙️ How to Run

1. Clone the repository:
  ```bash
   git clone https://github.com/yourusername/password-analyzer.git
   cd password-analyzer

2. Create virtual environment:
  ```bash
    python -m venv venv
    venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the app:

python app.py

5. Visit: http://127.0.0.1:5000


🧑‍💻 Author
Made with ❤️ by Saifeddine — aspiring cybersecurity engineer
