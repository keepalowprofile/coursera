"""
This module contains functions to translate text between English and French.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French using the MyMemory Translator.
    Args: english_text (str): The English text to be translated.
    Returns: str: The translated French text.
    """
    translator = MyMemoryTranslator()

    # Translate the English text to French
    french_text = translator.translate(english_text, from_lang="en", to_lang="fr")
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using the MyMemory Translator.
    Args: french_text (str): The French text to be translated.
    Returns: str: The translated English text.
    """
    translator = MyMemoryTranslator()

    # Translate the French text to English
    english_text = translator.translate(french_text, from_lang="fr", to_lang="en")
    return english_text
