# Machine Learning Abschlussprojekt — Persönlichkeitstyp-Vorhersage-App


**Abgabe:** Ein GitHub-Repository-Link, eingereicht über Codio

**Abgabefrist & -zeitpunkt:** Freitag, 9. Oktober 2026, um **09:44 Uhr** (punktgenau vor der Präsentation um 09:45 Uhr; stell sicher, dass dein Repository **öffentlich** ist).

---

## 1. Was du bauen wirst

Du wirst ein kleines, aber vollständiges System für maschinelles Lernen bauen: ein Modell, das den **Persönlichkeitstyp** einer Person anhand eines kurzen Fragebogens vorhersagt, verpackt in eine einfache **Streamlit-Web-App**, die von jedem genutzt werden kann.

Ein Benutzer beantwortet **19 kurze Persönlichkeitsfragen** (mit einer Skala von 1 = *Trifft nicht zu* bis 5 = *Trifft zu*), sowie Alter, Geschlecht und die Schreibhand. Dein Modell sagt den **Persönlichkeitstyp** voraus, und die Streamlit-App zeigt das Ergebnis sofort an.

> **Denk daran, was wir hier eigentlich tun.**
> Dieses Projekt **simuliert den gesamten Prozess des maschinellen Lernens** von Anfang bis Ende. Du beginnst mit Rohdaten, erkundest diese, erstellst eine Vorverarbeitungspipeline, trainierst und vergleichst Modelle, optimierst sie und wählst das beste aus. Die Streamlit-App ist der letzte Schritt: Sie **simuliert die Überführung deines Modells in die Produktion** — ein echter Benutzer interagiert mit einem echten Modell, bereitgestellt über eine Benutzeroberfläche. Jede Phase ist wichtig, nicht nur das Modell.

---

## 2. Was du abgeben musst — Die Checkliste

Es gibt **keine feste Vorgabe**, wie du dein Projekt in Notebooks, Skripte oder Ordner aufteilst. Diese Bestandteile müssen jedoch **in irgendeiner Form** vorhanden sein:

- [ ] **EDA**, die einen **bereinigten Datensatz** erzeugt.
- [ ] Der **Vergleich von mindestens 3 Modellen** deiner Wahl, bei denen jeweils ein **Hyperparameter-Tuning** durchgeführt wurde (welche Hyperparameter und Werte, ist dir überlassen).
- [ ] Die Berechnung des **`f1_macro`-Scores** als Vergleichspunkt. (Wenn du tiefer in die Leistung deines Modells einsteigen willst, kannst du optional eine Confusion Matrix oder weitere Metriken hinzufügen.)
- [ ] Das **Speichern des besten Modells** (`joblib` oder MLflow).
- [ ] Die **Streamlit-App** (`app.py`).
- [ ] Die **`README.md`** (siehe §9).
- [ ] Die **`requirements.txt`**.



---

## 3. Teamarbeit & Zusammenarbeit

Projekte können einzeln oder in Teams von **1 bis 3 Teilnehmern** durchgeführt werden.

* **Teambedingung:** Wenn du in einem Team mit mehr als einer Person arbeitest, **müsst ihr Git und GitHub gemeinsam nutzen**. Das bedeutet, dass der Commit-Verlauf des geteilten Repositorys die Beiträge aller Teammitglieder widerspiegeln muss.
* **Workflow-Strategie:** Wie ihr den Git-Workflow eures Teams organisiert (z. B. die Arbeit mit separaten Feature-Branches, Pull Requests oder direkte Commits auf den Main-Branch) bleibt ganz euch überlassen, solange die aktive Beteiligung aller im Commit-Log sichtbar ist.

---

## 4. Die Daten

Die Daten stammen aus dem **Big-Five-Persönlichkeitstest (OCEAN)**, einem bekannten Datensatz, der auf **Kaggle** veröffentlicht wurde. Die Originalversion hat 50 Fragen (10 für jedes der fünf Merkmale), die von etwa 19.000 Personen beantwortet wurden.

Wir haben eine bereinigte, optimierte Version für dich vorbereitet. Anstelle aller 50 Fragen enthält sie die **19 informativsten**, dazu einige demografische Daten sowie den **Persönlichkeitstyp**, den wir vorhersagen wollen.

Jede Zeile repräsentiert eine Person:

* **19 Fragen-Scores** (1–5)
* **Alter (age)**, **Geschlecht (gender)**, **Schreibhand (hand)**
* **Zielvariable (target)** — der Persönlichkeitstyp

