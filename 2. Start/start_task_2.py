def get_resistor_value(test):
        cifri = {
            'bk': 0, 'br': 1, 'rd': 2, 'or': 3, 'yl': 4,
            'gr': 5, 'bl': 6, 'vi': 7, 'gy': 8, 'wh': 9
        }
        mnozh = {
            'bk': 1, 'br': 10, 'rd': 100, 'or': 1000, 'yl': 10000,
            'gr': 100000, 'bl': 1000000, 'vi': 10000000, 'gy': 100000000,
            'wh': 1000000000
        }
        otklon = {
            'bk': None, 'br': 1, 'rd': 2, 'or': None,
            'yl': 5, 'gr': 0.5, 'bl': 0.25, 'vi': 0.1,
            'gy': 0.05, 'wh': None, 'au': 5, 'ag': 10
        }
        if len(test) < 4:
                print(f'Fewer than four colours provided in bands: {test}');
                return None, None;
        if any(test1 not in cifri and test1 not in mnozh and test1 not in otklon for test1 in test):
            print(f'Unidentified or invalid band colour in bands: {test}');
            return None, None;
        first = cifri[test[0]]
        second = cifri[test[1]]
        mnozh = mnozh[test[2]]
        otklon = otklon[test[3]]
        resistance_value = (first * 10 + second) * mnozh
        return resistance_value, otklon
print(get_resistor_value(['br', 'bk', 'yl', 'ag']))
print(get_resistor_value(['yl', 'vi', 'rd', 'au']))
print(get_resistor_value(['vi', 'yl', 'rd', 'gr']))
print(get_resistor_value(['ws', 'yl', 'rd', 'rd']))
print(get_resistor_value(['vi', 'yl', 'rd']))






