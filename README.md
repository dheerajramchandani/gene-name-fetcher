# gene-name-fetcher

This tool expects an Excel sheet as the input (`.xlsx` or `.xls` file). The input file should have only one column (and it has to be the first column) with the gene names that we want to look for. The heading for this column (essentially the cell A1) must be **Uniprot ID**.

## Instructions

### One time setup
1. Download Python 3.7 or 3.8 from python.org.
2. Open a Terminal window (on macOS) or Command Prompt (on Windows).
3. Run the command: `git clone https://github.com/dheerajramchandani/gene-name-fetcher.git`.
4. Run the command: `cd gene-name-fetcher`.
5. Run the command: `pwd` (on macOS) or `cd` (on Windows) and copy the output path. This is going to be the working directory while running this tool.
6. Run the command: `python -m venv ./venv/`.
7. Run the command: `source venv/bin/activate`.
8. Run the command: `pip install -r requirements.txt`. This will start building the python environment and will download some packages. Wait for the command to complete.
9. Close the Terminal or Command Prompt window.

With this your machine is setup to run the tool.

### How to run the tool after the initial setup
1. Copy your input files to the `gene-name-fetcher/input/` directory.
2. Open a Terminal window (on macOS) or Command Prompt (on Windows).
3. Run the command `cd <output-path-saved-in-point-5-above>`.
4. Run the command: `source venv/bin/activate`.
5. Run the command: `python src/runner.py input/<input-file-name>`.
6. Your output will be saved as a `.txt` file in the `gene-name-fetcher/output/` directory.