> 💡 **Wo du die Daten erhältst:** Der Datensatz wird über einen Google-Drive-Link bereitgestellt. Der Link wird hier angegeben https://drive.google.com/drive/folders/1KhwTPAG07EdaENW_XX9nVvKhC-DP1Ags?usp=sharing. **Schreib diesen Link in deine README** (siehe §8), damit jeder die Daten als Ausgangspunkt zur Reproduktion deiner Arbeit abrufen kann.

### Was wir vorhersagen — Die Persönlichkeitstypen

Der Persönlichkeitstyp basiert auf den fünf OCEAN-Merkmalen. Die ursprüngliche Formulierung dieser Aufgabe hat **fünf** Persönlichkeitstypen — aber **einer davon wurde aus unserem Datensatz entfernt**. Unsere Daten enthalten daher **nur vier** Typen, und dein Modell soll **genau diese vier Klassen** vorhersagen:

| Typ | In Kürze |
| --- | --- |
| **Moderat** | Ausgeglichen – keine extremen Merkmale |
| **Resilient** | Emotional stabil, ruhig unter Druck |
| **Überkontrolliert** | Ängstlich und introvertiert |
| **Unterkontrolliert** | Impulsiv, kümmert sich weniger um Regeln |

> ⚠️ **Hinweis:** Du wirst vier Klassen in der Zielspalte sehen, nicht fünf. Das ist beabsichtigt. Such nicht nach dem fehlenden Typ – er ist nicht in deinen Daten enthalten, und dein Modell muss ihn nicht vorhersagen.

---

## 5. Die Reise, von Anfang bis Ende

Deine Reise durch dieses Projekt folgt einem natürlichen Bogen des maschinellen Lernens: Du erkundest die Daten, erstellst eine robuste Vorverarbeitungspipeline, trainierst und vergleichst verschiedene Modelle, um die vielversprechendsten Kandidaten zu finden, optimierst deren Hyperparameter und speicherst schließlich dein leistungsstärkstes Modell permanent ab, um Vorhersagen über eine Streamlit-Webanwendung bereitzustellen.

---

## 6. Speichern deines besten Modells — `joblib` (offiziell) oder MLflow (optional)

Sobald du deine Modelle trainiert und optimiert hast, musst du **das beste auswählen und persistieren** (mithilfe von **`joblib`** oder optional **MLflow**), damit deine Streamlit-App es laden kann.

> ⚠️ **Wichtige Regel für die Reproduzierbarkeit:**
> Die trainierte Modelldatei selbst **darf NICHT in dein GitHub-Repository committed werden**. Stattdessen muss dein Repository alles enthalten, was erforderlich ist, um das Modell von Grund auf neu zu **rekreieren**. Um sicherzustellen, dass jeder, der deine Notebooks ausführt, genau dieselben Ergebnisse erzielt und dieselbe Modelldatei generiert, **musst du bei jedem einzelnen Schritt, der Zufälligkeit beinhaltet, feste Zufalls-States verwenden (`random_state=...`)** (z. B. Train-Test-Splits, Modellinitialisierung, Mischen, Randomized Search).

### Offizieller Ansatz — Speichern deines Modells mit `joblib`

> **Wichtig:** Speichere die **gesamte Pipeline** (Vorverarbeitung + Modell), nicht nur den Schätzer (Estimator). Dies garantiert, dass rohe Benutzereingaben zum Zeitpunkt der Vorhersage exakt genauso transformiert werden wie während des Trainings.

**Speichern und Laden einer Pipeline mit `joblib`:**

```python
import joblib

# 'best_pipeline' ist deine trainierte scikit-learn Pipeline
# (Vorverarbeitungsschritte + der finale Schätzer, bereits trainiert)
joblib.dump(best_pipeline, "models/personality_pipeline.joblib")

# Später – oder innerhalb deiner Streamlit-App – wieder laden:
loaded_pipeline = joblib.load("models/personality_pipeline.joblib")

# Direkt aus Rohdaten vorhersagen (die Pipeline übernimmt die Vorverarbeitung):
prediction = loaded_pipeline.predict(new_data)
```

Importiere dieses Modell anschließend in Streamlit. Deine `app.py` sollte die gespeicherte Pipeline laden und zur Bereitstellung von Vorhersagen nutzen:

