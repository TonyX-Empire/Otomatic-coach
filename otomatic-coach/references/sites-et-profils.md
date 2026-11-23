# Relier un site et créer un profil rédacteur

Libellés du SaaS web observés le 23 novembre 2026. Les exemples sont fictifs. La liste des domaines, auteurs, catégories et services déjà reliés appartient à l’utilisateur.

## 1. Quel site est concerné ?

| Situation | Chemin et action | Contrôle |
| --- | --- | --- |
| Suivre des performances | Tableau de bord → Ajouter un domaine → Importer depuis Google Search Console ou Importer depuis Bing Webmaster. Choisir la propriété correspondant au site. | Retrouver le domaine dans le tableau et regarder la période et la source de la métrique. Ce parcours établit un suivi, le plugin WordPress établit la liaison éditoriale. |
| Publier sur un WordPress existant | Tableau de bord → Ajouter un domaine → Télécharger le plugin, également accessible dans Réglages. Dans l’administration du WordPress cible, installer l’archive depuis Extensions, l’activer puis suivre l’association au compte proposée par la version installée. | Revenir au Tableau de bord. Vérifier le domaine exact, y compris un éventuel /blog, puis vérifier qu’il est proposé dans le sélecteur de Projets Autopilot. |
| Configurer un domaine existant | Tableau de bord → cliquer sur le domaine. L’écran du site WordPress observé propose Créer un contenu IA, Mes profils IA, Mes projets Autopilot et Régénérer le contenu. | Vérifier le titre de la fiche et la destination. Régénérer le contenu peut ouvrir l’administration WordPress et demander une connexion distincte. |
| Créer un site neuf | Site Builder → Créer un site. Utiliser le guide des autres modules. | Le projet se trouve dans Site Builder. La connexion d’un WordPress existant est un parcours indépendant. |

**Erreur de destination.** Un domaine racine et son installation dans un sous-dossier peuvent tous deux apparaître. Demander où les articles doivent réellement être publiés. Si un domaine figure dans le monitoring mais manque au sélecteur WordPress, vérifier d’abord le site d’installation, l’activation du plugin et le compte relié. Si l’utilisateur montre un écran d’installation différent, demander le libellé à l’étape bloquante, en masquant toute clé.

## 2. Fournisseurs et personnalisation du domaine

| Écran et saisie | Valeur et décision à proposer | Contrôle |
| --- | --- | --- |
| Réglages → Clés API → Modèles de texte → API key | Choisir la carte du fournisseur utilisé. Coller la clé de ce fournisseur directement dans sa carte. Sur l’écran web consulté, la carte OpenAI portait « Requis ». Mistral, Anthropic, Grok, Gemini et DeepSeek étaient proposés en option. | Sauvegarder sur la bonne carte et vérifier le message retourné. Une clé masquée sur une capture ne permet pas de conclure qu’elle est valide. |
| Même écran → Modèles d’images → API key | Choisir le service adapté au projet, par exemple un générateur d’images ou une banque photo. Expliquer le choix selon le besoin de réalisme, la source et le budget. | Vérifier le fournisseur disponible dans le sélecteur du projet. Ne pas confondre une clé de banque photo et une clé de modèle texte. |
| Envoi des clés API sur mes sites | Commande de distribution vers les WordPress. La simple configuration d’une carte et l’envoi des clés aux sites sont deux actions distinctes. Lire les destinations proposées à l’écran avec l’utilisateur. | Vérifier quels sites sont concernés avant d’utiliser la commande associée. Aucune clé dans un prompt, une capture ou un message. |
| Réglages → Comptes associés | Choisir le service pertinent parmi Google, Yandex ou Bing et le compte qui détient la propriété. Si l’utilisateur veut suivre le trafic, distinguer Google Analytics et Search Console. | Rouvrir la fiche du domaine et regarder la bonne source à la bonne période. Une valeur manquante se distingue d’une mesure à zéro. |
| Réglages → Custom IA → Sélectionnez un domaine → Custom IA | Saisir les règles communes aux contenus générés pour ce domaine. Ex. « N’annonce un prix que s’il est daté et présent dans une source fournie. » Améliorer le prompt est facultatif. | Relire le texte proposé, choisir Sauvegarder, puis revenir sur le même domaine. Pour une structure réservée à un format, préférer le template de ce format. |
| Réglages → Amazon → Sélectionnez un domaine → Affiliate ID | Renseigner l’identifiant de suivi du programme partenaire que l’utilisateur détient pour ce site et ce marché. | Vérifier le domaine avant de sauvegarder et le tag du lien obtenu sur un brouillon. |
| Même écran → Store | Choisir la boutique à laquelle correspond cet identifiant, par exemple France pour un identifiant associé à la boutique française. | Contrôler aussi Store dans le document si une option Amazon y est activée. Un identifiant de suivi n’est ni un ASIN ni une clé API. |

