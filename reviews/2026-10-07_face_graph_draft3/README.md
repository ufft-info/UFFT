# Consolidated review of Draft 3 and the supplied referee report

The nine-page report evaluates both inputs, recommends minor revision, and supplies
short proof additions for gauge classification, monomiality, and the Fedorov table.
It also records the newly identified centre-coordinate error, the numerical
relative-tolerance issue, and the unavailable public release tag.

## Reproduce independent checks

Install requirements.txt with Python 3, then run:

    python3 run_all.py

Do not use python -O; these checkers use assertions. The numerical charge sweep
runs after the baseline so it can use the generated graph certificate. Exact and
numerical results are distinguished in the report. NetworkX is only needed to
repeat the author's optional automorphism enumeration.

## Compile the report

    pdflatex Draft3_Consolidated_Referee_Report.tex
    pdflatex Draft3_Consolidated_Referee_Report.tex

The compiled PDF is included. No external bibliography is needed.

## Evidence

The author_evidence directory contains the source manifest, logs from executing
both author scripts at the pinned public-main commit, the negative test proving
that the old unconditional-success defect is fixed, the strict-tolerance rerun,
and the author's new JSON certificate. The original author source scripts are
not redistributed here; their SHA-256 hashes and repository commit identify them.
The negative test changed one expected factor in an in-memory copy; the strict
rerun changed all declared 1e-12 allclose calls to rtol=0 in an in-memory copy.
The downloaded originals and the user-supplied attachments were not modified.

The exact supplementary checker verifies the correct hexagon centres, explicit
magnetic rotation generators, and all four Fourier blocks for the elongated graph.
The deeper checker validates all 24 rotations and all 576 group products, as well
as the quarter-flux Gram identity, intertwiner, and weighted blocks. The weighted
extension is not imposed as a requirement on Draft 3.

The public tag face-graph-note-v3 was unavailable on 2026-10-07; the public tag
list was empty. The public-main commit inspected was
c1d95bad8d7e42b6a4a94f6dd3b1eb21f4d7718d. This is not a claim that the named tag
can never be published or that the author's intended local release does not exist.