```python
import joblib
import pandas as pd
import streamlit as st

# Die trainierte Pipeline einmal beim Start laden
pipeline = joblib.load("models/personality_pipeline.joblib")

# ... die 19 Antworten des Benutzers + Alter, Geschlecht, Hand in ein DataFrame sammeln ...
# (Spaltennamen und -reihenfolge müssen exakt zu den Trainingsdaten passen!)
input_df = pd.DataFrame([user_answers])

# Vorhersage ausgeben
prediction = pipeline.predict(input_df)[0]
st.write(f"Vorhergesagter Persönlichkeitstyp: **{prediction}**")
```

> ⚠️ **Achtung:** Die Spalten deines `input_df` müssen **exakt dieselben Namen** (und dieselben Datentypen) haben wie die Daten, auf denen deine Pipeline trainiert wurde. Das ist die häufigste Ursache für eine App, die nicht funktioniert. Prüfe das, bevor du deine Pipeline speicherst.

### So wählst du dein bestes Modell bei der Verwendung von Joblib

Während der Hyperparameter-Optimierung und des Modellvergleichs trainierst du verschiedene Konfigurationen (mindestens 3 verschiedene Modelle, jeweils mit Tuning). Vergleiche die Modelle anhand des **`f1_macro`-Scores** auf deinen Validierungs- oder Testdatensätzen (optional ergänzt um Accuracy, eine Confusion Matrix oder weitere Metriken), um festzustellen, welche Konfiguration am besten abgeschnitten hat.

Schreibe am Ende des Notebooks, in dem du dein finales Modell evaluierst, einen detaillierten abschließenden Absatz, der deine Entscheidung dokumentiert. Zum Beispiel:

> *"Nach der Evaluierung mehrerer Baseline-Modelle zeigte der Random Forest Classifier die stärkste anfängliche Leistung. Nach der Hyperparameter-Optimierung über RandomizedSearchCV (beim Testen verschiedener Konfigurationen von `n_estimators`, `max_depth` und `min_samples_split`) erzielte die Konfiguration mit `n_estimators=200` und `max_depth=15` den höchsten `f1_macro`-Score von 0,83 auf dem Testdatensatz (bei einer Accuracy von 84,2 %). Im Vergleich zu den Standardparametern reduzierte dieses Setup erfolgreich das Overfitting bei gleichbleibend starker Verallgemeinerung, weshalb es als finale Pipeline für das Deployment ausgewählt wurde."*

Dieser Absatz ist deine Entscheidungsdokumentation. Er erfüllt denselben Zweck wie die MLflow-Benutzeroberfläche für dich.

### Über die Hyperparameter-Optimierung

Du kannst jede gewünschte Optimierungsstrategie verwenden: `GridSearchCV`, `RandomizedSearchCV` oder `hyperopt`. Es gibt keine vorgeschriebene Methode.

*Hinweis:* Welche Hyperparameter optimiert werden sollen, wie viele und in welchen Bereichen, ist ein eigenes Thema für sich — und es ist nicht der Schwerpunkt dieses Projekts. Es steht dir frei, diejenigen Hyperparameter, Mengen und Werte auszuwählen, die du für jedes Modell interessant findest.

### Optionale Alternative — MLflow

Wenn du möchtest, kannst du MLflow verwenden, um deine Läufe, Parameter, Metriken und Modelle zu protokollieren. Führe die MLflow-Benutzeroberfläche aus, um Experimente zu vergleichen und dein bestes Modell auszuwählen. Dies ist nicht erforderlich und es gibt keine Bonuspunkte dafür – es ist einfach eine Alternative, falls du bereits mit dem Tool vertraut bist.

Das Ergebnis bleibt in jedem Fall dasselbe: ein gespeichertes bestes Modell, das deine App lädt und bereitstellt.

---

## 7. Die Streamlit-App — Was erwartet wird

### Zweck

Die App ist das „Produktionsende“ des Projekts. Sie soll ein einfaches Tool sein, bei dem eine Person den Fragebogen beantwortet und ihren vorhergesagten Persönlichkeitstyp erhält.

> ⚠️ **Wichtiger Hinweis zum Umfang der App:**
> **Die Streamlit-App ist NICHT der Ort zum Speichern von Daten oder zum Trainieren von Modellen.** Die App sollte strikt davon ausgehen, dass das Modell bereits über deine Notebooks trainiert und gespeichert wurde. Ihr einziger Zweck besteht darin, die gespeicherte `joblib`-Modelldatei zu laden, die Benutzeroberfläche bereitzustellen, Eingaben zu sammeln und Echtzeit-Vorhersagen bereitzustellen.

