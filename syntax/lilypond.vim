if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif

setlocal mps+=<:>

syn case match

source <sfile>:p:h/lilypond_gen.vim

hi def link lilyError            Error

hi def link lilyCustomFunction   Identifier
hi def link lilyBuiltin          PreProc
hi def link lilyMusicCommand     Function
hi def link lilyArticulation     lilyMusicCommand
hi def link lilyOrnament         lilyMusicCommand
hi def link lilyFermata          lilyMusicCommand
hi def link lilyInstrumentScript lilyMusicCommand
hi def link lilyRepeat           lilyMusicCommand
hi def link lilyAncient          lilyMusicCommand
hi def link lilyScale            lilyMusicCommand
hi def link lilyMarkupFunction   lilyMusicCommand

hi def link lilyDuration         Number
hi def link lilyRDuration        lilyDuration
hi def link lilyDurationMul      lilyDuration
hi def link lilyNumber           Number
hi def link lilyString           String
hi def link lilyComment          Comment

hi def link lilyPitch            Operator
hi def link lilyRest             Operator
hi def link lilySymbol           Special
hi def link lilyLyric            Normal
hi def link lilyChordname        Normal
hi def link lilyDrum             lilyPitch
hi def link lilyChord            Special
hi def link lilyChordRepeat      Special
hi def link lilyFigure           Special

hi def link lilyLyricHyphen      Operator
hi def link lilyLyricExtender    Operator

hi def link lilyVar              Identifier

hi def link lilyLayout           Statement
hi def link lilyMarkup           Statement
hi def link lilyNotemode         Statement
hi def link lilyLyricmode        Statement
hi def link lilyChordmode        Statement
hi def link lilyDrummode         Statement
hi def link lilyFiguremode       Statement
hi def link lilyHeader           Statement
hi def link lilyPaper            Statement
hi def link lilyMidi             Statement
hi def link lilyContextMod       Statement
hi def link lilyWith             Statement

hi def link lilyScheme           PreProc
hi def link _schemeLilyStart     PreProc

let b:current_syntax = "lilypond"
