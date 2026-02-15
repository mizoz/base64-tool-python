# Base64 Tool Python

[![PyPI Version](https://img.shields.io/pypi/v/base64-tool-python?style=flat-square)](https://pypi.org/project/base64-tool-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/base64-tool-python?style=flat-square)](https://pypi.org/project/base64-tool-python/)
[![License](https://img.shields.io/pypi/l/base64-tool-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/base64-tool-python?style=flat-square)](https://pypi.org/project/base64-tool-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/base64-tool-python?style=flat-square)](https://github.com/mizoz/base64-tool-python)

> A fast and efficient Python CLI tool for Base64 encoding and decoding operations.

## Features

- ✅ Encode strings to Base64
- ✅ Decode Base64 strings back to plain text
- ✅ File encoding and decoding support
- ✅ Batch processing capability
- ✅ Command-line interface
- ✅ Python API for integration

## Installation

### From PyPI

```bash
pip install base64-tool-python
```

### From Source

```bash
git clone https://github.com/mizoz/base64-tool-python.git
cd base64-tool-python
pip install -e .
```

## Usage

### Command Line

```bash
# Encode a string
base64-encode "Hello World"

# Decode a Base64 string
base64-decode "SGVsbG8gV29ybGQ="

# Encode a file
base64-encode --file input.txt

# Decode to a file
base64-decode --file encoded.txt --output decoded.txt
```

### Python API

```python
from base64_tool import Base64Codec

codec = Base64Codec()

# Encode a string
encoded = codec.encode("Hello World")
print(encoded)  # SGVsbG8gV29ybGQ=

# Decode a string
decoded = codec.decode("SGVsbG8gV29ybGQ=")
print(decoded)  # Hello World
```

## CLI Options

| Option | Description |
|--------|-------------|
| `-d, --decode` | Decode instead of encode |
| `-f, --file` | Process a file |
| `-o, --output` | Output file path |

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a [Pull Request](https://github.com/mizoz/base64-tool-python/pulls).

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

## Acknowledgments

- Thanks to the Python community for their continued support

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
