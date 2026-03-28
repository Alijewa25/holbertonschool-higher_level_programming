#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """CSV faylını oxuyur və məlumatları data.json faylına yazır."""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            data_list = [row for row in csv_reader]
            
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
            
        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
