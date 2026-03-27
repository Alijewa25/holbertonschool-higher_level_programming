#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """CSV faylını oxuyur və məlumatları data.json faylına yazır."""
    try:
        # 1. CSV faylını oxumaq üçün açırıq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # 2. DictReader hər sətri lüğətə çevirir
            csv_reader = csv.DictReader(csv_file)
            
            # 3. Oxunan sətirləri siyahı halına salırıq
            data_list = [row for row in csv_reader]
            
        # 4. Siyahını JSON faylına serialize edirik
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
            
        return True

    except FileNotFoundError:
        # Fayl tapılmadıqda False qaytarırıq
        return False
    except Exception:
        # Digər gözlənilməz xətalar zamanı False qaytarırıq
        return False
