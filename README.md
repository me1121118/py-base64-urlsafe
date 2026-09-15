# py-base64-urlsafe

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-base64-urlsafe/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency unpadded URL-safe base64 string and byte encoder/decoder for Python.

---

## 🚀 Features

- 🪶 **Zero Dependencies**: Pure Python standard library (`base64`).
- 🔗 **Clean URL Tokens**: Strips trailing `=` padding characters for shorter and cleaner URL query tokens.
- 🔄 **Auto Padding Recovery**: Automatically re-adds missing `=` padding during decode.

---

## 📦 Installation

```bash
pip install py-base64-urlsafe
```

---

## 🛠️ Quickstart

```python
from py_base64_urlsafe import urlsafe_b64encode, urlsafe_b64decode

# Encode string without padding
token = urlsafe_b64encode("hello world?")
print(token)  # aGVsbG8gd29ybGQ_

# Decode unpadded string
text = urlsafe_b64decode(token)
print(text)   # hello world?
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this base64 utility made your URL tokens cleaner, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [buymeacoffee.com/kcidi4148](https://buymeacoffee.com/kcidi4148)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
