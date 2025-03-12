#!/usr/bin/env python3
"""
Kaleidoscope AI System Launcher
==============================
Local development version
"""

import os
import json
import logging
import uvicorn
from pathlib import Path
from kaleidoscope_core import KaleidoscopeCore

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger("KaleidoscopeLauncher")

def main():
    """Main entry point"""
    try:
        # Load configuration
        config_path = Path(__file__).parent / "config.json"
        with open(config_path) as f:
            config = json.load(f)
        
        # Initialize core system
        core = KaleidoscopeCore(work_dir=config["system"]["work_dir"])
        
        # Start API server
        from kaleidoscope_core.api import create_app
        app = create_app()
        
        logger.info("Starting Kaleidoscope AI system...")
        uvicorn.run(
            app,
            host=config["api"]["host"],
            port=config["api"]["port"],
            log_level="info"
        )
        
        return 0
    except Exception as e:
        logger.error(f"Error launching system: {str(e)}")
        return 1

if __name__ == "__main__":
    main()
