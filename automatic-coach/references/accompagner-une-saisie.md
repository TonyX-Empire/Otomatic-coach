# Aider l’utilisateur devant un champ

Quand il demande « Qu’est-ce que je mets ici ? », ouvrir par une explication qui lui permettra de reconnaître le champ la prochaine fois. Une ligne peut suffire. Par exemple : « Biographie présente la personne ou la rédaction qui signe. Les consignes de style se placent dans Instructions personnalisées, sous Rédaction. » Si le libellé est simplement « Instructions personnalisées », identifier d’abord la rubrique parente, à partir du contexte ou d’une question courte.

## Choisir le bon emplacement

| Champ ou famille | Comment expliquer son rôle | Question utile si le contexte manque |
| --- | --- | --- |
| Domaine / site et sous-dossier | Il désigne l’installation ou la propriété à laquelle s’appliquent les réglages. | « Les articles doivent-ils paraître sur ton domaine principal ou dans son blog installé à part ? » |
| Custom IA, après sélection du domaine | Ce texte contient les règles qui doivent s’appliquer aux générations de ce site, quels que soient le rédacteur et le sujet. | « Quelle règle doit être vraie aussi bien pour un guide que pour une fiche ou une actualité ? » |
| Profil → Prénom, Nom, Âge, Métier, Biographie | Le prénom et le nom identifient la signature choisie. Le métier décrit le rôle. La biographie présente qui écrit, les sujets couverts et le public aidé. Utiliser des faits que l’utilisateur peut assumer. | « Qui signe ces contenus et pour quels lecteurs écrit cette personne ou cette rédaction ? » Si seul le métier manque, demander uniquement celui-ci. |
| Rédaction → Style d’écriture et Instructions personnalisées | Le style donne une direction générale. Les instructions traduisent la voix en habitudes concrètes et réutilisables, comme le tutoiement et le choix du vocabulaire. | « Comment veux-tu que cette personne s’adresse au lecteur ? » Si le style demandé est donné, illustrer directement son application. |
| Utilisateur WordPress → identifiant, e-mail, mot de passe, rôle | Ces champs configurent un compte sur le site et ses droits. L’Auteur de publication désigne la signature WordPress. | « Cet auteur doit-il préparer des brouillons ou aussi publier ? » Pour les identifiants et mots de passe, expliquer la saisie locale sans solliciter le secret. |
| Assistant → Requête cible, Titre, Langue | La requête exprime la recherche à laquelle l’article répond. Le titre formule la promesse au lecteur. La langue est celle du document. | « Quelle question le lecteur cherche-t-il à résoudre avec cet article ? » Ne jamais transformer un simple choix de langue en publicité pour un site multilingue. |
| Assistant → Brief de génération | Le brief donne le sujet, l’angle, le résultat attendu et les contraintes propres à cet article. | « Après la lecture, quelle décision ou quel geste veux-tu rendre possible ? » Proposer un brief rempli, sans réécrire toute la charte du site. |
| Assistant → Scraper, sources, entités, marques, mots-clés, structure | Une source apporte de la matière. Une entité ou une marque précise ce qu’il faut couvrir. Le plan ordonne les réponses. | Cibler la saisie affichée : « Quelles références compares-tu réellement ? » ou « Quelle source doit servir de base ? » |
| Médias → instructions d’images, source ou plafond | Les instructions d’images décrivent ce qui doit être visible. Le sélecteur choisit la source et le nombre fixe un maximum dans la portée indiquée. | « Quel détail le lecteur doit-il pouvoir reconnaître sur l’image ? » Pour un plafond, demander seulement le nombre utile au projet si inconnu. |
| Template, options de contenu, liens et métadonnées SEO | Un template réutilise un ensemble de réglages pour un format. Les options décident quels éléments produire. Un lien a une destination et une ancre. Le title et la meta description décrivent la page dans ses métadonnées. | « Veux-tu ce réglage sur chaque comparatif ou sur tous les formats du domaine ? » Pour une URL fixe, demander la destination réelle quand elle manque. |
| Autopilot → instructions pour le profil, le texte et les images | Dans le projet, la première saisie adapte la posture du rédacteur au lot, la deuxième fixe ce qui doit figurer dans ses textes, la troisième fixe l’intention visuelle. | « Cette consigne concerne-t-elle la façon de parler, le contenu de toute la série ou son illustration ? » |
| Autopilot → sources, titres, type de post et catégories | La source fournit les sujets, les titres déterminent les publications et les réglages WordPress définissent où les ranger. | Demander la matière disponible ou la destination exacte selon le champ. Si la personne a déjà ses titres, proposer le parcours de titres manuels. |
| Autopilot → Statut, cadence, dates et heures | Le statut détermine l’état WordPress du contenu. La cadence fixe quand le lot est traité. Expliquer l’effet de chacun avant de demander de lancer. | « Souhaites-tu relire chaque article avant sa mise en ligne ? » ou, pour les heures : « À quelle heure locale veux-tu que cela se produise ? » |
| Site Builder, SEO, Netlinking, Marketplace, agents | Appliquer le même dialogue. Dans le Builder, le brief exprime le site à produire. En netlinking, URL cible désigne la page à citer. Dans la Marketplace, un prix concerne l’annonce. Pour un agent, le rôle définit sa mission et son livrable. | Poser une question propre au contrôle visible, puis donner un texte ou une sélection vérifiable dans le guide du module. |
| Clés API, comptes associés, Affiliate ID, Store, champs personnalisés | Expliquer séparément fournisseur, propriété, identifiant d’affiliation, boutique ou clé technique attendue par le site. | Demander le service, le marché ou le format requis. Pour une valeur privée ou propre au compte, montrer comment la reconnaître et la vérifier localement. |

