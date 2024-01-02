# name:自动获取cookie（educoder）
# 作者：venti
# version：1.1.1
#！！！！！！！！！！！！！！！！！！！
#此函数只支持手机号和邮箱号登录
#！！！！！！！！！！！！！！！！！！！
import urllib.error, urllib.request, urllib.parse
import http.cookiejar
import getpass

def get_cookie():#login：登录手机号，password：登录密码（首次获取cookie用此函数）
    pwCorrect = False
    while not pwCorrect:
        login=input("请输入您的手机号/邮箱号：")#输入账号名
        password=getpass.getpass("请输入您的密码(密码内容不显示)：")#输入密码(不可见)
        print("正在登录...")
        headers = {#请求头，主要是浏览器标识
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",#pc/chrome浏览器标识
        }
        url="https://data.educoder.net/api/accounts/login.json"#cookie所在网址
        values={#用户登录数据
            "login": login,
            "password": password,
            "autologin": "true",
        }
        User_data= urllib.parse.urlencode(values).encode()#封装登陆数据
        # 将cookie保存在本地，并命名为cookie.txt
        cookie_filename = 'cookie.txt'
        cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
        handler = urllib.request.HTTPCookieProcessor(cookie_aff)
        opener = urllib.request.build_opener(handler)
        #发起登录请求
        request = urllib.request.Request(url, data=User_data, headers=headers)
        try:#捕获urlError
            response = opener.open(request)
        except urllib.error.URLError as e:
            print(e.reason)
        cookie_aff.save(ignore_discard=True, ignore_expires=True)#保存cookie到文件
        for item in cookie_aff:#检查cookie是否正常获取
            pwCorrect = True
            # print("cookie已保存到本地")
            print("\n登录成功")
            return
        else:print("帐号或密码错误或网络出现问题，请重新输入")

def login_in_cookie():#上面代码中我们保存cookie到本地了，以下代码我们能够直接从文件导入cookie进行登录
    get_url="https://data.educoder.net/api/accounts/login.json"
    cookie_filename = 'cookie.txt'#从文件获取cookie
    cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
    cookie_aff.load(cookie_filename, ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie_aff)
    opener = urllib.request.build_opener(handler)
    # 使用cookie登陆get_url
    get_request = urllib.request.Request(get_url)
    try:#检查获取cookie是否正确
        get_response = opener.open(get_request)
        print(get_response.read().decode())
    except urllib.error.HTTPError :
        print("login  failed")


#以下为测试代码
if __name__=="__main__":
    get_cookie()
    login_in_cookie()