from zipfile import ZipFile

import pytest

@pytest.fixture(scope="session")
def create_archive_file():
    with ZipFile("homework_7.zip", "w") as archive:
        archive.write("Employee Sample Data.csv", arcname='user_list.csv')
        archive.write("sample-empty.xls", arcname='user_list_for_xlsx.xlsx')
        archive.write("1718880779_Verzani-SimpleR.pdf", arcname='pdf_list.pdf')
    yield "files/archive.zip"