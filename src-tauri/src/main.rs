use std::fs::File;
use std::path::Path;
use walkdir::WalkDir;

use tauri::{command, api::shell, Window};

#[command]
fn scan_directory(path: String) -> Result<(), String> {
    let file = File::create("dir_list.csv").map_err(|e| e.to_string())?;
    let mut wtr = csv::Writer::from_writer(file);
    for entry in WalkDir::new(&path) {
        let entry = entry.map_err(|e| e.to_string())?;
        let p = entry.path().display().to_string();
        wtr.write_record(&[p]).map_err(|e| e.to_string())?;
    }
    wtr.flush().map_err(|e| e.to_string())?;
    Ok(())
}

#[command]
fn open_folder(path: String, window: Window) -> Result<(), String> {
    shell::open(&window.shell_scope(), Path::new(&path), None)
        .map_err(|e| e.to_string())
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![scan_directory, open_folder])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
