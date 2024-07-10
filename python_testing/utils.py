from pytube import YouTube 
import os
import numpy as np
import ffmpeg
from scipy.io import wavfile
import matplotlib.pyplot as plt

def get_video_url(video_url, download_path):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    download_file = stream.download(output_path=download_path)
    base, ext = os.path.splitext(download_file)
    print(ext)
    new_file = base + '.mp3'
    os.rename(download_file, new_file)
    return new_file

def convert_mp3_to_wav(mp3_file):
    try:
        
        ffmpeg_path = r'D:\\Carlo\\ffmpeg\\ffmpeg.exe'
        os.environ['PATH'] += os.pathsep + os.path.dirname(ffmpeg_path)
        wav_file = mp3_file[:-4] + ".wav"
        ffmpeg.input(mp3_file).output(wav_file).run()
        print(f"Conversion successful: {wav_file}")
        return wav_file
    except ffmpeg.Error as e:
        print("An error occurred:", e)

def read_wav(wav_file):
    samplerate, data = wavfile.read(wav_file)
    return data, samplerate


def plot_sound(name, num_channels, duration, data):
    fig, plots = plt.subplots(num_channels, 1, figsize=(10, 6 * num_channels))
    time = np.linspace(0, duration, num=data.shape[0])
    if num_channels == 1:
        plots.plot(time, data)
        plots.set_title(f'Waveform of {name}')
        plots.set_xlabel('Time [s]')
        plots.set_ylabel('Amplitude')
        plots.grid()
    else:
        for i in range(num_channels):
            plots[i].plot(time, data[:, i])
            plots[i].set_title(f'Waveform of {name} - Channel {i+1}')
            plots[i].set_xlabel('Time [s]')
            plots[i].set_ylabel('Amplitude')
            plots[i].grid()

    plt.tight_layout()
    plt.show()
