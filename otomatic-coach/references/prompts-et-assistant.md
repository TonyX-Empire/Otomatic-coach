# Le bon texte dans le bon champ

## Une même demande, quatre endroits différents

Exemple fictif d’un site jardinage qui prépare un comparatif de pots pour balcon. Ces textes sont prêts à coller dans les champs indiqués. Adapter les détails aux faits et au public de chaque projet.

**Profil du rédacteur → Rédaction → Instructions personnalisées**

```text
Tu écris pour des personnes qui jardinent sur un petit balcon. Vouvoie-les. Explique les termes techniques au premier emploi. Décris les gestes avec des verbes concrets. Distingue une observation documentée d’un conseil de culture.
```

**Réglages → Custom IA → domaine → Custom IA**

```text
Sur ce site, relie chaque conseil à une situation concrète. Pour une caractéristique produit ou un prix, utilise uniquement les informations des sources fournies. Si une donnée manque, indique « non renseigné ». Présente les liens commerciaux comme tels lorsqu’ils sont utilisés.
```

**Assistant de rédaction → Brief & Mots clés → Brief de génération**

```text
Aide un locataire à choisir entre une jardinière en terre cuite et une en plastique pour un balcon exposé au vent. Compare le poids à vide, le drainage et l’entretien à partir des fiches fournies. Insère un tableau si les données permettent la comparaison. Termine par deux cas de choix. Signale les données manquantes et évite d’attribuer une résistance au vent qui n’a pas été mesurée.
```

**Assistant → Options de contenu → Instructions personnalisées des images**, ou **Autopilot → Médias → Instructions personnalisées pour les images**

```text
Photographie réaliste de deux jardinières sans marque, l’une en terre cuite, l’autre en plastique, sur le même balcon. Lumière diffuse, cadrage horizontal à hauteur des pots. Les deux matériaux doivent être reconnaissables. Sans texte ajouté ni logo.
```

Pour automatiser cette série, guider ensuite vers la source, les titres et la cadence d’Autopilot. Un rythme de publication se choisit dans les contrôles de planification. Aucun de ces quatre textes ne configure le calendrier.

## Assistant de rédaction dans le SaaS

**Assistant de rédaction** dans la barre latérale ouvre le parcours dont le fil d’Ariane indique **Assistant IA**. Distinguer les parcours suivants.

- **Créer un nouveau document** ouvre le point de départ « Langue » et « Requête cible ». Exemple de requête : `jardinière terre cuite ou plastique pour balcon`. « Continuer » devient accessible quand la saisie convient. Donner une requête unique. Réserver le cahier des charges au brief.
- L’écran propose aussi **Contenu local**, **Contenu d’actualité**, **Contenu de marques**, **Comparatif de marques**, **Générer un guide**, **Comparateur Amazon**, **Fiche produit Amazon** et **Générez un simulateur**. Les premières saisies relevées pour ces parcours sont Langue et Requête cible. Ne pas promettre les mêmes étapes suivantes dans chaque modèle.
- **Nouveau document vierge** conduit directement à l’éditeur. Les libellés ci-dessous viennent de cet écran. Dans une branche avec requête, guider selon les sections effectivement affichées.

