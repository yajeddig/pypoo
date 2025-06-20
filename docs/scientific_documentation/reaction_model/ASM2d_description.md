# Modèle ASM2

## 1. Introduction – Modèle ASM2

Le modèle ASM2 est une extension de l’ASM1 destinée à mieux représenter la dynamique des constituants organiques et en particulier celle du phosphore. Il conserve la structure de base (séparation en phases solubles et particulaires, croissance de la biomasse, hydrolyse, etc.) et y ajoute :

- **La gestion du phosphore**, par l’introduction de nouveaux constituants (ex. S_PO pour le phosphore soluble et X_PP pour le phosphore associé aux particules ou aux produits de lyse) ;
- **Une description plus fine des transformations organiques** qui inclut à la fois la dégradation rapide et la conversion lente (hydrolyse) de la matière particulaire biodégradable.

Le modèle s’appuie sur des équations cinétiques de type Michaelis–Menten pour décrire les processus biologiques, et utilise une matrice stœchiométrique pour relier chaque réaction aux variations de concentrations des constituants.

---

## 2. Variables d’État – Tableaux des constituants

Les variables d’état représentent les concentrations des différents constituants dans le réacteur. On distingue notamment :

| Variable | Définition | Unité |
|----------|------------|-------|
| **S_I**  | Substrat inerte soluble (matière organique non biodégradable et soluble) | mg COD/L |
| **S_S**  | Substrat soluble biodégradable (matière organique facilement assimilable par les hétérotrophes) | mg COD/L |
| **X_I**  | Matière inerte particulaire (fraction particulaire non biodégradable) | mg COD/L |
| **X_S**  | Matière particulaire lentement biodégradable (fraction nécessitant une hydrolyse extracellulaire) | mg COD/L |
| **X_BH** | Biomasse hétérotrophe active (micro-organismes consommant S_S) | mg COD/L |
| **X_BA** | Biomasse autotrophe active (micro-organismes nitrifiants, convertissant S_NH en S_NO) | mg COD/L |
| **S_NH** | Azote ammoniacal (forme d’azote disponible, NH₄⁺/NH₃) | mg N/L |
| **S_NO** | Azote oxydé (nitrites et nitrates) | mg N/L |
| **S_O**  | Oxygène dissous (oxygène disponible pour la respiration) | mg O₂/L |
| **S_PO** | Phosphore soluble (phosphate biodisponible) | mg P/L |
| **X_PP** | Phosphore particulaire (lié à la biomasse ou issu de la lyse) | mg P/L |
| **S_ALK**| Alcalinité (capacité de neutralisation des acides) | meq/L |

Ces variables constituent l’état du système et sont suivies dans le réacteur pour la simulation des processus biologiques et physico-chimiques.

---

## 3. Conversion des Mesures (Interface Capteurs → Variables d’État)

Pour relier les données de terrain (capteurs et mesures opérationnelles) aux variables du modèle ASM2, on définit une interface de conversion. Par exemple :

| Capteur (Interface) | Mesure Opérationnelle | Variable d’État ASM2 | Méthode de Conversion / Calcul |
|---------------------|-----------------------|----------------------|--------------------------------|
| DO                  | Oxygène dissous       | S_O                  | Mesure directe en mg O₂/L      |
| NH4                 | Concentration d’ammonium | S_NH              | Mesure directe en mg N/L       |
| NO3                 | Nitrate + Nitrite     | S_NO                 | Mesure directe en mg N/L       |
| PO4                 | Phosphate             | S_PO                 | Mesure directe en mg P/L       |
| TSS                 | Solides totaux en suspension | X_BH + X_BA + X_I + X_S + X_PP | Conversion via un facteur F_TSS/COD |
| Online COD          | Demande chimique en oxygène totale (DCO) | S_I + S_S + X_I + X_S + X_BH + X_BA | Somme des constituants de COD |
| Online TN           | Azote total           | S_NH + S_NO + i_N·(X_BH + X_BA) | Avec i_N la teneur en N dans la biomasse |
| Online TP           | Phosphore total       | S_PO + X_PP          | Conversion selon la fraction de P |

