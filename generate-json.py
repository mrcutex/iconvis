import os
import json
import sys

def log(message):
    print(f"[DEBUG] {message}")

def generate_json():
    try:
        base_url = "https://raw.githubusercontent.com/mrcutex/iconvis/main"
        icons_dir = "icons"
        bold_dir = os.path.join(icons_dir, "bold")  
        all_items = []
        valid_extensions = {".png", ".jpg", ".jpeg", ".svg", ".ico", ".gif", ".webp"} 

        log(f"Scanning directory: {os.path.abspath(icons_dir)}")

        
        for root, _, files in os.walk(icons_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, icons_dir).replace("\\", "/")  

                
                if os.path.splitext(file_name)[1].lower() in valid_extensions:
                    name_without_ext = os.path.splitext(file_name)[0].replace("-", "_")  
                    
                    
                    icon_type = "bold" if bold_dir in root else "file"

                    all_items.append({
                        "type": icon_type,
                        "name": name_without_ext,  
                        "url": f"{base_url}/{icons_dir}/{relative_path}"
                    })
                else:
                    log(f"⚠️ Skipping non-icon file: {relative_path}")

        with open("icons.json", "w") as f:
            json.dump(all_items, f, indent=2)
            log(f"\n✔️ Total valid icon files added: {len(all_items)}")

    except Exception as e:
        log(f"🔥 Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    generate_json()
