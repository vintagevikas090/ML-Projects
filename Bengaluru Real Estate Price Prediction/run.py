

import subprocess
# Command to run the Streamlit app
command = [
    "streamlit",
    "run",
    "Bengaluru Real Estate Price Prediction.py"
]

try:
    # Execute the command
    subprocess.run(command, check=True)
except FileNotFoundError:
    print("Streamlit is not installed. Please install it using 'pip install streamlit'.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while running the Streamlit app: {e}")

