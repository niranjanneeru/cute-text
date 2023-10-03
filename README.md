# Cute Text

Text Converter - Can be used with chat bots

1. Convert to Tiny Text
    
    Hello World! - ᴴᵉᶫᶫᵒ ᵂᵒʳᶫᵈ﹗
2. Bubble Text

    Hello World! - ⓗⓔⓛⓛⓞ ⓦⓞⓡⓛⓓ!
3. Black Bubble Text

    Hello World! - 🅗🅔🅛🅛🅞 🅦🅞🅡🅛🅓!
4. Cursive Text

    Hello World! - ℋℯ𝓁𝓁ℴ 𝒲ℴ𝓇𝓁𝒹!

## Installation

```bash
pip install cutetext
```

## Documentation

```python
from cutetext import CuteTextConverter
from cutetext import TINY_TEXT, BUBBLE_TEXT, BLACK_BUBBLE_TEXT,CURSIVE_TEXT

print(CuteTextConverter().convert("Hello World!", TINY_TEXT))
print(CuteTextConverter().convert("Hello World!", BUBBLE_TEXT))
print(CuteTextConverter().convert("Hello World!", BLACK_BUBBLE_TEXT))
print(CuteTextConverter().convert("Hello World!", CURSIVE_TEXT))
```
