import requests
import json
class Mobil:
    def __init__(self):
        self.__id=None
        self.__plat = None
        self.__merk = None
        self.__jenis = None
        self.__warna = None
        self.__hargasewa = None
        self.__url = "http://f0835423.xsph.ru/apprental/mobil_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def plat(self):
        return self.__plat
        
    @plat.setter
    def plat(self, value):
        self.__plat = value
    @property
    def merk(self):
        return self.__merk
        
    @merk.setter
    def merk(self, value):
        self.__merk = value
    @property
    def jenis(self):
        return self.__jenis
        
    @jenis.setter
    def jenis(self, value):
        self.__jenis = value
    @property
    def warna(self):
        return self.__warna
        
    @warna.setter
    def warna(self, value):
        self.__warna = value
    @property
    def hargasewa(self):
        return self.__hargasewa
        
    @hargasewa.setter
    def hargasewa(self, value):
        self.__hargasewa = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_plat(self, plat):
        url = self.__url+"?plat="+plat
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__plat = item['plat']
            self.__merk = item['merk']
            self.__jenis = item['jenis']
            self.__warna = item['warna']
            self.__hargasewa = item['hargasewa']
        return data
    def simpan(self):
        payload = {
            "plat":self.__plat,
            "merk":self.__merk,
            "jenis":self.__jenis,
            "warna":self.__warna,
            "hargasewa":self.__hargasewa
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_plat(self, plat):
        url = self.__url+"?plat="+plat
        payload = {
            "plat":self.__plat,
            "merk":self.__merk,
            "jenis":self.__jenis,
            "warna":self.__warna,
            "hargasewa":self.__hargasewa
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_plat(self,plat):
        url = self.__url+"?plat="+plat
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
