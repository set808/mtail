# Mtail

Mtail is a barebones Python package that monitors all files in a directory for new content. Mtail accounts for log rotation.

## Installation

```$ pip install mtail```

## Usage

Navigate to the directory to be monitored:

```cd /path/to/directory```

Run mtail:

```$ mtail```

## Limitations

* New files created during program run will not be monitored
* Subprocess isn't closed on file deletion.


## TODO

* Add monitoring for new files created during runtime
* Convert to serverless function using OpenFAAS
* Test suite