### Läuft lokal — Keine Bereitstellung (Deployment) erforderlich

* Die App läuft lokal auf deinem Computer.
* Du musst sie nicht online bereitstellen.
* Kein Cloud-Hosting, keine öffentliche URL, keine Server-Einrichtung.
* Es reicht aus, dass die App auf deinem Computer läuft und jeder sie starten kann, indem er deiner README folgt.
* Der Sinn besteht darin, die Produktionserfahrung zu simulieren, keinen Live-Dienst zu hosten.

### Was die App tun muss

1. Die 19 Fragen so präsentieren, dass der Benutzer jede einzelne beantworten kann (z. B. auf einer Skala von 1 bis 5).
2. Die Eingaben für Alter, Geschlecht und Hand erfassen.
3. Dein gespeichertes Modell laden (die Joblib-Pipeline oder dein MLflow-Modell).
4. Die Vorhersage ausführen und dem Benutzer den vorhergesagten Persönlichkeitstyp anzeigen.

### Was dir überlassen bleibt

Alles andere. Wie die App aussieht und wie sie funktioniert, ist ganz deine Entscheidung. Dazu gehören das Layout, die Wortwahl, die verwendeten Widgets, ob du einen Konfidenzwert anzeigst, ob du einen Titel und eine Beschreibung hinzufügst, wie du sie stylst und so weiter. Es gibt kein vorgeschriebenes Design. Bau etwas, das funktioniert und das du stolz vorzeigen kannst. (Falls deine App irgendwo irgendetwas mit dem Ozean enthält — ein Bild, einen Fisch, eine Anspielung, ganz egal — gibt es +1 Extrapunkt von 100. Das hat überhaupt nichts mit dem Projekt zu tun, sondern nur damit, dass ich das Meer vermisse.)

---

## 8. Das Deliverable — Ein reproduzierbares GitHub-Repository

Du reichst das gesamte Projekt als GitHub-Repository ein. Die Messlatte ist einfach:

> **Jemand anderes sollte in der Lage sein, dein Repository zu klonen, deine Arbeit von Grund auf neu zu reproduzieren (beginnend mit dem Google-Drive-Link), deine Notebooks nacheinander auszuführen, um die Modelldatei neu zu generieren, und deine Streamlit-App erfolgreich zu starten** — alles, ohne dir eine einzige Frage zu stellen.

⚠️ **Es werden KEINE Daten oder Modelldateien in deinem Repository sein.** Dein Repository darf weder den Datensatz noch das kompilierte `joblib`-Modell enthalten. Jeder, der deine Arbeit reproduziert, lädt die Daten selbst über deinen Drive-Link herunter und erstellt das Modell neu, indem er deine Notebooks ausführt (was aufgrund fester Zufalls-States zuverlässig gelingt).

### Was dein Repository enthalten muss

* **Eine gute `README.md`** — die Eingangstür deines Projekts, komplett mit vollständigen Reproduktions- und Einrichtungsschritten. Siehe §9 für die erforderliche Struktur.
* **`requirements.txt`** — jede Bibliothek, die dein Projekt benötigt, damit jeder seine Umgebung mit `pip install -r requirements.txt` nachbauen kann. Pinne die Versionen, die du tatsächlich verwendet hast.
* **Deine Notebooks oder Skripte** — den Code, der deinen Workflow dokumentiert (EDA, Pipeline-Erstellung, Modellierung und Tuning) unter Verwendung fester `random_state`-Parameter.
* **Die Streamlit-App (`app.py`)** — die Web-App, die dein generiertes Modell lädt und Vorhersagen bereitstellt, zusammen mit ausdrücklichen Anweisungen in deiner README zum Ausführen.

### Beispiel für die Projektstruktur

> ⚠️ **WICHTIG — Hinweis zur Ordnerstruktur:**
> Das untenstehende Layout ist **nur ein Beispiel**. Es gibt **keine Notebooks, die du haben musst, und keine, die du nicht haben darfst**. Ordner, Dateinamen und die Anzahl der Notebooks entscheidest du selbst. Organisiere dein Projekt so, wie du willst — **solange jemand anderes jeden einzelnen Schritt, den du gemacht hast, nachvollziehen und reproduzieren kann, um am Ende eine funktionierende Streamlit-App zu erhalten.** Welche Bestandteile in irgendeiner Form vorhanden sein müssen, steht in der Checkliste in §2.

