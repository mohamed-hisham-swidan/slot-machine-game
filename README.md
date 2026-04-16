# 🎰 Python Slot Machine (Advanced CLI Edition)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A fully functional, terminal-based **Slot Machine** game featuring a sophisticated **Account & Save System**. This project demonstrates advanced Python concepts like file handling, dictionary mapping, object-oriented design, and data persistence.

## ✨ Key Features

* **🎰 Realistic Animations:** Experience the thrill with real-time spinning symbols using `sys.stdout` flushing.
* **💾 Account Persistence:** Save your progress! Your balance is linked to an account name and protected by a password.
* **🛡️ Error Handling:** Robust input validation ensures the game doesn't crash on invalid inputs or math errors.
* **📂 File-Based Database:** Custom-built system to store player data in `.txt` files within a `saves/` directory.
* **💰 Dynamic Payouts:** Triple symbols give a **5x** payout, while doubles give a **2x** reward!
* **🎯 Multi-Account Support:** Create and manage multiple player accounts with independent balances.
* **📊 Session Tracking:** View your game statistics and balance history.

## 🛠️ Technical Logic

This project utilizes several Python power-tools:
- **`random`**: To ensure fair and unpredictable slot outcomes.
- **`os`**: To manage the local file system for saving/loading accounts.
- **`time`**: To control the pacing and feel of the "spinning" effect.
- **`f-strings`**: For clean and precise currency formatting (`$100.00`).
- **`json`** (optional): For structured data serialization.

## 📸 Preview
<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/eedd53d1-364d-4587-83d0-4ceb24f2d3b9" />


## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mohamed-hisham-swidan/slot-machine-game.git
cd slot-machine-game
```

2. Run the game:
```bash
python main.py
```

## 📖 How to Play

1. **Create/Login Account:** Enter your username and password
2. **Place Your Bet:** Enter your wager amount
3. **Spin!:** Watch the reels spin and see your results
4. **Check Payouts:**
   - 🎰 Triple Match: 5x your bet
   - 🎰 Double Match: 2x your bet
   - 🎰 No Match: Lose your bet
5. **Save & Exit:** Your balance is automatically saved

## 📁 Project Structure

```
slot-machine-game/
├── main.py                 # Main game logic and CLI interface
├── saves/                  # Player account data directory
│   └── [username].txt     # Individual player data files
├── README.md              # This file
└── LICENSE                # MIT License
```

## 💾 Save System

Player data is stored in simple `.txt` files with the following format:
```
username: player_name
password: hashed_password
balance: 1000.00
created_at: 2026-04-16
last_played: 2026-04-16
```

## 🎮 Game Mechanics

| Result | Symbols | Payout | Example |
|--------|---------|--------|---------|
| Triple Match | 🍒🍒🍒 | 5x bet | Bet $10 → Win $50 |
| Double Match | 🍊🍊🔔 | 2x bet | Bet $10 → Win $20 |
| No Match | 🍒🔔🍊 | $0 | Bet $10 → Lose $10 |

## 🔒 Security Features

- Password-protected accounts
- Isolated player data files
- Input validation to prevent exploits
- Balance integrity checks

## 🐛 Error Handling

The game gracefully handles:
- Invalid bet amounts (negative, non-numeric, exceeds balance)
- Invalid account credentials
- File system errors
- Unexpected user inputs

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Improve documentation
- Submit pull requests

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mohamed Hisham Swidan**
- GitHub: [@mohamed-hisham-swidan](https://github.com/mohamed-hisham-swidan)

## 🙏 Acknowledgments

- Inspired by classic arcade slot machines
- Built with ❤️ using pure Python
- Special thanks to the Python community

## 📞 Support

If you encounter any issues:
1. Check the [Issues](https://github.com/mohamed-hisham-swidan/slot-machine-game/issues) section
2. Review the error messages carefully
3. Ensure Python 3.6+ is installed
4. Verify the `saves/` directory has proper permissions

---

**Enjoy spinning! 🎰💰**
