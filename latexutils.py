#===================================================================================================
def compile_latex(texfile, pdffile, latex_flavour='pdflatex'):
    import os
    
    tmp_filename = 'aux_latex'
    
    # now compile the new file
    current_dir = os.getcwd()
    tmp_dir = '/tmp/latextable'
    if not os.path.exists(tmp_dir): os.makedirs(tmp_dir)
    
    os.system(f'cp {texfile}.tex {tmp_dir}/{tmp_filename}.tex')
    os.chdir(tmp_dir)
    os.system(f'{latex_flavour} -interaction=batchmode {tmp_filename}.tex')
    os.system(f'pdfcrop {tmp_filename}.pdf {tmp_filename}_cropped.pdf')
    os.chdir(current_dir)
    os.system(f'cp {tmp_dir}/{tmp_filename}_cropped.pdf {pdffile}.pdf')
    
    return
#===================================================================================================

#===================================================================================================
def create_latex_doc(input_filename, output_filename):
    from textwrap import dedent
    
    with open(output_filename, 'w') as of:
        header = dedent("""
            \\documentclass{article}
            \\usepackage[T1]{fontenc}
            \\usepackage{graphicx}
            \\usepackage{underscore}
            \\usepackage{amsmath}
            \\usepackage{feynmp-auto}
            \\usepackage[landscape]{geometry}

            \\begin{document}
            \\pagestyle{empty}"""
        )

        of.write(header)

        with open(input_filename, 'r') as infile:
            of.writelines(infile.readlines())

        of.write('\n\\end{document}\n')
    
    return
#===================================================================================================

#===================================================================================================
def replace_single_latex(txt):
    try:
        return latex_math[txt]
    except KeyError:
        return txt
#===================================================================================================

#===================================================================================================
def replace_tuple_latex(els):
    lat = ''
    if isinstance(els, tuple):
        for i in els:
            lat += replace_single_latex(i)
    elif isinstance(els, str):
        lat = els
    return lat
#===================================================================================================