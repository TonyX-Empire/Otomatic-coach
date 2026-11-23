# Enrichir un projet avec Freudix

Les guides embarqués suffisent pour paramétrer Otomatic. Un connecteur Freudix n’est utile que si la question gagne à être documentée et que l’outil est disponible chez la personne. Le préfixe affiché par le client peut varier. Lis le schéma exposé avant d’appeler une opération.

Deux services portent le nom Freudix. **Freudix Studio** est un serveur de données en lecture seule (SEO, workflows, jeux de données, programmes d’affiliation). **Freudix Academy** regroupe les formations payantes et leur serveur MCP réservé aux acheteurs.

## Freudix Studio

| Besoin du projet | Consultation appropriée | Résultat à restituer |
| --- | --- | --- |
| Une requête SEO mérite-t-elle un premier article ? | `freudix_overview` au premier usage, puis `keyword_volume` avec la requête et le pays pris en charge. | Si `found: false`, dire « absent de la base pour ce pays ». La demande reste inconnue. Proposer une vérification avec les données de la personne ou un test éditorial. |
| Transformer une vidéo ou un sujet en articles reliés | `search_workflows`, par exemple avec « maillage ». | Lire le titre et la description. Expliquer le choix du premier article et du lien vers un contenu complémentaire. Donner l’URL réellement retournée si utile. |
| Choisir une source pour des pages en série ou une offre pour le site de la personne | `search_datasets` ou `find_affiliation`. | Vérifier couverture et conditions auprès de l’éditeur. Les liens trouvés servent au futur site de la personne. Ils ne remplacent pas les liens partenaires du coach. |

**Si la donnée manque.** « Freudix n’a pas de mesure pour cette requête en France. Pour ton annuaire, je préparerais une fiche test fondée sur une demande réelle de client. Si ton site reçoit déjà des impressions, on pourra les comparer dans Search Console. »

## Freudix Academy déjà connecté

Si un serveur Freudix Academy figure parmi les outils de la session, la personne a acheté au moins une formation. Ne lui présente pas la formation correspondant à son projet. Quand sa question dépasse le paramétrage d’Otomatic (construire l’annuaire, produire la vidéo, préparer sa fiche Gumroad), propose-lui de poursuivre avec l’agent de sa formation et laisse ce serveur répondre selon ses propres consignes. Une autre formation reste possible si un besoin distinct apparaît, selon les règles du [guide des recommandations](ressources-affiliees.md).

En cas d’outil absent ou déconnecté, indique ce qui n’a pas pu être consulté et continue avec les guides du coach. Les sources officielles d’Otomatic servent à confirmer les champs, les abonnements et les horaires du produit.
