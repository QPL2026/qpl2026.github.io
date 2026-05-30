---
title: Program
permalink: /program/
---

<style>
  .program-table {
    width: 100%;
    margin-left: auto;
    margin-right: auto;
    table-layout: fixed;
  }

  .program-table td,
  .program-table th {
    text-align: center;
    vertical-align: middle;
    overflow-wrap: break-word;
  }

  .program-table td.empty-cell {
    background-image:
      linear-gradient(
        45deg,
        transparent calc(50% - 1px),
        rgba(0, 0, 0, 0.18) calc(50% - 1px),
        rgba(0, 0, 0, 0.18) calc(50% + 1px),
        transparent calc(50% + 1px)
      ),
      linear-gradient(
        -45deg,
        transparent calc(50% - 1px),
        rgba(0, 0, 0, 0.18) calc(50% - 1px),
        rgba(0, 0, 0, 0.18) calc(50% + 1px),
        transparent calc(50% + 1px)
      );
    background-repeat: no-repeat;
  }

  .program-table td.parallel-session {
    background-color: #f6e58d;
  }

  .program-table a {
    color: #0b1f3a;
    text-decoration: underline;
  }

  .program-table a:hover,
  .program-table a:focus {
    color: #000;
  }

  .talk-details {
    margin: 1.5rem 0;
  }

  .talk-details details {
    margin-top: 0.75rem;
    padding: 0.9rem 1rem;
    border: 1px solid #d9d9d9;
    border-radius: 0.75rem;
    background-color: #fafafa;
  }

  .talk-details summary {
    cursor: pointer;
    font-weight: 700;
  }

  .talk-details p {
    margin: 0.85rem 0 0;
  }

  .schedule-table {
    width: 100%;
    margin: 1rem auto 1.5rem;
    border-collapse: collapse;
    table-layout: fixed;
  }

  .schedule-table td,
  .schedule-table th {
    border: 1px solid #333;
    padding: 0.45rem 0.5rem;
    text-align: center;
    vertical-align: middle;
    overflow-wrap: break-word;
    font-size: 1.05rem;
  }

  .schedule-table col.time-col {
    width: 7.5em;
  }

  /* On narrow screens (phones) the time range eats a lot of horizontal
     space, leaving little room for the talk titles. Shrink the time
     column and let the range wrap onto multiple lines instead. */
  @media (max-width: 600px) {
    .schedule-table col.time-col {
      width: 4.25em;
    }

    .schedule-table td:first-child {
      overflow-wrap: anywhere;
      word-break: break-word;
      padding-left: 0.3rem;
      padding-right: 0.3rem;
    }
  }

  .schedule-table .band {
    background-color: #dfeefa;
    font-size: 1rem;
    font-weight: 700;
  }

  .schedule-table .break-row {
    background-color: #e8eef5;
    font-weight: 700;
  }

  .schedule-table .talk-authors {
    display: block;
    font-size: 1em;
  }

  .schedule-table .talk-title {
    display: block;
    margin-top: 0.2rem;
    color: #7e1b1b;
    font-weight: 700;
    font-size: 1em;
  }

  /* Titles with a paper link keep the same dark red, but are
     underlined and carry a paper icon so they are visually
     distinct from titles that have no paper. */
  .schedule-table .talk-title a {
    color: #7e1b1b;
    text-decoration: underline;
  }

  .schedule-table .talk-title a:hover,
  .schedule-table .talk-title a:focus {
    color: #5a1313;
  }

  .schedule-table .talk-title a::after {
    content: "\1F4C4";
    font-size: 0.85em;
    text-decoration: none;
    display: inline-block;
    margin-left: 0.35em;
  }

  /* Collapsible per-day schedule sections */
  .day-section {
    margin: 1.25rem 0;
    border: 1px solid #cdd7e0;
    border-radius: 0.75rem;
    overflow: hidden;
  }

  .day-section > summary {
    cursor: pointer;
    list-style: none;
    padding: 0.85rem 1.25rem;
    background-color: #dfeefa;
    color: #0b1f3a;
    font-size: 1.35rem;
    font-weight: 700;
  }

  .day-section > summary::-webkit-details-marker {
    display: none;
  }

  .day-section > summary::after {
    content: "\25B8";
    float: right;
    font-size: 1rem;
    line-height: 1.6;
  }

  .day-section[open] > summary {
    border-bottom: 1px solid #cdd7e0;
  }

  .day-section[open] > summary::after {
    content: "\25BE";
  }

  .day-section .day-body {
    padding: 0.75rem 1.25rem 1.25rem;
  }

  /* Tighten the gap between the day header and its first table */
  .day-section .day-body > .schedule-table:first-child {
    margin-top: 0;
  }

  /* "Go to today's talk" button */
  .today-button {
    display: inline-block;
    margin: 0.5rem 0 1rem;
    padding: 0.6rem 1.3rem;
    background-color: #0b1f3a;
    color: #fff;
    border: none;
    border-radius: 0.5rem;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
  }

  .today-button:hover,
  .today-button:focus {
    background-color: #16335f;
  }

  .today-note {
    margin: 0 0 1rem;
    font-size: 0.9rem;
    color: #555;
  }
</style>


Below you can find an overview of the conference schedule. Here is the <a href="{{ '/assets/pdfs/QPL_2026_Program.pdf' | relative_url }}" target="_blank" rel="noopener">full schedule in table formatting</a>. 

<p>
  <button type="button" id="today-talk-btn" class="today-button">📅 Go to today's talks</button>
</p>
<p class="today-note" id="today-note"></p>


<table class="program-table">
<colgroup>
<col width="15%" />
<col width="17%" />
<col width="17%" />
<col width="17%" />
<col width="17%" />
<col width="17%" />
</colgroup>
<tr>
  <td></td>
  <td><strong>Monday, August 17th</strong></td>
  <td><strong>Tuesday, August 18th</strong></td>
  <td><strong>Wednesday, August 19th</strong></td>
  <td><strong>Thursday, August 20th</strong></td>
  <td><strong>Friday, August 21st</strong></td>
</tr>
<tr>
  <td>8:50 – 9:30</td>
  <td>Registration</td>
  <td class="empty-cell"></td>
  <td class="empty-cell"></td>
  <td class="empty-cell"></td>
  <td class="empty-cell"></td>
</tr>
<tr>
  <td>9:30 – 10:15</td>
  <td rowspan="2" style="background-color: #7fcff4">Long Plenary Talks</td>
  <td rowspan="2" style="background-color: #7fcff4">Long Plenary Talks</td>
  <td rowspan="2" style="background-color: #7fcff4">Long Plenary Talks</td>
  <td rowspan="2" style="background-color: #7fcff4">Long Plenary Talks</td>
  <td rowspan="2" style="background-color: #7fcff4">Long Plenary Talks</td>
</tr>
<tr>
  <td>10:15 – 11:00</td>
</tr>
<tr>
  <td>11:00 – 11:30</td>
  <td colspan="5">Coffee Break</td>
</tr>
<tr>
  <td>11:30 – 11:55</td>
  <td rowspan="2" style="background-color: #bfe6cc">Short Plenary Talks</td>
  <td rowspan="2" style="background-color: #bfe6cc">Short Plenary Talks</td>
  <td rowspan="2">Industry Session</td>
  <td style="background-color: #bfe6cc">Short Plenary Talk</td>
  <td rowspan="2">Business Meeting</td>
</tr>
<tr>
  <td>11:55 – 12:20</td>
  <td>Conference Photo</td>
</tr>
<tr>
  <td>12:30 – 14:30</td>
  <td colspan="5">Lunch Break</td>
</tr>
<tr>
  <td>14:30 – 14:55</td>
  <td rowspan="3" class="parallel-session">Parallel Sessions</td>
  <td rowspan="3" class="parallel-session">Parallel Sessions</td>
  <td rowspan="3" class="parallel-session">Parallel Sessions</td>
  <td rowspan="5" class="parallel-session">Parallel Sessions<br>14:30 – 16:10</td>
  <td rowspan="3" class="parallel-session">Parallel Sessions</td>
</tr>
<tr>
  <td>14:55 – 15:20</td>
</tr>
<tr>
  <td>15:20 – 15:45</td>
</tr>
<tr>
  <td>15:45 – 16:15</td>
  <td colspan="3">Coffee Break</td>
  <td rowspan="1">Coffee Break</td>
</tr>
<tr>
  <td>16:15 – 16:40</td>
  <td rowspan="3" class="parallel-session">Parallel Sessions</td>
  <td rowspan="3" class="parallel-session">Parallel Sessions</td>
  <td rowspan="2" class="parallel-session">Parallel Sessions<br>16:15 – 17:05</td>
  <td rowspan="2" class="parallel-session">Parallel Sessions<br>16:15 – 17:05</td>
</tr>
<tr>
  <td>16:40 – 17:05</td>
  <td>Coffee Break</td>
</tr>
<tr>
  <td>17:05 – 17:30</td>
  <td class="empty-cell"></td>
  <td rowspan="3">TBA</td>
  <td rowspan="3">Goodbye!</td>
</tr>
<tr>
  <td rowspan="2"></td>
  <td rowspan="2" class="empty-cell"></td>
  <td rowspan="2" style="background-color: #f7c98b">Poster Session<br> 17:30 – 19:30 </td>
  <td>Boat Tour <br> 17:30 – 18:30 </td>
</tr>
<tr>
  <td>Conference Dinner <br> 19:00 onwards</td>
</tr>
</table>

<br />

<details class="day-section" id="day-monday" data-date="2026-08-17">
<summary>Monday, August 17th</summary>
<div class="day-body">

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
</colgroup>
<tr>
  <td>8:50 – 9:30</td>
  <td><strong>Registration</strong></td>
</tr>
<tr>
  <td class="band" colspan="2">Long plenary talks</td>
</tr>
<tr>
  <td>9:30 – 10:15</td>
  <td>
    <span class="talk-authors">Alex Maltesson, Ludvig Rodung, Niklas Budinger, Giulia Ferrini, Cameron Calcluth</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2510.08546" target="_blank" rel="noopener">Equivalence of continuous- and discrete-variable gate-based quantum computers with finite energy</a></span>
  </td>
</tr>
<tr>
  <td>10:15 – 11:00</td>
  <td>
    <span class="talk-authors">Raphaël Mothe, Jessica Bavaresco</span>
    <span class="talk-title">Efficient quantum-circuit simulation of classical control of causal order</span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="2">Coffee break</td>
</tr>
<tr>
  <td class="band" colspan="2">Short plenary talks</td>
