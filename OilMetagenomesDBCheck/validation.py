import csv
import json
import pandas as pd
import numpy as np
import logging


def id_validity(json_file, flag):
    # Open and read the JSON file
    with open(json_file, "r") as jsonfile:
        # Load the JSON data as a dictionary object
        data = json.loads(jsonfile.read())

    # Create a set of all values in the "archive_accession" column
    if flag == "sample":
        id_flag = "archive_accession"
    else:
        id_flag = "archive_data_accession"

    all_accessions = set()
    accession_dict = {}
    for index, item in enumerate(data):
        archive_accession = item[id_flag]
        if archive_accession:
            accession_list = [
                value.strip() for value in archive_accession.split(",") if value.strip()
            ]
            for accession in accession_list:
                if accession in all_accessions:
                    print(
                        f"Duplicate value {accession} found in rows {accession_dict[accession]+2} and {index+2}"
                    )
                else:
                    all_accessions.add(accession)
                    accession_dict[accession] = index
    # Check if the number of unique values in the set is equal to the total number of values in the "archive_accession" column
    if len(all_accessions) != sum(1 for item in data if item[id_flag]):
        print("Error: Duplicate values found in accession ids")
        exit(1)
    else:
        print("All accession ids are unique")


def gap_validation(tsv_file):
    # Data loading
    data = pd.read_csv(tsv_file, delimiter="\t")
    # unique использовал, чтобы узнать какие значения воспринимает код (None, nan (для NA и пустых строк))
    # print(data.iloc[:, 2].unique())
    # Проверка на наличие пустых ячеек (исключая ячейки со значением 'None')
    empty_cells = np.where(pd.isna(data))

    # Вывод номеров строк и колонок с пустыми ячейками
    if len(empty_cells[0]) > 0:
        print("Empty cells are in the following places:")
        for row, col in zip(empty_cells[0], empty_cells[1]):
            print(f"Row: {row}, columns: {col}")
        exit(1)
    else:
        print("There is no empty cells! Good job!")