## 3. Créer un rédacteur, dans l’ordre de l’écran

Chemin web vérifié : Tableau de bord → domaine WordPress → Mes profils IA → Nouveau rédacteur. Les rubriques affichées sont **Profil**, **Rédaction** et **Utilisateur WordPress**. Un persona règle la voix. Le dernier bloc concerne le compte qui peut être créé sur WordPress. Demander l’identité à attribuer si elle doit apparaître en signature.

| Champ exact | Quoi renseigner ou choisir | Comment le contrôler |
| --- | --- | --- |
| Langue | La langue habituelle de rédaction, par exemple Français. | Elle correspond au lectorat visé. Vérifier séparément la langue du document. |
| Prénom | Le prénom de l’auteur autorisé ou l’identité éditoriale choisie. | Relire la signature attendue avec l’utilisateur. |
| Nom | Le nom approuvé si la signature en comporte un. Se fier à la validation affichée pour son caractère obligatoire. | L’ensemble prénom et nom ne crée aucune fausse attribution. |
| Âge | Un entier si pertinent et accepté par le formulaire. Utiliser une information approuvée pour une personne réelle. | Ne pas convertir un niveau d’expertise en âge inventé. |
| Métier | Le rôle éditorial précis, par exemple « Rédactrice jardinage ». | Le rôle explique l’angle. Il n’attribue aucun diplôme ou titre non établi. |
| Biographie | Deux ou trois phrases sur les sujets couverts et la manière d’aider le public. Exemple éditorial : « La rédaction explique aux jardiniers débutants comment prendre soin des plantes en pot. Chaque guide propose un geste simple à vérifier chez soi. » | Si Générer est utilisé, relire les expériences et qualifications proposées avant de les retenir. |
| Style d’écriture | Choisir un style proposé dans la liste de cet écran. Regarder les options visibles avant d’en recommander une par son nom. | À partir d’un paragraphe, le lecteur reconnaît le ton voulu. |
| Instructions personnalisées | Fixer la voix, la relation au lecteur, le vocabulaire et les limites du rédacteur. Exemple : « Vouvoie le lecteur. Décris chaque geste avec un verbe concret. Explique les termes horticoles à leur première apparition. » | Le texte reste pertinent pour deux articles de sujets différents. Utiliser Améliorer le prompt si la reformulation mérite une relecture. |
| Nom d’utilisateur | Identifiant WordPress prévu pour cette signature. Demander si un auteur approprié existe déjà avant d’en créer un autre. | Confirmer le bon site et éviter le doublon. |
| Mot de passe | L’utilisateur le crée et le saisit dans WordPress ou le formulaire prévu, idéalement depuis son gestionnaire. | Vérifier localement l’acceptation du champ. Ne jamais demander de le communiquer. |
| Adresse e-mail | L’adresse autorisée pour cet utilisateur WordPress. La personne peut la saisir directement. | Vérifier le destinataire des notifications liées au compte. |
| Rôle | Choisir dans la liste le niveau suffisant pour les tâches réellement confiées. Pour une relecture, envisager un rôle à droits limités s’il est proposé. | Le formulaire observé affichait **Administrator**. Attirer l’attention sur la portée du choix avant Créer. |

Après Créer, contrôler que le rédacteur figure dans **Mes profils IA** pour le site cible. Dans Autopilot, vérifier séparément le **Profil** et l’**Auteur** de destination.

**Exemple de premier échange.** Si la personne demande quoi mettre dans Biographie, commence par expliquer que ce champ présente qui écrit, son sujet et pour quel public. Le ton relève des Instructions personnalisées de la rubrique Rédaction. Si l’identité ou le public manque, demande-le avant de proposer une ou deux biographies. Après la proposition, demande si elle convient et ajuste le point indiqué. Voir [l’exemple de dialogue](accompagner-une-saisie.md).
