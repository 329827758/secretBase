import requests,json,tkinter
from lxml import etree

window=tkinter.Tk()
window.title('淘票票')
window.geometry('1200x300')


def get_page(url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    }
    params={
        "spm": "a1z21.3046609.header.4.32c0112au8mRNx",
        "n_s": "new"
    }
    response=requests.get(url,headers=headers,params=params)
    if response.status_code==200:
        return response.text
    else:
        return None

def parse_page(html):
    response=etree.HTML(html)
    node_list=response.xpath("//div[@class='tab-movie-list']/div")
    for node in node_list:
        try:
            yield {
            "片名":node.xpath(".//a/div[3]/span[1]/text()")[0],
            "导演":node.xpath(".//a/div[4]/div/span[1]/text()")[0],
            "演员":node.xpath(".//a/div[4]/div/span[2]/text()")[0],
            "类型":node.xpath(".//a/div[4]/div/span[3]/text()")[0],
            "地区":node.xpath(".//a/div[4]/div/span[4]/text()")[0],
            "语言":node.xpath(".//a/div[4]/div/span[5]/text()")[0],
            "时长":node.xpath(".//a/div[4]/div/span[6]/text()")[0],
            "上映时间":node.xpath(".//a[2]/text()")[0],
            "url":node_list[0].xpath(".//a/@href")[0],
            }
        except:
            yield {
            "片名":node.xpath(".//a/div[3]/span[1]/text()")[0],
            "导演":node.xpath(".//a/div[4]/div/span[1]/text()")[0],
            "演员":node.xpath(".//a/div[4]/div/span[2]/text()")[0],
            "类型":node.xpath(".//a/div[4]/div/span[3]/text()")[0],
            "地区":node.xpath(".//a/div[4]/div/span[4]/text()")[0],
            "语言":node.xpath(".//a/div[4]/div/span[5]/text()")[0],
            "时长":node.xpath(".//a/div[4]/div/span[6]/text()"),
            "上映时间":node.xpath(".//a[2]/text()")[0],
            "url":node_list[0].xpath(".//a/@href")[0],
            }

def write_to_file(content):
    with open("淘票票.txt",'w',encoding='utf-8') as f:
        for w in content:
            # for i in w:
            #     f.write(i+':'+w[i]+'\n')
            f.write(json.dumps(w,ensure_ascii=False,indent=1)+"\n")
            f.write('\n')
def printtext():
    a.insert("insert",main())

label=tkinter.Label(window,text="请输入影院热映电影")
label.pack()
xls_text =tkinter.StringVar()
xls = tkinter.Entry(window, textvariable = xls_text)
xls_text.set("")
xls.pack()
button=tkinter.Button(window,text='搜索',command=printtext,font=('Arial', 14))
button.pack()
a=tkinter.Text(window,width=150,height=5)
a.pack()



def main():
    condition=xls_text.get()
    url="https://dianying.taobao.com/showList.htm"
    res=get_page(url)
    films=[]
    dicts=parse_page(res)
    for film in dicts:
        if film["片名"]==condition:
            return film
    # write=input('是否写入文件？')
    # if write:
    #     write_to_file(films)

#按钮

#输入

#输出





window.mainloop()