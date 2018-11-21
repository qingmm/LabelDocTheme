import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['nlp_annotation.py','-w','-F','--icon=web.ico']
    run(opts)