Ces équations de conversion permettent d’obtenir des valeurs initiales pour la simulation et de calibrer le modèle sur les données observées.

---

## 4. Équations Cinétiques du Modèle ASM2

Chaque processus biologique est modélisé par une équation cinétique. Voici l’ensemble des équations principales :

### 4.1 Processus de Croissance et de Consommation de Substrat

1. **Croissance aérobie des hétérotrophes (ρ₁) :**

   $$
   \rho_1 = \mu_{mH} \cdot \frac{S_S}{K_S + S_S} \cdot \frac{S_O}{K_{OH} + S_O} \cdot X_{BH}
   $$

   *Description :* Conversion du substrat soluble biodégradable S_S en biomasse active X_BH en présence d’oxygène.

2. **Croissance anoxique (dénitrification) des hétérotrophes (ρ₂) :**

   $$
   \rho_2 = \mu_{mH} \cdot \frac{S_S}{S_S + K_S} \cdot \frac{K_{OH}}{K_{OH} + S_O} \cdot \frac{S_{NO}}{K_{NO} + S_{NO}} \cdot \eta_g \cdot X_{BH}
   $$

   *Description :* Utilisation du substrat S_S en absence (ou faible concentration) d’oxygène, avec nitrate servant d’accepteur d’électrons.

3. **Croissance autotrophe (nitrification) (ρ₃) :**

   $$
   \rho_3 = \mu_{mA} \cdot \frac{S_{NH}}{K_{NH} + S_{NH}} \cdot \frac{S_O}{K_{OA} + S_O} \cdot X_{BA}
   $$

   *Description :* Oxydation de l’azote ammoniacal S_NH en nitrate/nitrite S_NO par la biomasse autotrophe X_BA.

### 4.2 Processus de Décroissance et de Lyse

4. **Décroissance (lyse) des hétérotrophes (ρ₄) :**

   $$
   \rho_4 = b_H \cdot X_{BH}
   $$

   *Description :* Perte de biomasse active X_BH entraînant la formation de produits inertes et la libération partielle d’azote et de phosphore.

5. **Décroissance des autotrophes (ρ₅) :**

   $$
   \rho_5 = b_A \cdot X_{BA}
   $$

   *Description :* Diminution de la biomasse autotrophe X_BA par lyse.

### 4.3 Processus de Transformation de la Matière

6. **Hydrolyse de la matière particulaire organique (ρ₇) :**

   $$
   \rho_7 = k_{h} \cdot \frac{\frac{X_S}{X_{BH}}}{K_X + \frac{X_S}{X_{BH}}} \cdot \left[ \frac{S_O}{K_{OH}+S_O} + \eta_h \cdot \frac{K_{OH}}{K_{OH}+S_O} \cdot \frac{S_{NO}}{K_{NO}+S_{NO}} \right] \cdot X_{BH}
   $$

   *Description :* Conversion de la matière particulaire lentement biodégradable X_S en substrat soluble S_S, catalysée par la biomasse hétérotrophe.

### 4.4 Processus de Transformation de l’Azote et du Phosphore

7. **Ammonification de l’azote organique (ρ₆) :**

   $$
   \rho_6 = k_a \cdot S_{ND} \cdot X_{BH}
   $$

   *Description :* Conversion de l’azote organique soluble S_{ND} en ammoniac S_NH.

8. **Prélèvement du phosphore par la biomasse (ρ_{Puptake}) :**

   $$
   \rho_{Puptake} = \mu_{mH} \cdot \frac{S_{PO}}{K_{PO} + S_{PO}} \cdot X_{BH}
   $$

   *Description :* Intégration du phosphore soluble S_PO dans la biomasse lors de la croissance hétérotrophe. Un rendement α peut être appliqué pour convertir une fraction de S_PO en phosphore incorporé dans X_BH.

