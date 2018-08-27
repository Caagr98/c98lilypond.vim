import neovim
import ly
import ly.document
import ly.indent
import ly.words

alignable_words = {
	"and", "or", "cond", "begin"
	"<", "<=", "=", "=>", '>', "eq?", "eqv?", "equal?",
}

w = list(ly.words.lilypond_music_commands)
for f in ["chordmode", "drummode", "figuremode", "lyricmode", "notemode"]:
	if f in w: w.remove(f)
for f in ly.words.lilypond_keywords:
	if f in w: w.remove(f)
for f in ly.words.articulations:
	if f in w: w.remove(f)
for f in ly.words.ornaments:
	if f in w: w.remove(f)
for f in ly.words.fermatas:
	if f in w: w.remove(f)
for f in ly.words.instrument_scripts:
	if f in w: w.remove(f)
for f in ly.words.repeat_scripts:
	if f in w: w.remove(f)
for f in ly.words.ancient_scripts:
	if f in w: w.remove(f)
for f in ly.words.modes:
	if f in w: w.remove(f)

ly.words.drums = [
	"acousticbassdrum", "bda",   "bassdrum",     "bd",    "snare",        "sn",    "electricsnare", "sne",   "acousticsnare", "sna",
	"lowfloortom",      "tomfl", "highfloortom", "tomfh", "lowtom",       "toml",  "hightom",       "tomh",  "lowmidtom",     "tomml", "himidtom",    "tommh",
	"closedhihat",      "hhc",   "hihat",        "hh",    "pedalhihat",   "hhp",   "openhihat",     "hho",   "halfopenhihat", "hhho",
	"crashcymbala",     "cymca", "crashcymbal",  "cymc",  "ridecymbala",  "cymra", "ridecymbal",    "cymr",
	"chinesecymbal",    "cymch", "splashcymbal", "cyms",  "crashcymbalb", "cymcb", "ridecymbalb",   "cymrb", "ridebell",      "rb",    "cowbell",     "cb",
	"mutehibongo",      "bohm",  "hibongo",      "boh",   "openhibongo",  "boho",  "mutelobongo",   "bolm",  "lobongo",       "bol",   "openlobongo", "bolo",
	"mutehiconga",      "cghm",  "muteloconga",  "cglm",  "openhiconga",  "cgho",  "hiconga",       "cgh",   "openloconga",   "cglo",  "loconga",     "cgl",
	"hitimbale",        "timh",  "lotimbale",    "timl",  "hiagogo",      "agh",   "loagogo",       "agl",
	"hisidestick",      "ssh",   "sidestick",    "ss",    "losidestick",  "ssl",
	"shortguiro",       "guis",  "longguiro",    "guil",  "guiro",        "gui",   "cabasa",        "cab",   "maracas",       "mar",
	"shortwhistle",     "whs",   "longwhistle",  "whl",
	"handclap",         "hc",    "tambourine",   "tamb",  "vibraslap",    "vibs",  "tamtam",        "tt",
	"claves",           "cl",    "hiwoodblock",  "wbh",   "lowoodblock",  "wbl",
	"mutecuica",        "cuim",  "opencuica",    "cuio",  "mutetriangle", "trim",  "triangle",      "tri",   "opentriangle",  "trio",
	"oneup",            "ua",    "twoup",        "ub",    "threeup",      "uc",    "fourup",        "ud",    "fiveup",        "ue",
	"onedown",          "da",    "twodown",      "db",    "threedown",    "dc",    "fourdown",      "dd",    "fivedown",      "de",
]

