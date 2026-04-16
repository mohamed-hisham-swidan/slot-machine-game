# 🎰 Python Slot Machine (Advanced CLI Edition)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A fully functional, terminal-based **Slot Machine** game featuring a sophisticated **Account & Save System**. This project demonstrates advanced Python concepts like file handling, dictionary mapping, and real-time console animations.

## ✨ Key Features

* **🎰 Realistic Animations:** Experience the thrill with real-time spinning symbols using `sys.stdout` flushing.
* **💾 Account Persistence:** Save your progress! Your balance is linked to an account name and protected by a password.
* **🛡️ Error Handling:** Robust input validation ensures the game doesn't crash on invalid inputs or math errors.
* **📂 File-Based Database:** Custom-built system to store player data in `.txt` files within a `saves/` directory.
* **💰 Dynamic Payouts:** Triple symbols give a **5x** payout, while doubles give a **2x** reward!



## 🛠️ Technical Logic

This project utilizes several Python power-tools:
- **`random`**: To ensure fair and unpredictable slot outcomes.
- **`os`**: To manage the local file system for saving/loading accounts.
- **`time`**: To control the pacing and feel of the "spinning" effect.
- **`f-strings`**: For clean and precise currency formatting (e.g., `$100.00`).

## 📸 Preview
<img width="689" height="539" alt="image" src="https://github.com/user-attachments/assets/72e5dd14-04a3-4fa7-bb05-7573cfdb05ce" />
