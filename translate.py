import requests
import json
import argparse

# Diese Funktion übersetzt den eingegebenen Text in Deutsch mit Hilfe der DeepL API.
def translate_text(text, deepl_key):
    url = "https://api-free.deepl.com/v2/translate"
    payload = {
        "auth_key": deepl_key,
        "text": text,
        "target_lang": 'DE'
    }
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    response.encoding = 'utf-8'  # Setze die Kodierung der Antwort auf 'utf-8'
    result = response.json()
    return result['translations'][0]['text']

# Diese Funktion liest eine JSON-Datei, übersetzt die Tokens in jedem Eintrag und speichert das Ergebnis in einer neuen Datei.
def translate_tokens(input_file, output_file, deepl_key):
    # Datei wird geöffnet und Daten werden geladen.
    with open(input_file, 'r') as f:
        data = json.load(f)
    print("Successfully loaded data from", input_file)

    # Für jeden Datensatz im JSON wird die Übersetzung durchgeführt.
    for i, item in enumerate(data):
        sentence = " ".join(item['token'])
        print("Translating sentence", i+1, "of", len(data))
        translated_sentence = translate_text(sentence, deepl_key)
        item['token'] = translated_sentence.split()

    # Übersetzte Daten werden in die Ausgabedatei geschrieben.
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Successfully wrote translated data to", output_file)

# Main Funktion, die Argumente von der Kommandozeile liest und die Übersetzungsfunktion aufruft.
if __name__ == "__main__":
    # Definieren der erwarteten Kommandozeilenargumente.
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Input json file', required=True)
    parser.add_argument('--output', help='Output json file', required=True)
    parser.add_argument('--deepl_key', help='DeepL API Key', required=True)

    # Lesen der Argumente von der Kommandozeile.
    args = parser.parse_args()
    
    # Aufrufen der Übersetzungsfunktion mit den eingelesenen Argumenten.
    translate_tokens(args.input, args.output, args.deepl_key)