def highlight():
	def commands(name, words, **kwargs):
		syn_match(name, r"\V\\\({}\)\>".format(r"\|".join(words)), **kwargs)

	def mode(name, start, contains, mode_top=False, **kwargs):
		syn_match(name, r"\v\\{}\s*".format(start), nextgroup=name+"Body", **kwargs)
		syn_cluster(name, contains + [name+"Body"])
		syn_region(name+"Body", "{", "}", contains="@"+name, contained=not mode_top)
		syn_region(name+"Body", "<<", ">>", contains="@"+name, contained=not mode_top)

	def kw(kwargs):
		for k, v in kwargs.items():
			if v is True: yield k
			elif v is False: pass
			else: yield f"{k}={v}"

	def syn_cluster(name, vals, **kwargs):
		print("syn", "cluster", name, f"contains={','.join(vals)}", *kw(kwargs))

	def syn_match(name, regex, **kwargs):
		print("syn", "match", name, f"&{regex}&", *kw(kwargs))

	def syn_region(name, start, end, *, matchgroup=None, matchgroup2=None, **kwargs):
		def mg(b):
			return [f"matchgroup={b}"] if b else []
		mg1 = matchgroup or matchgroup2
		mg2 = matchgroup2 or matchgroup
		print("syn", "region", name, *mg(mg1), f"start=&{start}&", *mg(mg2), f"end=&{end}&", *kw(kwargs))

	def syn_keyword(name, words, **kwargs):
		print("syn", "keyword", name, " ".join(words), *kw(kwargs))

	syn_match("lilyCustomFunction", r"\\\w\+")
	commands("lilyBuiltin", ly.words.lilypond_keywords)
	commands("lilyMusicCommand", w)
	commands("lilyArticulation", ly.words.articulations)
	syn_match("lilyArticulation", r'\v[\-\^_]([\^+\-!>._]|"@=)')
	commands("lilyOrnament", ly.words.ornaments)
	commands("lilyFermata", ly.words.fermatas)
	commands("lilyInstrumentScript", ly.words.instrument_scripts)
	commands("lilyRepeat", ly.words.repeat_scripts)
	commands("lilyAncient", ly.words.ancient_scripts)
	commands("lilyScale", ly.words.modes)
	syn_match("lilySymbol", r"[|[\]~()]")
	syn_match("lilySymbol", r"\\[!()><[\]!\\]")

	syn_match("lilyNumber", r"\v-?\d+([./]\d+)?")
	noteLength = r"\v\d@<!\s*\zs(128|64|32|16|8|4|2|1|\\breve|\\longa|\\maxima)\.*\d@!"
	syn_match("lilyDuration", noteLength, nextgroup="lilyDurationMul")
	syn_match("lilyRDuration", noteLength, nextgroup="lilyDurationMul", contained=True)
	syn_match("lilyDurationMul", r"\v\s*\*\s*\d+(/\d+)?", nextgroup="lilyDurationMul", contained=True)
	syn_match("lilyNumber", r"\v\d+/\d+")
	syn_region("lilyString", '"', '"', contains="@Spell")
	syn_region("lilyComment", "%{", "%}")
	syn_region("lilyComment", r"%{\@!", "$")

	syn_cluster("lilyFunction", [
		"lilyCustomFunction",
		"lilyBuiltin", "lilyMusicCommand", "lilyArticulation",
		"lilyOrnament", "lilyFermata", "lilyInstrumentScript",
		"lilyRepeat", "lilyAncient", "lilyScales", "lilyMidiInstrument",
		"lilyRepeatType", "lilyAccidentalStyle", "lilyClef",
	])
	syn_cluster("lilyMode", [
		"lilyNotemode", "lilyLyricmode", "lilyChordmode",
		"lilyDrummode", "lilyFiguremode",
	])
	syn_cluster("lilyGlobal", [
		"lilyDuration", "lilyNumber", "lilyString",
		"lilyComment", "lilyScheme", "@lilyFunction",
		"lilyMarkup", "lilySymbol",
	])

	commands("lilyMarkupFunction", ly.words.markupcommands + ly.words.markuplistcommands, contained=True)
	mode("lilyMarkup", r"markup", [
		"@lilyGlobal", "lilyMarkupFunction"
	])

	syn_match("lilyPitch", r"\v"
		r"\a@<!%([a-g]%(%(es)?%(e[hs])?|%(is)?%(i[hs])?)|[ae]s%(es)?)\a@!" # Pitch
		r"%(%(\s*')+|%(\s*,)+|)" # Octave
		r"%(\s*!)*%(\s*\?)*") # Modifiers
	syn_match("lilyError", r"\v[!?,']")
	syn_match("lilyRest", r"\v\a@<![rRs]\a@!", nextgroup="lilyRDuration")
	syn_region("lilyChord", r"<\@<!<<\@!", ">", contains="lilyPitch,@lilyFunction,lilyScheme,lilyError")
	syn_match("lilyChordRepeat", r"\v\a@<!q\a@!")
	mode("lilyNotemode", r"notemode", ["TOP"], mode_top=True)

	syn_match("lilyLyric", r"\w\+", contained=True)
	syn_match("lilyLyricHyphen", r"\a\@<!--\w\@!", contained=True)
	syn_match("lilyLyricExtender", r"\a\@<!__\w\@!", contained=True)
	mode("lilyLyricmode", "lyric(mode|s)", [ "@lilyGlobal", "@lilyMode", "lilyLyric", "lilyLyricHyphen", "lilyLyricExtender" ])

	syn_match("lilyChordname", r"", contained=True)
	mode("lilyChordmode", "chord(mode|s)", [ "@lilyGlobal", "@lilyMode", "lilyChordname", "lilyRest" ])

	syn_match("lilyDrum", r"\v\a@<!(%s)\a@!" % "|".join(ly.words.drums), contained=True)
	mode("lilyDrummode", r"drum(mode|s)", [ "@lilyGlobal", "@lilyMode", "lilyDrum", "lilyRest" ])

	syn_match("lilyFigure", r"", contained=True)
	mode("lilyFiguremode", r"figure(mode|s)", [ "@lilyGlobal", "@lilyMode", "lilyFigure", "lilyRest" ])

	syn_match("lilyVar", r"\v[a-zA-Z-]+\ze\s*\=", contained=True)
	mode("lilyHeader", r"header", [ "@lilyGlobal", "lilyVar" ])
	mode("lilyPaper", r"paper", [ "@lilyGlobal", "lilyVar" ])
	mode("lilyLayout", r"layout", [ "@lilyGlobal", "lilyVar", "lilyContextMod" ])
	mode("lilyMidi", r"midi", [ "@lilyGlobal", "lilyVar", "lilyContextMod" ])
	mode("lilyContextMod", r"context", [ "@lilyGlobal" ], contained=True)
	mode("lilyWith", r"with", [ "@lilyGlobal", "lilyVar" ])

	print("syn include syntax/scheme.vim")
	print("unlet b:current_syntax")
	syn_cluster("_schemeRoot", [
		"schemeBoolean", "schemeCharacter", "schemeComment",
		"schemeConstant", "schemeDelimiter", "schemeError", "schemeNumber",
		"schemeOther", "_schemeQuote", "schemeString", "_schemeLily"
	])
	syn_cluster("_schemeAll", [
		"@_schemeRoot", "_schemeStruc", "schemeFunc", "schemeSyntax"
	])
	syn_cluster("_schemeQuoted", [
		"@_schemeRoot", "_schemeQuoted", "_schemeUnquote"
	])
	syn_match("_schemeQuote", r"['`]\s*", nextgroup="@_schemeQuoted", contained=True)
	syn_match("_schemeUnquote", r",@\?\s*", nextgroup="@_schemeAll", contained=True)
	syn_region("_schemeQuoted", "(", ")", matchgroup="Delimiter", contains="@_schemeQuoted", contained=True)
	syn_region("_schemeQuoted", "#(", ")", matchgroup="Delimiter", contains="@_schemeQuoted", contained=True)
	syn_region("_schemeStruc", "(", ")", matchgroup="Delimiter", contains="@_schemeAll", contained=True)
	syn_region("_schemeStruc", "#(", ")", matchgroup="Delimiter", contains="@_schemeQuoted", contained=True)
	syn_region("_schemeLily", "#{", "#}", matchgroup="_schemeLilyStart", contains="@lilyNotemode", contained=True)
	syn_match("lilyScheme", "[#$]@\\?", nextgroup="@_schemeAll")
if __name__ == "__main__":
	highlight()
