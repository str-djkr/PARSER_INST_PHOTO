import os
import fnmatch
import instaloader
from datetime import datetime
from itertools import dropwhile, takewhile


class download_post():
    def __init__(self) -> None:
        self.L = instaloader.Instaloader()

    def download__posts(self,username):
        posts = instaloader.Profile.from_username(self.L.context, username).get_posts()
        SINCE = datetime(2011, 8, 28)               #період
        UNTIL = datetime(2022, 11, 7)

        for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
            self.L.download_post(post, username)


class data_ac(download_post):
    def working(self,ms):
        wrk = download_post()
        for i in range(len(ms)):
            try:
                wrk.download__posts(ms[i])
            except:
                pass


    def read_date(self):
        inf = open('File.txt')
        ms = []
        for line in inf:
            line =line.replace(line[-1],'')
            ms.append(str(line))
        print(ms)
        return ms
        

    def clear_directory(self,ms):
        for i in ms:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{i}\\')
            for file in os.listdir(path):
                if not file.endswith(".jpg"):
                    if not file.endswith(".mp4"):
                        os.remove(path + file)
            

if __name__=="__main__":
    cls = download_post()
    cls1 = data_ac()
    ms = cls1.read_date()
    cls1.working(ms)
    cls1.clear_directory(ms)
