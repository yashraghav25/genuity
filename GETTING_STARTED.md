# Getting Started with genuity_os

## Installation

You can install `genuity_os` in two ways:

### Option 1: Clone from GitHub

```bash
git clone https://github.com/yourusername/genuity_os.git
cd genuity_os
pip install .
```

## Usage

After installation, you can import and use the library in your Python code or Kaggle notebook:

```python
import genuity

# Example: Access core generator
from genuity.core_generator import ctgan, tabudiff, tvae

# Use CTGAN
ctgan_model = ctgan.CTGAN(...)

# Use TabuDiff
from genuity.core_generator.tabudiff.basic import sampler
sampler_instance = sampler.Sampler(...)

# Use TVAEs
from genuity.core_generator.tvae import encoder, decoder
encoder_instance = encoder.Encoder(...)
```

## Documentation

- See individual README.md files in each module for more details and examples.
- For Kaggle, simply upload the library or install via pip, then import as shown above.

---

For issues or contributions, visit [GitHub](https://github.com/yourusername/genuity_os).
