import base64
from typing import Union

def urlsafe_b64encode(data: Union[str, bytes]) -> str:
    """Encode string or bytes to unpadded URL-safe base64 string."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    encoded = base64.urlsafe_b64encode(data).decode("ascii")
    return encoded.rstrip("=")

def urlsafe_b64decode(encoded: str, as_text: bool = True) -> Union[str, bytes]:
    """Decode unpadded URL-safe base64 string back to string or bytes."""
    s = encoded.strip()
    rem = len(s) % 4
    if rem > 0:
        s += "=" * (4 - rem)
    decoded = base64.urlsafe_b64decode(s.encode("ascii"))
    return decoded.decode("utf-8") if as_text else decoded
