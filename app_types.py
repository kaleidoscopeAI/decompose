"""
Type definitions for the Kaleidoscope AI system.
"""

from enum import Enum

class FileType(Enum):
    """Supported file types"""
    BINARY = "binary"
    JAVASCRIPT = "javascript"
    PYTHON = "python"
    CPP = "cpp"
    C = "c"
    UNKNOWN = "unknown"
