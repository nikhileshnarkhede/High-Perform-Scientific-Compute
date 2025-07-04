import os
from glob import glob
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import ipyparallel as ipp
import time
from warnings import filterwarnings
filterwarnings('ignore')

# %%

# Function to create a spectrogram from an audio file (unchanged)
def create_spectrogram(filename, name, store_path):
    plt.interactive(False)
    clip, sample_rate = librosa.load(filename, sr=None)
    fig = plt.figure(figsize=[0.72, 0.72])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    filename = os.path.join(store_path, name + '.jpg')
    plt.savefig(filename, dpi=400, bbox_inches='tight', pad_inches=0)
    plt.close()
    fig.clf()
    plt.close(fig)
    plt.close('all')
    del filename, name, clip, sample_rate, fig, ax, S


# Helper function to process a single audio file
def process_audio_file(file, folder_path):
    name = os.path.basename(file)
    create_spectrogram(file, name, folder_path)


# Convert Audio files to spectrogram JPG files with ipyparallel
def Convert_Audio_File_to_jpg_file(filename, number_of_worker):
    """
    Convert audio files to spectrogram JPG files using ipyparallel.

    Parameters:
        filename (str): Path to the main directory containing audio files.
    """
    # Set up ipyparallel cluster
    rc = ipp.Cluster(n=number_of_worker).start_and_connect_sync()  # Start and connect cluster with 4 workers
    dview = rc[:]  # Create a direct view to all workers

    dview.push({"create_spectrogram": create_spectrogram})
    dview.push({"process_audio_file": process_audio_file})
    dview.execute("import os")
    dview.execute("import librosa")
    dview.execute("import librosa.display")
    dview.execute("import numpy as np")
    dview.execute("import matplotlib.pyplot as plt")
    dview.execute("import time")

    start_time = time.time()
    # Make a dictionary for given class and their file path names
    file_list = glob(os.path.join(filename, "*"))
    file_dic = {}
    for file in file_list:
        all_files = []
        for root, dirs, files in os.walk(file):
            for file_ in files:
                # Join the root directory with the file name to get the full path
                all_files.append(os.path.join(root, file_))
        file_dic[file] = all_files

    # Create file directories to store the converted audio files into JPG
    file_path = []
    for folder in file_dic.keys():
        folder_rot = os.path.join('Convert_Audio_File_to_jpg_file', os.path.basename(folder))
        file_path.append(folder_rot)
        os.makedirs(folder_rot, exist_ok=True)

    # Delegate work to workers using dview.map_sync()
    for i, folder in enumerate(file_dic.keys()):
        music_files = file_dic[folder]
        folder_path = file_path[i]
        # Map the processing function across music files with ipyparallel
        dview.map_sync(lambda file: process_audio_file(file, folder_path), music_files)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Execution time: {elapsed_time:.2f} seconds")
    # Shut down the cluster after processing
    rc.shutdown()


Convert_Audio_File_to_jpg_file("genres",number_of_worker = 4)