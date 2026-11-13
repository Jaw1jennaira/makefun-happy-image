import os,shutil
# Copy the entry image to the output directory (deterministic: same bytes every run).
src=os.path.join(os.path.dirname(__file__),'entry.png')
out=os.environ.get('MAKEFUN_OUTPUT_DIR','/output')
os.makedirs(out,exist_ok=True)
shutil.copyfile(src,os.path.join(out,'entry.png'))
