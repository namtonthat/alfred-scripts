import os
import sys
import subprocess

# path to the engine
path_to_office = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

# path with files to convert
source_folder = "/Users/namtonthat/Library/CloudStorage/GoogleDrive-n.nam.tonthat@gmail.com/My Drive/Hobbies/Mandarin"

# changing directory to source
os.chdir(source_folder)

file_name = "{query}"
print(file_name)
# assign and running the command of converting files through LibreOffice
# command = f"{path_to_office}   --headless --convert-to pdf --outdir . {file_name}.pptx"
# subprocess.run(command)

# move files after completed
# mv_command = f"mv {file_name} {source_folder}/Conversational\ Chinese/"

print('Converted')