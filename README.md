## ✨ Features & General Startup Information

### LED Display System
- Chained **3× 32×32 RGB LED matrices**
- Smooth horizontal text scrolling
- Dynamic two-mode display loop:
  - 📣 **“Attention!!”** — EPIC announcements
  - 💻 **“CS News”** — Random tech headlines
- Clean title bar and color accents

### Automated Newsletter
- Sends a daily email at **8 AM** containing:
  - **5 random tech articles**
  - Titles, optional descriptions, and URLs
- Uses Gmail SMTP for delivery

### News Sources
- **New York Times Technology API**
- **The Guardian Technology RSS**
- **Hacker News Top Stories**
- EPIC campus CSV-formatted announcements from GitHub

## 📁 Project Structure

```text
├── controller.py   # Handles email automation & newsletter generation
├── model.py        # Fetches news, parses feeds, loads NYT API key
├── view.py         # LED matrix rendering, scrolling, PioMatter logic
├── News.txt        # Auto-generated aggregated news cache
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<Asublime01>/<Software-Engineering-News-Project>.git
cd <Software-Engineering-News-Project>
```
- Create a .env file and insert
   ```text
   NYT_API_KEY=YOUR_KEY_HERE
   ```
### 2. Install Packages
- `requests`
- `python-dotenv`
- `feedparser`
- `Pillow`
- `numpy`
- *(Plus Adafruit + PioMatter libraries depending on your hardware)*
****

### 3. Configure Gmail SMTP (for newsletter)

Enable **App Passwords** in your Google Account settings.

Then update `controller.py` with your credentials:

```python
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
receiver_email = "recipient_email_here"
```

## 🤝 Contributing

Pull requests and improvements are welcome, especially:

- Additional news sources  
- Better display styling  
- Animated transitions  
- Multi-panel support  

