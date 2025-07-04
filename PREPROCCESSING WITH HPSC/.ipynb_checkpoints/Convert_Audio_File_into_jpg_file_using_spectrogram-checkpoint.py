import time
import librosa
import librosa.display
import matplotlib.pyplot as plt
from glob import glob
import os
import numpy as np
# create_spectrogram from Audio data file for CNN classification.
def create_spectrogram(filename,name,store_path):
    plt.interactive(False)
    clip, sample_rate = librosa.load(filename, sr=None)
    fig = plt.figure(figsize=[0.72,0.72])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    filename  = store_path + name + '.jpg'
    plt.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()    
    fig.clf()
    plt.close(fig)
    plt.close('all')
    del filename,name,clip,sample_rate,fig,ax,S
    
# convert Audio file in jpg from given folder.
def Convert_Audio_File_to_jpg_file(filename):
    # make dic for given class and their filepath name
    file_list=list(glob(filename + "\\*"))
    file_dic = {}
    for i,file in enumerate(file_list):
        all_files = []
        for root, dirs, files in os.walk(file):
            for file_ in files:
                # Join the root directory with the file name to get the full path
                all_files.append(os.path.join(root, file_))
        file_dic[file] = all_files
        
    # create file directory to store the converted audio file in to jpg
    file_path = []
    for file in file_dic.keys():
        file_rot = r'Convert_Audio_File_to_jpg_file' + '\\' + file + '\\'
        file_path.append(file_rot)
        os.makedirs(file_rot, exist_ok=True)

    # Here each file is converted into jpg file using spectrogram and stored in above created directory.
    for i,folder in enumerate(file_dic.keys()):
        music_files = file_dic[folder]
        for file in music_files:
          create_spectrogram(file,file.split('\\')[-1],file_path[i])  


# Measure the execution time
start_time = time.time()

Convert_Audio_File_to_jpg_file('genres')

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.2f} seconds")