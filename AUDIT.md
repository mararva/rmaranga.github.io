# Portfolio audit - October 21, 2026

| Area | Finding | Change |
| --- | --- | --- |
| Home and About | Still described a current student and expected June 2026 graduation. | Replaced with statistics graduate and current USC Norris Data Analyst background. |
| Resume page | Only pointed to the PDF; no readable experience summary. | Added accessible HTML experience, skills, education, and project summaries with a PDF download. |
| Resume content | Omitted USC Norris and Cal Poly educational research work. | Added specific research/data duties and Cal Poly Research Assistant experience. |
| Prior employment | ARCH was titled Data Analyst; budget/Tableau/75% improvement claims were not corroborated by the supplied work history. | Used Technician / Shop Assistant and documented Python/CNC file organization responsibilities. |
| Education and skills | Mathematics minor and some broad tool claims lacked confirmation in the supplied current background. | Retained confirmed B.S. in Statistics and relevant skills; explicitly described SQL as basic. |
| Project links | Original Shiny app links and project listing remained useful; Colonel Blotto source code was not linked in its page. | Preserved all project URLs and listing order; added the verified `mararva/colonelblottogame` repository. |
| Presentation | Empty custom stylesheet and navigation led directly to the PDF. | Added modest typography, spacing, responsive image, keyboard focus, and print refinements; Resume navigation now opens the HTML page, with PDF downloads on key pages. |
| Build consistency | Root source differed from generated content; `_quarto.yml` referenced a missing root resume.pdf. | Updated source and `docs/` together; added root PDF and reproducible PDF/HTML refresh scripts. |
| Search | Search excerpts repeated outdated student and redirect text. | Updated Home, About, and Resume search entries. |

## Boundaries and remaining confirmation

- The USC role is treated as current because the portfolio owner explicitly identified it as current. A conflicting future start date in the supplied career history is not published. Confirm the actual start month/year before adding tenure.
- The completed mathematics minor is not claimed pending confirmation.
- Existing project descriptions and original dates remain unchanged. A project-link audit can establish destination availability at a point in time; it cannot establish application functionality or continued hosting uptime.
- The older `_site/` snapshot is retained; `docs/` is the configured output directory. Existing legacy pages and paths are retained.

## Verification

- Generated the single-page PDF from `resume.qmd`; checked text extraction, embedded links, page count, and a rendered page image.
- Checked updated HTML for stale student claims and unresolved `.qmd` links.
- Compared original and revised project link destinations, allowing the intentional Resume navigation change.
- Checked local link and asset targets. Browser rendering could not be verified: Chromium was unavailable and its download failed in this environment. Responsive CSS was reviewed statically.
- Checked the patch for whitespace errors. A full Quarto build was unavailable in the editing environment; the documented focused Pandoc refresh was used.
