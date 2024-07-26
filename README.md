# mac2droid

## Overview

mac2droid is a graphical user interface (GUI) tool designed for managing files between an Android device and a Mac computer using `adb` (Android Debug Bridge). This tool provides an intuitive interface to navigate directories, and copy files to and from your Android device.

## Features

- **Directory Navigation**: Easily browse through directories on your Android device.
- **File Operations**:
  - **Copy To**: Transfer files from your Android device to your Mac.
  - **Copy From [File]**: Transfer files from your Mac to your Android device.
  - **Copy From [Folder]**: Transfer entire folders from your Mac to your Android device.
- **Context Menus**: Right-click to access copy and paste options.

## Requirements

- Python 3.x
- Tkinter library
- ADB (Android Debug Bridge)

## Installation

1. **Install Anaconda**: It is recommended to use Anaconda for managing Python environments and packages. Download and install Anaconda from the [official website](https://www.anaconda.com/products/individual).

2. **Create a New Environment**: Create a new environment with Python 3.x:
    ```sh
    conda create --name mac2droid python=3.x
    conda activate mac2droid
    ```

3. **Install Tkinter**: Tkinter is usually included with Python, but you can ensure it's installed:
    ```sh
    conda install tk
    ```

4. **Install ADB**: Install ADB on macOS:
    ```sh
    brew install android-platform-tools
    ```

## Usage

1. **Prepare Your Device**:
   - Connect your Android device to your Mac using a USB cable.
   - Enable USB debugging on your Android device.

2. **Launch the Tool**:
    ```sh
    python mac2droid.py
    ```

3. **Navigate and Manage Files**:
   - Use the GUI to browse directories on your Android device.
   - Use context menus to copy files and folders to and from your Android device.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a detailed description of your changes.
4. Ensure your code follows the existing coding style and includes tests where appropriate.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
- [ADB](https://developer.android.com/studio/command-line/adb) for Android device management.