```text
personality-predictor/
├── README.md
├── requirements.txt
├── .gitignore
├── data/                       # NICHT committet — per README-Drive-Link herunterladen
├── notebooks/                  # Nur ein Beispiel — Struktur/Namen liegen bei dir
│   ├── 01_eda.ipynb
│   ├── 02_pipeline.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_tuning.ipynb
├── models/                     # NICHT committet — wird durch Ausführen der Notebooks generiert
└── app.py
```

> 💡 **Tipp:** Committe keine Wegwerf-Artefakte. Dinge wie `mlflow.db`, `mlruns/`, `mlartifacts/`, `__pycache__/` und dein Ordner für die virtuelle Umgebung werden beim Ausführen des Projekts generiert – füge sie stattdessen zu einer `.gitignore` hinzu.

---

## 9. Die README — Erforderliche Struktur

Deine `README.md` ist die wichtigste Datei in deinem Repository. Sie muss mindestens diese beiden Abschnitte in dieser Reihenfolge enthalten:

### 1. Überblick (Overview)

Erkläre das Projekt jemandem, der es noch nie gesehen hat. Decke ab:

* **Was das Projekt tut** — Vorhersage eines Persönlichkeitstyps anhand eines kurzen Fragebogens.
* **Das Problem** — Was wir vorhersagen und warum (eine überwachte Klassifikationsaufgabe).
* **Der Datensatz** — Wo er herkommt, was eine Zeile repräsentiert, die 19 Fragen plus Demografie und die Zielklassen (Moderat, Resilient, Überkontrolliert und Unterkontrolliert).
* **Der Ansatz** — Kurz der Workflow: EDA → Vorverarbeitungspipeline → Modellierung und Tuning → Speichern des besten Modells → Streamlit-App.
* **Das Ergebnis** — Dein bestes Modell, die verwendete Metrik und deren Score.
* **So verwendest du die App** — Ein oder zwei Sätze dazu, was der Benutzer tut und was er erhält.

### 2. Einrichtung (Setup)

Schritt-für-Schritt-Anweisungen für die vollständige End-to-End-Reproduzierbarkeit. Gehe davon aus, dass der Leser dein Repository gerade geklont hat und sonst nichts besitzt. Füge die genauen Befehle in der richtigen Reihenfolge ein:

1. **Daten beschaffen** — Stelle den Google-Drive-Link als Ausgangspunkt zur Verfügung und gib genau an, wo die Datei lokal abgelegt werden soll (z. B. in einem `data/`-Ordner).
2. **Umgebung erstellen** — Z. B. eine virtuelle Umgebung erstellen und aktivieren.
3. **Abhängigkeiten installieren** — Führe `pip install -r requirements.txt` aus.
4. **Notebooks ausführen** — Führe deine Notebooks in der korrekten sequenziellen Reihenfolge aus, um die Datenexploration, Pipeline-Erstellung, das Training und die Modellgenerierung vollständig zu reproduzieren (unter Nutzung fester Zufalls-States).
5. **Streamlit-App lokal starten** — Gib den genauen Befehl an, um die App auf dem Rechner zu starten, z. B.:

   ```bash
   streamlit run app.py
   ```

---

## 10. Präsentation

* **Datum & Uhrzeit:** Freitag, 9. Oktober 2026, um 09:45 Uhr.
* **Abgabefrist für das Repository:** Lade den Link zu deinem GitHub-Repository spätestens um **09:44 Uhr** hoch.

  > ⚠️ **Wichtig:** Stell sicher, dass die Sichtbarkeit deines Repositorys auf **öffentlich** (public) und nicht auf privat eingestellt ist, damit es überprüft werden kann.

* **Dauer:** Die genaue Zeit, die für jede Präsentation zur Verfügung steht, wird im Unterricht bekannt gegeben – abhängig von der Gesamtzahl der Gruppen.
* **Format:**
  * **Es sind keine Folien erforderlich.**
  * Dies ist **keine Code-Durchsprache oder -Erklärung**.
  * Stattdessen sollte sich die Präsentation auf folgendes konzentrieren:
    1. Einen Überblick über deine Ergebnisse.
    2. Eine Erklärung deiner EDA-Ergebnisse.
    3. Die verwendeten Modelle.
    4. Die getesteten Hyperparameter.
    5. Die verwendeten Evaluationsmetriken und erzielten Scores.
    6. Eine Live-Demonstration deiner Streamlit-App.
