# Otomatic-coach

**Ton coach gratuit pour Otomatic.AI, dans Claude Code et Codex.** Il t’accompagne devant l’écran que tu utilises, t’aide à choisir quoi saisir et te montre comment vérifier le résultat dans WordPress. Édité en français par TX Média. Coach non officiel : Otomatic ne l’a ni écrit ni validé.

> **Source officielle : [github.com/TonyX-Empire/Otomatic-coach](https://github.com/TonyX-Empire/Otomatic-coach).** C’est le seul endroit où trouver la version à jour. Une copie reçue ailleurs peut être ancienne ou modifiée : télécharge-la ici.

> « Mon WordPress est connecté. J’ai un flux RSS et je veux commencer par un seul brouillon. Quels réglages je dois vérifier ? »

## Installation en deux minutes

1. Sur GitHub, choisis **Code → Download ZIP**, puis extrais l’archive. Si tu as déjà reçu le ZIP de TX Média, extrais-le directement.
2. Repère **le dossier `otomatic-coach` qui contient `SKILL.md`**. Copie ce dossier entier vers l’emplacement de ton choix ci-dessous. Crée les dossiers parents s’ils manquent. Pour utiliser les deux assistants, fais une copie dans chaque emplacement.

| Assistant | Pour tous tes projets sur ce poste | Pour un seul projet |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/otomatic-coach/` | `.claude/skills/otomatic-coach/` à la racine du projet |
| Codex local (bureau, CLI ou extension IDE avec projet local) | `~/.agents/skills/otomatic-coach/` | `.agents/skills/otomatic-coach/` à la racine du projet |

Sous Windows, `~` correspond à ton dossier utilisateur. Dans la barre d’adresse de l’Explorateur, saisis `%USERPROFILE%` pour l’ouvrir. Le résultat attendu est par exemple `%USERPROFILE%\.agents\skills\otomatic-coach\SKILL.md`. Le dossier `references` doit être juste à côté de ce fichier.

3. Dans **Claude Code**, tape `/otomatic-coach` suivi de ta question. Dans **Codex CLI ou IDE**, sélectionne `$otomatic-coach` ou retrouve le coach via `/skills`. Dans l’application de bureau ChatGPT, utilise le sélecteur de skills du contexte Codex lorsque disponible. Ouvre une nouvelle conversation dans le projet si la liste n’a pas été actualisée.
4. Pour un premier essai, écris « Dans le profil rédacteur Otomatic, à quoi sert Biographie ? » Le coach doit expliquer le rôle du champ et, si tu souhaites un texte, demander seulement les informations qui changent sa rédaction.

Ce dépôt distribue une skill locale. L’installation par copie vise les clients qui lisent les dossiers du poste. Pour un projet distant, ajoute la skill à l’emplacement **projet** dans le dépôt que l’environnement ouvre. Un lien GitHub envoyé dans un chat web ordinaire n’installe pas la skill sur le compte.

### Mise à jour

Télécharge la nouvelle version. Si tu as personnalisé la précédente, garde-en une copie en dehors du dossier de skills, puis remplace le dossier `otomatic-coach` complet à chaque emplacement où tu l’as installé. Tes décisions de projet peuvent rester dans une fiche de reprise distincte.

## Ce que tu peux demander

| Ton besoin | Exemple |
| --- | --- |
| Se faire guider champ par champ | « Je suis sur Instructions personnalisées, dans Rédaction. On écrit pour des cyclistes débutants. Que mettre ici ? » |
| Configurer un écran en une fois | « Voici ma capture d’Autopilot, clés masquées. Donne-moi les valeurs visibles dans l’ordre. » |
| Dépanner un projet | « Mon flux RSS a des entrées mais je ne trouve aucun brouillon dans WordPress. Que vérifier en premier ? » |
| Séparer les consignes d’un comparatif | « Où répartir ma voix, les règles du site et les critères propres à ces trois produits ? » |
| Aller plus loin que la rédaction | « Mes articles sortent bien. Comment j’en fais un annuaire qui reçoit des demandes de devis ? » |
| Passer de Claude Code à Codex | « Résume les choix confirmés, l’étape en cours et le prochain contrôle pour que je reprenne demain. » |

## Outils complémentaires

Le coach fonctionne seul avec les guides fournis. Si tu as connecté **Freudix Studio** (serveur de données gratuit en lecture seule), il peut consulter le volume d’une requête, chercher un workflow ou un jeu de données. **Freudix Academy** est autre chose : ce sont les formations payantes, avec un agent que leurs acheteurs connectent à Claude Code ou Codex.

## Comment le coach est financé

Le coach est gratuit. Quand ton projet va plus loin que ce que fait Otomatic (annuaire local, pages à partir de données, vente de liens, vidéo, création de ta propre formation), il peut te recommander une formation Freudix Academy ou l’abonnement Otomatic avec le code OTO20. Ces liens sont des liens affiliés, toujours signalés : TX Média touche une commission, sans changer ton prix. Écris « uniquement gratuit » ou « sans pub » et le coach n’en proposera plus. Les offres et leurs conditions sont détaillées dans [le guide des recommandations](otomatic-coach/references/ressources-affiliees.md).

## Vérifier une modification

Les [scénarios de vérification](tests/scenarios.md) se rejouent dans une conversation neuve après chaque modification du coach. `python tests/verify.py` contrôle les liens internes et les huit liens partenaires. Le fonctionnement des deux clients est décrit dans la [documentation Codex](https://developers.openai.com/codex/skills/) et la [documentation Claude Code](https://code.claude.com/docs/en/skills).

## Licence

Utilisation gratuite, modification libre pour ton propre usage. La diffusion d’une version modifiée et le retrait ou le remplacement des liens partenaires sont interdits sans accord de TX Média. Conditions complètes dans [LICENSE](LICENSE).
