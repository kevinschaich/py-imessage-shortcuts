# `py-imessage-shortcuts`

Send iMessages using Python through the Shortcuts app.

Requires macOS Monterey (macOS 12) or later. Compatible with Apple Silicon including M1, M1 Pro, & M1 Max.

### Installation

1. Download [`send-imessage.shortcut`](https://github.com/kevinschaich/py-imessage-shortcuts/raw/master/send-imessage.shortcut) and open it using Finder.
2. Click the blue **Add Shortcut** button (you can use the 3-dot menu to inspect the steps executed if you desire).
3. Install `py-imessage-shortcuts` using `pip`:

```
pip install py-imessage-shortcuts
```

### Usage

```python
import imessage

imessage.send(['+1 555-555-5555'], 'Hello World!')
```

### Bugs

Use [Issues](https://github.com/kevinschaich/py-imessage-shortcuts/issues). PRs welcome and appreciated 😊

### License

[MIT License](https://github.com/kevinschaich/py-imessage-shortcuts/blob/master/LICENSE).