Les intitulés complets, options et conditions d’affichage restent dans les guides [sites](sites-et-profils.md), [assistant](prompts-et-assistant.md), [Autopilot](autopilot.md) et [autres modules](autres-modules.md). Pour tout champ supplémentaire visible, appliquer la même séquence à son type réel.

## Dialogue modèle pour Biographie

**Demande :** « Qu’est-ce que je mets dans Biographie ? »

**Première réponse quand le contexte manque :** « La biographie présente le rédacteur : qui signe, de quoi il parle et à qui il s’adresse. Les consignes comme “vouvoie le lecteur” vont dans Rédaction → Instructions personnalisées. Qui signe tes articles et pour quels lecteurs ? »

**Réponse de l’utilisateur :** « Une rédaction collective. On aide les citadins qui commencent un potager sur leur balcon. »

**Proposition courte**

```text
La rédaction accompagne les citadins qui cultivent leur premier potager sur un balcon. Ses guides expliquent comment choisir ses plantes et s’en occuper au fil des saisons.
```

**Proposition plus chaleureuse**

```text
Nous écrivons pour celles et ceux qui veulent faire pousser leurs premiers légumes sur un balcon. Du choix des pots aux premières récoltes, nous expliquons chaque geste avec des mots simples.
```

**Validation :** « Laquelle te ressemble le plus ? Je peux aussi la rendre plus sobre, plus chaleureuse ou plus courte. »

**Si la personne répond « La deuxième, mais en une phrase »**, livrer directement la version révisée, par exemple « Nous guidons les jardiniers de balcon de leurs premiers semis à leurs premières récoltes. » Puis demander « Cette version te convient ? ». Si la personne dit seulement « On améliore », demander quel point viser.

## Même méthode pour une consigne ambiguë

Demande : « Où mettre : “Toujours citer la source d’un prix, tutoyer le lecteur et comparer trois modèles de sécateurs dans ce guide” ? » Les trois intentions sont déjà claires. Expliquer la portée de chaque champ avant sa valeur à coller, puis valider les trois ensemble.

- **Custom IA du domaine.** Cette règle doit traverser toute la production du site. Texte : « Pour chaque prix cité, indique sa source et la date du relevé. »
- **Profil → Rédaction → Instructions personnalisées.** Cette règle définit la voix du rédacteur dans ses articles. Texte : « Tutoie le lecteur dans tout l’article. »
- **Assistant → Brief de génération.** Cette contrainte concerne le guide en cours. Texte : « Compare les trois modèles de sécateurs fournis. Explique pour quel usage chacun convient et appuie la comparaison sur les fiches disponibles. »

Si l’utilisateur parle d’un quatrième élément, par exemple « je veux une photo sur fond blanc », l’orienter vers les instructions personnalisées des images du document ou du lot concerné.

## Même méthode pour un sélecteur

Demande : « Je suis sur Statut dans Autopilot. Je veux relire mes articles. » Réponse : « Statut détermine dans quel état Autopilot envoie l’article à WordPress. Pour ta relecture, choisis **Brouillon**. Vérifie que le sélecteur affiche bien ce mot avant de lancer la génération. Ce réglage te convient ? » Une seule option suffit, car l’intention est déjà précise.
