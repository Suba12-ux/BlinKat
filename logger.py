"""Модуль для логирования с родительским классом LoggerBase."""
import logging
import sys
from pathlib import Path
from typing import Optional

from settings import LOG_LEVEL, LOG_FILE, LOG_FORMAT, LOG_DATE_FORMAT


class LoggerBase:
    """Родительский класс для логирования с настройками из settings.py."""

    def __init__(self, name: Optional[str] = None):
        """
        Инициализация логгера.

        Args:
            name: Имя логгера. Если не указано, используется имя класса.
        """
        if name is None:
            name = self.__class__.__name__

        self.logger = logging.getLogger(name)
        self._setup_logger()

    def _setup_logger(self):
        """Настройка логгера с конфигурацией из settings.py."""
        # Устанавливаем уровень логирования
        self.logger.setLevel(getattr(logging, LOG_LEVEL))

        if not self.logger.handlers:
            # Создаем форматтер
            formatter = logging.Formatter(
                fmt=LOG_FORMAT,
                datefmt=LOG_DATE_FORMAT
            )

            # Создаем обработчик для вывода в консоль
            # Для Windows используем правильную кодировку
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            # Не устанавливаем кодировку явно, пусть Python сам разбирается
            self.logger.addHandler(console_handler)

            # Создаем обработчик для записи в файл
            try:
                # Создаем директорию для логов, если её нет
                log_path = Path(LOG_FILE)
                log_path.parent.mkdir(parents=True, exist_ok=True)

                # Для файла используем UTF-8
                file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)
            except Exception as e:
                # Используем базовый print для ошибки инициализации логгера
                print(f"Не удалось создать файловый обработчик логов: {e}")

    def debug(self, message: str, *args, **kwargs):
        """Логирование на уровне DEBUG."""
        self.logger.debug(message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs):
        """Логирование на уровне INFO."""
        self.logger.info(message, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs):
        """Логирование на уровне WARNING."""
        self.logger.warning(message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs):
        """Логирование на уровне ERROR."""
        self.logger.error(message, *args, **kwargs)

    def critical(self, message: str, *args, **kwargs):
        """Логирование на уровне CRITICAL."""
        self.logger.critical(message, *args, **kwargs)

    def exception(self, message: str, *args, **kwargs):
        """Логирование исключения с уровнем ERROR."""
        self.logger.exception(message, *args, **kwargs)


# Создаем глобальный логгер для использования в других модулях
def get_logger(name: str) -> logging.Logger:
    """
    Получить логгер с указанным именем.

    Args:
        name: Имя логгера

    Returns:
        Настроенный логгер
    """
    logger = logging.getLogger(name)

    # Если у логгера еще нет обработчиков, настраиваем его
    if not logger.handlers:
        # Создаем форматтер
        formatter = logging.Formatter(
            fmt=LOG_FORMAT,
            datefmt=LOG_DATE_FORMAT
        )

        # Консольный обработчик
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Файловый обработчик
        try:
            log_path = Path(LOG_FILE)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except Exception as e:
            print(f"Не удалось создать файловый обработчик логов: {e}")

    logger.setLevel(getattr(logging, LOG_LEVEL))
    return logger
