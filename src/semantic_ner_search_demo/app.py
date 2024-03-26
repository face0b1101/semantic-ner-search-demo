import subprocess


def main():
    try:
        # Your main application code here
        print("Application is running. Press Ctrl+C to exit.")
        subprocess.run(["streamlit", "run", "src/semantic_ner_search_demo/main.py"])

        # Assuming a long-running process or a loop
        while True:
            pass

    except KeyboardInterrupt:
        print("\nUser requested to exit. Exiting gracefully.")
        # Perform any cleanup actions before exiting
        # For example, close files, release resources, etc.

    finally:
        print("Cleanup actions completed. Application has stopped.")
