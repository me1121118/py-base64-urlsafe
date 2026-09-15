import pytest
from py_base64_urlsafe import urlsafe_b64encode, urlsafe_b64decode

def test_urlsafe_b64():
    raw = "FastAPI & Python 3.10+ URL-safe tokens!"
    token = urlsafe_b64encode(raw)
    assert "=" not in token

    restored = urlsafe_b64decode(token)
    assert restored == raw
