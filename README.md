# Lotus-Menu

![Lotus_boot](https://github.com/user-attachments/assets/029b4b30-81d7-48c0-8a14-ca9b2a5d36e0)

This is a customizable multitool. The GUI is now provided as a [Tauri](https://tauri.app/) application.

## Building

1. **Install Rust** using [rustup](https://rustup.rs):
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```
2. **Install the Tauri CLI**:
   ```bash
   cargo install tauri-cli
   ```
3. **Run the application**:
   ```bash
   cargo tauri dev
   ```
   The compiled application will open with a simple "Browse Folder" button.

Building a release bundle is done with:
```bash
cargo tauri build
```
