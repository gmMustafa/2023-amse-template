from sqlalchemy import create_engine, inspect

from data.pipeline import (
    data_extraction_xls,
    data_transformation
)

# Db_Engine
db_engine = None


def test_xls_extract(path):
    df = data_extraction_xls(path)
    assert not df.empty, "XLS Extraction Failed"
    print("test_xls_extract: Test Passed")
    return df


def test_transformation(data, rename_col, drop_col):
    df = data_transformation(data, rename_col, drop_col)
    assert df.isna().any().any() == False, "NAN Found in Data"
    print("test_transformation: Test Passed")
    return df


def test_data_loader(table_name):
    engine = create_engine(f"sqlite:///nuremberg_stops_immoscout.sqlite")

    # Create an inspector object
    inspector = inspect(engine)

    # Check if a table exists in the database
    exists = inspector.has_table(table_name)
    assert exists, f"The table '{table_name}' does not exist in the database."
    print("test_data_loader: " + table_name + "Table exists, Test Passed")


def test_pipeline():
    path1 = "https://docs.google.com/spreadsheets/d/1yIMw92dv7yeztmDHAt8mvO74jFhTc9dS/export?format=xlsx"
    df1 = test_xls_extract(path1)
    test_transformation(df1, [], ["picturecount", "scoutId"])
    test_data_loader("immoscout")

    path2 = "https://docs.google.com/spreadsheets/d/19ASmxyaSSeiuWbagvZmzixJr261bTkoQ/export?format=xlsx"
    df2 = test_xls_extract(path2)
    test_transformation(df2, {
        "VGNKennung": "VAGIdentifier",
        "VAGKennung": "VAGIdentifierChar",
        "Haltepunkt": "breakpoint",
        "GlobalID": "GlobalID",
        "Haltestellenname": "stopName",
        "latitude": "latitude",
        "longitude": "longitude",
        "Betriebszweig": "branchOfService",
        "Dataprovider": "dataprovider"}, ["breakpoint", "GlobalID", "branchOfService", "dataprovider"])

    test_data_loader("nuremberg_stops")


if __name__ == "__main__":
    test_pipeline()
