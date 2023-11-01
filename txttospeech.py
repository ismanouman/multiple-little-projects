from gtts import gTTS
import tempfile
import subprocess

def text_to_speech(text):
    # Dictionary for symbol pronunciation
    symbol_pronunciation = {
        '?': 'question mark',
        '!': 'exclamation mark',
        '.': 'period',
        ',': 'comma',
        '(': 'left parenthesis',
        ')': 'right parenthesis',
        '/': 'slash',
        ';': 'semicolon',
        ':': 'colon',
        "'": 'apostrophe',
        '"': 'double quotation mark',
        '=': 'equal sign',
        '\\': 'backslash',
        '*': 'asterisk',
        '$': 'dollar sign',
        '#': 'hash symbol',
        '@': 'at symbol',
        '<': 'less than symbol',
        '>': 'greater than symbol',
        '+': 'plus sign',
        '-': 'minus sign',
        '_': 'underscore',
        '[': 'left bracket',
        ']': 'right bracket',
        '{': 'left brace',
        '}': 'right brace',
        '|': 'pipe',
        '`': 'backtick',
        '~': 'tilde',
        '^': 'caret',
        '%': 'percent sign',
        '&': 'ampersand',
        '§': 'section sign',
        '°': 'degree sign',
        '¥': 'yen sign',
        '€': 'euro sign',
        '£': 'pound sign',
        '©': 'copyright symbol',
        '®': 'registered symbol',
        '™': 'trademark symbol',
        'µ': 'mu symbol',
        '•': 'bullet point',
        '♦': 'diamond',
        '♣': 'club',
        '♠': 'spade',
        '♥': 'heart',
        '♫': 'music note',
        '♪': 'musical note'
    }

    # Replace symbols with their spoken equivalents
    for symbol, pronunciation in symbol_pronunciation.items():
        text = text.replace(symbol, pronunciation)

    # Create a temporary file to save the audio
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")

    # Initialize gTTS with the modified text
    tts = gTTS(text=text, lang='en')
    tts.save(temp_file.name)

    # Play the audio using the default system player
    subprocess.run(["start", temp_file.name], shell=True)

    temp_file.close()

user_input = input("Enter the text you want to convert to speech: ")
text_to_speech(user_input)
