# Chromium User Note Extraction Utility

User notes are stored in a Chromium profile's `PowerBookmarks.db` file as serialised protobuf messages.
This repository contains a script that can be used to easily extract the notes from your backed up `PowerBookmarks.db` database.
I wrote this because the recent Chrome UI update has removed the User notes functionality from the side panel.

## Requirements

You don't need to download/compile [protobuf](https://github.com/protocolbuffers/protobuf/releases/latest) yourself because I've already compiled the necessary files to handle the user notes data (in the proto directory). However, you will need Python 3 as well as the protobuf and sqlite packages for it. AFAICT, that means you only need to run `pip install protobuf` to get going.

## Installation

Either clone or extract this project somewhere convenient, make sure you have the required packages installed, and make sure that `extract.py` is executable (e.g. `chmod +x extract.py`).

# Locating `PowerBookmarks.db`

This tool needs to read the `PowerBookmarks.db` file to look for stored user notes. I recommend you put it somewhere that is easily accessed (for example, in the same folder as this script). Here's how to locate it:

1. Open the browser's version/info page (`chrome://version/`).
2. Use your file navigator to open the directory listed on the version page in the "Profile Path" section
3. Copy the `PowerBookmarks.db` file from inside the `power_bookmarks` folder
4. Paste this somewhere convenient to use for this script (or to keep as a back up if desired)

# Usage

You can use this script with only the database file as an option and it will print out all of the user notes in JSON format (i.e., `./extract.py ./PowerBookmarks.db`). This is helpful if you know you'll be piping the output into another tool (e.g., `jq`). If you want to write the output to a file, you can either redirect the command's output (check your shell's documentation) or use the `-o`/`--outfile` option to specify a file to store the exported data. Further, you can write the output as a CSV file which may be helpful if you intend to import into another program or database (e.g., `./extract.py -f csv -o notes.csv ./PowerBookmarks.db`). By default you cannot overwrite an existing file, please add the `-y`/`--yes` flag to enable this behaviour.

If you forget these instructions, use the `-h`/`--help` flag to see them again:

```text
usage: extract.py [-h] [-f {json,csv}] [-o OUTFILE] [-y] database

Chromium PowerBookmarks.db User Notes extraction utility.

positional arguments:
  database              Path to PowerBookmarks.db database file.

options:
  -h, --help            show this help message and exit

Output options:
  -f {json,csv}, --format {json,csv}
                        Output format for the converted notes.
  -o OUTFILE, --outfile OUTFILE
                        File to write the exported notes into (default is stdout).
  -y, --yes             Overwrite the output file if it already exists.
```

# Appendix

There's just miscellaneous details in here for anyone interested in the storage format for the user notes. Here's a small script (written for bash) that generates the python files needed to parse the message blob (from the protocol specification at the time of writing).

```bash
# Assume we're starting at the root of the project and move into the proto directory
mkdir -p proto && pushd proto >/dev/null

# Download the two relevant .proto files
wget -q "https://github.com/chromium/chromium/raw/71880697e267a240ea3d22e26cbfb9cf6956cf7d/components/sync/protocol/"{power_bookmark_specifics,note_entity}".proto"

# Patch the location of the import reference
git apply <<'EOF'
diff --git a/proto/power_bookmark_specifics.proto b/proto/power_bookmark_specifics.proto
index ac892c3..d527cff 100644
--- a/proto/power_bookmark_specifics.proto
+++ b/proto/power_bookmark_specifics.proto
@@ -11,7 +11,7 @@ option optimize_for = LITE_RUNTIME;
 
 package sync_pb;
 
-import "components/sync/protocol/note_entity.proto";
+import "note_entity.proto";
 
 // Data structure dedicated to each power type.
 // Should keep the field numbers of specifics in sync with the ones in PowerType
EOF

# Compile the necessary python files using `protoc`
protoc --python_out=. *.proto

# Return to previous folder
popd >/dev/null
```
