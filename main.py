from requests import post

def _xor(string):
    return "".join([hex(ord(c) ^ 5)[2:] for c in string])

def login(email, password):
    try:
        url = f'https://api22-normal-c-alisg.tiktokv.com/passport/user/login/?aid=1164'
        payload = f'password={_xor(password)}&account_sdk_source=app&email={_xor(email)}&mix_mode=1&multi_login=1'

        headers = {'user-agent': 'com.ss.android.tt.creator/320906 (Linux; U; Android 7.1.2; de_DE; G011A; Build/N2G48H;tt-ok/3.12.13.4-tiktok)'}
        res = post(url, headers=headers, data=payload).json()
        print(res)
    except:
        pass

login('kaylacarter84@gmail.com', 'kc386206')
