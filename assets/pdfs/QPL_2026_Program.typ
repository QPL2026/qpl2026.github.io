// QPL 2026 program, styled after qpl_program.pdf (Typst-generated, Libertinus Serif)

#set page(paper: "a4", margin: (x: 2.5cm, y: 2cm), numbering: "1")
#set text(font: "Libertinus Serif", size: 10.5pt)
#set par(justify: false, leading: 0.55em)
#show heading.where(level: 1): set text(size: 16pt, weight: "bold")
#show heading.where(level: 2): set text(size: 13pt, weight: "bold")
#show heading.where(level: 3): set text(size: 11pt, weight: "bold")

// Palette mirroring program.md
#let c-plenary     = rgb("#7fcff4")  // long plenary (light blue)
#let c-plenary2    = rgb("#bfe6cc")  // short plenary (light green)
#let c-parallel    = rgb("#f6e58d")  // parallel sessions (yellow)
#let c-poster      = rgb("#f7c98b")  // poster session (light orange)
#let c-break       = rgb("#e8eef5")  // coffee/lunch (soft grey-blue)
#let c-special     = rgb("#f7c98b")  // boat tour / dinner (peach, matches poster tone)
#let c-especial    = rgb("#bfe6cc")  // career fair (light green)
#let c-chair-bg    = rgb("#dfeefa")  // session band (very light blue)
#let c-title       = rgb("#7e1b1b")

// Helpers
#let titlec(t)  = text(fill: c-title, weight: "bold", t)
#let chairrow(label) = table.cell(fill: c-chair-bg, colspan: 2, align: center, text(size: 9pt, label))
#let banner(label, col: 2, fill: none) = table.cell(fill: fill, colspan: col, align: center, label)
#let cellc(fill, body, ..rest) = table.cell(fill: fill, align: center + horizon, ..rest, body)
#let timec(t) = align(center + horizon, t)
#let talkcell(authors, title) = block(breakable: false, align(center + horizon, {
  text(size: 9.5pt, authors)
  linebreak()
  titlec(text(size: 9.5pt, title))
}))

= QPL 2026 program (17 -- 21 August 2026 in Amsterdam, NL)

== Overview of the program

Welcome to Amsterdam! Registration opens at 8:50 AM on Monday, August 17, at the University of Amsterdam’s Roeterseiland campus. The conference runs through Friday, August 21, 2026, with three parallel sessions each afternoon. On Wednesday, there is a boat tour and conference dinner after the parallel sessions.

#v(0.4em)

#let xcell = text(fill: rgb("#bbbbbb"), size: 14pt)[$times$]

