(TeX-add-style-hook
 "report"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "paper=letter" "fontsize=12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "english") ("inputenc" "utf8") ("fixme" "draft") ("mathpazo" "sc") ("fontenc" "T1") ("geometry" "margin=1.5in")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "babel"
    "amsmath"
    "amsfonts"
    "amsthm"
    "inputenc"
    "float"
    "fixme"
    "lipsum"
    "blindtext"
    "graphicx"
    "caption"
    "subcaption"
    "mathpazo"
    "fontenc"
    "microtype"
    "geometry"
    "multicol"
    "booktabs"
    "hyperref"
    "lettrine"
    "paralist"
    "abstract"
    "titlesec"
    "algorithm"
    "algpseudocode"
    "fancyhdr")
   (TeX-add-symbols
    '("horrule" 1)))
 :latex)

