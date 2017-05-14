(TeX-add-style-hook
 "proposal"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "paper=letter" "fontsize=12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "english") ("inputenc" "utf8") ("fixme" "draft") ("fontenc" "T1") ("geometry" "hmarginratio=1:1" "top=20mm" "columnsep=15pt" "left=15mm")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "multicol"
    "babel"
    "amsmath"
    "amsfonts"
    "amsthm"
    "inputenc"
    "float"
    "natbib"
    "fixme"
    "lipsum"
    "blindtext"
    "graphicx"
    "caption"
    "subcaption"
    "fontenc"
    "microtype"
    "geometry"
    "booktabs"
    "hyperref"
    "paralist"
    "abstract"
    "titlesec"
    "fancyhdr"
    "titling"
    "etoolbox")
   (TeX-add-symbols
    '("horrule" 1))
   (LaTeX-add-bibliographies))
 :latex)

