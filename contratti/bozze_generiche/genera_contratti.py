"""Build a client copy of the contract.

usage: python3 build.py base_dir out.docx spec1.json [spec2.json ...]
spec json: {"set": {"<idx>": "text" | null},
            "after": {"<idx>": ["text" | {"text": "...", "like": <idx>}, ...]},
            "shift_refs": {"from": 7, "by": 1}}
Article references ("art. N", "artt. N e M", "Article(s) N") from `from` upward are shifted by `by`
after all edits; write references in the base numbering. "§" marks a number that must not shift.
Indices are the paragraph indices printed by dump.py on the base document.
Later specs override earlier ones. null deletes the paragraph. '\t' becomes a tab.
"""
import json, re, shutil, subprocess, sys, os, tempfile
from xml.sax.saxutils import escape

base, out, specs = sys.argv[1], sys.argv[2], sys.argv[3:]
sets, after, shift = {}, {}, None
for s in specs:
    d = json.load(open(s, encoding='utf-8'))
    sets.update({int(k): v for k, v in d.get('set', {}).items()})
    after.update({int(k): v for k, v in d.get('after', {}).items()})
    shift = d.get('shift_refs', shift)

xml = open(os.path.join(base, 'word/document.xml'), encoding='utf-8').read()
P = re.compile(r'<w:p(?:\s[^>]*)?>.*?</w:p>|<w:p(?:\s[^>]*)?/>', re.S)
RUN = re.compile(r'<w:r(?:\s[^>]*)?>.*?</w:r>', re.S)
HAS_TEXT = re.compile(r'<w:t(?:\s[^>]*)?>|<w:tab/>')

def runs_xml(text):
    parts = text.split('\t')
    s = ''
    for i, part in enumerate(parts):
        if i: s += '<w:tab/>'
        if part: s += '<w:t xml:space="preserve">%s</w:t>' % escape(part)
    return s

def set_text(p, text):
    runs = [m for m in RUN.finditer(p) if HAS_TEXT.search(m.group(0))]
    assert runs, 'paragraph without text'
    first = runs[0].group(0)
    m = re.match(r'(<w:r(?:\s[^>]*)?>)(<w:rPr>.*?</w:rPr>)?', first, re.S)
    new_first = m.group(1) + (m.group(2) or '') + runs_xml(text) + '</w:r>'
    res, last = [], 0
    for i, r in enumerate(runs):
        res.append(p[last:r.start()])
        res.append(new_first if i == 0 else '')
        last = r.end()
    res.append(p[last:])
    return ''.join(res)

REF = re.compile(r'((?:\bartt?\.|\bArticles?)\s*)(\d+(?:(?:,\s*|\s+e\s+|\s+and\s+)\d+)*)(?!\s+(?:del|of the)\s+GDPR)')
T = re.compile(r'(<w:t(?:\s[^>]*)?>)([^<]*)(</w:t>)')

def plain(p):
    return ''.join(m.group(2) for m in T.finditer(p))

def shift_refs(p):
    if not shift or '<w:t' not in p:
        return p.replace('§', '')
    def fix(m):
        nums = re.sub(r'\d+', lambda n: str(int(n.group(0)) + shift['by']) if shift['from'] <= int(n.group(0)) <= 99 else n.group(0), m.group(2))
        return m.group(1) + nums
    old = plain(p)
    new = REF.sub(fix, old).replace('§', '')
    return p if new == old else set_text(p, new.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&'))

paras = list(P.finditer(xml))
out_parts, last = [], 0
for i, m in enumerate(paras):
    out_parts.append(xml[last:m.start()])
    p = m.group(0)
    if i in sets:
        p = '' if sets[i] is None else set_text(p, sets[i])
    out_parts.append(shift_refs(p))
    for t in after.get(i, []):
        like = paras[t['like']].group(0) if isinstance(t, dict) else m.group(0)
        out_parts.append(shift_refs(set_text(like, t['text'] if isinstance(t, dict) else t)))
    last = m.end()
out_parts.append(xml[last:])

tmp = tempfile.mkdtemp()
shutil.copytree(base, tmp, dirs_exist_ok=True)
open(os.path.join(tmp, 'word/document.xml'), 'w', encoding='utf-8').write(''.join(out_parts))
if os.path.exists(out): os.remove(out)
subprocess.check_call(['zip', '-Xqr', os.path.abspath(out), '.'], cwd=tmp)
shutil.rmtree(tmp)
