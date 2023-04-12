import csv
import json


def tsv_converting(file_name, json_name):
    # Open TSV-fail for reading
    with open(file_name, 'r') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        # Преобразуем данные в список словарей, приводя значения полей к нужным типам данных
        rows = [
            {
                "project_name": str(row["project_name"]) if row["project_name"] != "None" else None,
                "publication_year": int(row["publication_year"]) if row["publication_year"] != "None" else None,
                "publication_doi": str(row["publication_doi"]) if row["publication_doi"] != "None" else None,
                "site_name": str(row["site_name"]) if row["site_name"] != "None" else None,
                "latitude": float(row["latitude"].replace(",", ".")) if isinstance(row["latitude"], str) and row["latitude"].replace(".", "", 1).isdigit() else None,
                "longitude": float(row["longitude"].replace(",", ".")) if isinstance(row["longitude"], str) and row["longitude"].replace(".", "", 1).isdigit() else None,
                "geo_loc_name": str(row["geo_loc_name"]) if row["geo_loc_name"] != "None" else None,
                "study_primary_focus": str(row["study_primary_focus"]) if row["study_primary_focus"] != "None" else None,
                "sequence_name": str(row["sequence_name"]) if row["sequence_name"] != "None" else None,
                "depth": float(row["depth"].replace(",", ".")) if isinstance(row["depth"], str) and row["depth"].replace(".", "", 1).isdigit() else None,
                "sample_name": str(row["sample_name"]) if row["sample_name"] != "None" else None,
                "sample_age": int(row["sample_age"]) if row["sample_age"] != "None" else None,
                "sample_age_doi": str(row["sample_age_doi"]) if row["sample_age_doi"] != "None" else None,
                "feature": str(row["feature"]) if row["feature"] != "None" else None,
                "material": str(row["material"]) if row["material"] != "None" else None,
                "sampling_date": int(row["sampling_date"]) if row["sampling_date"] != "None" else None,
                "archive": str(row["archive"]) if row["archive"] != "None" else None,
                "archive_project": str(row["archive_project"]) if row["archive_project"] != "None" else None,
                "archive_accession": str(row["archive_accession"]) if row["archive_accession"] != "None" else None
            }
            for row in reader
        ]
    # Open JSON-fail for writing
    with open(json_name, 'w') as jsonfile:
        # Записываем данные в формате JSON
        json.dump(rows, jsonfile, indent=4, ensure_ascii=False)
