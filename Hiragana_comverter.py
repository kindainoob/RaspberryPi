from pykakasi import kakasi

if __name__ == "__main__":
    text = u"かな 漢 字 交 じ り 文"
    text = ''.join(text.split())
    kakasi = kakasi()
    kakasi.setMode("H", "H")  # Hiragana to ascii, default: no conversion
    kakasi.setMode("K", "H")  # Katakana to ascii, default: no conversion
    kakasi.setMode("J", "H")  # Japanese to ascii, default: no conversion
    kakasi.setMode("r", "Hepburn")  # default: use Hepburn Roman table
    conv = kakasi.getConverter()
    result = conv.do(text)
    print(result)
