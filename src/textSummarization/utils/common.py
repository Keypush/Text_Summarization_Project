import os
from tabnanny import verbose
from box.exceptions import BoxValueError
import yaml
from textSummarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Returns:
        ConfigBox: A ConfigBox object containing the yaml data.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
        logger.info(f"YAML file loaded successfully: {path_to_yaml}")
        return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error occurred while converting YAML content to ConfigBox: {path_to_yaml}")
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(f"Error occurred while reading YAML file: {path_to_yaml}")
        raise e
    
def create_directories(path_to_directories: list, verbose: bool = True) -> None:
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): A list of paths to directories to be created.
        verbose (bool, optional): If True, logs the directory creation process. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created successfully: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file or directory in a human-readable format.

    Args:
        path (Path): Path to the file or directory.

    Returns:
        str: Size of the file or directory in a human-readable format.
    """
    size_in_bytes = os.path.getsize(path)
    size_in_kb = size_in_bytes / 1024
    size_in_mb = size_in_kb / 1024
    size_in_gb = size_in_mb / 1024

    if size_in_gb >= 1:
        return f"{size_in_gb:.2f} GB"
    elif size_in_mb >= 1:
        return f"{size_in_mb:.2f} MB"
    elif size_in_kb >= 1:
        return f"{size_in_kb:.2f} KB"
    else:
        return f"{size_in_bytes} Bytes"
