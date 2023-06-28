import os
import logging
import subprocess

# requires libreoffice to be installed
# use brew install --cask libreoffice

# path to the engine
path_to_office = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

# path with files to convert
# source_folder = "/Users/namtonthat/Library/CloudStorage/GoogleDrive-n.nam.tonthat@gmail.com/My Drive/Hobbies/Mandarin"
SOURCE_FOLDER = os.getcwd()
SOURCE_FOLDER = '/Users/ntonthat/Downloads/HSK3'

def move_files_into_subfolder(file_name, folder_name):
    logging.info('moving file: %s to %s', file_name, folder_name)
    os.makedirs(f"{SOURCE_FOLDER}/{folder_name}", exist_ok=True)
    mv_command = f'mv {file_name} "{SOURCE_FOLDER}/{folder_name}/"'
    subprocess.run(mv_command, shell=True)
    return 


if __name__ == "__main__":
    os.chdir(SOURCE_FOLDER)
    files = os.listdir()
    pptx = [file for file in files if file.endswith(".pptx")]

    for pptx_file in pptx:
        pptx_file = pptx_file.replace(" ", "\ ")
        file_name = pptx_file.split(".pptx")[0]
        
        # assign and running the command of converting files through LibreOffice
        command = f"{path_to_office}  --headless --convert-to pdf --outdir . {pptx_file}"
        # print(command)
        if subprocess.run(command, shell=True): 
            move_files_into_subfolder(f"{file_name}.pdf", "PDF")
            move_files_into_subfolder(f"{file_name}.pptx", "PPTX")

