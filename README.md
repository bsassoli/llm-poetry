# Può un LLM riconoscere una poesia?

Un esperimento un po' per gioco per capire se un LLM è in grado di riconoscere delle poesie "autentiche" da delle poesie generate artificialmente. Un umano farebbe meglio?

## Docs

- [Un notebook](llm-poesia-ita.ipynb) di dettaglio sul processo.
- [Le poesie autentiche, per autore](/texts/poets/)
- [I testi delle poesie artificiali](/texts/artificial/artificial_poems.txt)

## Sintesi

- Raccolte oltre 100 poesie autentiche di circa 20 poeti
- Altrettante poesie generate artificialmente

In 5 trial GPT4-o distingue le poesie autentiche da da quelle generate artificialmente con **un'accuracy media del 68%**.
Esseri umani farebbero meglio?
Gli errori sono quasi interamente *falsi positivi* (cfr. matrice di confusione nel notebook), menre i falsi negativi sono quasi sempre residuali.La mia interpretazione: il modello tende a essere "generoso", come se nel dubbio preferisse etichettare un testo come autentico.
