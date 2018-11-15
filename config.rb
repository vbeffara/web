
activate :syntax

set :markdown_engine, :redcarpet
set :markdown, :fenced_code_blocks => true, :smartypants => true

activate :bibtex do |opts|
    opts.path   = 'library.bib' # path to a bibtex file
    opts.style  = 'ieee'              # style from citeproc-styles
    opts.format = 'html'              # output format
end

# Per-page layout changes
page '/*.xml', layout: false
page '/*.json', layout: false
page '/*.txt', layout: false