9. **Libération du phosphore lors de la lyse (ρ_{Prelease}) :**

   $$
   \rho_{Prelease} = b_H \cdot X_{BH} \cdot f_P
   $$

   *Description :* Libération du phosphore contenu dans la biomasse active lors de sa décroissance, où f_P est la fraction de phosphore relâchée.

---

## 5. Matrice Stœchiométrique

La matrice stœchiométrique associe chaque réaction aux variations des constituants du système. Voici un tableau synthétique pour quelques réactions clés :

| Réaction                                | S_I  | S_S          | X_I  | X_S  | X_BH        | X_BA | X_PP / S_PO | S_NH            | S_NO             | S_ALK                | Commentaires                                        |
|-----------------------------------------|------|--------------|------|------|-------------|------|-------------|-----------------|------------------|----------------------|-----------------------------------------------------|
| **Croissance aérobie hétérotrophe (ρ₁)**  |  0   | -1/Y_H       |  0   |  0   | +1          |  0   |  0          | -i_N          | +(1 - Y_H)/Y_H   | -i_N/14             | Consommation de S_S, production de X_BH             |
| **Croissance anoxique (dénitrification) (ρ₂)** |  0   | -1/Y_H       |  0   |  0   | +1          |  0   |  0          | -i_N          | - (1 - Y_H)/(2.86·Y_H) | 0              | Dénitrification par X_BH                           |
| **Croissance autotrophe (nitrification) (ρ₃)** |  0   |  0           |  0   |  0   |  0          | +1   |  0          | -i_N          | +1               | -i_N/14             | Oxydation de S_NH en S_NO pour X_BA                 |
| **Décroissance des hétérotrophes (ρ₄)**       | +1   |  0           |  0   |  0   | -1          |  0   | +f_P (P libéré) |  0           |  0               ||  Contribution à la formation de X_PP               |
| **Hydrolyse de la matière particulaire (ρ₇)** |  0   | +1           |  0   | -1   |  0          |  0   |  0          |  0             |  0               || Conversion de X_S en S_S                             |
| **Prélèvement du phosphore (ρ_{Puptake})**     |  0   |  0           |  0   |  0   | +α (P incorporé) | 0  | -1         |  0             |  0               || Incorporation de S_PO dans X_BH (rendement α)       |
| **Libération du phosphore (ρ_{Prelease})**     |  0   |  0           |  0   |  0   | -β (P perdu)   | 0  | +1         |  0             |  0               || Libération de phosphore lors de la lyse (β)         |

*Notes :*  

- Les coefficients stœchiométriques (Y_H, i_N, f_P, α, β, etc.) sont déterminés par la littérature et calibrés sur des données expérimentales.  
- La contribution d’azote dans la biomasse est prise en compte via un coefficient i_N (en g N par g COD).

---

## 6. Synthèse Complète

Le modèle ASM2 s’appuie sur :

- **Un ensemble exhaustif de variables d’état** qui regroupent les constituants issus de la matière organique, de l’azote, du phosphore, de l’oxygène et de l’alcalinité.
- **Une interface de conversion** permettant de relier les mesures opérationnelles (DO, NH4, NO3, PO4, TSS, etc.) aux variables du modèle.
- **Des équations cinétiques détaillées** pour chaque processus clé :
  - Croissance aérobie et anoxique des hétérotrophes,
  - Croissance autotrophe (nitrification),
  - Hydrolyse de la matière particulaire,
  - Ammonification,
  - Transformation du phosphore (prélèvement et libération).
- **Une matrice stœchiométrique** qui relie chaque réaction aux variations de masse des constituants, garantissant la conservation de la matière et la cohérence des bilans.

Cette présentation exhaustive permet d’appréhender l’ensemble du modèle ASM2 pour la simulation dynamique des procédés biologiques de traitement des eaux, et de le calibrer sur des données de terrain pour une application opérationnelle.

---

Ce document présente ainsi, de manière détaillée et complète, toutes les variables, équations cinétiques et la matrice stœchiométrique qui constituent le modèle ASM2.
