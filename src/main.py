
import pandas as pd
import json
import time
import sys
import os
from pathlib import Path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
from src.data_pipeline.pipeline_builder import build_pipeline

def main():
    print("Starting the data pipeline...")
    print(os.getcwd())
    # Time tracking for pipeline execution
    start_time = time.time()
    try:
        print("Building and executing the data pipeline...")
        graph = build_pipeline()
        print("Data pipeline executed successfully.")

        # Further actions can be taken with the final output
        # For example, displaying results, further processing, etc.

    except Exception as e:
        print(f"An error occurred during pipeline execution: {e}")
        return

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Pipeline completed in {execution_time:.2f} seconds.")

if __name__ == "__main__":
    main()
