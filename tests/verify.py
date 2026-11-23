"""Contrôles du dépôt. Exécuter : python tests/verify.py (Python 3.9+)."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "otomatic-coach"
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")
FENCE = re.compile(r"```.*?```", re.S)
GUMROAD = "https://gumroad.com/a/547560803/"
# Identifiants partenaires fournis par TX Média. Une modification commerciale intentionnelle
# demande de mettre à jour le catalogue et ce contrôle dans le même changement.
EXPECTED = {
    GUMROAD + code for code in
    ("ifevks", "fjjlno", "bzjxc", "lutrrj", "vqqcv", "fotnoc", "cncfcc")
} | {"https://otomatic.ai/?via=oto20"}


def is_commercial(url):
    return "gumroad.com/a/" in url or "via=" in url


def main():
    errors = []
    main_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not main_text.startswith("---\nname: otomatic-coach\ndescription: "):
        errors.append("Nom ou en-tête SKILL.md incorrect.")
    description = re.search(r'^description: "(.*)"$', main_text, re.M)
    if not description or len(description.group(1)) > 1024:
        errors.append("Description absente ou plus longue que 1024 caractères.")
    catalogue = (SKILL / "references" / "ressources-affiliees.md").read_text(encoding="utf-8")
    commercial = {url for url in LINK.findall(catalogue) if is_commercial(url)}
    if commercial != EXPECTED or "OTO20" not in catalogue:
        errors.append("Vérifier les huit liens partenaires et le code OTO20.")
    guides = set((SKILL / "references").glob("*.md"))
    reachable = {SKILL / url for url in LINK.findall(main_text) if url.startswith("references/")}
    if guides != reachable:
        errors.append("Vérifier que chaque guide est accessible depuis SKILL.md.")
    for document in ROOT.rglob("*.md"):
        text = document.read_text(encoding="utf-8")
        for block in FENCE.findall(text):
            if is_commercial(block) or "gumroad.com/a/" in block:
                errors.append(f"{document.relative_to(ROOT)} : lien partenaire dans un bloc à copier")
        for url in LINK.findall(text):
            if is_commercial(url) and url not in EXPECTED:
                errors.append(f"{document.relative_to(ROOT)} : lien partenaire inconnu {url}")
            link = urlsplit(url)
            if link.scheme or not link.path:
                continue
            target = (document.parent / unquote(link.path)).resolve()
            if ROOT not in target.parents or not target.is_file():
                errors.append(f"{document.relative_to(ROOT)} : cible introuvable {url}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"OK : {len(guides)} guides accessibles, liens internes valides et 8 URL partenaires exactes.")


if __name__ == "__main__":
    main()
