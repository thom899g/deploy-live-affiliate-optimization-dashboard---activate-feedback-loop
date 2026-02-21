#!/usr/bin/env python3
"""
Firebase Hosting Setup and Deployment Script
Mission: Set up Firebase Hosting and deploy the dashboard
This script automates Firebase project creation and deployment
"""

import os
import sys
import json
import subprocess
import logging
import time
from pathlib import Path
from typing import Dict, Optional, Tuple
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s