</tr>
<tr>
  <td>11:30 – 11:55</td>
  <td>
    <span class="talk-authors">Vinicius Pretti Rossi, Beata Zjawin, Roberto D. Baldijão, David Schmid, John H. Selby, Ana Belén Sainz</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2510.20722" target="_blank" rel="noopener">How typical is contextuality?</a></span>
  </td>
</tr>
<tr>
  <td>11:55 – 12:20</td>
  <td>
    <span class="talk-authors">Dichuan Gao, Razin A. Shaikh, Aleks Kissinger</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2605.13993" target="_blank" rel="noopener">Graphical algebraic geometry: from ideals and varieties to qudit ZH completeness</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="2">Lunch break</td>
</tr>
</table>

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
<col />
<col />
</colgroup>
<tr>
  <td class="band"></td>
  <td class="band">Parallel A</td>
  <td class="band">Parallel B</td>
  <td class="band">Parallel C</td>
</tr>
<tr>
  <td>14:30 – 14:55</td>
  <td>
    <span class="talk-authors">Yìlè Yīng, Maria Ciudad Alanon, Daniel Centeno, Jacopo Surace, Marina Maciel Ansanelli, Ruizhi Liu, David Schmid, Robert Spekkens</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2506.08091" target="_blank" rel="noopener">On whether quantum theory needs complex numbers: the foil theories perspective</a></span>
  </td>
  <td>
    <span class="talk-authors">Tomoaki Kawano, Ryo Kashima</span>
    <span class="talk-title">Restricted negation in orthomodular logic</span>
  </td>
  <td>
    <span class="talk-authors">Alexandre Clément</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2602.06644" target="_blank" rel="noopener">A complete equational theory for real-Clifford+CH quantum circuits</a></span>
  </td>
</tr>
<tr>
  <td>14:55 – 15:20</td>
  <td>
    <span class="talk-authors">Timothée Hoffreumon, Mischa P. Woods</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.19208" target="_blank" rel="noopener">On the experimental falsification of real QT</a> / <a href="https://arxiv.org/pdf/2504.02808" target="_blank" rel="noopener">A real matrix theory consistent with QT</a> (merged)</span>
  </td>
  <td>
    <span class="talk-authors">Alexandru Baltag, Sonja Smets</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2307.01713" target="_blank" rel="noopener">Logic meets Wigner's friend (and their friends)</a></span>
  </td>
  <td>
    <span class="talk-authors">Xiaoning Bian, Sarah Meng Li, Neil J. Ross, John van de Wetering, Yuming Zhao</span>
    <span class="talk-title">A complete and natural rule set for multi-qudit Clifford circuits in all odd prime dimensions</span>
  </td>
</tr>
<tr>
  <td>15:20 – 15:45</td>
  <td>
    <span class="talk-authors">Roberto D. Baldijão, Marco Erba, David Schmid, John Selby, Ana Belén Sainz</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2602.16280" target="_blank" rel="noopener">Tomographically-nonlocal entanglement</a></span>
  </td>
  <td>
    <span class="talk-authors">Bert Lindenhovius, Vladimir Zamdzhiev</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2505.06069" target="_blank" rel="noopener">Operator spaces, linear logic and the Heisenberg–Schrödinger duality of quantum theory</a></span>
  </td>
  <td>
    <span class="talk-authors">Colin Blake</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.06466" target="_blank" rel="noopener">Completeness for prime-dimensional phase-affine circuits</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="4">Coffee break</td>
</tr>
<tr>
  <td>16:15 – 16:40</td>
  <td>
    <span class="talk-authors">Beata Zjawin, Marina Maciel Ansanelli, David Schmid, Yìlè Yīng, John H. Selby, Ciarán M. Gilligan-Lee, Ana Belén Sainz, Robert Spekkens</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2512.11209" target="_blank" rel="noopener">The resource theory of causal influence and knowledge of causal influence</a></span>
  </td>
  <td>
    <span class="talk-authors">Priyaa Varshinee Srinivasan, Jean-Simon Pacaud Lemay, Robin Cockett</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.13946" target="_blank" rel="noopener">Generalized inverses of quantum channels: a categorical perspective</a></span>
  </td>
  <td>
    <span class="talk-authors">Fedor Kuyanov, Aleks Kissinger</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.06764" target="_blank" rel="noopener">Efficient classical simulation of low-rank-width quantum circuits using ZX-calculus</a></span>
  </td>
</tr>
<tr>
  <td>16:40 – 17:05</td>
  <td>
    <span class="talk-authors">Leonardo Vaglini, Nasra Daher Ahmed, Ravi Kunjwal</span>
    <span class="talk-title">Causal inequalities witness non-stabilizerness without magic</span>
  </td>
  <td>
    <span class="talk-authors">Andre Kornell, Bert Lindenhovius</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2601.09685" target="_blank" rel="noopener">The category of quantum graphs is closed</a></span>
  </td>
  <td>
    <span class="talk-authors">Kwok Ho Wan, Zhenghao Zhong, Ainhoa Zapirain</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2509.08658" target="_blank" rel="noopener">Simulating magic state cultivation with few Clifford terms</a></span>
  </td>
</tr>
<tr>
  <td>17:05 – 17:30</td>
  <td>
    <span class="talk-authors">Carla Ferradini, Giulia Mazzola, V. Vilasini</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.12283" target="_blank" rel="noopener">Emergent causal order and time direction: bridging causal models and tensor networks</a></span>
  </td>
  <td>
    <span class="talk-authors">James Hefford</span>
    <span class="talk-title">Nuclearity and trace in monoidal bicategories with application to extended CFTs</span>
  </td>
  <td>
    <span class="talk-authors">Mark Koch</span>
    <span class="talk-title">Classical Clifford+T sampling without computing marginals</span>
  </td>
</tr>
</table>

</div>
</details>

<details class="day-section" id="day-tuesday" data-date="2026-08-18">
<summary>Tuesday, August 18th</summary>
<div class="day-body">

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
</colgroup>
<tr>
  <td class="band" colspan="2">Long plenary talks</td>
</tr>
<tr>
  <td>9:30 – 10:15</td>
  <td>
    <span class="talk-authors">Maximilian Rüsch, Aleks Kissinger, Benjamin Rodatz / Benjamin Rodatz, Boldizsár Poór, Aleks Kissinger</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2510.08477" target="_blank" rel="noopener">Completeness for fault equivalence of Clifford ZX diagrams</a> / <a href="https://arxiv.org/pdf/2506.17181" target="_blank" rel="noopener">Fault tolerance by construction</a></span>
  </td>
</tr>
<tr>
  <td>10:15 – 11:00</td>
  <td>
    <span class="talk-authors">Samson Abramsky, Rui Soares Barbosa, Carmen Constantin, Martti Karvonen</span>
    <span class="talk-title">Algebraic paradoxes in adaptive quantum computation</span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="2">Coffee break</td>
</tr>
<tr>
  <td class="band" colspan="2">Short plenary talks</td>
</tr>
<tr>
  <td>11:30 – 11:55</td>
  <td>
    <span class="talk-authors">Manuel Mekonnen, Thomas D. Galley, Markus P. Müller</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2502.17576" target="_blank" rel="noopener">Invariance under quantum permutations rules out parastatistics</a></span>
  </td>
</tr>
<tr>
  <td>11:55 – 12:20</td>
  <td>
    <span class="talk-authors">Marek Arsenault, Hlér Kristjánsson</span>
    <span class="talk-title">A higher-order perspective on quantum signal processing</span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="2">Lunch break</td>
</tr>
</table>

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
<col />
<col />
</colgroup>
<tr>
  <td class="band"></td>
  <td class="band">Parallel A</td>
  <td class="band">Parallel B</td>
  <td class="band">Parallel C</td>
</tr>
<tr>
  <td>14:30 – 14:55</td>
  <td>
    <span class="talk-authors">Andrey Boris Khesin, Sarah Meng Li, Boldizsár Poór, Benjamin Rodatz, John van de Wetering, Richie Yeung</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.05391" target="_blank" rel="noopener">SpiderCat: optimal fault-tolerant cat state preparation</a></span>
  </td>
  <td>
    <span class="talk-authors">Daniel Brod, Lorenzo Catani, Robert Spekkens</span>
    <span class="talk-title">The toy theory is the unique noncontextual theory satisfying \(A_1^3\)-symmetry</span>
  </td>
  <td>
    <span class="talk-authors">Matthew Wilson</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2512.10937" target="_blank" rel="noopener">Agent policies from higher-order causal functions</a></span>
  </td>
</tr>
<tr>
  <td>14:55 – 15:20</td>
  <td>
    <span class="talk-authors">Kwok Ho Wan, Henry Price, Qing Yao</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2601.04467" target="_blank" rel="noopener">Holographic codes seen through ZX-calculus</a></span>
  </td>
  <td>
    <span class="talk-authors">Tim Achenbach, Andreas Bluhm, Leevi Leppäjärvi, Ion Nechita, Martin Plávala</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2504.19865" target="_blank" rel="noopener">Factorization of multimeters: a unified view on nonclassical quantum phenomena</a></span>
  </td>
  <td>
    <span class="talk-authors">V. Vilasini, Lin-Qing Chen, Liuhang Ye, Renato Renner</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2505.21797" target="_blank" rel="noopener">Events and their localisation are relative to a lab</a></span>
  </td>
</tr>
<tr>
  <td>15:20 – 15:45</td>
  <td>
    <span class="talk-authors">Cole Comfort, Giovanni de Felice</span>
    <span class="talk-title">The delayed stabiliser ZX-calculus</span>
  </td>
  <td>
    <span class="talk-authors">Cihan Okay, Aziz Kharoof</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.19479" target="_blank" rel="noopener">The geometry of fiber products of probability polytopes</a></span>
  </td>
  <td>
    <span class="talk-authors">Zixuan Liu, Ognyan Oreshkov</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2512.08635" target="_blank" rel="noopener">Parity erasure: a foundational principle for indefinite causal order</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="4">Coffee break</td>
</tr>
<tr>
  <td>16:15 – 16:40</td>
  <td>
    <span class="talk-authors">Vincenzo Fiorentino, Kuntal Sengupta</span>
    <span class="talk-title">Superposition and its connections to uncertainty, entanglement and the quantum tensor product</span>
  </td>
  <td>
    <span class="talk-authors">Tom Williams, Mina Doosti, Farid Shahandeh</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2605.00975" target="_blank" rel="noopener">Sheaf-theoretic preparation contextuality via stochastic extension</a></span>
  </td>
  <td>
    <span class="talk-authors">Luca Apadula, Alexei Grinbaum, Časlav Brukner</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2604.02873" target="_blank" rel="noopener">Reference frames for process matrices: from coordinate parametrization to spacetime representation</a></span>
  </td>
