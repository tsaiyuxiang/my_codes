# watch.py
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0?si=cr_ztYUiqwUDqZFm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # 使用 re 表達式找出 src 屬性
    # <iframe    匹配字串 <iframe 的開頭
    # [^>]*      是「不是 > 的任一字元」， *  表示「0 個以上」，也就是「匹配任意長度、直到 > 為止的字元」
    # src="      找 src=" 開頭
    # ([^"]+)   「捕捉群組」的意思, 這會抓取一串不是 " 的字元（直到下1個 "），也就是網址本身,
    #            最後 + 表示至少1個字元
    # "          結尾的引號，也會被配對但不會放進 group
    match = re.search(r'<iframe[^>]*src="([^"]+)"', s)

    if match:  # 上方有匹配到, match 不是 None 才能進去

        # match.group(0)	整個匹配到的字串
        # match.group(1)	第一個捕捉群組 (第一對括號 (...)) 中的內容
        # match.group(2)	第二個捕捉群組中的內容（如果有的話）
        url = match.group(1)

        # 檢查是不是 YouTube 嵌入連結
        if "youtube.com/embed/" in url:
            video_id = url.split("/embed/")[-1].split("?")[0]
            return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()

'''
def parse(s):
    s = s.strip()
    len1 = len(s)
    url_found = False
    if len1 > 17:
        if (s[:7] == "<iframe") and (s[-9:] == "</iframe>"):
            if 'src="' in s:
                s = s[s.find('src="')+5:]
                if '"' in s:
                    s = s[0:s.find('"')]  # s = url
                    url_found = True
    if not url_found:
        return None
    if r"https://www.youtube.com/embed/" in s:
        s = re.sub(r"https://www.youtube.com/embed/",r"https://youtu.be/",s)
    elif  r"http://www.youtube.com/embed/" in s:
        s = re.sub(r"http://www.youtube.com/embed/",r"https://youtu.be/",s)
    if "?" in s:
        s = s[0:s.find("?")]
    return s

if __name__ == "__main__":
    main()
'''

