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

## 🚀 How to Run

1.  Make sure you have **Python 3** installed.
2.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Slot-Machine-Python.git](https://github.com/YOUR_USERNAME/Slot-Machine-Python.git)
    ```
3.  Run the script:
    ```bash
    python slot_machine.py
    ```

## 🛠️ Technical Logic

This project utilizes several Python power-tools:
- **`random`**: To ensure fair and unpredictable slot outcomes.
- **`os`**: To manage the local file system for saving/loading accounts.
- **`time`**: To control the pacing and feel of the "spinning" effect.
- **`f-strings`**: For clean and precise currency formatting (e.g., `$100.00`).

## 📸 Preview

```text
       ------------ welcome to Slot ------------
       -            *************** -
       -            * 🥭🍎🍉🍒🍍 * -
       -            *************** -            balance:100.00$
       -                                       -
       -    **** what are you here for ? **** -
       -    * 1-play the slot machine🎰    * -
       -    *2-recover your saved balance???* -
       -    * 3- Exit solt game🚪        * -# slot-machine-game
it is a simple slot machine game that  i made it my self , withou
