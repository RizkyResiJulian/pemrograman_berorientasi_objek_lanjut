dictionary = {"satu": "ketuhanan yang maha esa", "dua": "kemanusiaan yang adil dan beradab", "tiga": "persatuan indonesia"}
try:
    value = dictionary["empat"]
except KeyError:
    print("kata kunci yang diminta tidak ditemukan pada dictionary!")
