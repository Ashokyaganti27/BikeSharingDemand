
from dataclasses import dataclass
from pathlib import Path
@dataclass
class DataIngestionConfig:
    filepath:Path
    link: str
    unzip_path: Path

@dataclass
class DatavalidationConfig:
    root_dir : Path
    train_path: Path
    test_path: Path
    status_file: str

    
  