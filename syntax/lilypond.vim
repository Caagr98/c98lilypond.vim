if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif

setlocal mps+=<:>

syn case match

call LilypondHighlight()

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

if 0
syn match lilyDurationFancy    /\v\d@<!128\d@!/          contained containedin=lilyDuration    conceal cchar=𝅘𝅥𝅲
syn match lilyDurationFancy    /\v\d@<!64\d@!/           contained containedin=lilyDuration    conceal cchar=𝅘𝅥𝅱
syn match lilyDurationFancy    /\v\d@<!32\d@!/           contained containedin=lilyDuration    conceal cchar=𝅘𝅥𝅰
syn match lilyDurationFancy    /\v\d@<!16\d@!/           contained containedin=lilyDuration    conceal cchar=𝅘𝅥𝅯
syn match lilyDurationFancy    /\v\d@<!8\d@!/            contained containedin=lilyDuration    conceal cchar=𝅘𝅥𝅮
syn match lilyDurationFancy    /\v\d@<!4\d@!/            contained containedin=lilyDuration    conceal cchar=𝅘𝅥
syn match lilyDurationFancy    /\v\d@<!2\d@!/            contained containedin=lilyDuration    conceal cchar=𝅗𝅥
syn match lilyDurationFancy    /\v\d@<!1\d@!/            contained containedin=lilyDuration    conceal cchar=𝅝
syn match lilyDurationFancy    /\\breve/                 contained containedin=lilyDuration    conceal cchar=𝅜
syn match lilyDurationFancy    /\./                      contained containedin=lilyDuration    conceal cchar=·
hi link lilyDurationFancy lilyDuration

syn match lilyRDurationFancy   /\v\d@<!128\d@!/          contained containedin=lilyRDuration   conceal cchar=𝅂
syn match lilyRDurationFancy   /\v\d@<!64\d@!/           contained containedin=lilyRDuration   conceal cchar=𝅁
syn match lilyRDurationFancy   /\v\d@<!32\d@!/           contained containedin=lilyRDuration   conceal cchar=𝅀
syn match lilyRDurationFancy   /\v\d@<!16\d@!/           contained containedin=lilyRDuration   conceal cchar=𝄿
syn match lilyRDurationFancy   /\v\d@<!8\d@!/            contained containedin=lilyRDuration   conceal cchar=𝄾
syn match lilyRDurationFancy   /\v\d@<!4\d@!/            contained containedin=lilyRDuration   conceal cchar=𝄽
syn match lilyRDurationFancy   /\v\d@<!2\d@!/            contained containedin=lilyRDuration   conceal cchar=𝄼
syn match lilyRDurationFancy   /\v\d@<!1\d@!/            contained containedin=lilyRDuration   conceal cchar=𝄻
syn match lilyRDurationFancy   /\\breve/                 contained containedin=lilyRDuration   conceal cchar=𝄺
syn match lilyRDurationFancy   /\./                      contained containedin=lilyRDuration   conceal cchar=·
hi link lilyRDurationFancy lilyRDuration

syn match lilyDurationMulFancy /\*/                      contained containedin=lilyDurationMul conceal cchar=⋆
syn match lilyDurationMulFancy +\v\d@<!1/2\d@!+          contained containedin=lilyDurationMul conceal cchar=½
syn match lilyDurationMulFancy +\v\d@<!1/3\d@!+          contained containedin=lilyDurationMul conceal cchar=⅓
syn match lilyDurationMulFancy +\v\d@<!2/3\d@!+          contained containedin=lilyDurationMul conceal cchar=⅔
syn match lilyDurationMulFancy +\v\d@<!1/4\d@!+          contained containedin=lilyDurationMul conceal cchar=¼
syn match lilyDurationMulFancy +\v\d@<!3/4\d@!+          contained containedin=lilyDurationMul conceal cchar=¾
syn match lilyDurationMulFancy +\v\d@<!1/5\d@!+          contained containedin=lilyDurationMul conceal cchar=⅕
syn match lilyDurationMulFancy +\v\d@<!2/5\d@!+          contained containedin=lilyDurationMul conceal cchar=⅖
syn match lilyDurationMulFancy +\v\d@<!3/5\d@!+          contained containedin=lilyDurationMul conceal cchar=⅗
syn match lilyDurationMulFancy +\v\d@<!4/5\d@!+          contained containedin=lilyDurationMul conceal cchar=⅘
syn match lilyDurationMulFancy +\v\d@<!1/6\d@!+          contained containedin=lilyDurationMul conceal cchar=⅙
syn match lilyDurationMulFancy +\v\d@<!5/6\d@!+          contained containedin=lilyDurationMul conceal cchar=⅚
syn match lilyDurationMulFancy +\v\d@<!1/7\d@!+          contained containedin=lilyDurationMul conceal cchar=⅐
syn match lilyDurationMulFancy +\v\d@<!1/8\d@!+          contained containedin=lilyDurationMul conceal cchar=⅛
syn match lilyDurationMulFancy +\v\d@<!3/8\d@!+          contained containedin=lilyDurationMul conceal cchar=⅜
syn match lilyDurationMulFancy +\v\d@<!5/8\d@!+          contained containedin=lilyDurationMul conceal cchar=⅝
syn match lilyDurationMulFancy +\v\d@<!7/8\d@!+          contained containedin=lilyDurationMul conceal cchar=⅞
syn match lilyDurationMulFancy +\v\d@<!1/9\d@!+          contained containedin=lilyDurationMul conceal cchar=⅑
" syn match lilyDurationMulFancy +\v\d@<!1/10\d@!+ transparent contained containedin=lilyDurationMul conceal cchar=⅒
hi link lilyDurationMulFancy lilyDurationMul

syn match lilyPitchFancy       /'/                       contained containedin=lilyPitch       conceal cchar=↑
syn match lilyPitchFancy       /''/                      contained containedin=lilyPitch       conceal cchar=⇈
syn match lilyPitchFancy       /,/                       contained containedin=lilyPitch       conceal cchar=↓
syn match lilyPitchFancy       /,,/                      contained containedin=lilyPitch       conceal cchar=⇊
syn match lilyPitchFancy       /\v\a@<![a-g]\zses\a@!/   contained containedin=lilyPitch       conceal cchar=♭
syn match lilyPitchFancy       /\v\a@<![ae]\zss\a@!/     contained containedin=lilyPitch       conceal cchar=♭
syn match lilyPitchFancy       /\v\a@<![a-g]\zseses\a@!/ contained containedin=lilyPitch       conceal cchar=𝄫
syn match lilyPitchFancy       /\v\a@<![a-g]\zsis\a@!/   contained containedin=lilyPitch       conceal cchar=♯
syn match lilyPitchFancy       /\v\a@<![a-g]\zsisis\a@!/ contained containedin=lilyPitch       conceal cchar=𝄪
hi link lilyPitchFancy lilyPitch

setlocal conceallevel=1 concealcursor=nc
endif

let b:current_syntax = "lilypond"
