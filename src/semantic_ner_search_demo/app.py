import subprocess


def main():
    subprocess.run(["streamlit", "run", "src/semantic_ner_search_demo/main.py"])
