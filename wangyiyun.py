import requests
from lxml import etree
import os,time

headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400",
         "referer":"https://music.163.com/",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
         "Host": "music.163.com"}

faverite_singer=input('https://music.163.com/#/discover/artist\n输入歌手名（只能查首页的歌手）：')

def name_id():
    singer_url="https://music.163.com/weapi/artist/top?csrf_token="
    data={
    "params": "dKUMg7sJLYzlEG5ZKdFcr47e5dgd6zTkORsDbjF0BEHx4kjA//WRED7bnTvNC0UIlwlCib4XhWQU3CVe2xi1z+Wtj2mq1da6ADBciMm3q6+M4js1OU1REBG8DqwYUX03",
    "encSecKey": "de1f26cb7bdaed1ab7d3f87cb9a92e5603683e4974c5702f8f2c5e6e263fcee7d92c4030ac57715ab1cc4fb1b1d2a4e5b967b23ecf34769b662cab8d7f283cd47244cfc506356045739ae3953bafac0e4038df40fa4ee916a9129c0da0bb44f32c78eecc8d9db4b9a54a279862c9e0b26a956f37e70485190cdd0807c6a1e029"
    }
    singer=requests.post(singer_url,data=data)
    singer=singer.json()
    singer_info=singer['artists']
    id_list={}
    for a in singer_info:
        # print(a)
        id_list[a['name']]=a['id']
    if faverite_singer in id_list:
        id=id_list[faverite_singer]
    # print(singer_list)
        return id
    else:
        id=input('如果没有，自行查找id：')
        return id

def sings():
    ss_url='https://music.163.com/artist'
    params = {"id": name_id()}
    session=requests.session()
    session.headers.update(headers)
    response=session.get(ss_url,params=params)
    html=etree.HTML(response.text)
    song_list={}
    # print(response.text)
    songname_list=html.xpath("//ul[@class='f-hide']/li/a/text()")
    songurl_list=html.xpath("//ul[@class='f-hide']/li/a/@href")
    # print(song_list)
    for a in range(len(songname_list)):
        song_list[songname_list[a]]=("http://music.163.com/song/media/outer/url"+songurl_list[a][5:]+".mp3")
    # for song in song_list:
        # print(song,song_list[song])
    return song_list


def down_load():
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400",}
    song_list=sings()
    print(song_list.keys())
    while True:
        down_song=input('复制要下载的歌曲名或者按回车全部下载：')
        if  not down_song:
            for song in song_list:
                if not os.path.exists(faverite_singer):
                    os.mkdir(faverite_singer)
                # print(a.content)
                try:
                    if not os.path.exists(faverite_singer+'/'+song+'.mp3'):
                        # print(song_list[song])
                        a = requests.get(song_list[song],headers=header)
                        time.sleep(1)
                        with open(faverite_singer+'/'+song+'.mp3','wb') as f:
                            print('下载：'+song)
                            f.write(a.content)
                            print(song+'下载完成')
                    else:
                        print(song+'已存在')
                except Exception as e:
                    print(song + '下载失败')
        else:
            for song in song_list:
                if not os.path.exists(faverite_singer):
                    os.mkdir(faverite_singer)
                # print(a.content)
                if song==down_song:
                    try:
                        if not os.path.exists(faverite_singer+'/'+song+'.mp3'):
                            # print(song_list[song])
                            a = requests.get(song_list[song],headers=header)
                            time.sleep(1)
                            with open(faverite_singer+'/'+song+'.mp3','wb') as f:
                                print('下载：'+song)
                                f.write(a.content)
                                print(song+'下载完成')
                        else:
                            print(song+'已存在')
                    except Exception as e:
                        print(song + '下载失败')

# sings()
down_load()
# name_id()

