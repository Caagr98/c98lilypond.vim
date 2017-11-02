"""
import neovim
import ly.lex
import ly.colorize

@neovim.plugin
class LilyVim:
	def __init__(self, nvim: neovim.api.nvim.Nvim):
		# global HIGHLIGHT
		self.nvim = nvim

	@neovim.function("LilypondSyntaxUpdate", sync=False)
	def update(self, args):
		update(self.nvim)

	# rel2abs
	# abs2rel
	# transpose
	# rhythm_double
	# rhythm_halve
	# rhythm_explicit
	# rhythm_implicit
	# rhythm_implicit_per_line
	# indent

buffer_vars = []
class Vars:
	def __str__(self):
		return str(vars(self))

	def __init__(self, buf):
		self.parsedLines = []
		self.highlight = buf.add_highlight("", 0, src_id=0)

class ParsedLine:
	def __init__(self, lineno, text, prevState, tokens, nextState):
		self.number = lineno
		self.text = text
		self.prevState = prevState
		self.tokens = tokens
		self.nextState = nextState
nullLine = ParsedLine(None, None, None, None, ly.lex.state("lilypond").freeze())

def get_buf_vars(buf: neovim.api.buffer.Buffer):
	if "lily_vars" not in buf.vars:
		buf.vars["lily_vars"] = len(buffer_vars)
		buffer_vars.append(Vars(buf))
	return buffer_vars[buf.vars["lily_vars"]]

def updateLines(buf: neovim.api.buffer.Buffer, *, start=0, end=-1):
	vars = get_buf_vars(buf)
	for n, line in enumerate(buf[start:end]):
		if n == 0:
			prevState = nullLine.nextState
		else:
			prevState = vars.parsedLines[n-1].nextState
		if len(vars.parsedLines) < n + 1:
			vars.parsedLines.append(nullLine)

		if (vars.parsedLines[n].text, vars.parsedLines[n].prevState) == (line, prevState):
			continue
		state = ly.lex.State.thaw(prevState)
		tokens = list(state.tokens(line))
		vars.parsedLines[n] = ParsedLine(n, line, prevState, tokens, state.freeze())
		yield vars.highlight, vars.parsedLines[n]

def update(nvim: neovim.api.nvim.Nvim):
	buf = nvim.current.buffer
	win = nvim.current.window
	calls = []
	for hl, line in updateLines(buf, end=win.cursor[0] + win.height):
		calls.append(("nvim_buf_clear_highlight", [buf.number, hl, line.number, line.number+1]))
		buf.clear_highlight(hl, line.number, line.number+1, async=False)
		for token in line.tokens:
			t = type(token)
			if t not in styles:
				for t2 in t.__mro__:
					if t2 in styles:
						styles[t] = styles[t2]
						break
				else:
					styles[t] = None
			if styles[t]:
				calls.append(("nvim_buf_add_highlight", [buf.number, hl, "lily" + styles[t], line.number, token.pos, token.end]))
	nvim._session.request("nvim_call_atomic", calls)

from ly.lex import lilypond as l
from ly.lex import scheme as s
styles = {
	l.Keyword: "Keyword",
	l.Command: "Command",
	l.Skip: "Skip",
	l.Note: "Note",
	l.LyricSkip: "LyricSkip",
	l.Rest: "Rest",
	l.Spacer: "Spacer",
	l.DrumNote: "DrumNote",
	l.Octave: "Octave",
	l.Accidental: "Accidental",
	l.Duration: "Duration",
	l.Tie: "Tie",
	l.PipeSymbol: "PipeSymbol",
	l.OctaveCheck: "OctaveCheck",
	l.Articulation: "Articulation",
	l.Direction: "Direction",
	l.Dynamic: "Dynamic",
	l.Fingering: "Fingering",
	l.StringNumber: "StringNumber",
	l.Tremolo: "Tremolo",
	l.Slur: "Slur",
	l.Beam: "Beam",
	l.Chord: "Chord",
	l.ChordItem: "ChordItem",
	l.Q: "Q",
	l.Markup: "Markup",
	l.InputMode: "InputMode",
	l.LyricText: "LyricText",
	l.LyricHyphen: "LyricHyphen",
	l.LyricExtender: "LyricExtender",
	l.Specifier: "Specifier",
	l.UserCommand: "UserCommand",
	l.Delimiter: "Delimiter",
	l.ContextName: "ContextName",
	l.GrobName: "GrobName",
	l.ContextProperty: "ContextProperty",
	l.Variable: "Variable",
	l.UserVariable: "UserVariable",
	l.Value: "Value",
	l.String: "String",
	l.StringQuoteEscape: "StringEscape",
	l.Comment: "Comment",
	l.Error: "Error",
	l.SchemeStart: "Scheme",
	l.Translator: "Translator",

	s.LilyPond: "SLily",
	s.String: "SString",
	s.StringQuoteEscape: "SStringEscape",
	s.Comment: "SComment",
	s.Number: "SNumber",
	s.Keyword: "SKeyword",
	s.Function: "SFunction",
	s.Variable: "SVariable",
	s.Constant: "SConstant",
	s.OpenParen: "SDelimiter",
	s.CloseParen: "SDelimiter",
	s.Dot: "SDelimiter",
"""
