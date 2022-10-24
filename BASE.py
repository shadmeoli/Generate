# for path and other details extraction
import os
import sys
# for simulated delays
import time
# for serilization & deserlization of dicts
import json
# ---
from copy import deepcopy
import asyncio
# better debbuging
import pprint
# caching lib
from functools import lru_cache, wraps
# for datetime extraction on execution
from datetime import datetime, timedelta
# for types
from dataclasses import dataclass
from typing import Optional

# --- Third Party Libraries -> installation candidates in the requirements.txt file
# Yaml loaders and dumpers
import yaml
from yaml import Loader
from ruamel.yaml.main import round_trip_load as yaml_load
from ruamel.yaml.main import round_trip_dump as yaml_dump
# Yaml commentary
from ruamel.yaml.comments import \
    CommentedMap as OrderedDict, \
    CommentedSeq as OrderedList
# For manual creation of tokens
from ruamel.yaml.tokens import CommentToken
from ruamel.yaml.error import CommentMark
# for the CLI stryling and flow
import emoji
import typer
from rich import console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich.table import Table
from rich.themes import Theme
from rich.syntax import Syntax
from rich.console import Console
from rich.prompt import Confirm
from rich.prompt import Prompt