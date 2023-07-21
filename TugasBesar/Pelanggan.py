import requests
import json
class Pelanggan:
    def __init__(self):
        self.__id=None
        self.__idpelanggan = None
        self.__nama = None
        self.__jk = None
        self.__alamat = None
        self.__telp = None
        self.__url = "http://f0835423.xsph.ru/apprental/pelanggan_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def idpelanggan(self):
        return self.__idpelanggan
        
    @idpelanggan.setter
    def idpelanggan(self, value):
        self.__idpelanggan = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jk(self):
        return self.__jk
        
    @jk.setter
    def jk(self, value):
        self.__jk = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    @property
    def telp(self):
        return self.__telp
        
    @telp.setter
    def telp(self, value):
        self.__telp = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_idpelanggan(self, idpelanggan):
        url = self.__url+"?idpelanggan="+idpelanggan
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['no']
            self.__idpelanggan = item['idpelanggan']
            self.__nama = item['nama']
            self.__jk = item['jk']
            self.__alamat = item['alamat']
            self.__telp = item['telp']
        return data
    def simpan(self):
        payload = {
            "idpelanggan":self.__idpelanggan,
            "nama":self.__nama,
            "jk":self.__jk,
            "alamat":self.__alamat,
            "telp":self.__telp
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_idpelanggan(self, idpelanggan):
        url = self.__url+"?idpelanggan="+idpelanggan
        payload = {
            "idpelanggan":self.__idpelanggan,
            "nama":self.__nama,
            "jk":self.__jk,
            "alamat":self.__alamat,
            "telp":self.__telp
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_idpelanggan(self,idpelanggan):
        url = self.__url+"?idpelanggan="+idpelanggan
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
