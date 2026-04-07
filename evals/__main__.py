"""CLI entry point: python -m evals"""

import argparse
import sys

from evals import CATEGORIES
from evals.run import run_evals

parser = argparse.ArgumentParser(description="Run Dash evals")
parser.add_argument("--category", type=str, choices=list(CATEGORIES.keys()), help="Run a single category")
parser.add_argument("--verbose", action="store_true", help="Show response previews and failure reasons")
args = parser.parse_args()
success = run_evals(category=args.category, verbose=args.verbose)
sys.exit(0 if success else 1)
