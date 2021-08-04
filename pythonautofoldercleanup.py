#Modules needed to use os level functions
import os 
from shutil import move

user = os.getenv('USER')

#Downloads Folder
root_dir = "C:\\Users\\{}\\Downloads".format(user)
#Output Directories
image_dir = "C:\\Users\\{}\\\Downloads\\Images Downloads".format(user)
video_dir = "C:\\Users\\{}\\Downloads\\Video Downloads".format(user)
audio_dir  = "C:\\Users\\{}\\Downloads\\Audio Downloads".format(user)
docs_dir = "C:\\Users\\{}\\Downloads\\Document Downloads".format(user)
software_dir = "C:\\Users\\{}\\Downloads\\Executables Downloads".format(user)
others_dir = "C:\\Users\\{}\\Documents\\Others Directory".format(user)

#File Extensions
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx', '.zip', '.tsv', '.ics', '.apkg', '.ttf')
vid_types = ('.mp4', '.m4v', '.vlc', '.mov', '.avi')
audio_types = ('.mp3', '.wav')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff', '.PNG', '.jfif')
software_types = ('.exe', '.pkg', '.dmg', '.msi')
python_ext = (".py")
folder_ext = (".dir")

def get_non_hidden_files_except_current_file(root_dir):
    return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.endswith(python_ext) and not f.endswith(folder_ext) and not f.__eq__(__file__)]

#Main loop
def move_files(files):
  for file in files:
    # file moved and overwritten if already exists
    if file.endswith(doc_types):
      move(file, '{}/{}'.format(docs_dir, file))
      print('file {} moved to {}'.format(file, docs_dir))
    elif file.endswith(img_types):
      move(file, '{}/{}'.format(image_dir, file))
      print('file {} moved to {}'.format(file, image_dir))
    elif file.endswith(audio_types):
      move(file, '{}/{}'.format(image_dir, file))
      print('file {} moved to {}'.format(file, image_dir))
    elif file.endswith(vid_types):
      move(file, '{}/{}'.format(video_dir, file))
      print('file {} moved to {}'.format(file, video_dir))
    elif file.endswith(software_types):
      move(file, '{}/{}'.format(software_dir, file))
      print('file {} moved to {}'.format(file, software_dir))


if __name__ == "__main__":
    files = get_non_hidden_files_except_current_file(root_dir)
    move_files(files)