| Section ou champ | Quoi y mettre et comment choisir | Contrôle observable |
| --- | --- | --- |
| Sélecteurs texte et image | Choisir parmi les modèles ou sources affichés. Pour une première comparaison, changer un seul paramètre à la fois. | Le fournisseur choisi est disponible pour le compte et cohérent avec le média demandé. |
| Utiliser un template | Charger le jeu de réglages qui correspond au format récurrent. | Relire les options préremplies et le domaine avant de générer. |
| Domaine | Choisir le site de destination, sous-dossier compris. | Le domaine affiché correspond au site prévu. |
| Requête cible → Titre et Langue dans le document vierge | Donner un titre de travail qui traduit l’intention, par exemple « Terre cuite ou plastique : quelle jardinière pour un balcon ? ». Sélectionner la langue du texte final. | Ne pas confondre ce titre de travail, le champ de l’éditeur « Titre de votre article » et une balise title SEO. Relire chacun lorsqu’il apparaît. |
| Profil de rédaction → Nom, Âge, Métier, Style d’écriture, Instructions personnalisées | Reprendre l’identité approuvée et les consignes stables. Les options de cette section concernent la rédaction du document ouvert. | Comparer avec le profil de référence. Un réglage dans le document ne prouve pas la modification du profil enregistré pour le site. |
| Scraper → Intentions de recherche | À activer si l’analyse des résultats Google aide à préciser la demande. | Contrôler la pertinence des intentions relevées pour le pays, le public et l’article. |
| Scraping personnalisé → Ajouter des urls personnalisées | Fournir des pages sources précises et pertinentes. Pour une comparaison, préférer les fiches de référence des produits. | Ouvrir chaque URL et vérifier que ses données répondent aux critères retenus. Une source à analyser et un lien à insérer ont des rôles différents. |
| Brief & Mots clés → Brief de génération | Préciser objectif, lecteur, angle, sources, critères, plan imposé si nécessaire, livrable attendu. | Chaque demande est vérifiable à la relecture. Retirer les instructions sans rapport avec cet article. |
| Personnes / Entités | Entités dont la présence est réellement justifiée. Exemple pour un article agricole : un organisme consulté comme source. | Ne conserver que les entités utiles et correctement identifiées. |
| Mots clés récurrents | Vocabulaire pertinent si le sens le justifie, par exemple « drainage » et « soucoupe ». | Relire la fluidité et éviter une fréquence arbitraire. |
| Marques citées | Marques effectivement traitées ou présentes dans les sources. Laisser la liste vide pour un comparatif générique si l’écran l’autorise. | Chaque marque citée a un rôle précis dans le texte. |
| Structure de l’article | Relire le plan proposé via Générer la structure de l’article. Si des sections sont éditables, ordonner le choix du lecteur, les critères et les cas d’usage. | Chaque titre apporte une réponse distincte. Une génération de structure est une action IA. |
| Options de contenu → Structure du texte | Introduction pour poser le problème, En bref pour une réponse courte, Listes pour des étapes, Tableaux pour des critères comparables, FAQ pour des questions résiduelles, Toolbox pour un outil utile au lecteur. Guider chaque case visible. | Le contenu justifie chaque élément coché. Pour un tableau, les lignes comparent la même unité et le même type de donnée. |
| Mise en forme → Mots en gras, Emojis | Gras pour les repères utiles. Pour une charte sobre, laisser Emojis décoché. | Contrôler un paragraphe dans l’aperçu. |
| Médias → YouTube, Images, image de mise en avant | Décider séparément pour la vidéo, les illustrations du corps et la couverture. | Vérifier que chaque média illustre le sujet. L’image du corps et la couverture peuvent relever de réglages différents. |
| Nombre maximum d’images et Instructions personnalisées des images | Exemple conseillé pour un essai : une illustration. Donner sujet, cadrage, style, éléments à éviter. | Contrôler lisibilité et fidélité au sujet. Le nombre indiqué est un plafond. |
| Liens internes, Liens externes, Ajouter un lien personnalisé | Pour un lien manuel, choisir une page réelle et une ancre descriptive. Si « Ancre du lien » apparaît, exemple : « choisir une jardinière pour balcon ». | Cliquer dans l’aperçu, contrôler destination et ancre. |
| Amazon Affiliate → Produits Amazon, Affiliate ID, Store | Activer si le document est prévu pour l’affiliation et si l’utilisateur a un identifiant valide sur ce marché. | Vérifier boutique, attribution et correspondance article-produit. Éviter tout prix, score, test personnel ou disponibilité fabriqués. |
| Enregistrer un template / Générer le contenu | Enregistrer un jeu de réglages pour le réutiliser. Générer lance la production du document. | Vérifier le titre final, la structure, les données, les liens et les images dans le document produit. La génération seule ne prouve pas sa publication dans WordPress. |

### Adapter le brief au format

| Format | Valeur de départ | Ce que le coach demande seulement si cela manque |
| --- | --- | --- |
| Local | « Aide une personne qui cherche un atelier de réparation de vélos à Dijon. Utilise uniquement les adresses et horaires fournis. » | Zone exacte et sources locales. |
| Actualité | « Explique l’annonce du fabricant, date les faits et distingue ce qui est déjà disponible de ce qui est annoncé. » | Date de référence et annonce originale. |
| Présentation d’une marque | « Décris la gamme documentée, pour qui elle convient, ses limites et les éléments vérifiables. » | Marque, marché et sources de première main. |
| Comparatif / comparateur Amazon | « Compare uniquement les références fournies. Indique les usages recommandés et la source de chaque caractéristique discriminante. » | Références exactes, critères communs, marché et identifiant si affiliation. |
| Fiche produit | « Explique à qui convient la référence, ses dimensions publiées, son usage et ses limites. » | Identifiant du modèle et fiche fabricant. |
| Guide | « Accompagne un débutant de la préparation au contrôle final, avec un exemple à chaque étape difficile. » | Niveau du lecteur et résultat attendu. |
| Simulateur | « Demande la longueur et la largeur en mètres. Calcule la surface en m² et montre la formule. Signale une saisie vide ou négative. » | Entrées, unités, formule et exemple de résultat connu. Contrôle : 3 m × 2 m donne 6 m². |

Si l’utilisateur veut un modèle réutilisable, séparer les emplacements à compléter manuellement de toute syntaxe réellement interprétée par Otomatic. Aucune interpolation automatique de `{keyword}` ou d’une autre variable ne doit être promise sans aide vérifiée pour le champ et la version concernés.
