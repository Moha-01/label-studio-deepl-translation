# label-studio-deepl-translation
Python Script that translates Data using DeepL API to use them under Label Studio

<br>

## Requierments
You will need to install the `requests` pip Package to handle the Request.

Command:
```python
python -m pip install requests
```

<br>


The Script uses those imports:
```python
import requests
import json
import argparse
```
<hr>

## Usage
To run the Skript, you will need to give it three parameters: 
- `--input` defines the Data should be translated.
- `--output` defines the name of the translated data file.
- `--deepl_key` defines the access token, that we need to be able to translate data.

<br>

On Commandline:
```sh
python translate.py --input INPUT_FILE --output OUTPUT_FILE --deepl_key API_TOKEN
```

<br>

Example based on the current File-Structure:
```sh
python translate.py --input .\test.json --output translated_test.json --deepl_key bc16f600-c938-1a7b-9147-4bbb96901b75:fx
```
This API Token ist not valid. Replace it with your own one.
