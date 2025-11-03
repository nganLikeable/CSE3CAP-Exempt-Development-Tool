# Exempt Development Assessment Tool  
### Rule-Based Compliance Checker for Small-Scale Residential Structures 

## Overview  
The **Exempt Development Assessment Tool** is a rule-based web application built to assist **Albury City Council** staff and residents in determining whether a proposed residential structure (e.g., **shed**, **patio**, **carport**, or **retaining wall**) qualifies as *Exempt Development* under **SEPP 2008 – Part 2**.

The system uses a **Flask backend** with **HTML/JS frontend** to process user inputs, evaluate them against SEPP clauses, and display compliance outcomes with detailed explanations. It streamlines early-stage planning checks and reduces manual review effort for council teams.

---

## Core Objectives
- Automate the SEPP compliance check for minor structures.  
- Provide instant feedback — *Exempt*, *Non compliant (Requires DA)*, or *Manual Review*.  
- Offer clause-based transparency for staff and residents.  
- Support learning and consistency in applying SEPP planning rules.

---

## Key Features
- **Rule-based validation engine** for SEPP clause checks.  
- **Integrated property dataset** with zoning and overlay attributes.  
- **Quiz-style form** for structure details (type, height, location, setbacks).  
- **Clause justification panel** explaining results.  
- **Flask backend API** managing inputs and results.  
- **Council portal** planned for future integration.  

---

## Tech Stack

| Layer | Technology | Description |
|-------|-------------|-------------|
| Frontend | HTML, CSS, JavaScript | User interface and map view |
| Backend | Python Flask | Handles rule validation and responses |
| Database | SQLite | Stores property data and SEPP rules |
| Tools | GitHub, Jira, Confluence | Version control, task tracking, documentation |

---

## System Flow

```text
User Input → Flask Backend → SEPP Rule Validation → Clause Reference → Result Output
```

## Getting Started
```
Step 1: Clone the Repository

git clone https://github.com/nganLikeable/cap-exempt-dev.git
cd cap-exempt-dev

Step 2: Setup Virtual Environment

python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run the App
flask --app app.py run
```

## Sample Property Example
```
{
  "id": "001",
  "address": "12 Wattle Street, Albury",
  "zone": "R1",
  "lotSize_m2": 700,
  "bushfireProne": false,
  "heritageListed": false,
  "cornerLot": false,
  "proposal": {
    "type": "shed",
    "width_m": 3,
    "length_m": 4,
    "height_m": 2.4,
    "attachedToDwelling": false,
    "setbackSide_m": 0.9,
    "setbackRear_m": 1.0
  }
}
```

## Project Milestones

Sprint 1: Project setup, SEPP research, basic HTML layout
Sprint 2: Flask backend, property dataset integration
Sprint 3: UI refinement, validation engine implementation
Sprint 4: QA testing, documentation, clause justification
Sprint 5: Final fixes, council user guide, presentation


## Tools We Used
```
	•	GitHub → Version control, collaboration, issue tracking
	•	Jira → Sprint planning, velocity charts, burndown tracking
	•	Confluence → Meeting notes, property samples, SEPP clause validation logs
	•	VS Code → Development environment
```

## Contributors

Jason Bennett - Fronetend - UI logic, JS functions, validation interface
Devjoy Chakma - Frontend & Integration - JS Function & map integration
Ngoc Kim Ngan Nguyen - Frontend & Backend - Flask setup, database design, SEPP logic
Nicholas Mclntyre - QA & Testing - Rule verification, documentation, error testing
Komal Sharma - Data analyst - Data collection and testing.

## Example Use

Scenario:
A resident wants to build a 3×4 m shed in their rear yard on a 650 m² lot in Zone R1.

Steps:
	1.	Select the property from the sample list or input manually.
	2.	Enter structure type: Shed, dimensions = 3×4 m, height = 2.4 m.
	3.	Input location = Rear, setbacks > 0.9 m.
	4.	Click Check Exempt Status.

Result:
 Exempt under Clause 2.18 (setbacks and height comply).


 Feedback

Found a bug or have suggestions?
Open an issue or submit a pull request.