# """
# <ul class="f-hide">
#     <li>
#         <a href="/song?id=1367452194">我的一个道姑朋友</a>
#     </li>
#     <li>
#         <a href="/song?id=478303470">心做し（Cover GUMI）</a>
#     </li>
#   /song?id=1433786440
#   https://music.163.com/#/song?id=1367452194
# 'http://music.163.com/song/media/outer/url?id=1405283464.mp3'
#     <li><a href="/song?id=409650851">霜雪千年（Cover 洛天依 / 乐正绫）</a></li><li><a href="/song?id=534540498">藏</a></li><li><a href="/song?id=409654891">故梦（Cover 橙翼）</a></li><li><a href="/song?id=504974392">女孩你为何踮脚尖</a></li><li><a href="/song?id=409649830">九九八十一（翻自 乐正绫 / 洛天依） </a></li><li><a href="/song?id=36895537">采茶纪</a></li><li><a href="/song?id=429460399">世末歌者（Cover 乐正绫）</a></li><li><a href="/song?id=499299379">谓风</a></li><li><a href="/song?id=531040898">马步谣</a></li><li><a href="/song?id=436668683">【3D】We Don't Talk Anymore</a></li><li><a href="/song?id=36117196">月出</a></li><li><a href="/song?id=539603870">风缘</a></li><li><a href="/song?id=1296550461">上里与手抄卷</a></li><li><a href="/song?id=416385506">大鱼  （Cover 周深）</a></li><li><a href="/song?id=1345820742">单向箭头</a></li><li><a href="/song?id=409649817">琴师（Cover 音频怪物）</a></li><li><a href="/song?id=430053202">四重罪孽</a></li><li><a href="/song?id=1302601503">【bilibili音乐】一话一世界 《一花依世界》方言合唱版</a></li><li><a href="/song?id=461687747">不朽之罪</a></li><li><a href="/song?id=1344200119">【33只】2019～予你成歌～</a></li><li><a href="/song?id=1424969678">终于</a></li><li><a href="/song?id=459412983">问剑江湖</a></li><li><a href="/song?id=484692395">千梦（Cover HITA / Aki阿杰）</a></li><li><a href="/song?id=516997458">白石溪（Cover 洛天依 / 乐正绫）</a></li><li><a href="/song?id=1344088470">时光卷轴</a></li><li><a href="/song?id=409650841">小幸运（Cover 田馥甄）</a></li><li><a href="/song?id=1418352641">【26只】2020～此间未来～</a></li><li><a href="/song?id=499274374">纯白</a></li><li><a href="/song?id=481697663">达拉崩吧（Cover 洛天依 / 言和）</a></li><li><a href="/song?id=1316479227">【星火行动】朝汐（泠鸢&双笙）</a></li><li><a href="/song?id=526680601">那一天从梦中醒来</a></li><li><a href="/song?id=409649919">桃花笑（Cover 洛天依+言和+乐正绫）</a></li><li><a href="/song?id=468469640">棠梨煎雪（Cover 银临）</a></li><li><a href="/song?id=409649822">腐草为萤（Cover 银临）</a></li><li><a href="/song?id=515481072">扬州姑娘</a></li><li><a href="/song?id=460075883">万神纪（Cover 星尘 / 肥皂菌|海鲜面）</a></li><li><a href="/song?id=409649811">竹枝词</a></li><li><a href="/song?id=1344200357">2019～予你成歌～</a></li><li><a href="/song?id=409649814">小棋童 （Cover 不纯君）</a></li><li><a href="/song?id=453003622">外婆桥（Cover 初音ミク）</a></li><li><a href="/song?id=538632915">【34只】2018～朝你靠近～</a></li><li><a href="/song?id=1347007305">生而为匠</a></li><li><a href="/song?id=475072040">倩音流年</a></li><li><a href="/song?id=409649818">牵丝戏【合唱】（Cover 银临 / Aki阿杰）</a></li><li><a href="/song?id=416890449">栖枝</a></li><li><a href="/song?id=410042102">孤竹遗梦</a></li><li><a href="/song?id=1436207678">失春</a></li><li><a href="/song?id=440353134">巷（Cover 洛天依）</a></li></ul>
# """

# d8c63c433375c5334b1eb7f135b934e71d64bc5c097ac9f7fe1a8a3ffa8ad49c77b9f3bbf851e99911aee09fedea5050c50e59c55db3ed58b891e3ba403bbced34c85cf4ec5447d701c7606686782d40d5b99ca3ddc69ae32081fdd4fe9896e751dac41ca6681d8d388eccbdb66456df2010d0e1972252d691ab1aa1ab3febde
# 2fe26e6a1e76e7e03bb84221e11ac27611fc7da1bcd461eab561d162a721cb4b41fd30a019061522328310efe6576aa6dcbebecfdf553877c0301adebc71569f40c3bd080c41aa54812ea13a8b2dfebd93c3122b8c6e4d655a41048f6d53fe22737c454049ac18bd3627f5a2882b04e8262193fcbcc13e68442e80f57db9dd81

