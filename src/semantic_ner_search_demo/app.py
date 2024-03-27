import os
import signal
import subprocess


def main():
    try:
        # Ensure the correct path for main.py
        main_app_path = os.path.join(os.path.dirname(__file__), "main.py")

        # Start streamlit as a subprocess
        process = subprocess.Popen(["streamlit", "run", main_app_path])

        # Assuming a long-running process or a loop
        while True:
            pass

    except KeyboardInterrupt:
        print("\nUser requested to exit. Exiting gracefully.")
        # Terminate the subprocess gracefully
        process.send_signal(signal.SIGINT)
        process.wait()
        # Perform any cleanup actions before exiting

    finally:
        print("Cleanup actions completed. Application has stopped.")


if __name__ == "__main__":
    main()
