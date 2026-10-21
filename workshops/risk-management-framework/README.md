# Cybersecurity Risk Management Framework

**Type:** Workshop deliverable (presentation)  
**Role:** Cybersecurity Analyst  
**Context:** Designing a risk management framework for a mid-sized organization

---

## Overview

A self-contained framework for handling cyber risk end to end, built around a
continuous five-step cycle: **Identify → Assess → Treat → Accept → Monitor.**
The deck walks through each step, compares the methods available at every stage,
and makes an explicit, justified recommendation rather than just listing options.

The focus is decision-making under real-world constraints (limited budget and
staff, regulatory pressure from GDPR / NIS2 / ISO 27001) and translating
technical findings into business-level risk decisions.

## What it covers

- **Risk identification:** threat modeling vs. vulnerability assessment vs.
  incident review — compared by coverage of external, insider and human-error
  threats, and combined into a layered approach.
- **Risk assessment:** a 5×5 likelihood × impact model with concrete,
  euro-denominated impact criteria (financial, operational, reputational/legal),
  plus a qualitative risk matrix vs. quantitative **ALE / FAIR** comparison
  (incl. a worked `ALE = SLE × ARO` example).
- **Risk treatment:** mitigation vs. transfer, with selection logic
  (avoid → mitigate → transfer → accept) driven by tolerability and ROSI.
- **Risk acceptance:** score-band-based approval authority, from risk owner up
  to executive escalation, with defined review cadences.
- **Monitoring:** automated (SIEM / IDS/IPS / EDR) vs. periodic assessments, and
  a tiered hybrid model (continuous / monthly / quarterly / annual).

## Why this matters for security work

Finding a vulnerability is only the first step; the real question is how urgent
it is, what it would cost the business, how to treat it, and who signs off on the
residual risk. This workshop shows I can frame technical findings in those terms
and connect a single finding to prioritization, treatment and governance.

## Key concepts

Risk cycle, likelihood/impact scoring, qualitative vs. quantitative risk analysis
(risk matrix, ALE, FAIR), ROSI, risk appetite and tolerance, residual risk,
risk register, KRIs, MITRE-aligned triggers for out-of-cycle review.

## File

- [`Cyber_Risk_Management_Framework.pdf`](./Cyber_Risk_Management_Framework.pdf)

> Thresholds and figures in the deck are illustrative example values, meant to be
> calibrated to a given organization's revenue and risk appetite.
