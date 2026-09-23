import logging
import os
import tempfile
import unittest
from pathlib import Path

from app.logging_config import setup_logging


class SetupLoggingTests(unittest.TestCase):
    def setUp(self):
        self.root_logger = logging.getLogger()
        self.original_level = self.root_logger.level
        self.original_handlers = list(self.root_logger.handlers)
        self._clear_handlers()

    def tearDown(self):
        self._clear_handlers()

        for handler in self.original_handlers:
            self.root_logger.addHandler(handler)

        self.root_logger.setLevel(self.original_level)

    def _clear_handlers(self):
        for handler in list(self.root_logger.handlers):
            self.root_logger.removeHandler(handler)
            handler.flush()
            handler.close()

    def test_setup_logging_creates_console_and_file_handlers(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            cwd = os.getcwd()
            os.chdir(tmp_dir)
            try:
                setup_logging()

                self.assertEqual(self.root_logger.level, logging.DEBUG)
                self.assertEqual(len(self.root_logger.handlers), 2)

                stream_handlers = [
                    handler for handler in self.root_logger.handlers
                    if isinstance(handler, logging.StreamHandler)
                ]
                file_handlers = [
                    handler for handler in self.root_logger.handlers
                    if isinstance(handler, logging.FileHandler)
                ]

                self.assertTrue(stream_handlers)
                self.assertTrue(file_handlers)
                self.assertTrue(Path("app.log").exists())
                self.assertTrue(file_handlers[0].baseFilename.endswith("app.log"))
            finally:
                self._clear_handlers()
                os.chdir(cwd)

    def test_setup_logging_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            cwd = os.getcwd()
            os.chdir(tmp_dir)
            try:
                setup_logging()
                first_handler_count = len(self.root_logger.handlers)

                setup_logging()

                self.assertEqual(len(self.root_logger.handlers), first_handler_count)
                self.assertEqual(first_handler_count, 2)
            finally:
                self._clear_handlers()
                os.chdir(cwd)


if __name__ == "__main__":
    unittest.main()
