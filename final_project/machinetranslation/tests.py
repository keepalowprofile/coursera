import unittest
from unittest.mock import patch
import machinetranslation
from machinetranslation.translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):

    @patch('translator.MyMemoryTranslator')
    def test_english_to_french_translation(self, mock_translator):
        mock_translate = mock_translator.return_value.translate
        mock_translate.return_value = "Bonjour"

        english_text = "Hello"
        expected_french_text = "Bonjour"
        translated_text = english_to_french(english_text)

        mock_translate.assert_called_once_with(english_text, from_lang="en", to_lang="fr")
        self.assertEqual(translated_text, expected_french_text)

    @patch('translator.MyMemoryTranslator')
    def test_french_to_english_translation(self, mock_translator):
        mock_translate = mock_translator.return_value.translate
        mock_translate.return_value = "Hello"

        french_text = "Bonjour"
        expected_english_text = "Hello"
        translated_text = french_to_english(french_text)

        mock_translate.assert_called_once_with(french_text, from_lang="fr", to_lang="en")
        self.assertEqual(translated_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()
