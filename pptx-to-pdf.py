import os
import sys
import subprocess

# path to the engine
path_to_office = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

# path with files to convert
source_folder = "/Users/namtonthat/Library/CloudStorage/GoogleDrive-n.nam.tonthat@gmail.com/My Drive/Hobbies/Mandarin"

# changing directory to source
os.chdir(source_folder)

file_name = sys.argv[1]
# file_name = "L15"

# assign and running the command of converting files through LibreOffice
command = f"{path_to_office}  --headless --convert-to pdf --outdir . {file_name}.pptx"
subprocess.run(command, shell=True)

# move files after completed
mv_pdf_command = f"mv {file_name}.pdf \"{source_folder}/Conversational Chinese\""
mv_pptx_command = f"mv {file_name}.pptx \"{source_folder}/Conversational Chinese/\""

subprocess.run(mv_pdf_command, shell=True)
subprocess.run(mv_pptx_command, shell=True)

print('Converted')