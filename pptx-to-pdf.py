import os

# import sys
import subprocess

# requires libreoffice to be installed
# use brew install --cask libreoffice

# path to the engine
path_to_office = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

# path with files to convert
source_folder = "/Users/namtonthat/Library/CloudStorage/GoogleDrive-n.nam.tonthat@gmail.com/My Drive/Hobbies/Mandarin"
# SOURCE_FOLDER = "/Users/ntonthat/Downloads/HSK3\ 1-10/"
SOURCE_FOLDER = os.getcwd()
OUTPUT_FOLDER = "HSK3"

# changing directory to source
# os.chdir(source_folder)

# file_name = sys.argv[1]
# file_name = "L15"
files = os.listdir()
pptx = [file for file in files if file.endswith(".pptx")]

for pptx_file in pptx:
    file_name = pptx_file.split(".pptx")[0]
    file_name = file_name.replace(" ", "\ ")
    # print(file_name)
    # assign and running the command of converting files through LibreOffice
    command = f"{path_to_office}  --headless --convert-to pdf --outdir . {file_name}"
    subprocess.run(command, shell=True)

    # move files after completed
    # command to create folder if not exist
    # os.makedirs(f"{source_folder}/PDF", exist_ok=True)
    # mv_pdf_command = f'mv {file_name}.pdf "{source_folder}/PDF/"'
    # subprocess.run(mv_pdf_command, shell=True)

    # os.makedirs(f"{source_folder}/PPTX", exist_ok=True)
    # mv_pptx_command = f'mv {file_name}.pptx "{source_folder}/PPTX/"'
    # subprocess.run(mv_pptx_command, shell=True)

    print("Converted")
