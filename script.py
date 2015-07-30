import youtube_dl
import sys
import os

class YoutubeDownloader(object):
    def __init__(self, youtube_link):
        self.youtube_link = youtube_link
        self.extractors()
        self.get_youtube_link_and_process()

    def extractors(self):
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        ydl.add_default_info_extractors()
        self.result = ydl.extract_info('%s'%self.youtube_link, download=False)

    def get_youtube_link_and_process(self):        
        if 'entries' in self.result:
            video = self.result['entries'][0]
        else:
            video = self.result
        video_name = str(video['title'])
        formats = self.result['formats']
        self.video_name = video_name
        return video_name, formats

    def make_directories(self):
        directory = os.getcwd() + "/K-Youtube-Downloader/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def processing(self, format_id, resolution, extension):
        directory = self.make_directories()
        filename = directory + self.video_name + "." + extension
        os.system("wget -O \"%s\" $(youtube-dl -g -f %s %s)" % (filename, str(format_id), self.youtube_link))
