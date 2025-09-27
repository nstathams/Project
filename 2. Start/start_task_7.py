def _iban_lengths(file_path):
    iban_lengths = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                country_code = parts[0]
                length = int(parts[1])
                iban_lengths[country_code] = length
    return iban_lengths
file_path = 'iban_lenght.txt'
iban_dict = _iban_lengths(file_path)
print(iban_dict)
