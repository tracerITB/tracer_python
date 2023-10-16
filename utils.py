"""Module providing a function for image file manipulation."""
import base64


def replace_image(file_path, file_type):
    """Read and convert image files to base64-encoded strings."""
    if file_type == "svg":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        with open(file_path, "rb") as f:
            return (
                f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"
            )
