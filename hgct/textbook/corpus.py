import csv
import re
from pathlib import Path
from textbook.configs import NUMERAL_MAPPING, ORD_MAPPING
from textbook.pipes import meta2yaml


def get_semester(grade: str):
    if grade.endswith("下"):
        return grade.replace("下", "S")
    return grade.replace("上", "F")


def filter_lesson(lesson: str):
    if not lesson.startswith("附錄"):
        return lesson
    key = re.search("附錄(.)", lesson).group(1)
    return NUMERAL_MAPPING[key]


def build_time_meta(semester: str, year: str, grade: str, time_meta: dict):
    metadata = time_meta.get(semester)
    if metadata is None:
        time_meta[semester] = {
            "year": [year],
            "label": f"教科書課文 - {grade}",
            "ord": ORD_MAPPING[grade],
        }
    else:
        years: list = metadata["year"]
        if year not in years:
            years.append(year)
 
def build_subcorpus(filename: str, content: str):
    with open(filename, "w") as file:
        filtered = re.sub(r"\n{3,}", "\n\n", content)
        filtered_new_lines = re.sub(r"(?<!\n)\n(?!\n)", "\n\n", filtered)
        file.write(filtered_new_lines)


def build_corpus(csv_file: str, corpus_folder: str, encoding: str = "utf-8"):
    if not Path(csv_file).exists():
        raise Exception(f"File {csv_file} not found")

    text_meta = {}
    time_meta = {}

    with open(csv_file, mode="r", encoding=encoding) as file:
        rows = csv.reader(file)
        next(rows)

        for row in rows:
            id, subject, grade, year, publisher, type, lesson, title, content = row
            stripped_title = title.strip()
            semester = get_semester(grade=grade)
            filtered_lesson = filter_lesson(lesson=lesson)
            subcorpus_file = f"{year}-{filtered_lesson}-{stripped_title}.txt"
            filename = Path(corpus_folder) / semester / subcorpus_file
            filename.parent.mkdir(parents=True, exist_ok=True)

            text_meta[f'{semester}/{subcorpus_file}'] = {
                "year": year,
                "lesson": filtered_lesson,
                "title": stripped_title,
            }

            build_time_meta(
                time_meta=time_meta, semester=semester, year=year, grade=grade
            )
            build_subcorpus(filename=filename, content=content)

    text_meta_filename = Path(corpus_folder) / "text_meta.yaml"
    time_meta_filename = Path(corpus_folder) / "time.yaml"

    meta2yaml(filename=text_meta_filename, metadata=text_meta)
    meta2yaml(filename=time_meta_filename, metadata=time_meta, is_time_meta=True)