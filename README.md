# `py-imessage-shortcuts`

Send iMessages using Python through the Shortcuts app.

Requires macOS Monterey (macOS 12) or later. Compatible with Apple Silicon including M1, M1 Pro, & M1 Max.

## Installation

1. Download the `send-imessage.shortcut` file from this repository and open it using Finder.
2. Click the blue **Add Shortcut** button (you can use the 3-dot menu to inspect actions if desire).
3. Install the python package:

```
pip install py-imessage-shortcuts
```

## Usage

```python
import imessage

imessage.send(['+1 555-555-5555'], 'Hello World!')
```
