#!/usr/bin/env python3
"""Convert Unicode math notation to LaTeX in all markdown files."""

import re
import os
import glob

def convert_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Split into YAML frontmatter and body
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[0] + '---' + parts[1] + '---'
        body = parts[2]
    else:
        frontmatter = ''
        body = content

    # Don't convert inside code blocks
    code_blocks = []
    def save_code(m):
        code_blocks.append(m.group(0))
        return f'__CODE_BLOCK_{len(code_blocks)-1}__'

    body = re.sub(r'```[\s\S]*?```', save_code, body)

    # Track already-converted LaTeX spans to avoid double-conversion
    latex_spans = []
    def save_latex(m):
        latex_spans.append(m.group(0))
        return f'__LATEX_{len(latex_spans)-1}__'

    # Save existing LaTeX (both $$ and $)
    body = re.sub(r'\$\$[\s\S]*?\$\$', save_latex, body)
    body = re.sub(r'\$[^\$\n]+?\$', save_latex, body)

    # === CONVERSION RULES ===

    # QED symbol
    body = body.replace(' ∎', ' $\\blacksquare$')
    body = body.replace('\n∎', '\n$\\blacksquare$')

    # Standalone Greek with context - full expressions first

    # Common compound expressions (order matters - longer patterns first)

    # "Σ = 0"
    body = re.sub(r'(?<!\$)Σ\s*=\s*0(?!\$)', r'$\\Sigma = 0$', body)
    # Lone Σ in math context
    body = re.sub(r'(?<![a-zA-Z\$])Σ(?![a-zA-Z\$])', r'$\\Sigma$', body)

    # ∃ (existence)
    body = re.sub(r'(?<!\$)∃(?!\$)', r'$\\exists$', body)

    # ∞
    body = re.sub(r'(?<!\$)∞(?!\$)', r'$\\infty$', body)

    # Convert "φ-strand", "ψ-strand", "φ-triangle", "ψ-triangle" patterns
    body = re.sub(r'(?<!\$)φ-strand', r'$\\varphi$-strand', body)
    body = re.sub(r'(?<!\$)ψ-strand', r'$\\psi$-strand', body)
    body = re.sub(r'(?<!\$)φ-triangle', r'$\\varphi$-triangle', body)
    body = re.sub(r'(?<!\$)ψ-triangle', r'$\\psi$-triangle', body)
    body = re.sub(r'(?<!\$)φ-spiral', r'$\\varphi$-spiral', body)
    body = re.sub(r'(?<!\$)ψ-spiral', r'$\\psi$-spiral', body)
    body = re.sub(r'(?<!\$)φ-lobe', r'$\\varphi$-lobe', body)
    body = re.sub(r'(?<!\$)ψ-lobe', r'$\\psi$-lobe', body)

    # Powers of phi with unicode superscripts
    superscript_map = {
        '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
        '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
        '⁻': '-', '⁺': '+'
    }

    def convert_superscript(match):
        base = match.group(1)
        sups = match.group(2)
        # Convert unicode superscripts to regular chars
        exp = ''
        for c in sups:
            exp += superscript_map.get(c, c)
        # Map base to LaTeX
        base_map = {
            'φ': '\\varphi', 'ψ': '\\psi', 'α': '\\alpha',
            'x': 'x', 'r': 'r', 'n': 'n', 'a': 'a', 'b': 'b',
            'c': 'c', 'e': 'e', 'i': 'i', 'p': 'p', 'z': 'z',
            'A': 'A', 'σ': '\\sigma',
        }
        latex_base = base_map.get(base, base)
        if len(exp) > 1:
            return f'${latex_base}^{{{exp}}}$'
        else:
            return f'${latex_base}^{exp}$'

    sup_chars = '[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+'
    body = re.sub(r'(?<!\$)([φψαxrnabceipzAσ])(' + sup_chars + r')(?!\$)', convert_superscript, body)

    # S¹, S², S³, T² (topological spaces)
    body = re.sub(r'(?<!\$)S¹', r'$S^1$', body)
    body = re.sub(r'(?<!\$)S²', r'$S^2$', body)
    body = re.sub(r'(?<!\$)S³', r'$S^3$', body)
    body = re.sub(r'(?<!\$)T²', r'$T^2$', body)

    # Subscript characters
    body = re.sub(r'(?<!\$)mₑ(?!\$)', r'$m_e$', body)
    body = re.sub(r'(?<!\$)m₁(?!\$)', r'$m_1$', body)
    body = re.sub(r'(?<!\$)m₂(?!\$)', r'$m_2$', body)
    body = re.sub(r'(?<!\$)s_A(?!\$)', r'$s_A$', body)
    body = re.sub(r'(?<!\$)s_B(?!\$)', r'$s_B$', body)
    body = re.sub(r'(?<!\$)d₁(?!\$)', r'$d_1$', body)
    body = re.sub(r'(?<!\$)d₂(?!\$)', r'$d_2$', body)
    body = re.sub(r'(?<!\$)r₁(?!\$)', r'$r_1$', body)
    body = re.sub(r'(?<!\$)r₂(?!\$)', r'$r_2$', body)
    body = re.sub(r'(?<!\$)p₁(?!\$)', r'$p_1$', body)
    body = re.sub(r'(?<!\$)p₂(?!\$)', r'$p_2$', body)
    body = re.sub(r'(?<!\$)q₁(?!\$)', r'$q_1$', body)
    body = re.sub(r'(?<!\$)q₂(?!\$)', r'$q_2$', body)
    body = re.sub(r'(?<!\$)x₁(?!\$)', r'$x_1$', body)
    body = re.sub(r'(?<!\$)x₂(?!\$)', r'$x_2$', body)
    body = re.sub(r'(?<!\$)ω_b(?!\$)', r'$\\omega_b$', body)
    body = re.sub(r'(?<!\$)ω_d(?!\$)', r'$\\omega_d$', body)

    # sqrt symbol
    body = re.sub(r'√5', r'$\\sqrt{5}$', body)
    body = re.sub(r'√φ', r'$\\sqrt{\\varphi}$', body)
    body = re.sub(r'√\(([^)]+)\)', lambda m: f'$\\sqrt{{{m.group(1)}}}$', body)
    body = re.sub(r'√(\d+)', lambda m: f'$\\sqrt{{{m.group(1)}}}$', body)

    # Standalone Greek letters (not already in LaTeX, not in compound words)
    # Must be careful not to convert in headings, YAML, etc.

    # φ alone (not in φ-strand which was already handled, not in words)
    body = re.sub(r'(?<![a-zA-Z\$\\])φ(?![a-zA-Z\$-])', r'$\\varphi$', body)
    # ψ alone
    body = re.sub(r'(?<![a-zA-Z\$\\])ψ(?![a-zA-Z\$-])', r'$\\psi$', body)
    # α alone (not in alpha)
    body = re.sub(r'(?<![a-zA-Z\$\\])α(?![a-zA-Z\$_])', r'$\\alpha$', body)
    # η alone
    body = re.sub(r'(?<![a-zA-Z\$\\])η(?![a-zA-Z\$])', r'$\\eta$', body)
    # σ alone (careful - used as breath phase)
    body = re.sub(r'(?<![a-zA-Z\$\\])σ(?![a-zA-Z\$_])', r'$\\sigma$', body)
    # θ alone
    body = re.sub(r'(?<![a-zA-Z\$\\])θ(?![a-zA-Z\$_])', r'$\\theta$', body)
    # τ alone (but not in "tau")
    body = re.sub(r'(?<![a-zA-Z\$\\])τ(?![a-zA-Z\$])', r'$\\tau$', body)
    # λ alone
    body = re.sub(r'(?<![a-zA-Z\$\\])λ(?![a-zA-Z\$])', r'$\\lambda$', body)
    # ω alone
    body = re.sub(r'(?<![a-zA-Z\$\\])ω(?![a-zA-Z\$_])', r'$\\omega$', body)
    # ν alone
    body = re.sub(r'(?<![a-zA-Z\$\\])ν(?![a-zA-Z\$])', r'$\\nu$', body)
    # δ alone
    body = re.sub(r'(?<![a-zA-Z\$\\])δ(?![a-zA-Z\$])', r'$\\delta$', body)
    # Δ alone
    body = re.sub(r'(?<![a-zA-Z\$\\])Δ(?![a-zA-Z\$])', r'$\\Delta$', body)
    # μ alone (not in "mu" or units)
    body = re.sub(r'(?<![a-zA-Z\$\\])μ(?![a-zA-Z\$])', r'$\\mu$', body)
    # Λ alone
    body = re.sub(r'(?<![a-zA-Z\$\\])Λ(?![a-zA-Z\$])', r'$\\Lambda$', body)

    # π - only when it's the math constant, not in words
    body = re.sub(r'(?<![a-zA-Z\$\\])π(?![a-zA-Z\$])', r'$\\pi$', body)

    # Math operators
    body = body.replace(' ≈ ', ' $\\approx$ ')
    body = body.replace(' ≠ ', ' $\\neq$ ')
    body = body.replace(' ≥ ', ' $\\geq$ ')
    body = body.replace(' ≤ ', ' $\\leq$ ')
    body = body.replace(' ∈ ', ' $\\in$ ')
    body = body.replace(' ⊂ ', ' $\\subset$ ')
    body = body.replace(' ± ', ' $\\pm$ ')
    body = re.sub(r'(?<!\|) × (?!\|)', r' $\\times$ ', body)

    # ℏ
    body = body.replace('ℏ', '$\\hbar$')

    # ℝ
    body = body.replace('ℝ', '$\\mathbb{R}$')
    # ℤ
    body = body.replace('ℤ', '$\\mathbb{Z}$')

    # Clean up double-dollar adjacencies: $...$$ ...$  →  merge
    # Fix $\varphi$$^2$ type artifacts by merging adjacent LaTeX spans
    body = re.sub(r'\$\$(?!\$)', '$', body)  # Be careful - don't break display math

    # Actually, let's be more careful. Fix adjacent $...$ $...$ that should be one span
    # Pattern: $X$ $Y$ where there's no text between → $X Y$
    # This is tricky, skip for now

    # Restore LaTeX spans
    for i, span in enumerate(latex_spans):
        body = body.replace(f'__LATEX_{i}__', span)

    # Restore code blocks
    for i, block in enumerate(code_blocks):
        body = body.replace(f'__CODE_BLOCK_{i}__', block)

    # Clean up any double-wrapped LaTeX: $$\varphi$$ → $\varphi$
    # (but preserve actual display math $$...$$)

    result = frontmatter + body

    with open(filepath, 'w') as f:
        f.write(result)

    return filepath

# Find all markdown files
md_files = []
for root, dirs, files in os.walk('/home/ncwardell/WorkBench/Phi-Mathematics'):
    # Skip _old directory and .git
    if '_old' in root or '.git' in root or '.claude' in root:
        continue
    for f in files:
        if f.endswith('.md'):
            md_files.append(os.path.join(root, f))

md_files.sort()
print(f"Processing {len(md_files)} files...")

for fp in md_files:
    try:
        convert_file(fp)
        print(f"  ✓ {os.path.relpath(fp, '/home/ncwardell/WorkBench/Phi-Mathematics')}")
    except Exception as e:
        print(f"  ✗ {os.path.relpath(fp, '/home/ncwardell/WorkBench/Phi-Mathematics')}: {e}")

print("Done!")
