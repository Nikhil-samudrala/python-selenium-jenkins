import random
import string

from faker import Faker


class AddCompanyData:
    ADD_NEW_COMPANY_DETAILS = [
        {'legal_name': 'test autoa3',
         'short_name': 'tae',
         'short_code1': 'ta',
         'short_code2': 'e',
         'cin': 'U67100TG2022PTC164766',
         'gstin': '36AAECM9413G2ZD',
         'line1': 'madhapur',
         'line2': 'hitec city',
         'locality': 'india',
         'pincode': '500081',
         'phone': '9876543216',
         'parent_company': 'Optival',
         'company_logo': '/home/mphs/Downloads/lambo_1_100x63_10.jpg',
         'state': 'TELANGANA',
         'city': 'HYDERABAD',
         },
        {'legal_name': 'test autoa3',
         'short_name': 'tae',
         'short_code1': 'ta',
         'short_code2': 'e',
         'cin': 'U67100TG2022PTC164766',
         'gstin': '36AAECM9413G2ZD',
         'line1': 'madhapur',
         'line2': 'hitec city',
         'locality': 'india',
         'pincode': '500081',
         'phone': '9876543216',
         'parent_company': 'Optival',
         'company_logo': '/home/mphs/Downloads/lambo_1_100x63_10.jpg',
         'state': 'TELANGANA',
         'city': 'HYDERABAD',
         },
    ]

    def __init__(self, count):
        self.ADD_NEW_COMPANY_DETAILS_RANDOM = self.new_company_data_generator(count)

    STATE_CODES = ['AD', 'AR', 'AS', 'BR', 'CG', 'DL', 'GA', 'GJ', 'HR', 'HP',
                   'JK', 'JH', 'KA', 'KL', 'LD', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PB', 'RJ', 'SK',
                   'TN', 'TS', 'TR', 'UP', 'UK', 'WB']
    COMPANY_TYPE = ['PLC', 'PTC', 'FTC', 'FLC', 'GAP', 'GAT', 'GOI', 'NPL', 'OPC', 'SGC', 'ULL', 'ULT']

    LISTING_STATUS = ['L', 'U']

    STATES = ["ANDAMAN AND NICOBAR ISLANDS", "ANDHRA PRADESH", "ARUNACHAL PRADESH", "ASSAM", "BIHAR", "CHANDIGARH",
              "CHHATTISGARH", "DADAR AND NAGAR HAVELI", "DAMAN AND DIU", "DELHI", "GOA", "GUANGDONG", "GUJARAT",
              "HARYANA", "HIMACHAL PRADESH", "JAMMU AND KASHMIR", "JHARKHAND", "JIANGXI", "KARNATAKA", "KERALA",
              "LAKSHADEEP",
              "MADHYA PRADESH", "MAHARASHTRA", "MANIPUR", "MEGHALAYA", "MIZORAM", "NAGALAND", "ODISHA", "PUDUCHERRY",
              "PUNJAB", "RAJASTHAN", "SHARJAH", "SIKKIM", "TAMIL NADU", "TELANGANA", "TRIPURA", "UTTAR PRADESH",
              "UTTARAKHAND", "WEST BENGAL"]
    CITIES = ["ANEKAL", "ANKOLA", "ATTIBELE", "BAGALKOT", "BAGEPALLI", "BAILHONGAL", "BAJPE", "BANGALORE", "BANGARAPET",
              "BANTWAL", "BASAVAKALYAN", "BELGAUM", "BELLARY", "BELTHANGADY", "BHADRAVATJI", "BHALKI", "BHATKAL",
              "BIDADI",
              "BIDAR", "BIJAPUR", "BIRUR", "CHALLAKERE", "CHAMARAJANAGAR", "CHANNAGIRI", "CHANNARAYAPATNA",
              "CHENNAPATNA",
              "CHIKKABALLAPUR", "CHIKKODI", "CHIKMAGALUR", "CHINTAMANI", "CHITAPUR", "CHITRDURGA", "DAKSHINA KANNDA",
              "DANDELI", "DAVANAGERE", "DEVADURGA", "DEVANAHALLI", "DHARUR", "DHARWAD", "DODDABALLAPUR", "GADAG",
              "GANGAVATHI", "GAURIBIDANUR", "GOKAK", "GULBARGA", "GUNDLUPET", "GURMATKAL", "HALIYAL", "HANGAL",
              "HARAPANAHALLI", "HARIHAR", "HAROHALLI", "HASSAN", "HATTI", "HAVERI", "HEGGADADEVANKOTE", "HIREKERUR",
              "HIRIYUR", "HOLALKERE", "HONALLI", "HONNALI", "HOOVINA HADAGALI", "HOSADURGA", "HOSAKOTE", "HOSDURGA",
              "HOSKOTE", "HOSPET", "HUBLI", "HUKKERI", "ILKAL", "INDI", "JAMKHANDI", "KADUR", "KALABURAGI", "KAMPLI",
              "KANAKAPURA", "KARAIKKUDI", "KARATAGI", "KARKALA", "KARWAR", "KAUP", "KIKUDA", "KOLAR",
              "KOLAR GOLD FIELDS",
              "KOLLEGAL", "KOPPAL", "KOPPAL_", "KORATAGERE", "KRISHNARAJPET", "KUNIGAL", "KUSHALNAGAR", "LAKSHMESHWARA",
              "LAXMESHWAR", "LINGASUGUR", "LINGSUGUR", "MADDUR", "MADHUGIRI", "MADIKERI", "MAGADI", "MALUR", "MANDYA",
              "MANGALORE", "MANIPAL", "MANVI", "MOLAKALMURU", "MUDALAGI", "MUDHOL", "MULBAGAL", "MULGUND", "MUNDARGI",
              "MUNDGOD", "MYSORE", "NANJANGUD", "NELMANGALA", "NIPANI", "PANDAVAPURA", "PAVAGADA", "PIRIYAPATNA",
              "PUTTUR_",
              "RABKAVI BANHATTI", "RAICHUR", "RAJANKUNTE", "RAMADURG", "RAMANAGARA", "RAMANAGARAM", "RAMNAGARA",
              "RANEBENNURU", "ROBERTSONPET", "SAGARA", "SHAHABAD", "SHAHAPUR", "SHIGGAON", "SHIKARIPUR", "SHIKARIPURA",
              "SHIMOGA", "SHRIRANGAPATTANA", "SINDAGI", "SINDHANUR", "SIRA", "SIRSI", "SIRUGUPPA", "SRINIVASPUR",
              "SRIRANGAPATNA", "SULLIA", "T NARSIPURA", "TALIKOTA", "TARIKERE", "THIRTHAHALLI", "TIPTUR", "TUMKUR",
              "TURUVEKERE", "UDUPI", "VIJAYAPURA", "VIRAJPET", "YADAGIRI", "YADGIR", "YADGIRI",
              "TELANGANA", "ACHAMPET",
              "ADILABAD", "ARMOOR", "ASIFABAD", "BADEPALLE", "BANSWADA", "BELLAMPALLE", "BHADRACHALAM", "BHAINSA",
              "BHEEMGAL", "BHONGIR", "BHUPALPALLY", "BHUVANAGIRI", "BOATH", "BODHAN", "BOLLARAM", "CHENNUR", "CHEVELLA",
              "CHITYALA", "CHOPPADANDI", "CHOUTUPPAL", "DAMARACHERLA", "DEVARAKONDA", "DEVARKONDA", "ECHODA",
              "FARRUKHNAGAR", "GADWAL", "GAJWEL", "GHANPUR", "GHATKESAR", "GODAVARI KHANI", "HALIYA", "HANAMKONDA",
              "HUZURABAD", "HUZURNAGAR", "HYDERABAD", "IBRAHIMPATNAM", "ICHODA", "IEEJA", "ISNAPUR", "JADCHERLA",
              "JAGTIAL", "JAMMIKUNTA", "JANGAON", "KAGAZNAGAR", "KALWAKURTHY", "KAMAREDDY", "KAREEMNAGAR", "KAZIPET",
              "KHALEELWADI", "KHAMMAM", "KHANAPUR", "KODADA", "KOLLAPUR", "KONDA MALLEPALLY", "KORUTLA", "KOTHAGUDEM",
              "KOTHAKOTA", "KOTHUR", "KOTTAGUDEM", "KYATHAMPALLE", "LUXETTIPET", "MADHIRA", "MAHABUBABAD",
              "MAHBUBNAGAR", "MAHBUBNAGAR", "MAKHTAL", "MANCHERIAL", "MANDAMARRI", "MANTHANI", "MANUGURU", "MEDAK",
              "MEDCHAL", "MEDIPALLY", "METPALLE", "METPALLY", "MIRYALAGUDA", "MIRYALGUDA", "MULUG", "MUSTABAD",
              "NAGARKURNOOL", "NAKREKAL", "NALGONDA", "NAMDEVWADA", "NANDIPET", "NARAYANKHED", "NARAYANPET",
              "NARSAMPET", "NARSAMPETA", "NARSAPUR", "NIRMAL", "NIZAMABAD", "PALAKURTHY", "PALONCHA", "PALWANCHA",
              "PARKAL", "PATANCHERU", "PEDDAPALLE", "PEDDAPALLY", "PERKIT", "POTHIREDDYPALLY", "RAIKAL", "RAMAGUNDAM",
              "RAMAYAMPET", "SADASIVPET", "SANGAREDDY", "SARAPAKA", "SATHUPALLI", "SECUNDERABAD", "SHADNAGAR",
              "SIDDIPET", "SINGAPUR", "SIRCILLA", "SULTANABAD", "SURYAPET", "TANDUR", "THORRUR", "TOOPRAN", "UTNOOR",
              "VANSTHALIPURAM", "VEMULAWADA", "VIKARABAD", "WANAPARTHY", "WARANGAL", "WARDHANNAPET", "WYRA", "YELLANDU",
              "ZAHEERABAD", "ZAHIRABAD"]

    def new_company_data_generator(self, count):
        arr = []
        for i in range(count):
            legal_name_rand = self.generate_legal_name()
            data = {
                'legal_name': legal_name_rand,
                'short_name': legal_name_rand[:len(legal_name_rand) // 2],
                'short_code1': legal_name_rand[:2],
                'short_code2': legal_name_rand[-1],
                'cin': self.generate_random_cin(),
                'gstin': self.generate_random_gstin(),
                'line1': 'madhapur',
                'line2': 'hitec city',
                'locality': 'india',
                'pincode': self.generate_random_pincode(),
                'phone': self.generate_random_mobile_number(),
                'parent_company': 'Optival',
                'company_logo': '/home/mphs/Downloads/lambo_1_100x63_10.jpg',
                'state': self.generate_random_state(),
                'city': self.generate_random_city(),
            }
            arr.append(data)
        return arr + AddCompanyData.ADD_NEW_COMPANY_DETAILS

    def generate_random_state(self):
        return random.choices(AddCompanyData.STATES)[0]

    def generate_random_city(self):
        return random.choices(AddCompanyData.CITIES)[0]

    def generate_legal_name(self):
        fake = Faker()
        name = fake.word() + fake.word()
        return name

    def generate_random_cin(self):
        # pattern = r'\[A-Z]{1}d{5}[A-Z]{2}d{4}[A-Z]{3}d{6}'
        cin = ''
        cin += self.generate_random_value(1, AddCompanyData.LISTING_STATUS)
        cin += str(random.randint(10000, 99999))
        cin += self.generate_random_value(1, AddCompanyData.STATE_CODES)
        cin += str(random.randint(1000, 9999))
        cin += self.generate_random_value(1, AddCompanyData.COMPANY_TYPE)
        cin += str(random.randint(100000, 999999))
        return cin

    def generate_random_gstin(self):
        # pattern = r'\d{2}[A-Z]{5}d{4}[A-Z]{1}d{1}Zd{1}'
        gstin = ''
        gstin += str(random.randint(10, 99))
        gstin += self.generate_random_value(5)
        gstin += str(random.randint(1000, 9999))
        gstin += self.generate_random_value(1)
        gstin += str(random.randint(0, 9))
        gstin += 'Z'
        gstin += str(random.randint(0, 9))
        return gstin

    def generate_random_pincode(self):
        pincode = str(random.randint(100000, 999999))
        return pincode

    def generate_random_mobile_number(self):
        mobile_number = '9' + ''.join(random.choices('0123456789', k=9))
        return mobile_number

    def generate_random_value(self, length, choices=None):
        word = ''
        if choices is None:
            letters = string.ascii_uppercase
            word = ''.join(random.choices(letters, k=length))
        else:
            word = ''.join(random.choices(choices, k=length))
        return word
