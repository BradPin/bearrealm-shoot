import argparse
import os
import sys
try:
    from rembg import remove
except ImportError:
    remove = None
from PIL import Image
import io

def process_asset(input_path, output_path=None, remove_bg=True, resize=None):
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} not found.")
        sys.exit(1)
        
    print(f"Processing asset: {input_path}")
    
    try:
        with open(input_path, 'rb') as i:
            input_data = i.read()
            
        if remove_bg:
            if remove is None:
                print("Warning: rembg module not found. Skipping background removal.")
                img = Image.open(io.BytesIO(input_data))
            else:
                print("Removing background...")
                output_data = remove(input_data)
                img = Image.open(io.BytesIO(output_data))
        else:
            img = Image.open(io.BytesIO(input_data))
            
        if resize:
            # Format: WIDTHxHEIGHT
            w, h = map(int, resize.lower().split('x'))
            print(f"Resizing to {w}x{h}...")
            img = img.resize((w, h), Image.LANCZOS)
            
        if output_path is None:
            # Default: input_processed.png
            base, ext = os.path.splitext(input_path)
            output_path = f"{base}_processed.png"
            
        img.save(output_path)
        print(f"Processed image saved to: {output_path}")
        
    except Exception as e:
        print(f"Error processing asset: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process game assets (remove bg, resize)')
    parser.add_argument('input', type=str, help='Input image path')
    parser.add_argument('--out', type=str, help='Output image path')
    parser.add_argument('--no-bg', action='store_false', dest='remove_bg', help='Do not remove background')
    parser.add_argument('--resize', type=str, help='Resize to WxH')
    
    args = parser.parse_args()
    process_asset(args.input, args.out, args.remove_bg, args.resize)
