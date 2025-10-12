"""
Minimal logger module that provides easy-to-use logging functionality. Logging
can be globally enabled or disabled, and the log level can be set to control the
verbosity of the output.
"""

_MAX_LOG_LEVEL = 40
_LOG_LEVEL = 20  # Default to INFO level
_LOG_THRESHOLD = _MAX_LOG_LEVEL - _LOG_LEVEL


class Logger:
    """Logger class that can be used to log messages on the terminal"""

    global _LOG_THRESHOLD

    def __init__(self, module: str):
        """Initializes the logger
        :param module: The name of the module that is doing the logging.
        """
        self._module = module

    def debug(self, message: str) -> None:
        """Log a debug level message.

        :param message: The message to log.
        """
        if _LOG_THRESHOLD >= 30:
            print(f"{self._module}|DEBUG: {message}")

    def info(self, message: str) -> None:
        """Log an info level message.

        :param message: The message to log.
        """
        if _LOG_THRESHOLD >= 20:
            print(f"{self._module}| INFO: {message}")

    def error(self, message: str) -> None:
        """Log an error level message.

        :param message: The message to log.
        """
        if _LOG_THRESHOLD >= 10:
            print(f"{self._module}|ERROR: {message}")


def set_log_level(level: int) -> None:
    """Set the logging level globally. Changing this value instantly changes
    the log levels for all logger instances.

    :param level: The logging level to set (10 for DEBUG, 20 for INFO, 30 for
    ERROR, 100 for DISABLED).
    """
    global _MAX_LOG_LEVEL
    global _LOG_LEVEL
    global _LOG_THRESHOLD

    if level in (100, 10, 20, 30):
        _LOG_LEVEL = level
        _LOG_THRESHOLD = _MAX_LOG_LEVEL - _LOG_LEVEL
    else:
        raise ValueError(
            (
                f"Invalid log level [{level}]. "
                "Use 100 - DISABLED, 10 - DEBUG, 20 -INFO or 30 - ERROR."
            )
        )


def disable_logging() -> None:
    """Disable all logging. This is equivalent to calling set_log_level(100)."""
    set_log_level(100)