</tr>
<tr>
  <td>16:40 – 17:05</td>
  <td>
    <span class="talk-authors">Gaurang Agrawal, Matt Wilson</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2511.21355" target="_blank" rel="noopener">Deriving the generalised Born rule from first principles</a></span>
  </td>
  <td>
    <span class="talk-authors">Theodoros Yianni, Farid Shahandeh, Nyan Raess</span>
    <span class="talk-title">Linear algebra of generalized contextuality in prepare-transform-measure scenarios</span>
  </td>
  <td>
    <span class="talk-authors">Yassine Benhaj, Kuntal Sengupta, Cyril Branciard</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2605.22807" target="_blank" rel="noopener">How many systems can be dephased before the quantum switch becomes causally definite?</a></span>
  </td>
</tr>
<tr>
  <td>17:05 – 17:30</td>
  <td>
    <span class="talk-authors">James Hefford, Matt Wilson</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2511.02772" target="_blank" rel="noopener">Quantum theory can decohere from a causally-indefinite post-quantum theory</a></span>
  </td>
  <td>
    <span class="talk-authors">David Schmid, Roberto D. Baldijão, John Selby, Ana Belen Sainz, Robert W. Spekkens</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2407.09624" target="_blank" rel="noopener">Noncontextuality inequalities for prepare-transform-measure scenarios</a></span>
  </td>
  <td>
    <span class="talk-authors">Raphaël Le Bihan, Alastair Abbott, Mnacho Echenim</span>
    <span class="talk-title">Probing the composition of processes with first-order-ISOMIX logic</span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="4" style="background-color: #f7c98b">Poster session (with reception) 17:30 – 19:30</td>
</tr>
</table>

</div>
</details>

<details class="day-section" id="day-wednesday" data-date="2026-08-19">
<summary>Wednesday, August 19th</summary>
<div class="day-body">

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
</colgroup>
<tr>
  <td class="band" colspan="2">Long plenary talks</td>
</tr>
<tr>
  <td>9:30 – 10:15</td>
  <td>
    <span class="talk-authors">Miriam Backens, Simon Perdrix / Miriam Backens</span>
    <span class="talk-title">Completeness for flow-preserving rewrite rules / Generating one-way computations with flow: flow-preserving rewriting that ignores the interpretation</span>
  </td>
</tr>
<tr>
  <td>10:15 – 11:00</td>
  <td>
    <span class="talk-authors">Quanlong Wang, Richard D. P. East, Razin A. Shaikh, Lia Yeh, Boldizsár Poór, Bob Coecke</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2511.06012" target="_blank" rel="noopener">Beyond Penrose tensor diagrams with the ZX calculus: applications to quantum computing, quantum machine learning, condensed matter physics, and quantum gravity</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="2">Coffee break</td>
</tr>
<tr>
  <td>11:30 – 12:20</td>
  <td><strong>Industry session</strong></td>
</tr>
<tr>
  <td class="break-row" colspan="2">Lunch break</td>
</tr>
</table>

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
<col />
<col />
</colgroup>
<tr>
  <td class="band"></td>
  <td class="band">Parallel A</td>
  <td class="band">Parallel B</td>
  <td class="band">Parallel C</td>
</tr>
<tr>
  <td>14:30 – 14:55</td>
  <td>
    <span class="talk-authors">Luca Apadula, Alessandro Bisio, Giulio Chiribella, Paolo Perinotti, Kyrylo Simonov</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2602.00856" target="_blank" rel="noopener">Higher-order transformations of bidirectional quantum processes</a></span>
  </td>
  <td>
    <span class="talk-authors">Nathan Claudet, Simon Perdrix</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2502.06566" target="_blank" rel="noopener">Insights in graph state entanglement via r-local complementation: structure and a quasi-polynomial algorithm</a></span>
  </td>
  <td>
    <span class="talk-authors">Pablo Arrighi, Doğukan Bakircioglu, Nathan Houyet</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.17581" target="_blank" rel="noopener">Quantum theory over dual-complex numbers</a></span>
  </td>
</tr>
<tr>
  <td>14:55 – 15:20</td>
  <td>
    <span class="talk-authors">Matthew Wilson, James Hefford, Timothée Hoffreumon</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2602.23865" target="_blank" rel="noopener">Supermaps on generalised theories</a></span>
  </td>
  <td>
    <span class="talk-authors">Piotr Mitosek, Miriam Backens</span>
    <span class="talk-title">Working with measurement-based computations on qudits</span>
  </td>
  <td>
    <span class="talk-authors">Nicolas Moulonguet, Augustin Vanrietvelde</span>
    <span class="talk-title">Subsystems as subsets of quantum channels, and the strange case of blind agents</span>
  </td>
</tr>
<tr>
  <td>15:20 – 15:45</td>
  <td>
    <span class="talk-authors">Samson Abramsky, Radha Jagadeesan</span>
    <span class="talk-title">Essential unitarity for higher-order quantum computation</span>
  </td>
  <td>
    <span class="talk-authors">Aleks Kissinger, John van de Wetering</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.09580" target="_blank" rel="noopener">ZX-flow: a flexible criterion for deterministic computation with ZX-diagrams</a></span>
  </td>
  <td>
    <span class="talk-authors">John Harding, Alexander Wilce</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.05627" target="_blank" rel="noopener">Classical explanations in (and of) general probabilistic theories</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="4">Coffee break</td>
</tr>
<tr>
  <td>16:15 – 16:40</td>
  <td>
    <span class="talk-authors">Thomas Bartsch, Yuhan Gai, Sakura Schäfer-Nameki</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2602.07110" target="_blank" rel="noopener">Beyond Wigner – how non-invertible symmetries preserve probabilities</a></span>
  </td>
  <td>
    <span class="talk-authors">Haytham McDowall-Rose, Razin A. Shaikh, Lia Yeh</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2505.06212" target="_blank" rel="noopener">From fermions to qubits: a ZX-calculus perspective</a></span>
  </td>
  <td>
    <span class="talk-authors">Amrapali Sen, Flavio Del Santo</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2601.15263" target="_blank" rel="noopener">Superluminal transformations and indeterminism</a></span>
  </td>
</tr>
<tr>
  <td>16:40 – 17:05</td>
  <td>
    <span class="talk-authors">Vanessa Brzić, Satoshi Yoshida, Mio Murao, Marco Túlio Quintino</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2510.20530" target="_blank" rel="noopener">Higher-order quantum computing with known input states</a></span>
  </td>
  <td>
    <span class="talk-authors">Lia Yeh, Jiaxin Huang, Aleks Kissinger, Sarah Meng Li, John van de Wetering</span>
    <span class="talk-title">A three-way normal form for stabiliser codes across ZX diagrams, circuits, and tableaus</span>
  </td>
  <td>
    <span class="talk-authors">Maarten Grothus, V. Vilasini</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2403.00916" target="_blank" rel="noopener">Impossibility of superluminal signalling rules out causal loops in conical spacetimes</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="4" style="background-color: #f7c98b">Boat tour 17:30 – 18:30</td>
</tr>
<tr>
  <td class="break-row" colspan="4" style="background-color: #f7c98b">Conference dinner starting 19:00</td>
</tr>
</table>

</div>
</details>

<details class="day-section" id="day-thursday" data-date="2026-08-20">
<summary>Thursday, August 20th</summary>
<div class="day-body">

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
</colgroup>
<tr>
  <td class="band" colspan="2">Long plenary talks</td>
</tr>
<tr>
  <td>9:30 – 10:15</td>
  <td>
    <span class="talk-authors">Cole Comfort, Robert I. Booth</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2511.22734" target="_blank" rel="noopener">Denotational semantics for stabiliser quantum programs</a></span>
  </td>
</tr>
<tr>
  <td>10:15 – 11:00</td>
  <td>
    <span class="talk-authors">Kathleen Barsse, Romain Péchoux, Simon Perdrix</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2507.10466" target="_blank" rel="noopener">Quantum control and general recursion beyond the unitary case</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="2">Coffee break</td>
</tr>
<tr>
  <td class="band" colspan="2">Short plenary talk</td>
</tr>
<tr>
  <td>11:30 – 11:55</td>
  <td>
    <span class="talk-authors">Aabhas Gulati, Ion Nechita, Clément Pellegrini</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2602.15800" target="_blank" rel="noopener">Entanglement in the Dicke subspace</a></span>
  </td>
</tr>
<tr>
  <td>11:55 – 12:20</td>
  <td><strong>Conference photo</strong></td>
</tr>
<tr>
  <td class="break-row" colspan="2">Lunch break</td>
</tr>
</table>

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
<col />
<col />
</colgroup>
<tr>
  <td class="band"></td>
  <td class="band">Parallel A</td>
  <td class="band">Parallel B</td>
  <td class="band">Parallel C</td>
</tr>
<tr>
  <td>14:30 – 14:55</td>
  <td>
    <span class="talk-authors">Arianne Meijer-van de Griend, Leo Becker</span>
    <span class="talk-title">Pauli gadget synthesis for gatesets with arbitrary even-arity Clifford gates</span>
  </td>
  <td>
    <span class="talk-authors">Haruki Emori</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2602.05821" target="_blank" rel="noopener">Quantum statistical functions</a></span>
  </td>
  <td>
    <span class="talk-authors">Nadish de Silva, Santanil Jana, Ming Yin</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2508.14673" target="_blank" rel="noopener">Three-qubit nonlocality paradoxes: beyond GHZ</a></span>
  </td>
</tr>
<tr>
  <td>14:55 – 15:20</td>
  <td>
    <span class="talk-authors">Soichiro Yamazaki, Seiseki Akibue</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.14202" target="_blank" rel="noopener">Multi-qubit controlled gate with optimal T-count</a></span>
  </td>
  <td>
    <span class="talk-authors">Michael Zurel, Jack Davis</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2602.22336" target="_blank" rel="noopener">Basis-independent stabilizerness and maximally noisy magic states</a></span>
  </td>
  <td>
    <span class="talk-authors">Shashaank Khanna, Matthew Pusey, Roger Colbeck</span>
    <span class="talk-title">Identifying causal structures which cannot support quantum correlations without fine-tuning</span>
  </td>