#table(
  columns: (2.2cm, 1fr, 1fr, 1fr, 1fr, 1fr),
  stroke: 0.5pt + black,
  align: center + horizon,
  inset: 6pt,
  // Header
  [],
  [*Monday,\ August 17th*],
  [*Tuesday,\ August 18th*],
  [*Wednesday,\ August 19th*],
  [*Thursday,\ August 20th*],
  [*Friday,\ August 21st*],

  // 8:50 - 9:30: Registration on Monday only
  [8:50 -- 9:30], [Registration], xcell, xcell, xcell, xcell,

  // 9:30 - 11:00: Long Plenary Talks (rowspan 2)
  [9:30 -- 10:15],
    table.cell(rowspan: 2, fill: c-plenary)[Long Plenary\ Talks],
    table.cell(rowspan: 2, fill: c-plenary)[Long Plenary\ Talks],
    table.cell(rowspan: 2, fill: c-plenary)[Long Plenary\ Talks],
    table.cell(rowspan: 2, fill: c-plenary)[Long Plenary\ Talks],
    table.cell(rowspan: 2, fill: c-plenary)[Long Plenary\ Talks],
  [10:15 -- 11:00],

  // 11:00 - 11:30: Coffee Break
  [11:00 -- 11:30], table.cell(colspan: 5, fill: c-break)[Coffee Break],

  // 11:30 - 12:20
  [11:30 -- 11:55],
    table.cell(rowspan: 2, fill: c-plenary2)[Short Plenary\ Talks],
    table.cell(rowspan: 2, fill: c-plenary2)[Short Plenary\ Talks],
    table.cell(rowspan: 2)[Industry\ Session],
    table.cell(fill: c-plenary2)[Short Plenary\ Talk],
    table.cell(rowspan: 2)[Business\ Meeting],
  [11:55 -- 12:20], [Conference\ Photo],

  // 12:30 - 14:30: Lunch Break
  [12:30 -- 14:30], table.cell(colspan: 5, fill: c-break)[Lunch Break],

  // 14:30 - 15:45: Parallel sessions (Mon/Tue/Wed/Fri rs3; Thu rs5 until 16:15-16:40)
  [14:30 -- 14:55],
    table.cell(rowspan: 3, fill: c-parallel)[Parallel\ Sessions],
    table.cell(rowspan: 3, fill: c-parallel)[Parallel\ Sessions],
    table.cell(rowspan: 3, fill: c-parallel)[Parallel\ Sessions],
    table.cell(rowspan: 5, fill: c-parallel)[Parallel\ Sessions\ 14:30 -- 16:10],
    table.cell(rowspan: 3, fill: c-parallel)[Parallel\ Sessions],
  [14:55 -- 15:20],
  [15:20 -- 15:45],

  // 15:45 - 16:15: Coffee Break (Mon-Tue-Wed merged); Thu still in parallel block; Fri Coffee Break
  [15:45 -- 16:15],
    table.cell(colspan: 3, fill: c-break)[Coffee Break],
    table.cell(fill: c-break)[Coffee Break],

  // 16:15 - 16:40: Mon/Tue parallel rs3 (until 17:30); Wed/Fri parallel rs2 (16:15-17:05); Thu still covered
  [16:15 -- 16:40],
    table.cell(rowspan: 3, fill: c-parallel)[Parallel\ Sessions],
    table.cell(rowspan: 3, fill: c-parallel)[Parallel\ Sessions],
    table.cell(rowspan: 2, fill: c-parallel)[Parallel\ Sessions\ 16:15 -- 17:05],
    table.cell(rowspan: 2, fill: c-parallel)[Parallel\ Sessions\ 16:15 -- 17:05],

  // 16:40 - 17:05: only Thu has a new cell here (Coffee Break)
  [16:40 -- 17:05], table.cell(fill: c-break)[Coffee Break],

  // 17:05 - 17:30: Wed Boat Tour; Thu TBA (rs2); Fri Goodbye! (rs2)
  [17:05 -- 17:30],
    [Boat Tour],
    table.cell(rowspan: 2)[TBA],
    table.cell(rowspan: 2)[Goodbye!],

  // After 17:30 (no time label)
  [], xcell,
    table.cell(fill: c-poster)[Poster Session\ 17:30 -- 19:30],
    table.cell(fill: c-special)[Conference\ Dinner],
)

#pagebreak()

== Monday, August 17th

#table(
  columns: (3cm, 1fr),
  stroke: 0.5pt,
  inset: 6pt,
  align: left + horizon,
  timec[8:50 -- 9:30], align(center, [Registration]),
  table.cell(colspan: 2, fill: c-chair-bg, align: center, text(size: 9pt, [Long plenary talks])),
  timec[9:30 -- 10:15], talkcell(
    [Alex Maltesson, Ludvig Rodung, Niklas Budinger, Giulia Ferrini, Cameron Calcluth],
    [Equivalence of continuous- and discrete-variable gate-based quantum computers with finite energy]
  ),
  timec[10:15 -- 11:00], talkcell(
    [Raphaël Mothe, Jessica Bavaresco],
    [Efficient quantum-circuit simulation of classical control of causal order]
  ),
  table.cell(colspan: 2, fill: c-break, align: center)[Coffee break],
  table.cell(colspan: 2, fill: c-chair-bg, align: center, text(size: 9pt, [Short plenary talks])),
  timec[11:30 -- 11:55], talkcell(
    [Vinicius Pretti Rossi, Beata Zjawin, Roberto D. Baldijão, David Schmid, John H. Selby, Ana Belén Sainz],
    [How typical is contextuality?]
  ),
  timec[11:55 -- 12:20], talkcell(
    [Dichuan Gao, Razin A. Shaikh, Aleks Kissinger],
    [Graphical algebraic geometry: from ideals and varieties to qudit ZH completeness]
  ),
  table.cell(colspan: 2, fill: c-break, align: center)[Lunch break],
)

