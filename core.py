"""
Core implementation of the Kaleidoscope AI system.
"""

import os
import logging
from typing import Dict, Any
from .types import FileType

logger = logging.getLogger(__name__)

class KaleidoscopeCore:
    """Core system for software ingestion and reconstruction"""
    
    def __init__(self, work_dir: str = "workdir"):
        self.work_dir = work_dir
        self.decompiled_dir = os.path.join(self.work_dir, "decompiled")
        self.visualization = None  # Will be initialized on demand
        os.makedirs(self.decompiled_dir, exist_ok=True)
        logger.info(f"Kaleidoscope Core initialized in {self.work_dir}")

    def detect_file_type(self, file_path: str) -> FileType:
        """Detect the type of a file"""
        ext_map = {".py": FileType.PYTHON, ".cpp": FileType.CPP, ".c": FileType.C, ".js": FileType.JAVASCRIPT}
        return ext_map.get(os.path.splitext(file_path)[1].lower(), FileType.UNKNOWN)

    def ingest_software(self, file_path: str) -> Dict[str, Any]:
        """Analyze and decompile software"""
        file_type = self.detect_file_type(file_path)
        result = {"file_type": file_type.value, "decompiled_files": []}

        if file_type == FileType.BINARY:
            decompiled_path = os.path.join(self.decompiled_dir, os.path.basename(file_path) + "_decompiled.txt")
            with open(decompiled_path, 'w') as f:
                f.write("Decompiled binary content (simulated)\n")
            result["decompiled_files"].append(decompiled_path)

        return result

    def get_visualizer(self):
        """Get or create visualization component"""
        if self.visualization is None:
            from kaleidoscope_visualization import KaleidoscopeVisualizer
            self.visualization = KaleidoscopeVisualizer()
        return self.visualization
