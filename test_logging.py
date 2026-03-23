"""Тестирование работы логирования."""
from logger import LoggerBase, get_logger


class TestClass(LoggerBase):
    """Тестовый класс для демонстрации логирования."""

    def test_method(self):
        """Тестовый метод с разными уровнями логирования."""
        self.debug("Это сообщение уровня DEBUG")
        self.info("Это сообщение уровня INFO")
        self.warning("Это сообщение уровня WARNING")
        self.error("Это сообщение уровня ERROR")

        try:
            raise ValueError("Тестовое исключение")
        except ValueError as e:
            self.exception(f"Произошло исключение: {e}")


def test_global_logger():
    """Тестирование глобального логгера."""
    logger = get_logger("global_test")
    logger.info("Тестирование глобального логгера")
    logger.debug("Debug сообщение от глобального логгера")


if __name__ == "__main__":
    print("=== Тестирование класса LoggerBase ===")
    test_obj = TestClass()
    test_obj.test_method()

    print("\n=== Тестирование глобального логгера ===")
    test_global_logger()

    print("\n=== Проверка создания директории для логов ===")
    from pathlib import Path
    from settings import LOG_FILE

    log_path = Path(LOG_FILE)
    print(f"Путь к файлу логов: {log_path.absolute()}")
    print(f"Директория существует: {log_path.parent.exists()}")
