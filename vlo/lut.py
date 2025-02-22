import datetime
import json
from pathlib import Path

import requests

_PATH = Path("./vlo")
#LUT = json.load((_PATH / "lut.json").open("r", encoding="utf8"))

LUT = {"AGENTS": ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0"], "VLO": {"TEACHERS": {"ID": {"SHORT": {"-9": "Adamska", "-94": "UA", "-96": "An", "-127": "Andryka", "-27": "Bajer", "-102": "Bałucka", "-103": "Bednarek", "-75": "Berkowicz", "-43": "Borcz", "-37": "Boroń", "-64": "Brezdeń", "-86": "Burek", "-106": "Chodacka", "-1": "Chruściel", "-92": "Ciepielowska", "-139": "Czyrnecka", "-42": "Drabczyk", "-10": "Dudek", "-67": "Duraj", "-44": "Dymel", "-77": "Dziedzic", "-101": "Faryna", "-54": "Fryt", "-38": "Garlicki", "-58": "Gełdon", "-76": "Gł", "-138": "Gluszko", "-141": "Gluszko", "-98": "Gorczyca", "-45": "Gunia", "-68": "Gś", "-88": "Herman", "-128": "Jachowicz", "-21": "Rabiega", "-3": "Jantos", "-39": "Jaworski", "-145": "JędrychowskiT", "-70": "Kabłak", "-144": "KaczorN", "-111": "Kamińska", "-11": "Kandyba", "-95": "Kaniecka", "-29": "Kapłon", "-46": "Kaszuba", "-47": "Kielar", "-79": "Kieres", "-129": "Kmiecik", "-87": "Kobos", "-40": "Kobylec", "-116": "Kołdras", "-133": "Kopiec", "-4": "Kos", "-72": "Kosiński", "-108": "Koszałka", "-28": "Kotula", "-48": "Kraszewski", "-59": "Kręgiel", "-55": "Król", "-105": "cV", "-85": "Kulczycki", "-33": "Kurzawińska", "-120": "Mach", "-126": "Malcharek", "-84": "Marcinek", "-140": "Marcińska", "-112": "Maruszczak", "-142": "MS", "-104": "Micygała", "-143": "MyslinskaD", "-49": "Niedźwiedź", "-109": "Niemczyk", "-14": "Olszewska", "-15": "Oniszczuk", "-60": "Zuchmańska", "-6": "Ostachowska-Kos", "-16": "Ostrowska", "-61": "Osuch", "-22": "Pabian", "-34": "Pach", "-7": "Pasieka", "-115": "Pezarski", "-71": "Piekarska", "-114": "Pieniążek", "-52": "Pietras", "-17": "Płaneta", "-56": "Przybylski", "-81": "Ptak-Grzesik", "-32": "Rojewska", "-118": "MS", "-62": "Słowiak", "-125": "Słowikowska", "-83": "Sokołowska", "-35": "Sokólska", "-18": "Sowińska", "-132": "Stańczyk", "-24": "SM", "-130": "Stokłosa", "-73": "Stolarski", "-74": "Studnicki", "-131": "Stypuła", "-136": "Szarek", "-30": "Szewczyk", "-36": "Szklarska", "-137": "SzymlakE", "-91": "PU", "-134": "ZV", "-135": "pV", "-122": "V1", "-123": "AV", "-124": "3V", "-31": "Wadowska", "-25": "Wojtasiewicz", "-121": "Wy", "-20": "Zagórny", "-53": "Zając", "-82": "Zawadzki", "-26": "Zborczyńska"}}}, "SUBJECTS": {"ID": {"SHORT": {"-62": "algorytmika", "-61": "Algorytmika", "-31": "biologia", "-33": "R - biologia", "-32": "Biologia", "-34": "Biol. dla ch", "-28": "chemia", "-30": "R - chemia", "-29": "Chemia", "-77": "C", "-64": "Dor. zawod.", "-44": "EdB", "-47": "etyka", "-75": "Fm", "-71": "filozofia", "-79": "filozofia z", "-27": "S - fizyka", "-72": "Fizyka-UJ", "-24": "fizyka", "-25": "R - fizyka", "-35": "geografia", "-36": "R - geografi", "-45": "Godz. wych", "-46": "godz.wych", "-14": "historia", "-15": "R - historia", "-17": "HiS", "-16": "his", "-39": "informatyka", "-41": "R - informat", "-42": "S - inform.", "-40": "Informatyka", "-13": "j.chiński", "-8": "j.angielski", "-9": "j.francuski", "-11": "j.hiszpański", "-7": "J.niemiecki", "-4": "j.obcy I", "-6": "j. obcy II", "-2": "j.polski", "-3": "R - j. polsk", "-1": "J. polski", "-10": "j.rosyjski", "-12": "j.włoski", "-5": "K - j. obcy ", "-78": "KonA", "-81": "KonF", "-82": "KonH", "-80": "KonN", "-65": "Chiny", "-22": "matematyka", "-23": "R - matematy", "-21": "Matematyka", "-60": "naucz.indyw.", "-54": "biblioteka", "-55": "pedagog", "-56": "psycholog", "-50": "historia szt", "-38": "przedsięb.", "-37": "przyroda", "-49": "religia", "-48": "Religia o", "-67": "rewalidacja", "-74": "szcz. uzdol.", "-76": "UP", "-66": "urlop zdrow.", "-20": "kultura", "-18": "wos", "-19": "R - WoS", "-51": "wych.rodz.", "-43": "wf", "-73": "zaj. wyr.", "-57": "chemia 2c UJ", "-58": "chemia 1c UJ", "-59": "MO", "-63": "chór", "-52": "dyrektor", "-53": "wicedyr. dyd"}, "LONG": {"-62": "algorytmika", "-61": "algorytmika o", "-31": "Biologia", "-33": "Biologia - R", "-32": "Biologia - R o", "-34": "Biologia dla chemików", "-28": "Chemia", "-30": "Chemia - R", "-29": "Chemia - R o", "-77": "Chmura", "-64": "Doradztwo zawodowe", "-44": "Edukacja dla bezpieczeństwa", "-47": "Etyka", "-75": "Fakultet matematyczny", "-71": "Filozofia", "-79": "Filozofia z elementami psychologii", "-27": "Fizyka stosowana", "-72": "Fizyka UJ", "-24": "Fizyka z astronomią", "-25": "Fizyka z astronomią - R", "-35": "Geografia", "-36": "Geografia - R", "-45": "Godzina z wychowawc ą  o", "-46": "Godzina z wychowawcą", "-14": "Historia", "-15": "Historia - R", "-17": "Historia i społeczeństwo", "-16": "Historia i społeczeństwo o", "-39": "Informatyka", "-41": "Informatyka - R", "-42": "Informatyka - S", "-40": "informatyka o", "-13": "j.chiński", "-8": "Język angielski", "-9": "Język francuski", "-11": "Język hiszpański", "-7": "Język niemiecki", "-4": "Język obcy I", "-6": "Język obcy II", "-2": "Język polski", "-3": "Język polski - R", "-1": "Język polski o", "-10": "Język rosyjski", "-12": "Język włoski", "-5": "Konwersatorium", "-78": "Konwersatorium z jęyka angielskiego", "-81": "Konwersatorium z języka francuskiego", "-82": "Konwersatorium z języka hizpańskiego", "-80": "Konwersatorium z języka niemieckiego", "-65": "Kultura Chin", "-22": "Matematyka", "-23": "Matematyka - R", "-21": "Matematyka o", "-60": "Nauczanie indywidualne", "-54": "Obowiązki bibliotekarza", "-55": "Obowiązki pedagoga", "-56": "Obowiązki psychologa", "-50": "Podstawy historii sztuki", "-38": "Podstawy przedsiębiorczości", "-37": "Przyroda", "-49": "Religia", "-48": "Religia o ", "-67": "rewalidacja", "-74": "szcz. uzdolnieni", "-76": "UJ Polski", "-66": "Urlop dla poratowania zdrowia", "-20": "Wiedza o kulturze", "-18": "Wiedza o społeczeństwie", "-19": "Wiedza o społeczeństwie - R", "-51": "Wychowanie do życia w rodzinie", "-43": "Wychowanie fizyczne", "-73": "zaj. wyrównawcze", "-57": "Zajęcia laboratoryjne UJ", "-58": "Zajęcia laboratoryjne UJ 1", "-59": "Zajęcia międzyoddziałowe - chemia", "-63": "Zajęcia pozalekcyjne artystyczne", "-52": "Zniżka - dyrektor", "-53": "Zniżka - wicedyrektor"}}}, "CLASS": {"ROOM": {"ID": {"-78": "PN", "-33": "01", "-34": "02", "-35": "03", "-36": "04", "-1": "1", "-6": "13", "-7": "13A", "-9": "13C", "-10": "14", "-11": "15", "-12": "16", "-13": "17", "-14": "18", "-15": "19", "-2": "2", "-16": "20", "-17": "21", "-18": "22", "-19": "23", "-20": "24", "-21": "25", "-22": "26", "-23": "27", "-24": "28", "-25": "29", "-3": "3", "-26": "31", "-27": "32", "-31": "33", "-28": "35", "-29": "36", "-30": "37", "-4": "5", "-66": "A1", "-75": "A10", "-76": "A11", "-67": "A2", "-68": "A3", "-69": "A4", "-70": "A5", "-71": "A6", "-72": "A7", "-73": "A8", "-74": "A9", "-64": "g_mala", "-32": "aula", "-60": "Biblio", "-59": "CUJ4", "-48": "CUJ 1", "-57": "CUJ2", "-58": "CUJ3", "-42": "dH1", "-43": "DH2", "-44": "DH3", "-63": "DPN", "-65": "g_duza", "-50": "piw_lewa", "-49": "piw_prawa", "-53": "I lewy", "-54": "I prawy", "-55": "II lewy", "-56": "II prawy", "-37": "inf1", "-77": "13B", "-38": "inf2", "-79": "IP", "-61": "mpn", "-51": "par_lewy", "-52": "par_prawy", "-39": "siłownia"}}, "IDR": {"1A": "-45", "1B": "-46", "1C": "-47", "1D": "-48", "1E": "-49", "1F": "-50", "1G": "-51", "1H": "-52", "2A": "-29", "2Ag": "-37", "2B": "-30", "2Bg": "-38", "2C": "-31", "2Cg": "-39", "2D": "-32", "2Dg": "-40", "2E": "-33", "2Eg": "-41", "2F": "-34", "2Fg": "-42", "2G": "-35", "2Gg": "-43", "2H": "-36", "2Hg": "-44", "3A": "-1", "3B": "-2", "3C": "-3", "3D": "-4", "3E": "-5", "3F": "-6", "3G": "-7", "3H": "-8"}, "ID": {"-45": "1A", "-46": "1B", "-47": "1C", "-48": "1D", "-49": "1E", "-50": "1F", "-51": "1G", "-52": "1H", "-29": "2A", "-37": "2Ag", "-30": "2B", "-38": "2Bg", "-31": "2C", "-39": "2Cg", "-32": "2D", "-40": "2Dg", "-33": "2E", "-41": "2Eg", "-34": "2F", "-42": "2Fg", "-35": "2G", "-43": "2Gg", "-36": "2H", "-44": "2Hg", "-1": "3A", "-2": "3B", "-3": "3C", "-4": "3D", "-5": "3E", "-6": "3F", "-7": "3G", "-8": "3H"}}, "TIME": {"DATA": {"0": {"begin": "07:10", "end": "07:55"}, "1": {"begin": "08:00", "end": "08:45"}, "2": {"begin": "09:00", "end": "09:45"}, "3": {"begin": "10:00", "end": "10:45"}, "4": {"begin": "11:00", "end": "11:45"}, "5": {"begin": "12:00", "end": "12:45"}, "6": {"begin": "13:00", "end": "13:45"}, "7": {"begin": "14:00", "end": "14:45"}, "8": {"begin": "14:50", "end": "15:35"}, "9": {"begin": "15:40", "end": "16:25"}, "10": {"begin": "16:30", "end": "17:15"}}, "RMAP": {"0": "07:10", "1": "08:00", "2": "09:00", "3": "10:00", "4": "11:00", "5": "12:00", "6": "13:00", "7": "14:00", "8": "14:50", "9": "15:40", "10": "16:30"}, "MAP": {"07:10": "0", "08:00": "1", "09:00": "2", "10:00": "3", "11:00": "4", "12:00": "5", "13:00": "6", "14:00": "7", "14:50": "8", "15:40": "9", "16:30": "10"}}}}

def FetchLUT():
	today = datetime.datetime.today()
	year = today.year
	last_monday = today + datetime.timedelta(days=-today.weekday(), weeks=0)
	next_friday = last_monday + datetime.timedelta(days=4)

	resp = requests.post(
		url="https://v-lo-krakow.edupage.org/rpr/server/maindbi.js?__func=mainDBIAccessor",
		headers={
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
			"Referer": "https://v-lo-krakow.edupage.org/timetable/"
		},
		json={
			"__args": [
				None,
				2020,
				{
					"vt_filter": {
						"datefrom": last_monday.strftime("%Y-%m-%d"),
						"dateto": next_friday.strftime("%Y-%m-%d")
					}
				},
				{
					"op": "fetch",
					"tables": [],
					"columns":[],
					"needed_part": {
						"teachers": ["__name","short"],
						"classes": ["__name","classroomid"],
						"classrooms":["__name","name","short"],
						"igroups":["__name"],
						"students":["__name","classid"],
						"subjects":["__name","name","short"],
						"events":["typ","name"],
						"event_types":["name"],
						"subst_absents":["date","absent_typeid","groupname"],
						"periods":["__name","period","starttime","endtime"],
						"dayparts":["starttime","endtime"],
						"dates":["tt_num","tt_day"]
					},
					"needed_combos":{},
					"client_filter":{},
					"info_tables":[],
					"info_columns":[],
					"has_columns":{}
				}
			],
			"__gsh":"00000000"
		}
	)

	LUT = {
		"AGENTS": [
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0"
		],
		"VLO": {
			"TEACHERS": {
				"ID": {
					"SHORT": {}
				}
			},
			"SUBJECTS": {
				"ID": {
					"SHORT": {},
					"LONG": {}
				}
			},
			"CLASS": {
				"ROOM": {
					"ID": {}
				},
				"IDR": {},
				"ID": {}
			},
			"TIME": {
				"DATA": {},
				"RMAP": {},
				"MAP": {}
			}
		}
	}

	resp_json = resp.json()["r"]
	for teacher in resp_json["tables"][0]["data_rows"]:
		x,y = teacher.values()
		LUT["VLO"]["TEACHERS"]["ID"]["SHORT"][x] = y

	for subj in resp_json["tables"][1]["data_rows"]:
		x,y,z = subj.values()
		LUT["VLO"]["SUBJECTS"]["ID"]["LONG"][x] = y
		LUT["VLO"]["SUBJECTS"]["ID"]["SHORT"][x] = z

	for clasrm in resp_json["tables"][2]["data_rows"]:
		x,y = clasrm.values()
		LUT["VLO"]["CLASS"]["ROOM"]["ID"][x] = y

	#Classes
	for klass in resp_json["tables"][3]["data_rows"]:
		x,y,_ = klass.values()
		LUT["VLO"]["CLASS"]["ID"][x] = y
		LUT["VLO"]["CLASS"]["IDR"][y] = x

	for time in resp_json["tables"][6]["data_rows"]:
		x,_,_,_,y,z = time.values()
		LUT["VLO"]["TIME"]["DATA"][x] = {"begin":y,"end":z}
		LUT["VLO"]["TIME"]["MAP"][y] = x
		LUT["VLO"]["TIME"]["RMAP"][x] = y

	#with (_PATH / "lut.json").open("w", encoding="utf8") as f:
	#	json.dump(LUT,f,ensure_ascii=False)

FetchLUT()