#v(0.5em)

#table(
  columns: (2.4cm, 1fr, 1fr, 1fr),
  stroke: 0.5pt,
  inset: 5pt,
  align: left + horizon,
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel A])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel B])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel C])),
  timec[14:30 -- 14:55],
    talkcell([Yìlè Yīng, Maria Ciudad Alanon, Daniel Centeno, Jacopo Surace, Marina Maciel Ansanelli, Ruizhi Liu, David Schmid, Robert Spekkens],
      [On whether quantum theory needs complex numbers: the foil theories perspective]),
    table.cell(align: center + horizon, talkcell([Tomoaki Kawano, Ryo Kashima], [Restricted negation in orthomodular logic])),
    table.cell(align: center + horizon, talkcell([Alexandre Clément], [A complete equational theory for real-Clifford+CH quantum circuits])),
  timec[14:55 -- 15:20],
    talkcell([Timothée Hoffreumon, Mischa P. Woods], [On the experimental falsification of real QT / A real matrix theory consistent with QT (merged)]),
    table.cell(align: center + horizon, talkcell([Alexandru Baltag, Sonja Smets], [Logic meets Wigner's friend (and their friends)])),
    table.cell(align: center + horizon, talkcell([Xiaoning Bian, Sarah Meng Li, Neil J. Ross, John van de Wetering, Yuming Zhao],
      [A complete and natural rule set for multi-qudit Clifford circuits in all odd prime dimensions])),
  timec[15:20 -- 15:45],
    talkcell([Roberto D. Baldijão, Marco Erba, David Schmid, John Selby, Ana Belén Sainz],
      [Tomographically-nonlocal entanglement]),
    table.cell(align: center + horizon, talkcell([Bert Lindenhovius, Vladimir Zamdzhiev],
      [Operator spaces, linear logic and the Heisenberg--Schrödinger duality of quantum theory])),
    table.cell(align: center + horizon, talkcell([Colin Blake], [Completeness for prime-dimensional phase-affine circuits])),
  table.cell(colspan: 4, fill: c-break, align: center)[Coffee break],
  timec[16:15 -- 16:40],
    talkcell([Beata Zjawin, Marina Maciel Ansanelli, David Schmid, Yìlè Yīng, John H. Selby, Ciarán M. Gilligan-Lee, Ana Belén Sainz, Robert Spekkens],
      [The resource theory of causal influence and knowledge of causal influence]),
    table.cell(align: center + horizon, talkcell([Priyaa Varshinee Srinivasan, Jean-Simon Pacaud Lemay, Robin Cockett],
      [Generalized inverses of quantum channels: a categorical perspective])),
    table.cell(align: center + horizon, talkcell([Fedor Kuyanov, Aleks Kissinger],
      [Efficient classical simulation of low-rank-width quantum circuits using ZX-calculus])),
  timec[16:40 -- 17:05],
    talkcell([Leonardo Vaglini, Nasra Daher Ahmed, Ravi Kunjwal],
      [Causal inequalities witness non-stabilizerness without magic]),
    table.cell(align: center + horizon, talkcell([Andre Kornell, Bert Lindenhovius], [The category of quantum graphs is closed])),
    table.cell(align: center + horizon, talkcell([Kwok Ho Wan, Zhenghao Zhong, Ainhoa Zapirain],
      [Simulating magic state cultivation with few Clifford terms])),
  timec[17:05 -- 17:30],
    talkcell([Carla Ferradini, Giulia Mazzola, V. Vilasini],
      [Emergent causal order and time direction: bridging causal models and tensor networks]),
    table.cell(align: center + horizon, talkcell([James Hefford], [Nuclearity and trace in monoidal bicategories with application to extended CFTs])),
    table.cell(align: center + horizon, talkcell([Mark Koch], [Classical Clifford+T sampling without computing marginals])),
)

#pagebreak()

== Tuesday, August 18th

#table(
  columns: (3cm, 1fr),
  stroke: 0.5pt,
  inset: 6pt,
  align: left + horizon,
  table.cell(colspan: 2, fill: c-chair-bg, align: center, text(size: 9pt, [Long plenary talks])),
  timec[9:30 -- 10:15], talkcell(
    [Maximilian Rüsch, Aleks Kissinger, Benjamin Rodatz #h(1em) / #h(1em) Benjamin Rodatz, Boldizsár Poór, Aleks Kissinger],
    [Completeness for fault equivalence of Clifford ZX diagrams / Fault tolerance by construction]
  ),
  timec[10:15 -- 11:00], talkcell(
    [Samson Abramsky, Rui Soares Barbosa, Carmen Constantin, Martti Karvonen],
    [Algebraic paradoxes in adaptive quantum computation]
  ),
  table.cell(colspan: 2, fill: c-break, align: center)[Coffee break],
  table.cell(colspan: 2, fill: c-chair-bg, align: center, text(size: 9pt, [Short plenary talks])),
  timec[11:30 -- 11:55], talkcell(
    [Manuel Mekonnen, Thomas D. Galley, Markus P. Müller],
    [Invariance under quantum permutations rules out parastatistics]
  ),
  timec[11:55 -- 12:20], talkcell(
    [Marek Arsenault, Hlér Kristjánsson],
    [A higher-order perspective on quantum signal processing]
  ),
  table.cell(colspan: 2, fill: c-break, align: center)[Lunch break],
)

#v(0.5em)

#table(
  columns: (2.4cm, 1fr, 1fr, 1fr),
  stroke: 0.5pt,
  inset: 5pt,
  align: left + horizon,
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel A])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel B])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel C])),
  timec[14:30 -- 14:55],
    talkcell([Andrey Boris Khesin, Sarah Meng Li, Boldizsár Poór, Benjamin Rodatz, John van de Wetering, Richie Yeung],
      [SpiderCat: optimal fault-tolerant cat state preparation]),
    talkcell([Daniel Brod, Lorenzo Catani, Robert Spekkens],
      [The toy theory is the unique noncontextual theory satisfying $A_1^3$-symmetry]),
    talkcell([Matthew Wilson], [Agent policies from higher-order causal functions]),
  timec[14:55 -- 15:20],
    talkcell([Kwok Ho Wan, Henry Price, Qing Yao], [Holographic codes seen through ZX-calculus]),
    talkcell([Tim Achenbach, Andreas Bluhm, Leevi Leppäjärvi, Ion Nechita, Martin Plávala],
      [Factorization of multimeters: a unified view on nonclassical quantum phenomena]),
    talkcell([V. Vilasini, Lin-Qing Chen, Liuhang Ye, Renato Renner],
      [Events and their localisation are relative to a lab]),
  timec[15:20 -- 15:45],
    talkcell([Cole Comfort, Giovanni de Felice], [The delayed stabiliser ZX-calculus]),
    talkcell([Cihan Okay, Aziz Kharoof], [The geometry of fiber products of probability polytopes]),
    talkcell([Zixuan Liu, Ognyan Oreshkov], [Parity erasure: a foundational principle for indefinite causal order]),
  table.cell(colspan: 4, fill: c-break, align: center)[Coffee break],
  timec[16:15 -- 16:40],
    talkcell([Vincenzo Fiorentino, Kuntal Sengupta],
      [Superposition and its connections to uncertainty, entanglement and the quantum tensor product]),
    talkcell([Tom Williams, Mina Doosti, Farid Shahandeh],
      [Sheaf-theoretic preparation contextuality via stochastic extension]),
    talkcell([Luca Apadula, Alexei Grinbaum, Časlav Brukner],
      [Reference frames for process matrices: from coordinate parametrization to spacetime representation]),
  timec[16:40 -- 17:05],
    talkcell([Gaurang Agrawal, Matt Wilson], [Deriving the generalised Born rule from first principles]),
    talkcell([Theodoros Yianni, Farid Shahandeh, Nyan Raess],
      [Linear algebra of generalized contextuality in prepare-transform-measure scenarios]),
    talkcell([Yassine Benhaj, Kuntal Sengupta, Cyril Branciard],
      [How many systems can be dephased before the quantum switch becomes causally definite?]),
  timec[17:05 -- 17:30],
    talkcell([James Hefford, Matt Wilson],
      [Quantum theory can decohere from a causally-indefinite post-quantum theory]),
    talkcell([David Schmid, Roberto D. Baldijão, John Selby, Ana Belen Sainz, Robert W. Spekkens],
      [Noncontextuality inequalities for prepare-transform-measure scenarios]),
    talkcell([Raphaël Le Bihan, Alastair Abbott, Mnacho Echenim],
      [Probing the composition of processes with first-order-ISOMIX logic]),
  table.cell(colspan: 4, fill: c-poster, align: center)[Poster session (with reception) #h(1em) 17:30 -- 19:30],
)

