import requests
import os


def download_file(url, local_filename):
    # Download the file
    with requests.get(url, stream=True) as r:
        if r.status_code != 200:
            raise Exception(f"Failed to download the file from {url}, status code: {r.status_code}")

        # Write the content to a file
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)

    return local_filename


# Example usage
url = "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/GitHub/vsextensions/copilot/1.188.0/vspackage"  # Replace with your URL
file_name = "example.vsix"  # Replace with the desired file path


try:
    download_file(url, file_name)
    print("File downloaded and verified successfully.")
except Exception as e:
    print(f"Error: {e}")

