import pandas as pd
from config import ROWS_TO_SKIP_WHILE_READING_CSV, INPUT_FOLDER, OUTPUT_FOLDER
from chatgpt import return_chatgpt_response
from os import listdir

input_files = listdir(INPUT_FOLDER)

if not input_files:
    raise ValueError("No input files found")

for file in input_files:
    INPUT_FILE = f"{INPUT_FOLDER}/{file}"
    OUTPUT_FILE = f"{OUTPUT_FOLDER}/{file}"
    
    # Reading csv
    csv = pd.read_csv(INPUT_FILE, skiprows=ROWS_TO_SKIP_WHILE_READING_CSV)

    # Getting formated strings
    step = list(csv["Step"])
    formatted_steps = "\n".join(step) if isinstance(step, list) else step

    # Replace steps
    csv["Step"] = return_chatgpt_response(formatted_steps)

    # save to outputs folder
    csv.to_csv(OUTPUT_FILE, index=False)
