import hashlib

BINARY_TO_DNA = {
    "00": "A",
    "01": "T",
    "10": "C",
    "11": "G"
}

DNA_TO_BINARY = {v: k for k, v in BINARY_TO_DNA.items()}


def text_to_binary(text: str) -> str:
    return ''.join(format(ord(char), '08b') for char in text)


def binary_to_dna(binary: str) -> str:
    if len(binary) % 2 != 0:
        binary += "0"

    return ''.join(BINARY_TO_DNA[binary[i:i+2]] for i in range(0, len(binary), 2))


def text_to_dna(text: str) -> str:
    return binary_to_dna(text_to_binary(text))


def dna_to_binary(dna: str) -> str:
    invalid = set(dna) - {"A", "T", "C", "G"}
    if invalid:
        raise ValueError(f"Invalid DNA bases found: {invalid}")

    return ''.join(DNA_TO_BINARY[base] for base in dna)


def dna_to_text(dna: str) -> str:
    binary = dna_to_binary(dna)
    chars = []

    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))

    return ''.join(chars)


def checksum(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def package_data(text: str) -> dict:
    dna = text_to_dna(text)
    return {
        "original_text": text,
        "dna_sequence": dna,
        "checksum": checksum(text),
        "dna_length": len(dna)
    }


def verify_decoded_text(decoded_text: str, expected_checksum: str) -> bool:
    return checksum(decoded_text) == expected_checksum
