# 🐱 BlinKot - Telegram Bot for Cat Pictures

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

**A Telegram bot that sends random cat pictures with dog fallback**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Configuration](#configuration) • [Project Structure](#project-structure) • [API Reference](#api-reference) • [Contributing](#contributing)

</div>

## ✨ Features

- **Random Cat Pictures**: Fetches random cat images from [TheCatAPI](https://thecatapi.com/)
- **Fallback to Dogs**: Automatically switches to dog pictures if cat API fails
- **Simple Commands**: Easy-to-use `/start` command with keyboard
- **Fast & Reliable**: Built with async-ready libraries and proper error handling
- **Configurable**: Easy environment-based configuration
- **Logging**: Built-in logging system with example configuration

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Telegram Bot Token (get it from [@BotFather](https://t.me/BotFather))
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/blinkot-bot.git
   cd blinkot-bot
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   ```
   
   Edit `.env` file and add your Telegram Bot Token:
   ```env
   token=YOUR_TELEGRAM_BOT_TOKEN_HERE
   ```

5. **Run the bot**
   ```bash
   python main.py
   ```

## Usage

1. **Start the bot** by running `python main.py`
2. **Open Telegram** and search for your bot
3. **Send `/start`** command to receive a random cat picture
4. **Enjoy!** The bot will send a new cat picture each time you use `/start`

### Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Get a random cat picture |
| Any text | Bot responds with "Мяу" (Meow) |

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
token=YOUR_TELEGRAM_BOT_TOKEN_HERE

# Optional (with defaults)
REQUEST_TIMEOUT=10
MAX_RETRIES=3
```

### API Configuration

The bot uses the following APIs (configured in `settings.py`):

- **Primary**: [TheCatAPI](https://thecatapi.com/) - `https://api.thecatapi.com/v1/images/search`
- **Fallback**: [TheDogAPI](https://thedogapi.com/) - `https://api.thedogapi.com/v1/images/search`

## Project Structure

```
blinkot-bot/
├── main.py              # Main bot implementation
├── settings.py          # Configuration and constants
├── example_for_log.py   # Logging examples
├── README.md           # This file
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment file
└── venv/               # Virtual environment
```

### File Descriptions

- **`main.py`**: Contains the `BlinKot` class with all bot logic
- **`settings.py`**: Configuration, constants, and environment setup
- **`example_for_log.py`**: Example logging configuration and usage
- **`.env`**: Environment variables (not in repo, create from `.env.example`)

## API Reference

### BlinKot Class

The main bot class with the following methods:

```python
class BlinKot:
    def __init__(self) -> None:
        """Initialize the bot with keyboard and handlers."""
    
    def get_new_image(self) -> Optional[str]:
        """Fetch random image URL from cat API with dog fallback."""
    
    def run(self) -> None:
        """Start the bot polling."""
```

### Key Functions

- `get_new_image()`: Fetches random animal image (cat → dog fallback)
- `_handle_start_command()`: Processes `/start` command
- `_handle_text_message()`: Handles text messages
- `_setup_keyboard()`: Configures Telegram keyboard
- `_register_handlers()`: Registers message handlers

## Troubleshooting

### Common Issues

1. **Bot not starting**
   - Check if `.env` file exists and contains valid token
   - Verify Python version (3.8+ required)
   - Ensure all dependencies are installed

2. **No images received**
   - Check internet connection
   - Verify API endpoints are accessible
   - Check logs for API errors

3. **Permission errors**
   - Ensure virtual environment is activated
   - Check file permissions for `.env` file

### Logging

The project includes logging examples. To enable logging:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

See `example_for_log.py` for detailed logging configuration.

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide
- Add type hints for new functions
- Update documentation for new features
- Write clear commit messages

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [TheCatAPI](https://thecatapi.com/) for providing cat pictures
- [TheDogAPI](https://thedogapi.com/) for dog fallback images
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library
- All contributors and users of the bot

## Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing [Issues](https://github.com/yourusername/blinkot-bot/issues)
3. Create a new issue with detailed description

---

<div align="center">

Made with ❤️ and 🐱 by [EmomovS]

**Star this repo if you found it useful!**

[⬆ Back to Top](#-blinkot---telegram-bot-for-cat-pictures)

</div>