#pagebreak()

== Wednesday, August 19th

#table(
  columns: (3cm, 1fr),
  stroke: 0.5pt,
  inset: 6pt,
  align: left + horizon,
  table.cell(colspan: 2, fill: c-chair-bg, align: center, text(size: 9pt, [Long plenary talks])),
  timec[9:30 -- 10:15], talkcell(
    [Miriam Backens, Simon Perdrix #h(1em) / #h(1em) Miriam Backens],
    [Completeness for flow-preserving rewrite rules / Generating one-way computations with flow: flow-preserving rewriting that ignores the interpretation]
  ),
  timec[10:15 -- 11:00], talkcell(
    [Quanlong Wang, Richard D. P. East, Razin A. Shaikh, Lia Yeh, Boldizsár Poór, Bob Coecke],
    [Beyond Penrose tensor diagrams with the ZX calculus: applications to quantum computing, quantum machine learning, condensed matter physics, and quantum gravity]
  ),
  table.cell(colspan: 2, fill: c-break, align: center)[Coffee break],
  table.cell(colspan: 2, align: center, text(weight: "bold", [Industry session #h(1em) 11:30 -- 12:20])),
  table.cell(colspan: 2, fill: c-break, align: center)[Lunch break],
)

#v(0.5em)

#table(
  columns: (2.4cm, 1fr, 1fr, 1fr),
  stroke: 0.5pt,
  inset: 5pt,
  align: left + horizon,
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel A])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel B])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel C])),
  timec[14:30 -- 14:55],
    talkcell([Luca Apadula, Alessandro Bisio, Giulio Chiribella, Paolo Perinotti, Kyrylo Simonov],
      [Higher-order transformations of bidirectional quantum processes]),
    talkcell([Nathan Claudet, Simon Perdrix],
      [Insights in graph state entanglement via r-local complementation: structure and a quasi-polynomial algorithm]),
    talkcell([Pablo Arrighi, Doğukan Bakircioglu, Nathan Houyet],
      [Quantum theory over dual-complex numbers]),
  timec[14:55 -- 15:20],
    talkcell([Matthew Wilson, James Hefford, Timothée Hoffreumon], [Supermaps on generalised theories]),
    talkcell([Piotr Mitosek, Miriam Backens], [Working with measurement-based computations on qudits]),
    talkcell([Nicolas Moulonguet, Augustin Vanrietvelde],
      [Subsystems as subsets of quantum channels, and the strange case of blind agents]),
  timec[15:20 -- 15:45],
    talkcell([Samson Abramsky, Radha Jagadeesan], [Essential unitarity for higher-order quantum computation]),
    talkcell([Aleks Kissinger, John van de Wetering],
      [ZX-flow: a flexible criterion for deterministic computation with ZX-diagrams]),
    talkcell([John Harding, Alexander Wilce],
      [Classical explanations in (and of) general probabilistic theories]),
  table.cell(colspan: 4, fill: c-break, align: center)[Coffee break],
  timec[16:15 -- 16:40],
    talkcell([Thomas Bartsch, Yuhan Gai, Sakura Schäfer-Nameki],
      [Beyond Wigner -- how non-invertible symmetries preserve probabilities]),
    talkcell([Haytham McDowall-Rose, Razin A. Shaikh, Lia Yeh],
      [From fermions to qubits: a ZX-calculus perspective]),
    talkcell([Amrapali Sen, Flavio Del Santo], [Superluminal transformations and indeterminism]),
  timec[16:40 -- 17:05],
    talkcell([Vanessa Brzić, Satoshi Yoshida, Mio Murao, Marco Túlio Quintino],
      [Higher-order quantum computing with known input states]),
    talkcell([Lia Yeh, Jiaxin Huang, Aleks Kissinger, Sarah Meng Li, John van de Wetering],
      [A three-way normal form for stabiliser codes across ZX diagrams, circuits, and tableaus]),
    talkcell([Maarten Grothus, V. Vilasini],
      [Impossibility of superluminal signalling rules out causal loops in conical spacetimes]),
  table.cell(colspan: 4, fill: c-special, align: center)[Boat tour #h(1em) 17:30 -- 18:30],
  table.cell(colspan: 4, fill: c-special, align: center)[Conference dinner #h(1em) starting 19:00],
)

#pagebreak()

== Thursday, August 20th

#table(
  columns: (3cm, 1fr),
  stroke: 0.5pt,
  inset: 6pt,
  align: left + horizon,
  table.cell(colspan: 2, fill: c-chair-bg, align: center, text(size: 9pt, [Long plenary talks])),
  timec[9:30 -- 10:15], talkcell(
    [Cole Comfort, Robert I. Booth],
    [Denotational semantics for stabiliser quantum programs]
  ),
  timec[10:15 -- 11:00], talkcell(
    [Kathleen Barsse, Romain Péchoux, Simon Perdrix],
    [Quantum control and general recursion beyond the unitary case]
  ),
  table.cell(colspan: 2, fill: c-break, align: center)[Coffee break],
  table.cell(colspan: 2, fill: c-chair-bg, align: center, text(size: 9pt, [Short plenary talk])),
  timec[11:30 -- 11:55], talkcell(
    [Aabhas Gulati, Ion Nechita, Clément Pellegrini],
    [Entanglement in the Dicke subspace]
  ),
  table.cell(colspan: 2, align: center, text(weight: "bold", [Conference photo #h(1em) 11:55 -- 12:20])),
  table.cell(colspan: 2, fill: c-break, align: center)[Lunch break],
)

#v(0.5em)

#table(
  columns: (2.4cm, 1fr, 1fr, 1fr),
  stroke: 0.5pt,
  inset: 5pt,
  align: left + horizon,
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel A])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel B])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel C])),
  timec[14:30 -- 14:55],
    talkcell([Arianne Meijer-van de Griend, Leo Becker],
      [Pauli gadget synthesis for gatesets with arbitrary even-arity Clifford gates]),
    talkcell([Haruki Emori], [Quantum statistical functions]),
    talkcell([Nadish de Silva, Santanil Jana, Ming Yin],
      [Three-qubit nonlocality paradoxes: beyond GHZ]),
  timec[14:55 -- 15:20],
    talkcell([Soichiro Yamazaki, Seiseki Akibue], [Multi-qubit controlled gate with optimal T-count]),
    talkcell([Michael Zurel, Jack Davis],
      [Basis-independent stabilizerness and maximally noisy magic states]),
    talkcell([Shashaank Khanna, Matthew Pusey, Roger Colbeck],
      [Identifying causal structures which cannot support quantum correlations without fine-tuning]),
  timec[15:20 -- 15:45],
    talkcell([Akash Kundu],
      [Tensor and gadget reinforcement learning for improved, hardware-aware quantum architecture search]),
    talkcell([Cameron Calcluth, Oliver Hahn, Juani Bermejo Vega, Alessandro Ferraro, Giulia Ferrini],
      [Classical simulation of circuits with realistic odd-dimensional Gottesman--Kitaev--Preskill states]),
    talkcell([C. E. Lopetegui-Gonzalez, G. Masse, E. Oudot, U. I. Meyer, F. Centrone, F. Grosshans, P. E. Emeriau, U. Chabaud, M. Walschaers],
      [A unified framework for Bell inequalities from continuous-variable contextuality]),
  timec[15:45 -- 16:10],
    talkcell([Mark Deaconu, Nihar Gargava, Amolak Ratan Kalra, Michele Mosca, Jon Yard],
      [Buildings for synthesis with Clifford+R]),
    talkcell([Massimo Frigerio, Mattia Walschaers, Andrei Aralov, Carlos Ernesto Lopetegui-Gonzalez, Emilie Gillet],
      [Algebraic techniques for photonic state preparation and characterization]),
    talkcell([Martin J. Renner, Edwin Peter Lobo, Arturo Konderak, Remigiusz Augusiak, Antonio Acín],
      [Full nonlocality for non-maximally entangled states]),
  table.cell(colspan: 4, fill: c-break, align: center)[Coffee break #h(1em) 16:10 -- 16:40],
  table.cell(colspan: 4, fill: c-especial, align: center, [Career fair #h(1em) 16:40 -- 19:00]),
)

#pagebreak()

== Friday, August 21st

#table(
  columns: (3cm, 1fr),
  stroke: 0.5pt,
  inset: 6pt,
  align: left + horizon,
  table.cell(colspan: 2, fill: c-chair-bg, align: center, text(size: 9pt, [Long plenary talks])),
  timec[9:30 -- 10:15], talkcell(
    [Thea Li, Vladimir Zamdzhiev],
    [Quantum coherence spaces revisited: a von Neumann (co)algebraic approach]
  ),
  timec[10:15 -- 11:00], talkcell(
    [Matilde Baroni, Dominik Leichtle, Ivan Šupić, Damian Markham, Marco Túlio Quintino],
    [Composable simultaneous purification: when all communication scenarios reduce to spatial correlations]
  ),
  table.cell(colspan: 2, fill: c-break, align: center)[Coffee break],
  table.cell(colspan: 2, align: center, text(weight: "bold", [Business meeting #h(1em) 11:30 -- 12:20])),
  table.cell(colspan: 2, fill: c-break, align: center)[Lunch break],
)

#v(0.5em)

#table(
  columns: (2.4cm, 1fr, 1fr, 1fr),
  stroke: 0.5pt,
  inset: 5pt,
  align: left + horizon,
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel A])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel B])),
  table.cell(fill: c-chair-bg, align: center, text(size: 9pt, [Parallel C])),
  timec[14:30 -- 14:55],
    talkcell([Simon Burton, Hussain Anwar], [Meromorphic quantum computing]),
    talkcell([Noé Delorme, Simon Perdrix],
      [Diagrammatic reasoning with control as a constructor, applications to quantum circuits]),
    talkcell([David Schmid, John H. Selby, Vinicius Pretti Rossi, Roberto D. Baldijão, Ana Belén Sainz],
      [Shadows and subsystems of generalised probabilistic theories: when tomographic incompleteness is not a loophole for contextuality proofs]),
  timec[14:55 -- 15:20],
    talkcell([Christine Li, Lia Yeh], [Transversal AND in quantum codes]),
    talkcell([Chris Heunen, Robin Kaarsgaard, Louis Lemonnier], [One rig to control them all]),
    talkcell([Jan-Åke Larsson], [The contextual Heisenberg microscope]),
  timec[15:20 -- 15:45],
    talkcell([Jin Ming Koh, Anqi Gong, Andrei C. Diaconu, Daniel Bochen Tan, Alexandra A. Geim, Michael J. Gullans, Norman Y. Yao, Mikhail D. Lukin, Shayan Majidy],
      [Phantom codes: entangling logical qubits without physical operations]),
    talkcell([William Schober, Scott Wesley],
      [A complete equational theory for quantum circuits with generalized control]),
    talkcell([Daniel McNulty], [Quantifying quantum measurement incompatibility via graph invariants]),
  table.cell(colspan: 4, fill: c-break, align: center)[Coffee break],
  timec[16:15 -- 16:40],
    talkcell([Vivien Vandaele], [Asymptotically optimal quantum circuits for comparators and incrementers]),
    talkcell([Sacha Cerf, Harold Ollivier], [The perturbative method for quantum correlations]),
    talkcell([Raffaele D'Avino, Lorenzo Caramelli, Raja Yehia, Gabriel Senno, Roberto González Pousa, Antonio Acín, Tamás Kriváchy],
      [Device independent quantum key distribution with a single measurement per site]),
  timec[16:40 -- 17:05],
    talkcell([Giuseppe De Riso, Giuseppe Catalano, Seth Lloyd, Vittorio Giovannetti, Dario De Santis],
      [A resource-efficient quantum-walker quantum RAM]),
    talkcell([Subhendu Bikas Ghosh, Snehasish Roy Chowdhury, Guruprasad Kar, Arup Roy, Tamal Guha, Manik Banik],
      [Strong inequivalence of quantum nonlocal resources]),
    talkcell([Paul Becsi, Matthew Joseph Hoban],
      [Bounding classical and quantum correlations in Bayesian networks with quasiprobabilities]),
  table.cell(colspan: 4, align: center, text(weight: "bold", [End of QPL 2026. Goodbye!])),
)
