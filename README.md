# PyAssistant

**Version:** 0.1
**Author:** Brent Bradford

## Note
	
This application uses pretrained hugging face models which are downloaded and stored locally
on your machine. Please ensure you have sufficient disk space and VRAM to download and initialize
these models. Refer to the model's documentation for more detailed information on model requirements
and licenses.

### Models

**NLP:**

- [gpt2-medium](https://huggingface.co/openai-community/gpt2-medium)

**Diffuser:**

- [PixArt-alpha/PixArt-XL-2-1024-MS](https://huggingface.co/PixArt-alpha/PixArt-XL-2-1024-MS)

The GUI and event logic are still under development. The only tested model so far is the PixArt 
model optimized for low VRAM requirements. 

## Description

PyAssistant is a user interface designed for interacting with pretrained, locally stored AI models. 

### Important

Please wait for the GUI to be fully implemented before downloading. This project is currently
in the prototyping phase; selecting a model from the main window only downloads it locally.

## Requirements

### Poetry

- [Poetry 1.8.2+](https://python-poetry.org/)

### Python

- [Python 3.10+](https://www.python.org/downloads/)

#### Dependencies:

  1. diffusers[torch]
  2. transformers[torch]
  3. torchvision
  4. pyyaml
  5. python-dotenv
  6. accelerate
  7. safetensors
  8. sentencepiece
  9. bitsandbytes
  10. beautifulsoup4
  11. ftfy

#### Developer Dependencies:

  1. pytest
  2. pytest-cov
  3. pytest-mock

## Installation

'''bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Clone the repository
git clone https://
cd PyAssistant

# Install dependencies
poetry install

## Usage

poetry run pyassistant

### GUI Instructions

  1. Select a model type and model from the "Models" menu.

  **Under Development**
  2. The application will then download and initialize the model. After
  the model has been downloaded you will be greeted by the model.

#### NLP Model
  1. After you have been greeted by the model you can use the entry widget
  at the bottom of the window to chat with the model.

  2. You can select a different model from the "Models" menu at
  any time.

#### Diffuser Model
  1. After you have been greeted by the model you will be prompted to
  enter a description of the image you would like the model to generate.

  2. Input your image desceription in the entry widget located at the bottom
  of the window and press enter to submit your description to the model.

  3. The model will then generate an image (this can take a few minutes
  depending on the model type and your system's hardware). 

  4. When the model has finished you will be shown a dialog window asking
  if you would like to save the image.

  5. if you pressed yes, you will be shown a new dialog that will allow you
  to save your image.

  6. After you have finished saving or cancelling your image, you can input
  another image description, or change models.

  **NOTE**
  While the image is being generated you will not be able to switch models.

## License

**PyAssistant**
Copyright (c) 2024 Brent Bradford

This product is licensed under the Apache License 2.0 (see LICENSE file for details).

## Changes

Initial Commit
