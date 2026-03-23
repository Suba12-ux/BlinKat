"""Главный файл инициализации бота."""
import requests  # type: ignore

from telebot import TeleBot, types

from settings import (
    CAT_API_URL,
    TOKEN,
    URL_BUFER
)
from logger import LoggerBase


class BlinKot(LoggerBase):
    """Класс бота для отправки картинок котиков."""

    def __init__(self):
        # Инициализируем родительский класс LoggerBase
        super().__init__()

        self.bot = TeleBot(TOKEN)
        self._setup_keyboard()
        self._register_handlers()

        self.logger.info("Бот инициализирован")

    def _setup_keyboard(self):
        """Настройка клавиатуры."""
        self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_newcat = types.KeyboardButton('/start')
        self.keyboard.add(button_newcat)
        self.logger.debug("Клавиатура настроена")

    def _register_handlers(self):
        """Регистрация обработчиков сообщений."""

        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self._handle_start_command(message)

        @self.bot.message_handler(content_types=['text'])
        def handle_text(message):
            self._handle_text_message(message)

        self.logger.debug("Обработчики сообщений зарегистрированы")

    def get_new_image(self):
        """Получение картинки кошки с fallback на собаку."""
        self.logger.debug("Запрос новой картинки")

        try:
            response = requests.get(CAT_API_URL, timeout=5)
            response.raise_for_status()
            data = response.json()
            self.logger.info("Успешно получена картинка кошки")
        except Exception as error:
            self.logger.warning(f"Ошибка при запросе котика: {error}")
            try:
                response = requests.get(URL_BUFER, timeout=5)
                response.raise_for_status()
                data = response.json()
                self.logger.info("Успешно получена картинка собаки (fallback)")
            except Exception as fallback_error:
                self.logger.error(
                    f"Ошибка при запросе собаки: {fallback_error}")
                return None

        if data and isinstance(data, list) and len(data) > 0:
            img_url = data[0].get('url')
            self.logger.debug(f"Получен URL картинки: {img_url}")
            return img_url

        self.logger.warning("Не удалось получить URL картинки из ответа API")
        return None

    def _handle_start_command(self, message):
        """Обработка команды /start."""
        chat_id = message.chat.id
        self.logger.info(f"Получена команда /start от пользователя {chat_id}")

        img_url = self.get_new_image()

        if img_url:
            self.logger.info(f"Отправка картинки пользователю {chat_id}")
            self.bot.send_message(
                chat_id=chat_id,
                text='И так вот тебе фотка котика!'
            )
            self.bot.send_photo(
                chat_id,
                img_url,
                reply_markup=self.keyboard,
            )
        else:
            self.logger.error(
                f"Не удалось получить картинку для пользователя {chat_id}")
            self.bot.send_message(
                chat_id=chat_id,
                text='Извините, не удалось загрузить картинку'
            )

    def _handle_text_message(self, message):
        """Обработка текстовых сообщений."""
        chat_id = message.chat.id
        text = message.text
        self.logger.info(f"Получено текстовое сообщение от {chat_id}: {text}")

        self.bot.send_message(
            chat_id=chat_id,
            text='Мяу'
        )
        self.logger.debug(f"Отправлен ответ 'Мяу' пользователю {chat_id}")

    def run(self):
        """Запуск бота."""
        self.logger.info("Запуск бота...")
        print("Бот запущен...")

        try:
            self.bot.polling(non_stop=True)
        except KeyboardInterrupt:
            self.logger.info("Бот остановлен пользователем")
        except Exception as e:
            self.logger.critical(f"Критическая ошибка при работе бота: {e}")
            raise


if __name__ == "__main__":
    bot = BlinKot()
    bot.run()
