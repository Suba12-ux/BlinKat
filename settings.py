"""Файл с настройками окружения, константами и конфигурациями."""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / 'venv' / '.env')

# Константы API
TOKEN: str = os.getenv('token', '')
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в .env файле")

CAT_API_URL: str = 'https://api.thecatapi.com/v1/images/search'
URL_BUFER: str = 'https://api.thedogapi.com/v1/images/search'

# Настройки запросов
REQUEST_TIMEOUT = 10
MAX_RETRIES = 3

# Настройки логирования
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
LOG_FILE = os.getenv('LOG_FILE', 'logs/blinkot.log')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Допустимые уровни логирования
VALID_LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
if LOG_LEVEL not in VALID_LOG_LEVELS:
    LOG_LEVEL = 'INFO'
    print(
        f"Предупреждение: Неверный LOG_LEVEL. Используется значение по умолчанию: {LOG_LEVEL}")
