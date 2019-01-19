
activate :syntax

set :markdown_engine, :redcarpet
set :markdown, :fenced_code_blocks => true, :smartypants => true, :footnotes => true, :tables => true

activate :bibtex do |opts|
    opts.path   = 'zotero.bib' # path to a bibtex file
    opts.style  = 'ieee'              # style from citeproc-styles
    opts.format = 'html'              # output format
end

# Prevent bibtex-ruby from decoding LaTeX
LaTeX::Decode::Maths.class_eval do
    def self.decode! (string)
        "(disabled)"
    end
end

# Per-page layout changes
page '/*.xml', layout: false
page '/*.json', layout: false
page '/*.txt', layout: false
