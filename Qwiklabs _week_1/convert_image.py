import os
from PIL import Image

src_dir ="real_world_task/Qwiklabs _week_1/images/images/"
new_dir = "real_world_task/Qwiklabs _week_1/sample/"
"""
# set reprocess vars:
rx_90dg = -90
rx_size = (128, 128)
# NOTE: the required output format results in black images because the source
# TIFF files have transparent backaground which original JPG format doesn't
# support. PNG would be a more suitable option, but the lab calls for JPEG.
rx_frmt = "JPEG"

# gather list of image files:
img_files = [f for f in os.listdir(src_dir) if f.startswith("ic_")]

# reprocess images:
for file in img_files:
    src_img = Image.open(src_dir + file)

    # rotate & resize image:
    new_img = src_img.rotate(rx_90dg).resize(rx_size)

    # NOTE: we need to convert to RGB here to avoid error:
    new_img = new_img.convert("RGB")

    # save new output file:
    new_img.save(new_dir + file+".jpg")
   
"""
size = (128, 128)

for infile in os.listdir(src_dir):
    outfile = os.path.splitext(infile)[0]
    try:
        with Image.open(src_dir+infile).convert('RGB') as im:
            im.thumbnail(size)
            im.rotate(270).save(new_dir + outfile +".JPEG")
    except OSError:
        pass
  


        