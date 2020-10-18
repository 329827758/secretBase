import requests,os
from multiprocessing import Pool
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
name='清平乐67'
def download(num):
    video_url = "https://xigua-cdn.haima-zuida.com/20200517/7254_0d51e8e8/1000k/hls/b40a9d6b5c200{:0>4}.ts".format(num)
    if not os.path.exists(name):
        os.mkdir(name)
    if not os.path.exists('./'+name+'/'+ video_url[-8:-3] + '.mp4'):
        res=requests.get(video_url,headers=headers)
        if b"html" not in res.content:
            print('下载'+video_url[-8:])
            with open('./'+name+'/'+video_url[-8:-3]+'.mp4',"wb")as f:
                f.write(res.content)
if __name__ == '__main__':
    pool=Pool(20)
    for num in range(2000):
        pool.apply_async(download,args=(num,))

    pool.close()
    pool.join()

