#!/usr/bin/env python3

import argparse, sqlite3, json, csv, os, sys
from datetime import datetime, timedelta, timezone

# This is a hack to allow us to import the compiled protobuf code from the proto directory.
sys.path.insert(0, os.path.abspath("./proto"))
from power_bookmark_specifics_pb2 import PowerBookmarkSpecifics

# User notes are split between the saves and blobs tables.
# The saves table contains the metadata for the power_bookmark while the blobs table contains the protobuf message.
# A power_type of 2 corresponds to a user note.
# We annotate the type of "pbs" column so we can use a custom converter to parse the blob.
select_query = """
    SELECT
        CAST(blobs.specifics AS BLOB) AS "pbs [specifics]"
    FROM
        saves
        INNER JOIN blobs
            ON saves.id = blobs.id
    WHERE
        saves.power_type = 2
    ORDER BY
        saves.time_added ASC
"""

# This function converts the WebKit/Chrome timestamp to a local datetime object (and drops the microseconds and timezone).
def convert_timestamp(usec):
    windows_epoch = datetime(1601, 1, 1, tzinfo=timezone.utc)
    return (windows_epoch + timedelta(microseconds=usec)).astimezone().replace(tzinfo=None, microsecond=0)

# This function uses the compiled protobuf code to parse the power_bookmark_specifics blob.
def parse_power_bookmark_specifics(specifics):
    pbs = PowerBookmarkSpecifics()
    pbs.ParseFromString(specifics)
    return pbs
# We register this function as a converter for the "specifics" type.
sqlite3.register_converter("specifics", parse_power_bookmark_specifics)

# This function converts a protobuf message into a concise dictionary with just the fields we care about.
def convert_protobuf_message(pbs):
    return {
        "url": pbs.url,
        "created": convert_timestamp(pbs.creation_time_usec),
        "modified": convert_timestamp(pbs.update_time_usec),
        "note": pbs.power_entity.note_entity.plain_text
    }

def main():
    # Parse command line arguments...
    parser = argparse.ArgumentParser(description="Chromium PowerBookmarks.db User Notes extraction utility.")
    parser.add_argument("database", type=str, help="Path to PowerBookmarks.db database file.")
    outopts = parser.add_argument_group("Output options")
    outopts.add_argument("-f", "--format", type=str, choices=["json", "csv"], default="json", help="Output format for the converted notes.")
    outopts.add_argument("-o", "--outfile", type=str, help="File to write the exported notes into (default is stdout).")
    outopts.add_argument("-y", "--yes", action="store_true", help="Overwrite the output file if it already exists.")
    args = parser.parse_args()

    # Check that the given database file exists.
    if not os.path.isfile(args.database):
        raise ValueError(f"{args.database} is not a file.")

    # Connect to the database and execute the query to load the notes.
    with sqlite3.connect(args.database, detect_types=sqlite3.PARSE_COLNAMES) as conn:
        conn.row_factory = sqlite3.Row
        notes = [convert_protobuf_message(row["pbs"]) for row in conn.execute(select_query)]

    # Check that we actually found some notes.
    if len(notes) == 0:
        print(f"No power_bookmarks corresponding to user_notes where found in {args.database}.")
        exit()

    # Open the output stream (or advise the user to force overwriting if the file already exists)
    if (args.outfile):
        if os.path.isfile(args.outfile) and not args.yes:
            raise RuntimeWarning(f"{args.outfile} already exists. Use -y to overwrite.")
        else:
            outstream = open(args.outfile, "w")
    else:
        outstream = sys.stdout

    # Finally, write the notes to the output stream in the requested format.
    if args.format == "json":
        json.dump(notes, outstream, indent=2, default=str)
    else:
        writer = csv.DictWriter(outstream, fieldnames=notes[0].keys())
        writer.writeheader()
        writer.writerows(notes)

    exit()

if __name__ == "__main__":
    main()
