# Draft 2 detailed independent referee review

The report treats Luke Martin's face-graph paper independently of UFFT.

## Main findings

Draft 2 fixes the main first-review errors. The core spectra pass exact checks.
The review develops an explicit quarter-flux incidence identity, block proof,
symmetry-compatible intertwiner, genuine rotation representation, and weighted
extension. These are additional results of this audit, not claims already proved
in the manuscript. The author's ordinary script has an unconditional ALL PASS
message, demonstrated by a controlled incorrect-expected-polynomial test.

## Build and run

Compile Draft2_Detailed_Referee_Report.tex twice with pdflatex.
The PDF is supplied. No bibliography download is needed.

With Python 3.12 and the dependencies in requirements.txt, run:

    python3 verify_baseline.py
    python3 verify_deeper.py
    python3 verify_flux_sweep.py
    python3 check_author_certificate.py

The baseline writes verification_results.json. The deeper checker writes
exact symbolic results to deeper_results.json. The sweep writes
magnetic_sweep.csv (25 charges, all 14 eigenvalues, numerical).
Do not run Python with -O: these verification scripts use assertions.

## Evidence provenance

The author_evidence directory contains author-script execution logs, the generated
gauge certificate, a source manifest with the inspected commit and SHA-256 hashes,
and the controlled failure-injection log. The original author source files are
not redistributed here; fetch the two filenames in source_manifest.json from the
verification directory at the pinned commit if repeating those executions.
Both must be in the same directory because the magnetic script imports the
ordinary script. The original source was not modified by the failure injection.

The exact certificate checker validates the author's graph, orientations and
holonomies without importing the author's programs. Our deeper checker also
verifies the geometric square permutations underlying the compensated rotations
and equivariance of the intertwiner.

All tests reported were executed. Numerical versus exact checks are distinguished
in the report. No priority certification or personal endorsement is implied.
