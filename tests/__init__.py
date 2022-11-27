import os
import sys
PROJECT_PATH: str = os.getcwd()
SOURCE_PATH: list[str] = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.insert(0, SOURCE_PATH)
