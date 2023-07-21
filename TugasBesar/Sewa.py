import requests
import json
class Sewa:
    def __init__(self):
        self.__id=None
        self.__idsewa = None
        self.__idpelanggan = None
        self.__plat = None
        self.__tglsewa = None
        self.__waktu = None
        self.__tglkembali = None
        self.__hargasewa = None
        self.__totalbiaya = None
        self.__url = "http://f0835423.xsph.ru/apprental/sewa_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def idsewa(self):
        return self.__idsewa
        
    @idsewa.setter
    def idsewa(self, value):
        self.__idsewa = value
    @property
    def idpelanggan(self):
        return self.__idpelanggan
        
    @idpelanggan.setter
    def idpelanggan(self, value):
        self.__idpelanggan = value
    @property
    def plat(self):
        return self.__plat
        
    @plat.setter
    def plat(self, value):
        self.__plat = value
    @property
    def tglsewa(self):
        return self.__tglsewa
        
    @tglsewa.setter
    def tglsewa(self, value):
        self.__tglsewa = value
    @property
    def waktu(self):
        return self.__waktu
        
    @waktu.setter
    def waktu(self, value):
        self.__waktu = value
    @property
    def tglkembali(self):
        return self.__tglkembali
        
    @tglkembali.setter
    def tglkembali(self, value):
        self.__tglkembali = value
    @property
    def hargasewa(self):
        return self.__hargasewa
        
    @hargasewa.setter
    def hargasewa(self, value):
        self.__hargasewa = value
    @property
    def totalbiaya(self):
        return self.__totalbiaya
        
    @totalbiaya.setter
    def totalbiaya(self, value):
        self.__totalbiaya = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_idsewa(self, idsewa):
        url = self.__url+"?idsewa="+idsewa
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['no']
            self.__idsewa = item['idsewa']
            self.__idpelanggan = item['idpelanggan']
            self.__plat = item['plat']
            self.__tglsewa = item['tglsewa']
            self.__waktu = item['waktu']
            self.__tglkembali = item['tglkembali']
            self.__hargasewa = item['hargasewa']
            self.__totalbiaya = item['totalbiaya']
        return data
    def simpan(self):
        payload = {
            "idsewa":self.__idsewa,
            "idpelanggan":self.__idpelanggan,
            "plat":self.__plat,
            "tglsewa":self.__tglsewa,
            "waktu":self.__waktu,
            "tglkembali":self.__tglkembali,
            "hargasewa":self.__hargasewa,
            "totalbiaya":self.__totalbiaya
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_idsewa(self, idsewa):
        url = self.__url+"?idsewa="+idsewa
        payload = {
            "idsewa":self.__idsewa,
            "idpelanggan":self.__idpelanggan,
            "plat":self.__plat,
            "tglsewa":self.__tglsewa,
            "waktu":self.__waktu,
            "tglkembali":self.__tglkembali,
            "hargasewa":self.__hargasewa,
            "totalbiaya":self.__totalbiaya
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_idsewa(self,idsewa):
        url = self.__url+"?idsewa="+idsewa
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
