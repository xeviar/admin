


def get_provider_name(provider_id):
    provider_id = str(provider_id)
    if len(provider_id) != 6:
        return provider_id

    result = ""
    first_1 = provider_id[0]
    if first_1 == "3":
        result += "shop_"

    country = provider_id[1:3]
    country_dict = {"01": "SG","02": "MY","03": "TW","04":"PH","05":"VN","06": "CIS","07": "TH","08": "ID","09": "TR","99": "Int"}
    if country in  country_dict.keys():
        result += country_dict[country] + "_"
    else:
        result += "ZZ_"

    product = provider_id[3:6]
    product_dict = {"000":"Shop",
"001":"Poker",
"002":"Pirate",
"003":"M3go",
"004":"Blackshot",
"005":"GoKart",
"006":"HoN",
"007":"LoL",
"008":"GCA",
"009":"TencentPoker",
"010":"The7",
"011":"The_Dice",
"012":"Garena_Plus",
"013":"Mstar",
"014":"LDJ",
"015":"PerfectWorld",
"016":"PerfectWorldEN",
"017":"GPL_Bet",
"018":"PointBlank",
"019":"HoN_Slot_Machine",
"020":"ZhanSanGuo",
"021":"LoL_Slot_Machine",
"022":"DNF",
"023":"TalkTalk",
"024":"FO3"}
    if product in product_dict.keys():
        result += product_dict[product]
    else:
        result += "INVALID_PRDUCT"

    return result
    
