"""
This script converts PowerPoint (.pptx) files in a specified directory to PDF format using LibreOffice.
After converting, the script moves the PDF files to a 'PDF' subdirectory and the original PPTX files to a 'PPTX' subdirectory within the source folder.
Requires LibreOffice to be installed on the system.
brew install --cask libreoffice
"""

import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Path to the LibreOffice engine
path_to_office = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

# Source folder with files to convert
source_folder = "/Users/namtonthat/Library/CloudStorage/GoogleDrive-n.nam.tonthat@gmail.com/My Drive/Hobbies/Mandarin"

# Get the current working directory
source_folder = os.getcwd()

# Create output folder if it does not exist
os.makedirs(os.path.join(source_folder, "PDF"), exist_ok=True)
os.makedirs(os.path.join(source_folder, "PPTX"), exist_ok=True)

# Get a list of all .pptx files in the source folder
pptx_files = [file for file in os.listdir(source_folder) if file.endswith(".pptx")]

for pptx_file in pptx_files:
    pttx_file = pptx_file.replace(" ", "\ ")
    file_name = os.path.splitext(pptx_file)[0]

    # Convert PPTX to PDF using LibreOffice
    command = f"{path_to_office} --headless --convert-to pdf --outdir {source_folder} {os.path.join(source_folder, pptx_file)}"
    subprocess.run(command, shell=True)
    logging.info(f"Converted {pptx_file} to PDF")

    # Move the PDF and PPTX files to their respective folders
    mv_pdf_command = f'mv {file_name}.pdf "{source_folder}/PDF/"'
    subprocess.run(mv_pdf_command, shell=True)

    mv_pptx_command = f'mv {file_name}.pptx "{source_folder}/PPTX/"'
    subprocess.run(mv_pptx_command, shell=True)

    logging.info(f"Moved {file_name}.pdf and {pptx_file} to respective folders")
