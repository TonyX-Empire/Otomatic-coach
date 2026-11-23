# Automatic Coach

**Ton coach gratuit pour Otomatic.AI, dans Claude Code et Codex.** Il t’accompagne devant l’écran que tu utilises, t’aide à choisir quoi saisir et te montre comment vérifier le résultat dans WordPress. Édité en français par TX Média.

> « Mon WordPress est connecté. J’ai un flux RSS et je veux commencer par un seul brouillon. Quels réglages je dois vérifier ? »

## Installation en deux minutes

1. Sur GitHub, choisis **Code → Download ZIP**, puis extrais l’archive. Si tu as déjà reçu le ZIP de TX Média, extrais-le directement.
2. Repère **le dossier `automatic-coach` qui contient `SKILL.md`**. Copie ce dossier entier vers l’emplacement de ton choix ci-dessous. Crée les dossiers parents s’ils manquent. Pour utiliser les deux assistants, fais une copie dans chaque emplacement.

| Assistant | Pour tous tes projets sur ce poste | Pour un seul projet |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/automatic-coach/` | `.claude/skills/automatic-coach/` à la racine du projet |
| Codex local (bureau, CLI ou extension IDE avec projet local) | `~/.agents/skills/automatic-coach/` | `.agents/skills/automatic-coach/` à la racine du projet |

Sous Windows, `~` correspond à ton dossier utilisateur. Dans la barre d’adresse de l’Explorateur, saisis `%USERPROFILE%` pour l’ouvrir. Le résultat attendu est par exemple `%USERPROFILE%\.agents\skills\automatic-coach\SKILL.md`. Le dossier `references` doit être juste à côté de ce fichier.

3. Dans **Claude Code**, tape `/automatic-coach` suivi de ta question. Dans **Codex CLI ou IDE**, sélectionne `$automatic-coach` ou retrouve le coach via `/skills`. Dans l’application de bureau ChatGPT, utilise le sélecteur de skills du contexte Codex lorsque disponible. Ouvre une nouvelle conversation dans le projet si la liste n’a pas été actualisée.
4. Pour un premier essai, écris « Dans le profil rédacteur Otomatic, à quoi sert Biographie ? » Le coach doit expliquer le rôle du champ et, si tu souhaites un texte, demander seulement les informations qui changent sa rédaction.

Ce dépôt distribue une skill locale. L’installation par copie vise les clients qui lisent les dossiers du poste. Pour un projet distant, ajoute la skill à l’emplacement **projet** dans le dépôt que l’environnement ouvre. Un lien GitHub envoyé dans un chat web ordinaire n’installe pas la skill sur le compte.

### Mise à jour

Télécharge la nouvelle version. Si tu as personnalisé la précédente, garde-en une copie en dehors du dossier de skills, puis remplace le dossier `automatic-coach` complet à chaque emplacement où tu l’as installé. Tes décisions de projet peuvent rester dans une fiche de reprise distincte.

## Ce que tu peux demander

| Ton besoin | Exemple |
| --- | --- |
| Se faire guider champ par champ | « Je suis sur Instructions personnalisées, dans Rédaction. On écrit pour des cyclistes débutants. Que mettre ici ? » |
| Configurer un écran en une fois | « Voici ma capture d’Autopilot, clés masquées. Donne-moi les valeurs visibles dans l’ordre. » |
| Dépanner un projet | « Mon flux RSS a des entrées mais je ne trouve aucun brouillon dans WordPress. Que vérifier en premier ? » |
| Séparer les consignes d’un comparatif | « Où répartir ma voix, les règles du site et les critères propres à ces trois produits ? » |
| Passer de Claude Code à Codex | « Résume les choix confirmés, l’étape en cours et le prochain contrôle pour que je reprenne demain. » |

**Les outils complémentaires sont facultatifs.** Le coach fonctionne avec les guides fournis. Avec Freudix Studio connecté, il peut consulter une requête SEO ou chercher un workflow. Avec l’accès personnel d’un membre de la Wizards Academy, il peut demander à Albus une leçon ou une méthode. Chacun utilise ses propres connexions.

**Comment le coach est financé.** Certains conseils incluent un lien affilié identifié. TX Média peut percevoir une commission. Tu peux demander un accompagnement exclusivement gratuit ou sans recommandations commerciales. Le catalogue, les conditions du code OTO20 et les règles de sélection figurent dans [les ressources affiliées](automatic-coach/references/ressources-affiliees.md).

## Déposer cette version sur GitHub

Crée un dépôt vide, par exemple `automatic-coach`. Depuis le dépôt, utilise **Add file → Upload files** (ou **uploading an existing file** pour un dépôt vide), puis dépose le **contenu extrait** du dossier contenant ce README. À la racine de GitHub, tu dois voir `README.md`, `automatic-coach/` et `tests/`. Valide avec **Commit changes**. L’adresse de ce dépôt est celle à partager à ta communauté.

Les [scénarios de vérification](tests/scenarios.md) permettent de vérifier une modification du coach. Le fonctionnement de référence des deux clients est décrit dans la [documentation Codex](https://developers.openai.com/codex/skills/) et la [documentation Claude Code](https://code.claude.com/docs/en/skills).
