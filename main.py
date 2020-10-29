from __future__ import unicode_literals
import youtube_dlc


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
        print(d['filename'])
    if d['status'] == 'downloading':
        print('speed: ', d['speed']/1024, 'kbps')


ydl_opts = {
    'format': 'best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    #  'external_downloader': 'aria2c',
    #  'external_downloader_args': '-x 16',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
    ydl.download([''])