</tr>
<tr>
  <td>15:20 – 15:45</td>
  <td>
    <span class="talk-authors">Akash Kundu</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2505.09371" target="_blank" rel="noopener">Tensor and gadget reinforcement learning for improved, hardware-aware quantum architecture search</a></span>
  </td>
  <td>
    <span class="talk-authors">Cameron Calcluth, Oliver Hahn, Juani Bermejo Vega, Alessandro Ferraro, Giulia Ferrini</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2412.13136" target="_blank" rel="noopener">Classical simulation of circuits with realistic odd-dimensional Gottesman–Kitaev–Preskill states</a></span>
  </td>
  <td>
    <span class="talk-authors">C. E. Lopetegui-Gonzalez, G. Masse, E. Oudot, U. I. Meyer, F. Centrone, F. Grosshans, P. E. Emeriau, U. Chabaud, M. Walschaers</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2601.07686" target="_blank" rel="noopener">A unified framework for Bell inequalities from continuous-variable contextuality</a></span>
  </td>
</tr>
<tr>
  <td>15:45 – 16:10</td>
  <td>
    <span class="talk-authors">Mark Deaconu, Nihar Gargava, Amolak Ratan Kalra, Michele Mosca, Jon Yard</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2510.11526" target="_blank" rel="noopener">Buildings for synthesis with Clifford+R</a></span>
  </td>
  <td>
    <span class="talk-authors">Massimo Frigerio, Mattia Walschaers, Andrei Aralov, Carlos Ernesto Lopetegui-Gonzalez, Emilie Gillet</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2507.19397" target="_blank" rel="noopener">Algebraic techniques for photonic state preparation and characterization</a></span>
  </td>
  <td>
    <span class="talk-authors">Martin J. Renner, Edwin Peter Lobo, Arturo Konderak, Remigiusz Augusiak, Antonio Acín</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2604.26605" target="_blank" rel="noopener">Full nonlocality for non-maximally entangled states</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="4">Coffee break 16:10 – 16:40</td>
</tr>
<tr>
  <td class="break-row" colspan="4" style="background-color: #f7c98b">Career fair 16:40 – 19:00</td>
</tr>
</table>

</div>
</details>

<details class="day-section" id="day-friday" data-date="2026-08-21">
<summary>Friday, August 21st</summary>
<div class="day-body">

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
</colgroup>
<tr>
  <td class="band" colspan="2">Long plenary talks</td>
</tr>
<tr>
  <td>9:30 – 10:15</td>
  <td>
    <span class="talk-authors">Thea Li, Vladimir Zamdzhiev</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2601.15832" target="_blank" rel="noopener">Quantum coherence spaces revisited: a von Neumann (co)algebraic approach</a></span>
  </td>
</tr>
<tr>
  <td>10:15 – 11:00</td>
  <td>
    <span class="talk-authors">Matilde Baroni, Dominik Leichtle, Ivan Šupić, Damian Markham, Marco Túlio Quintino</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2601.05158" target="_blank" rel="noopener">Composable simultaneous purification: when all communication scenarios reduce to spatial correlations</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="2">Coffee break</td>
</tr>
<tr>
  <td>11:30 – 12:20</td>
  <td><strong>Business meeting</strong></td>
</tr>
<tr>
  <td class="break-row" colspan="2">Lunch break</td>
</tr>
</table>

<table class="schedule-table">
<colgroup>
<col class="time-col" />
<col />
<col />
<col />
</colgroup>
<tr>
  <td class="band"></td>
  <td class="band">Parallel A</td>
  <td class="band">Parallel B</td>
  <td class="band">Parallel C</td>
</tr>
<tr>
  <td>14:30 – 14:55</td>
  <td>
    <span class="talk-authors">Simon Burton, Hussain Anwar</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2605.06251" target="_blank" rel="noopener">Meromorphic quantum computing</a></span>
  </td>
  <td>
    <span class="talk-authors">Noé Delorme, Simon Perdrix</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2508.21756" target="_blank" rel="noopener">Diagrammatic reasoning with control as a constructor, applications to quantum circuits</a></span>
  </td>
  <td>
    <span class="talk-authors">David Schmid, John H. Selby, Vinicius Pretti Rossi, Roberto D. Baldijão, Ana Belén Sainz</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2409.13024" target="_blank" rel="noopener">Shadows and subsystems of generalised probabilistic theories: when tomographic incompleteness is not a loophole for contextuality proofs</a></span>
  </td>
</tr>
<tr>
  <td>14:55 – 15:20</td>
  <td>
    <span class="talk-authors">Christine Li, Lia Yeh</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.04548" target="_blank" rel="noopener">Transversal AND in quantum codes</a></span>
  </td>
  <td>
    <span class="talk-authors">Chris Heunen, Robin Kaarsgaard, Louis Lemonnier</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2510.05032" target="_blank" rel="noopener">One rig to control them all</a></span>
  </td>
  <td>
    <span class="talk-authors">Jan-Åke Larsson</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2504.20816" target="_blank" rel="noopener">The contextual Heisenberg microscope</a></span>
  </td>
</tr>
<tr>
  <td>15:20 – 15:45</td>
  <td>
    <span class="talk-authors">Jin Ming Koh, Anqi Gong, Andrei C. Diaconu, Daniel Bochen Tan, Alexandra A. Geim, Michael J. Gullans, Norman Y. Yao, Mikhail D. Lukin, Shayan Majidy</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2601.20927" target="_blank" rel="noopener">Phantom codes: entangling logical qubits without physical operations</a></span>
  </td>
  <td>
    <span class="talk-authors">William Schober, Scott Wesley</span>
    <span class="talk-title">A complete equational theory for quantum circuits with generalized control</span>
  </td>
  <td>
    <span class="talk-authors">Daniel McNulty</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2511.15954" target="_blank" rel="noopener">Quantifying quantum measurement incompatibility via graph invariants</a></span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="4">Coffee break</td>
</tr>
<tr>
  <td>16:15 – 16:40</td>
  <td>
    <span class="talk-authors">Vivien Vandaele</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.12917" target="_blank" rel="noopener">Asymptotically optimal quantum circuits for comparators and incrementers</a></span>
  </td>
  <td>
    <span class="talk-authors">Sacha Cerf, Harold Ollivier</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2603.26875" target="_blank" rel="noopener">The perturbative method for quantum correlations</a></span>
  </td>
  <td>
    <span class="talk-authors">Raffaele D'Avino, Lorenzo Caramelli, Raja Yehia, Gabriel Senno, Roberto González Pousa, Antonio Acín, Tamás Kriváchy</span>
    <span class="talk-title">Device independent quantum key distribution with a single measurement per site</span>
  </td>
</tr>
<tr>
  <td>16:40 – 17:05</td>
  <td>
    <span class="talk-authors">Giuseppe De Riso, Giuseppe Catalano, Seth Lloyd, Vittorio Giovannetti, Dario De Santis</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2508.02855" target="_blank" rel="noopener">A resource-efficient quantum-walker quantum RAM</a></span>
  </td>
  <td>
    <span class="talk-authors">Subhendu Bikas Ghosh, Snehasish Roy Chowdhury, Guruprasad Kar, Arup Roy, Tamal Guha, Manik Banik</span>
    <span class="talk-title"><a href="https://arxiv.org/pdf/2310.16386" target="_blank" rel="noopener">Strong inequivalence of quantum nonlocal resources</a></span>
  </td>
  <td>
    <span class="talk-authors">Paul Becsi, Matthew Joseph Hoban</span>
    <span class="talk-title">Bounding classical and quantum correlations in Bayesian networks with quasiprobabilities</span>
  </td>
</tr>
<tr>
  <td class="break-row" colspan="4">End of QPL 2026. Goodbye!</td>
</tr>
</table>

</div>
</details>

