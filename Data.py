import requests
import json
import requests


class basic():
    def __init__(self):
        self.url = 'https://www.topuniversities.com/rankings/endpoint'
        self.headers = {
            'authority': 'www.topuniversities.com',
            'accept': '*/*',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'STYXKEY_first_visit=yes; __gads=ID=34389584587a7f8a:T=1671455533:S=ALNI_MayyuzrSPebL9k2HURG0FWL2OeL2g; _tt_enable_cookie=1; _ttp=F1aJYr1vHdbjxpqYQCDEMot8OVy; _mkto_trk=id:335-VIN-535&token:_mch-topuniversities.com-1671455534239-27009; sa-user-id=s%253A0-b9679505-f143-4905-4062-703f7f2ea9cb.oGVcL%252F4%252F9SzOe5rjKkw0vdX1wj0DxGOFx%252FIY6l9woAI; sa-user-id-v2=s%253AuWeVBfFDSQVAYnA_fy6py8GMwhA.4Dl2Pg68Goex8iDywa%252B4FDfWqYsy1agx55tBeYMEe8o; hubspotutk=2f6413c39634a579d828e3bdc0b4f1c4; messagesUtk=6b8042711acd47e299c46653b2d94d28; _hjSessionUser_173635=eyJpZCI6IjMxZTZjOTU5LWMxOWYtNTNjZi04NWE3LTNiOWM4OTM2MWM2NiIsImNyZWF0ZWQiOjE2NzE0NTU1MzM0NjIsImV4aXN0aW5nIjp0cnVlfQ==; __gpi=UID=00000b94bd6c89ea:T=1671455533:RT=1683730643:S=ALNI_MbuR3puLZg4IddnY7Yozo_ZmWZa6w; STYXKEY-globaluserUUID=TU-1683730644156-59714474; _gid=GA1.2.1938834057.1683730644; _gcl_au=1.1.1564738234.1683730644; _fbp=fb.1.1683730644703.1488171613; _clck=mmmz69|1|fbh|0; __hssrc=1; cookie-agreed-version=1.0.0; cookie-agreed=2; _parsely_session={%22sid%22:6%2C%22surl%22:%22https://www.topuniversities.com/university-rankings/university-subject-rankings/2023/arts-humanities%22%2C%22sref%22:%22https://www.topuniversities.com/subject-rankings/2023%22%2C%22sts%22:1683748985783%2C%22slts%22:1683742689497}; _parsely_visitor={%22id%22:%22pid=e9acca9e57733538ceaf6742eebba261%22%2C%22session_count%22:6%2C%22last_session_ts%22:1683748985783}; _hjSession_173635=eyJpZCI6Ijk3Y2E0M2YyLTM5MDctNGVkNS1iNWQzLTg2NThhODVjZmVkYiIsImNyZWF0ZWQiOjE2ODM3NDg5ODkxODksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __hstc=238059679.2f6413c39634a579d828e3bdc0b4f1c4.1671455535251.1683743215048.1683748993464.7; _vwo_uuid_v2=D380105E5FB602538FC4BC65D12845261|3e5266a8ae8bdfef752a28e6bf041681; __hssc=238059679.3.1683748993464; _ga=GA1.2.1017728944.1671455531; _gat_UA-37767707-2=1; _clsk=10krv8s|1683750407023|10|1|w.clarity.ms/collect; _ga_16LPMES2GR=GS1.1.1683748985.7.1.1683750420.0.0.0; _ga_YN0B3DGTTZ=GS1.1.1683748985.7.1.1683750420.44.0.0; _gat_%5Bobject%20Object%5D=1',
            'if-none-match': 'W/"1683750406"',
            'referer': 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2023/arts-humanities?&page=1&tab=indicators&sort_by=rank&order_by=asc',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            }
        self.params = {
            'nid': '3846211',
            'page': '1',
            'items_per_page': '15',
            'tab': 'indicators',
            'region': '',
            'countries': '',
            'cities': '',
            'search': '',
            'star': '',
            'sort_by': 'rank',
            'order_by': 'asc',
        }
    def get_json(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            print("Error: ", response.status_code)
            return None
        return response.json()

class University():
    def __init__(self,name,country):
        self.__name = name
        self.country = country
        self.ranking = None
class Country():
    def __init__(self,name,total=0):
        self.__name = name
        self.universities = []
        self.total = total
        self.avg = 0
    def addUniversity(self,University):
        self.universities.append(University)
        self.total += University.ranking
        self.avg = self.total / len(self.universities)