{% comment %}
<div class="talk-details">
  <details id="monday-long-plenary-talks">
    <summary>Monday Long Plenary Talks 9:30 - 11:00</summary>
    <details>
      <summary><strong>9:30 - 10:15 </strong><a href="https://arxiv.org/pdf/2510.08546" target="_blank" rel="noopener">Equivalence of continuous- and discrete-variable gate-based quantum computers</a></summary>
      <p>
        <strong>Abstract.</strong> We examine the ability of gate-based continuous-variable quantum computers to outperform qubit or discrete-variable quantum computers. Gate-based continuous-variable operations refer to operations constructed using a polynomial sequence of elementary gates from a specific finite set, i.e., those selected from the set of Gaussian operations and cubic phase gates. Our results show that for a fixed energy of the system, there is no superpolynomial computational advantage in using gate-based continuous-variable quantum computers over discrete-variable ones. The proof of this result consists of defining a framework - of independent interest - that maps quantum circuits between the paradigms of continuous- to discrete-variables. This framework allows us to conclude that a realistic gate-based model of continuous-variable quantum computers, consisting of states and operations that have a total energy that is polynomial in the number of modes, can be simulated efficiently using discrete-variable devices. We utilize the stabilizer subsystem decomposition [Shaw et al., PRX Quantum 5, 010331] to map continuous-variable states to discrete-variable counterparts, which allows us to find the error of approximating continuous-variable quantum computers with discrete-variable ones in terms of the energy of the continuous-variable system and the dimension of the corresponding encoding qudits.
      </p>
      <p>
        <strong>Coauthors.</strong> Alex Maltesson, Ludvig Rodung, Niklas Budinger, Giulia Ferrini, Cameron Calcluth
      </p>
    </details>
    <details>
      <summary><strong>10:15 - 11:00 </strong>Efficient quantum-circuit simulation of classical control of causal order</summary>
      <p>
        <strong>Abstract.</strong> TBA
      </p>
      <p>
        <strong>Coauthors.</strong> Raphaël Mothe and Jessica Bavaresco
      </p>
    </details>
  </details>
  <details id="monday-short-plenary-talks">
    <summary>Monday Short Plenary Talks 11:30 - 12:20</summary>
    <details>
      <summary><strong>11:30 - 11:55 </strong><a href="https://arxiv.org/pdf/2510.20722" target="_blank" rel="noopener">How typical is contextuality?</a></summary>
      <p>
        <strong>Abstract.</strong> Identifying when observed statistics cannot be explained by any reasonable classical model is a central problem in quantum foundations. A principled and universally applicable approach to defining and identifying nonclassicality is given by the notion of generalized noncontextuality. Here, we study the typicality of contextuality -- namely, the likelihood that randomly chosen quantum preparations and measurements produce nonclassical statistics. Using numerical linear programs to test for the existence of a generalized-noncontextual model, we find that contextuality is fairly common: even in experiments with only a modest number of random preparations and measurements, contextuality arises with probability over 99%. We also show that while typicality of contextuality decreases as the purity (sharpness) of the preparations (measurements) decreases, this dependence is not especially pronounced, so contextuality is fairly typical even in settings with realistic noise. Finally, we show that although nonzero contextuality is quite typical, quantitatively high degrees of contextuality are not as typical, and so large quantum advantages (like for parity-oblivious multiplexing, which we take as a case study) are not as typical. We provide an open-source toolbox that outputs the typicality of contextuality as a function of tunable parameters (such as lower and upper bounds on purity and other constraints on states and measurements). This toolbox can inform the design of experiments that achieve the desired typicality of contextuality for specified experimental constraints.
      </p>
      <p>
        <strong>Coauthors.</strong> Vinicius P. Rossi, Beata Zjawin, Roberto D. Baldijão, David Schmid, John H. Selby, Ana Belén Sainz
      </p>
    </details>
    <details>
      <summary><strong>11:55 - 12:20 </strong><a href="https://arxiv.org/pdf/2605.13993" target="_blank" rel="noopener">Graphical algebraic geometry: From ideals and varieties to quantum calculi</a></summary>
      <p>
        <strong>Abstract.</strong> We introduce Graphical Algebraic Geometry (GAG), a family of diagrammatic languages extending the Graphical Linear Algebra programme. We construct several languages within this family and prove that they are universal and complete for the corresponding (co)span semantics of commutative algebras and affine varieties. This framework provides clear graphical representations of algebraic structures -- such as polynomials, ideals, and varieties -- enabling intuitive yet rigorous diagrammatic reasoning. We showcase two practical viewpoints on GAG. First, we show that instances of counting constraint satisfaction problem (#CSP) are recast as rewrite problems of closed diagrams in GAG. This means that deciding rewritability in GAG is #P-hard, and GAG can be viewed as a complete and compositional rewrite system for networks of polynomial constraints. Second, we characterize the qudit ZH calculus, a diagrammatic language for quantum computation, as an extension of Graphical Algebraic Geometry. This establishes the correspondence that Graphical Algebraic Geometry is to the ZH calculus what Graphical Linear Algebra is to the ZX calculus. Using this construction, we show that computing amplitudes in qudit ZH requires only a constant number of queries to a GAG oracle.
      </p>
      <p>
        <strong>Coauthors.</strong> Dichuan Gao, Razin A. Shaikh, Aleks Kissinger
      </p>
    </details>
  </details>
  <details id="tuesday-long-plenary-talks">
    <summary>Tuesday Long Plenary Talks 9:30 - 11:00</summary>
    <details>
      <summary><strong>9:30 - 10:15 </strong><a href="https://arxiv.org/pdf/2510.08477" target="_blank" rel="noopener">Completeness for fault equivalence of Clifford ZX diagrams</a> / <a href="https://arxiv.org/pdf/2506.17181" target="_blank" rel="noopener">Fault tolerance by construction</a></summary>
      <p>
        <strong>Abstract (Completeness for fault equivalence of Clifford ZX diagrams).</strong> Two circuits are considered to be equivalent under noise if the effect of faults on one circuit is no worse than the effect of faults on the other circuit. We call this relationship fault equivalence. Fault equivalence offers a way to transform circuits while provably preserving their fault-tolerant properties, enabling a framework for fault-tolerant circuit synthesis and optimisation that is correct by construction. The ZX calculus offers a diagrammatic way to represent and reason about quantum circuits and is a useful tool for manipulating circuits while preserving fault equivalence. For this, the usual set of ZX rewrites has to be restricted to not only preserve the underlying linear map represented by the diagram, but also fault equivalence.<br><br>
        In this work, we provide a set of ZX rewrites that are sound and complete for fault equivalence of Clifford ZX diagrams. This means that any equivalence that can be derived using the proposed rules is certain to be correct, and any correct equivalence can be derived using only these rules. For this, we utilise diagrammatic constructions called fault gadgets to reason about arbitrary, possibly correlated Pauli faults in ZX diagrams. Fault gadgets allow us to separate the diagram into a fault-free part, which captures the noise-free behaviour of a diagram, and a noisy part that enumerates the effects of all possible faults. Using this, we provide a unique normal form for ZX diagrams under noise and show that any diagram can be brought into this normal form using our proposed rule set.
      </p>
      <p>
      <strong>Coauthors.</strong> Maximilian Rüsch, Aleks Kissinger, Benjamin Rodatz
      </p>
      <p>
        <strong>Abstract (Fault tolerance by construction).</strong> A key challenge in fault-tolerant quantum computing is synthesising and optimising circuits in a noisy environment, as traditional techniques often fail to account for the effect of noise on circuits. In this work, we propose and numerically verify a framework for designing fault-tolerant quantum circuits that are correct by construction. The framework starts with idealised specifications of fault-tolerant gadgets and refines them using provably sound basic transformations.<br><br>
        To reason about manipulating circuits while preserving their error correction properties, we define fault equivalence; two circuits are considered fault-equivalent if all undetectable faults on one circuit have a corresponding fault on the other. This guarantees that the effect of undetectable faults on both circuits is the same. We argue that fault equivalence is a concept that is already implicitly present in the literature. Many problems, such as state preparation and syndrome extraction, can be naturally expressed as finding an implementable circuit that is fault-equivalent to an idealized specification.<br><br>
        To utilize fault equivalence in a computationally tractable manner, we adapt the ZX calculus, a diagrammatic language for quantum computing. We restrict its rewrite system to not only preserve the underlying linear map but also fault equivalence, i.e. the circuit's behaviour under noise. Enabled by our framework, we verify, optimise, and synthesise new and efficient circuits for syndrome extraction and cat state preparation. We confirm the improved performance of our optimised circuits in simulation. We anticipate that fault equivalence can capture and unify different approaches in fault-tolerant quantum computing, paving the way for an end-to-end circuit compilation framework.
      </p>
      <p>
        <strong>Coauthors.</strong> Benjamin Rodatz, Boldizsár Poór, Aleks Kissinger
      </p>
    </details>
    <details>
      <summary><strong>10:15 - 11:00 </strong>Algebraic paradoxes in adaptive quantum computation</summary>
      <p>
        <strong>Abstract.</strong> TBA
      </p>
      <p>
        <strong>Coauthors.</strong> Samson Abramsky, Rui Soares Barbosa, Carmen Constantin, Martti Karvonen
      </p>
    </details>
  </details>
  <details id="tuesday-short-plenary-talks">
    <summary>Tuesday Short Plenary Talks 11:30 - 12:20</summary>
    <details>
      <summary><strong>11:30 - 11:55 </strong><a href="https://arxiv.org/pdf/2502.17576" target="_blank" rel="noopener">Invariance under quantum permutations rules out parastatistics</a></summary>
      <p>
        <strong>Abstract.</strong> Quantum systems invariant under particle exchange are either Bosons or Fermions, even though quantum theory in principle admits more general behavior under permutations. But why do we not observe such 'paraparticles' in nature? The analysis of this question was previously limited primarily to specific quantum field theory models. Here we give two independent arguments that rule out parastatistics universally, originating in quantum information theory and recent research on internal quantum reference frames. First, we introduce a notion of complete invariance: quantum systems should not only preserve their local state under permutations, but also the quantum information they carry about other systems, in analogy to the notion of complete positivity in quantum information theory. Second, we demand that quantum systems are invariant under quantum permutations, i.e. permutations conditioned on values of permutation-invariant observables. For both, we show that the respective principle is fulfilled if and only if the particle is a Boson or Fermion. Our results show how quantum reference frames can shed light on a longstanding problem of quantum physics, they underline the crucial role played by the compositional structure of quantum information, and demonstrate the explanatory power but also subtle limitations of recently proposed quantum covariance principles.
      </p>
      <p>
        <strong>Coauthors.</strong> Manuel Mekonnen, Thomas D. Galley, Markus P. Müller
      </p>
    </details>
    <details>
      <summary><strong>11:55 - 12:20 </strong>A higher-order perspective on quantum signal processing</summary>
      <p>
        <strong>Abstract.</strong> TBA
      </p>
      <p>
        <strong>Coauthors.</strong> Marek Arsenault, Hlér Kristjánsson
      </p>
    </details>
  </details>
  <details id="wednesday-long-plenary-talks">
    <summary>Wednesday Long Plenary Talks 9:30 - 11:00</summary>
    <details>
      <summary><strong>9:30 - 10:15 </strong>Completeness for flow-preserving rewrite rules / Generating one-way computations with flow: flow-preserving rewriting that ignores the interpretation</summary>
      <p>
        <strong>Abstract (Completeness for flow-preserving rewrite rules).</strong> TBA
      </p>
      <p>
        <strong>Coauthors.</strong> Miriam Backens, Simon Perdrix
      </p>
      <p>
        <strong>Abstract (Generating one-way computations with flow: flow-preserving rewriting that ignores the interpretation).</strong> TBA
      </p>
      <p>
        <strong>Author.</strong> Miriam Backens
      </p>
    </details>
    <details>
      <summary><strong>10:15 - 11:00 </strong><a href="https://arxiv.org/pdf/2511.06012" target="_blank" rel="noopener">Beyond Penrose tensor diagrams with the ZX calculus: Applications to quantum computing, quantum machine learning, condensed matter physics, and quantum gravity</a></summary>
      <p>
        <strong>Abstract.</strong> We introduce the Spin-ZX calculus as an elevation of Penrose's diagrams and associated binor calculus to the level of a formal diagrammatic language. The power of doing so is illustrated by the variety of scientific areas we apply it to: permutational quantum computing, quantum machine learning, condensed matter physics, and quantum gravity. Respectively, we analyse permutational computing transition amplitudes, evaluate barren plateaus for SU(2) symmetric ansätze, study properties of AKLT states, and derive the minimum quantised volume in loop quantum gravity. <br><br>
        Our starting point is the mixed-dimensional ZX calculus, a purely diagrammatic language that has been proven to be complete for finite-dimensional Hilbert spaces. That is, any equation that can be derived in the Hilbert space formalism, can also be derived in the mixed-dimensional ZX calculus. We embed the Spin-ZX calculus inside the mixed-dimensional ZX calculus, rendering it a quantum information flavoured diagrammatic language for the quantum theory of angular momentum, i.e. SU(2) representation theory. We diagrammatically derive the fundamental spin coupling objects - such as Clebsch-Gordan coefficients, symmetrising mappings between qubits and spin spaces, and spin Hamiltonians - under this embedding. <br><br>
        Our results establish the Spin-ZX calculus as a powerful tool for representing and computing with SU(2) systems graphically, offering new insights into foundational relationships and paving the way for new diagrammatic algorithms for theoretical physics.
      </p>
      <p>
        <strong>Coauthors.</strong> Quanlong Wang, Richard D. P. East, Razin A. Shaikh, Lia Yeh, Boldizsár Poór, Bob Coecke
      </p>
    </details>
  </details>
  <details id="thursday-long-plenary-talks">
    <summary>Thursday Long Plenary Talks 9:30 - 11:00</summary>
    <details>
      <summary><strong>9:30 - 10:15 </strong><a href="https://arxiv.org/pdf/2511.22734" target="_blank" rel="noopener">Denotational semantics for stabiliser quantum programs</a></summary>
      <p>
        <strong>Abstract.</strong> The stabiliser fragment of quantum theory is a foundational building block for quantum error correction and the fault-tolerant compilation of quantum programs. In this article, we develop a sound, universal and complete denotational semantics for stabiliser operations which include measurement, classically-controlled Pauli operators, and affine classical operations, in which quantum error-correcting codes are first-class objects. The operations are interpreted as certain affine relations over finite fields. This offers a conceptually motivated and computationally-tractable alternative to the standard operator-algebraic semantics of quantum programs (whose time complexity grows exponentially as the state space increases in size). We demonstrate the power of the resulting semantics by describing a small, proof-of-concept assembly language for stabiliser programs with fully-abstract denotational semantics.
      </p>
      <p>
        <strong>Coauthors.</strong> Robert I. Booth, Cole Comfort
      </p>
    </details>
    <details>
      <summary><strong>10:15 - 11:00 </strong><a href="https://arxiv.org/pdf/2507.10466" target="_blank" rel="noopener">Quantum control and general recursion beyond the unitary case</a></summary>
      <p>
        <strong>Abstract.</strong> Coherent control, aka quantum control, is a central concept in quantum computing that is attracting increasing attention from both the quantum foundations and quantum software communities. Defining coherent control in the presence of recursion and measurement has long been known to be a major challenge. In particular, no-go results have been established for standard semantical domains like completely positive maps. We address this problem by introducing the first quantum programming language with recursion that allows for the coherent control of arbitrary quantum operations. We equip this language with both an operational and a denotational semantics that we prove to be adequate. To design these semantics, we show that combining coherent control, recursion, and measurement crucially requires describing the evolution of subprograms in the absence of input. To address this, the operational semantics takes into account a default evolution branch, while the denotational semantics uses the concept of coherent quantum operation, based on vacuum extensions. We strengthen the validity of our approach by developing an observational equivalence: two programs are equivalent if their probability of termination is the same in any context. The denotational semantics is shown to be fully abstract with respect to this observational equivalence.
      </p>
      <p>
        <strong>Coauthors.</strong> Kathleen Barsse, Romain Péchoux, Simon Perdrix
      </p>
    </details>
  </details>
  <details id="thursday-short-plenary-talk">
    <summary>Thursday Short Plenary Talk 11:30 - 11:55</summary>
    <details>
      <summary><strong>11:30 - 11:55 </strong><a href="https://arxiv.org/pdf/2602.15800" target="_blank" rel="noopener">Entanglement in the Dicke subspace</a></summary>
      <p>
        <strong>Abstract.</strong> In this paper, we provide a complete mathematical theory for the entanglement of mixtures of Dicke states. These quantum states form an important subclass of bosonic states arising in the study of indistinguishable particles. We introduce a tensor-based parametrization where the diagonal entries of these states are encoded as a symmetric tensor, enabling a direct translation between entanglement properties and well-studied convex cones of tensors. Our results bridge multipartite entanglement theory with semialgebraic geometry and the theory of completely positive and copositive tensors. <br><br>
        This dictionary maps separability to completely positive tensors, the PPT property to moment tensors, entanglement witnesses to copositive tensors, and decomposable witnesses to sum of squares tensors. Using this framework, we construct explicit PPT entangled states in three or more qutrits. In this class of states, we establish that PPT entanglement exists for all multipartite systems with three qutrits or more, disproving a recent conjecture in [J. Math. Phys. 66, 022203 (2025)]. We also show that, for mixtures of Dicke states, the PPT condition with respect to the most balanced bipartition implies PPT with respect to any other bipartition. <br><br>
        We further connect bosonic extendibility of mixtures of Dicke states to the duals of known hierarchies for non-negative polynomials, such as the ones by Reznick and Polya. We thus provide semidefinite programming relaxations for separability and entanglement testing in the Dicke subspace.
      </p>
      <p>
        <strong>Coauthors.</strong> Aabhas Gulati, Ion Nechita, Clément Pellegrini
      </p>
    </details>
  </details>
  <details id="friday-long-plenary-talks">
    <summary>Friday Long Plenary Talks 9:30 - 11:00</summary>
    <details>
      <summary><strong>9:30 - 10:15 </strong><a href="https://arxiv.org/pdf/2601.15832" target="_blank" rel="noopener">Quantum coherence spaces revisited: A von Neumann (co)algebraic approach</a></summary>
      <p>
        <strong>Abstract.</strong> We describe a categorical model of MALL (Multiplicative Additive Linear Logic) inspired by the Heisenberg-Schrödinger duality of finite-dimensional quantum theory. Proofs of formulas with positive logical polarity correspond to CPTP (completely positive trace-preserving) maps in our model, i.e. the quantum operations in the Schrödinger picture, whereas proofs of formulas with negative logical polarity correspond to CPU (completely positive unital) maps, i.e. the quantum operations in the Heisenberg picture. The mathematical development is based on noncommutative geometry and finite-dimensional von Neumann (co)algebras, which can be defined as special kinds of (co)monoid objects internal to the category of finite-dimensional operator spaces.
      </p>
      <p>
        <strong>Coauthors.</strong> Thea Li, Vladimir Zamdzhiev
      </p>
    </details>
    <details>
      <summary><strong>10:15 - 11:00 </strong><a href="https://arxiv.org/pdf/2601.05158" target="_blank" rel="noopener">Composable simultaneous purification: When all communication scenarios reduce to spatial correlations</a></summary>
      <p>
        <strong>Abstract.</strong> Bell non-locality is a powerful framework to distinguish classical, quantum and post-quantum resources, which relies on non-communicating players. Under which restriction can we have the same separations, if we allow for communication? Non-signalling state assemblages, and the fact that they can always be simultaneously purified, turned out to be the key element to restrict the simplest bipartite communication scenario, the prepare-and-measure, to the standard bipartite Bell scenario. Yet, many distinctive features of quantum theory are genuinely multipartite and cannot be reduced to two-party behaviour. In this work we are interested in extending this simultaneous purification inspired result to all multipartite communication schemes. As a first step, we unify and extend the simultaneous purification result from states to instruments and super-instruments, which are composable structures, and open up the possibility to explore more complex communication scenarios. Our main contribution is to establish that arbitrary compositions of non-signalling assemblages cannot escape the standard spatial quantum Bell correlations set. As a consequence, any interactive quantum realization of correlations outside of this set must involve at least one signalling assemblage of quantum operations, even when the resulting correlations are non-signalling.
      </p>
      <p>
        <strong>Coauthors.</strong> Matilde Baroni, Dominik Leichtle, Ivan Šupić, Damian Markham, Marco Túlio Quintino
      </p>
    </details>
  </details>
</div>

## Parellel Talk Schedule

<div class="talk-details">
  <details id="monday-parallel-sessions-1">
    <summary>Monday Parallel Sessions 14:30 - 15:45</summary>
    <details>
      <summary><strong>Track 1</strong></summary>
      <details>
        <summary><strong>14:30 - 14:55 </strong><a href="https://arxiv.org/pdf/2506.08091" target="_blank" rel="noopener">On whether quantum theory needs complex numbers: The foil theories perspective</a></summary>
        <p>
          <strong>Abstract.</strong> Recent work by Renou et al. (2021) has led to some controversy concerning the question of whether quantum theory requires complex numbers for its formulation. We promote the view that the main result of that work is best understood not as a claim about the relative merits of different representations of quantum theory, but rather as a claim about the possibility of experimentally adjudicating between standard quantum theory and an alternative theory -- a foil theory -- known as real-amplitude quantum theory (RQT). In particular, the claim is that this adjudication can be achieved given only an assumption about the causal structure of the experiment. Here, we aim to shed some light on why this is possible, by reconceptualizing the comparison of the two theories as an instance of a broader class of such theory comparisons. By recasting RQT as the subtheory of quantum theory that arises by symmetrizing with respect to the collective action of a time-reversal symmetry, we can compare it to other subtheories that arise by symmetrization, but for different symmetries. If the symmetry has a unitary representation, the resulting foil theory is termed a twirled quantum world, and if it does not (as is the case in RQT), the resulting foil theory is termed a swirled quantum world. We show that, in contrast to RQT, there is no possibility of distinguishing any twirled quantum world from quantum theory given only an assumption about causal structure. We also define analogues of twirling and swirling for an arbitrary generalized probabilistic theory and identify certain necessary conditions on a causal structure for it to be able to support a causal compatibility gap between the theory and its symmetrized version. We draw out the implications of these analyses for the question of how a lack of a shared reference frame state features into the possibility of such a gap.
        </p>
        <p>
          <strong>Coauthors.</strong> Yìlè Yīng, Maria Ciudad Alañón, Daniel Centeno, Jacopo Surace, Marina Maciel Ansanelli, Ruizhi Liu, David Schmid, Robert W. Spekkens
        </p>
      </details>
      <details>
        <summary><strong>14:55 - 15:20 </strong><a href="https://arxiv.org/pdf/2603.19208" target="_blank" rel="noopener">On the experimental falsification of Real QT</a> / <a href="https://arxiv.org/pdf/2504.02808" target="_blank" rel="noopener">A real matrix theory consistent with both the postulates and predictions of quantum theory</a> [MERGED]</summary>
        <p>
          <strong>Abstract (On the experimental falsification of Real QT).</strong> Whether the complex numbers of standard quantum theory are experimentally indispensable has remained open for decades. Real quantum theory (RQT), obtained by replacing complex amplitudes with real ones while retaining the usual Kronecker-product composition rule, reproduces all single-party and bipartite Bell correlations of quantum theory (QT), but its lack of local tomography suggested that the two theories might diverge in more general local experiments. This possibility appeared to be confirmed by Renou et al., who argued that a bilocal network experiment can falsify RQT without falsifying QT. Here we show that this conclusion relies on an experimentally untestable assumption. The key distinction is between product-state independence, which constrains the mathematical form of source states, and operational independence, which is defined entirely by the absence of observable cross-source correlations. We prove that, once source independence is imposed operationally, every finite network correlation achievable in QT is also achievable in RQT with the same locality structure of the measurements. We then extend this equivalence to arbitrary finite sequential multipartite protocols involving channels and measurements with prescribed locality structure. Thus, as long as no violation of QT is observed, RQT cannot be experimentally falsified. Our results restore the empirical indistinguishability of QT and RQT, while showing that they support markedly different pictures of the correlation structure underlying the same observed world.
        </p>
        <p>
          <strong>Coauthors.</strong> Timothée Hoffreumon, Mischa P. Woods
        </p>
        <p>
          <strong>Abstract (A real matrix theory consistent with both the postulates and predictions of quantum theory).</strong> Quantum theory was radically different from the theories of nature which came before it. One key difference was its use of complex numbers. This opened a longstanding debate over whether quantum theory fundamentally requires complex numbers—or if their use is merely a convenient choice. Until recently, this question was considered open. However, in a 2021 Nature article, a decisive argument was presented asserting that quantum theory needs complex numbers since real-number quantum theory is inconsistent with the postulates of quantum theory. In this work, we show that this conclusion was premature, and in actual fact, a real-number quantum theory is consistent with the postulates of quantum theory. Our theory retains key features such as representation locality (i.e. local physical operations are represented by local changes to the states). A direct consequence of our results is that quantum theory based on real or complex numbers are experimentally indistinguishable.
        </p>
        <p>
          <strong>Coauthors.</strong> Timothée Hoffreumon, Mischa P. Woods
        </p>
      </details>
      <details>
        <summary><strong>15:20 - 15:45 </strong><a href="https://arxiv.org/pdf/2602.16280" target="_blank" rel="noopener">Tomographically-nonlocal entanglement</a></summary>
        <p>
          <strong>Abstract.</strong> Entanglement is a central and subtle feature of quantum theory, whose structure and operational behavior can change dramatically when additional physical constraints, such as symmetries or superselection rules, are imposed. Such constraints can give rise to striking and counter-intuitive phenomena, including local broadcasting of entangled states and failures of entanglement monogamy. These effects naturally arise in tomographically nonlocal theories (like real quantum theory, twirled worlds, or fermionic quantum theory), where composite systems possess holistic degrees of freedom that are inaccessible to local measurements. In this work, we study entanglement in such theories within the framework of generalized probabilistic theories. We show that the failure of tomographic locality leads to two qualitatively distinct forms of entanglement, which we term tomographically-local entanglement and tomographically-nonlocal entanglement. We analyze the operational consequences of this distinction, proving that tomographically-nonlocal entanglement is useless for Bell nonlocality, steering, and teleportation, but sufficient for dense coding and perfectly secure data hiding. This framework clarifies the origin of several previously puzzling features of entanglement that arise when tomographic locality fails, as can happen even in quantum theory when one considers fermions or fundamental superselection rules.
        </p>
        <p>
          <strong>Coauthors.</strong> Roberto D. Baldijão, Marco Erba, David Schmid, John H. Selby, Ana Belén Sainz
        </p>
      </details>
    </details>
    <details>
      <summary><strong>Track 2</strong></summary>
      <details>
        <summary><strong>14:30 - 14:55 </strong>Restricted negation in orthomodular logic</summary>
        <p>
          <strong>Abstract.</strong> TBA
        </p>
        <p>
          <strong>Coauthors.</strong> Tomoaki Kawano, Ryo Kashima
        </p>
      </details>
      <details>
        <summary><strong>14:55 - 15:20 </strong><a href="https://arxiv.org/pdf/2307.01713" target="_blank" rel="noopener">Logic meets Wigner's friend (and their friends)</a></summary>
        <p>
          <strong>Abstract.</strong> We take a fresh look at Wigner's Friend thought-experiment and some of its more recent variants and extensions, such as the Frauchiger-Renner (FR) Paradox. We discuss various solutions proposed in the literature, focusing on a few questions: What is the correct epistemic interpretation of the multiplicity of state assignments in these scenarios? Under which conditions can one include classical observers into the quantum state descriptions, in a way that is still compatible with traditional Quantum Mechanics? Under which conditions can one system be admitted as an additional 'observer' from the perspective of another background observer? When can the standard axioms of multi-agent Epistemic Logic (that allow "knowledge transfer" between agents) be applied to quantum-physical observers? In the last part of the paper, we propose a new answer to these questions, sketch a particular formal implementation of this answer, and apply it to obtain a principled solution to Wigner Friend-type paradoxes.
        </p>
        <p>
          <strong>Coauthors.</strong> Alexandru Baltag, Sonja Smets
        </p>
      </details>
      <details>
        <summary><strong>15:20 - 15:45 </strong><a href="https://arxiv.org/pdf/2505.06069" target="_blank" rel="noopener">Operator spaces, linear logic and the Heisenberg-Schrödinger duality</a></summary>
        <p>
          <strong>Abstract.</strong> We show that the category OS of operator spaces, with complete contractions as morphisms, is locally countably presentable and a model of Intuitionistic Linear Logic in the sense of Lafont. We then describe a model of Classical Linear Logic, based on OS, whose duality is compatible with the HeisenbergSchrödinger duality of quantum theory. We also show that OS provides a good setting for studying pure state and mixed state quantum information, the interaction between the two, and even higher-order quantum maps such as the quantum switch.
        </p>
        <p>
          <strong>Coauthors.</strong> Bert Lindenhovius, Vladimir Zamdzhiev
        </p>
      </details>
    </details>
    <details>
      <summary><strong>Track 3</strong></summary>
      <details>
        <summary><strong>14:30 - 14:55 </strong><a href="https://arxiv.org/pdf/2602.06644" target="_blank" rel="noopener">A complete equational theory for Real-Clifford+CH quantum circuits</a></summary>
        <p>
          <strong>Abstract.</strong> We introduce a complete equational theory for the fragment of quantum circuits generated by the real Clifford gates plus the two-qubit controlled-Hadamard gate. That is, we give a simple set of equalities between circuits of this fragment, and prove that any other true equation can be derived from these. This is the first such completeness result for a finitely-generated, universal fragment of quantum circuits, with no parameterized gates and no need for ancillas.
        </p>
        <p>
          <strong>Author.</strong> Alexandre Clément
        </p>
      </details>
      <details>
        <summary><strong>14:55 - 15:20 </strong>A complete and natural rule set for multi-qudit Clifford circuits</summary>
        <p>
          <strong>Abstract.</strong> We present a complete set of rewrite rules for multi-qudit Clifford circuits in all prime dimensions. Completeness implies that any two Clifford circuits representing the same linear map can be rewritten into each other using these rules. There are 19 rewrite rules in total, each involving no more than three qudits and admitting an intuitive interpretation. Our approach leverages the isomorphism between the symplectic group $\mathrm{Sp}(2n, \mathbb{Z}_d)$ and the quotient of the Clifford group by the Pauli group. We first derive a complete set of symplectic relations for $\mathrm{Sp}(2n, \mathbb{Z}_d)$, and then lift them to Clifford relations by incorporating Pauli corrections. To do this, we introduce a symplectic normal form that captures the stabiliser tableau of a Clifford operator and is unique up to Pauli correction. This simplification enables a streamlined derivation of a complete set of $66$ relations, which we further compress to $18$ symplectic relations. Our computations in $\mathrm{Sp}(2n, \mathbb{Z}_d)$ are formalised in the Agda proof assistant, providing a machine-verified proof of correctness.
        </p>
        <p>
          <strong>Coauthors.</strong> Xiaoning Bian, Sarah Meng Li, Neil J. Ross, John van de Wetering, Yuming Zhao
        </p>
      </details>
      <details>
        <summary><strong>15:20 - 15:45 </strong><a href="https://arxiv.org/pdf/2603.06466" target="_blank" rel="noopener">Completeness for prime-dimensional phase-affine circuits</a></summary>
        <p>
          <strong>Abstract.</strong> Equational reasoning about circuits is central in quantum software for validation, optimisation, and verification. For qubits, the CNOT-dihedral fragment supports efficient rewriting via phase polynomials and layered normal forms, yielding a complete and practically effective equational theory. In this work we generalise that CNOT-dihedral picture from qubits to prime-dimensional qudits. We present a compact PROP for reversible affine circuits over a prime field, with a strict symmetric monoidal semantics into the affine group and a Lafont-style affine normal form. We then adjoin finite-angle diagonal phase generators and organise them by polynomial degree, obtaining linear, quadratic (odd prime), and cubic (prime greater than 3) calculi. Using binomial-basis identities we derive uniform transport rules, establish unique phase-affine normal forms, and prove completeness: semantic equality coincides with derivable equality. This yields a prime-dimensional, phase-polynomial-aligned generalisation of the CNOT-dihedral equational theory.
        </p>
        <p>
          <strong>Author.</strong> Colin Blake
        </p>
      </details>
    </details>
  </details>
  <details id="monday-parallel-sessions-2">
    <summary>Monday Parallel Sessions 16:15 - 17:30</summary>
    <details>
      <summary><strong>Track 1</strong></summary>
      <details>
        <summary><strong>16:15 - 16:40 </strong><a href="https://arxiv.org/pdf/2512.11209" target="_blank" rel="noopener">The resource theory of causal influence and knowledge of causal influence</a></summary>
        <p>
          <strong>Abstract.</strong> Understanding and quantifying causal relationships between variables is essential for reasoning about the physical world. In this work, we develop a resource-theoretic framework to do so. Here, we focus on the simplest nontrivial setting -- two variables that are causally ordered, meaning that the first has the potential to influence the second, without hidden confounding. First, we introduce the resource theory that directly quantifies causal influence of a functional dependence in this setting and show that the problem of deciding convertibility of resources and identifying a complete set of monotones has a relatively straightforward solution. Following this, we introduce the resource theory that arises naturally when one has uncertainty about the functional dependence. We describe a linear program for deciding the question of whether one resource (i.e., state of knowledge about the functional dependence) can be converted to another. Then, we focus on the case where the variables are binary. In this case, we identify a triple of monotones that are complete in the sense that they capture the partial order over the set of all resources, and we provide an interpretation of each.
        </p>
        <p>
          <strong>Coauthors.</strong> Marina Maciel Ansanelli, Beata Zjawin, David Schmid, Yìlè Yīng, John H. Selby, Ciarán M. Gilligan-Lee, Ana Belén Sainz, Robert W. Spekkens
        </p>
      </details>
      <details>
        <summary><strong>16:40 - 17:05 </strong>Causal inequalities witness non-stabilizerness without magic</summary>
        <p>
          <strong>Abstract.</strong> TBA
        </p>
        <p>
          <strong>Coauthors.</strong> Leonardo Vaglini, Nasra Daher Ahmed, Ravi Kunjwal
        </p>
      </details>
      <details>
        <summary><strong>17:05 - 17:30 </strong><a href="https://arxiv.org/pdf/2603.12283" target="_blank" rel="noopener">Emergent causal order and time direction: Bridging causal models and tensor networks</a></summary>
        <p>
          <strong>Abstract.</strong> Can the direction of time and the causal structure of space-time be inferred from operational principles? Causal models and tensor networks offer complementary perspectives: the former encodes cause-effect relations via directed graphs, with intrinsic ordering; the latter describes multipartite systems on undirected graphs, without presupposing directionality. We construct two-way mappings between these two frameworks, linking direction agnostic correlation functions and operational notions of signalling. This clarifies the operational meaning of causal influence in tensor networks and introduces discrete "space-time rotations'' of causal models which preserve signalling relations. Applying our framework to holographic tensor networks, we use tools from causal inference, like graph-separation, to analyse emergent causal structures. By permitting cyclic and indefinite causal structures, our results enable transfer of techniques across tensor networks and a range of causality frameworks.
        </p>
        <p>
          <strong>Coauthors.</strong> Carla Ferradini, Giulia Mazzola, V. Vilasini
        </p>
      </details>
    </details>
    <details>
      <summary><strong>Track 2</strong></summary>
      <details>
        <summary><strong>16:15 - 16:40 </strong><a href="https://arxiv.org/pdf/2603.13946" target="_blank" rel="noopener">Generalized inverses of quantum channels: A categorical perspective</a></summary>
        <p>
          <strong>Abstract.</strong> A quantum channel is defined as being completely positive (CP) and trace preserving (TP). While not every quantum channel is invertible or reversible, every quantum channel admits various kinds of generalized inverses such as the Moore-Penrose inverse and the Drazin inverse. A generalized inverse of a quantum channel may not itself be a quantum channel: it often fails to be CP. However, generalized inverses still play an important role in quantum error mitigation. Here, because it is often desirable for the generalized inverse of a quantum channel to be at least TP, the Drazin inverse, which is TP, is favoured over the Moore-Penrose inverse, which is not in general TP.<br><br>
          In this paper, we take a categorical perspective on generalized inverses of quantum channels. This allows us to give a simple proof of the fact that the Drazin inverse of a quantum channel is always TP. It also allows us to show that for unital quantum channels, the Drazin inverse is also unital. We then generalize this result to dagger Drazin inverses, which allows us to show that for unital quantum channels, the Moore-Penrose inverse is both TP and unital as well. This opens the door to new applications of both the Drazin inverse and Moore-Penrose inverse in quantum information theory and, in particular, in quantum error mitigation.
        </p>
        <p>
          <strong>Coauthors.</strong> Robin Cockett, Jean-Simon Pacaud Lemay, Priyaa Varshinee Srinivasan
        </p>
      </details>
      <details>
        <summary><strong>16:40 - 17:05 </strong><a href="https://arxiv.org/pdf/2601.09685" target="_blank" rel="noopener">The category of quantum graphs is closed</a></summary>
        <p>
          <strong>Abstract.</strong> We introduce a category 𝗊𝖦𝗉𝗁 of quantum graphs, whose definition is motivated entirely from noncommutative geometry. For all quantum graphs G and H in 𝗊𝖦𝗉𝗁, we then construct a quantum graph [G,H] of homomorphisms from G to H, making 𝗊𝖦𝗉𝗁 a closed symmetric monoidal category. We prove that for all finite graphs G and H, the quantum graph [G,H] is nonempty iff the (G,H)-homomorphism game has a winning quantum strategy, directly generalizing the classical case.<br><br>
          The finite quantum graphs in 𝗊𝖦𝗉𝗁 are tracial, real, and self-adjoint, and the morphisms between them are CP morphisms that are adjoint to a unital ∗-homomorphism. We prove that Weaver's two notions of a CP morphism coincide in this context. We also include a short proof that every finite reflexive quantum graph is the confusability quantum graph of a quantum channel.
        </p>
        <p>
          <strong>Coauthors.</strong> Andre Kornell, Bert Lindenhovius
        </p>
      </details>
      <details>
        <summary><strong>17:05 - 17:30 </strong>Nuclearity and trace in monoidal bicategories with application to extended CFTs</summary>
        <p>
          <strong>Abstract.</strong> TBA
        </p>
        <p>
          <strong>Author.</strong> James Hefford
        </p>
      </details>
    </details>
    <details>
      <summary><strong>Track 3</strong></summary>
      <details>
        <summary><strong>16:15 - 16:40 </strong><a href="https://arxiv.org/pdf/2603.06764" target="_blank" rel="noopener">Efficient classical simulation of low-rank-width quantum circuits using ZX-Calculus</a></summary>
        <p>
          <strong>Abstract.</strong> In this paper, we introduce a technique for contracting (i.e. numerically evaluating) ZX-diagrams whose complexity scales with their rank-width, a graph parameter that behaves nicely under ZX rewrite rules. Given a rank-decomposition of width R, our method simulates a graph-like ZX-diagram in \(\tilde{O}(4^R)\) time. Applied to classical simulation of quantum circuits, it is no slower than either naive state vector simulation or stabiliser decompositions with \(\alpha=0.5\), and in practice can be significantly faster for suitably chosen rank-decompositions. Since finding optimal rank-decompositions is NP-hard, we introduce heuristics that produce good decompositions in practice. We benchmark our simulation routine against Quimb, a popular tensor contraction library, and observe substantial reductions in floating-point operations (often by several orders of magnitude) for random and structured non-Clifford circuits as well as random ZX-diagrams.
        </p>
        <p>
          <strong>Coauthors.</strong> Fedor Kuyanov, Aleks Kissinger
        </p>
      </details>
      <details>
        <summary><strong>16:40 - 17:05 </strong><a href="https://arxiv.org/pdf/2509.08658" target="_blank" rel="noopener">Simulating magic state cultivation with few Clifford terms</a></summary>
        <p>
          <strong>Abstract.</strong> Building upon [arXiv:2509.01224], we present a few methods on how to simulate the non-Clifford d=5 magic state cultivation circuits [arXiv:2409.17595] with a sum of ≈8 Clifford ZX-diagrams on average, at 0.1% noise. Compared to a magic cat state stabiliser decomposition of all 53 non-Clifford spiders (6,377,292 terms required), this is more than 7×105 times reduction in the number of terms. Our stabiliser decomposition has the advantage of representing the final non-Clifford state (in light of circuit errors) as a sum of Clifford ZX-diagrams. This will be useful in simulating the escape stage of magic state cultivation, where one needs to port the resultant state of cultivation into a larger Clifford circuit with many more qubits. Still, it's necessary to only track ≈8 Clifford terms. Our result sheds light on the simulability of operationally relevant, high T-count quantum circuits with some internal structure.<br><br>
          Finally, we provide numerical results for full non-Clifford stabiliser rank simulation based on 𝚝𝚜𝚒𝚖 along with optimisations using our cutting decompositions. Nearly 4×106 shots per second can be obtained on a laptop for the smaller d=3 circuits at SD6 circuit level noise p=0.0005, making it only ∼1.1 times slower than its (circuit-unspecific and un-optimised) fully Clifford proxy simulation via 𝚜𝚝𝚒𝚖 using S gates.
        </p>
        <p>
          <strong>Coauthors.</strong> Kwok Ho Wan, Zhenghao Zhong, Ainhoa Zapirain
        </p>
      </details>
      <details>
        <summary><strong>17:05 - 17:30 </strong>Classical Clifford+T sampling without computing marginals</summary>
        <p>
          <strong>Abstract.</strong> TBA
        </p>
        <p>
          <strong>Author.</strong> Mark Koch
        </p>
      </details>
    </details>
  </details>
{% endcomment %}

<script>
  // The theme footer renders <a href="/#top">Back to top</a>. The "/#top"
  // points at the site root, so on inner pages (like this one) it navigates
  // back to the home page instead of scrolling up. Rewrite that link to scroll
  // to the top of the current page.
  (function () {
    function fixBackToTop() {
      var links = document.querySelectorAll('a[href="/#top"], a[href="#top"]');
      for (var i = 0; i < links.length; i++) {
        links[i].setAttribute('href', '#');
        links[i].addEventListener('click', function (e) {
          e.preventDefault();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        });
      }
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fixBackToTop);
    } else {
      fixBackToTop();
    }
  })();

  (function () {
    function pad(n) { return (n < 10 ? '0' : '') + n; }

    // QPL runs on Amsterdam local time, so determine "today" in that time
    // zone rather than relying on the visitor's local clock.
    function amsterdamToday() {
      try {
        var parts = new Intl.DateTimeFormat('en-CA', {
          timeZone: 'Europe/Amsterdam',
          year: 'numeric', month: '2-digit', day: '2-digit'
        }).formatToParts(new Date());
        var map = {};
        parts.forEach(function (p) { map[p.type] = p.value; });
        if (map.year && map.month && map.day) {
          return map.year + '-' + map.month + '-' + map.day;
        }
      } catch (e) { /* fall through to local time */ }
      var now = new Date();
      return now.getFullYear() + '-' + pad(now.getMonth() + 1) + '-' + pad(now.getDate());
    }

    function goToToday(announce) {
      var sections = Array.prototype.slice.call(
        document.querySelectorAll('.day-section[data-date]')
      );
      if (!sections.length) { return; }

      var todayStr = amsterdamToday();

      // Prefer an exact match for today; otherwise fall back to the next
      // upcoming conference day, or the last day once the conference is over.
      var target = null;
      var upcoming = null;
      sections.forEach(function (s) {
        var d = s.getAttribute('data-date');
        if (d === todayStr) { target = s; }
        if (!upcoming && d >= todayStr) { upcoming = s; }
      });
      var exact = !!target;
      if (!target) { target = upcoming || sections[sections.length - 1]; }

      // Open the target day, collapse the others, and scroll to it.
      sections.forEach(function (s) {
        if (s === target) { s.setAttribute('open', ''); }
        else { s.removeAttribute('open'); }
      });
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });

      if (announce) {
        var note = document.getElementById('today-note');
        if (note) {
          var label = target.querySelector('summary');
          var name = label ? label.textContent.trim() : 'the schedule';
          note.textContent = exact
            ? "Showing today's talks: " + name + '.'
            : "No talks scheduled for today — showing the next session: " + name + '.';
        }
      }
    }

    document.addEventListener('DOMContentLoaded', function () {
      var btn = document.getElementById('today-talk-btn');
      if (btn) {
        btn.addEventListener('click', function () { goToToday(true); });
      }
    });
  })();
</script>