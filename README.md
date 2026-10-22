# Ryan Marangattu's portfolio

A Quarto portfolio published from `docs/` at https://ryan.marangatwo.com.
The Home, About, Resume, and Projects pages retain their existing paths and project listing structure.

## Editing and rebuilding

Edit the root `.qmd` files and project sources under `posts/`. `resume.qmd` is the shared content source for the HTML resume and downloadable PDF.

1. Install Pandoc, Python 3, and ReportLab. The PDF script uses DejaVu Sans from `/usr/share/fonts/truetype/dejavu/` (adjust the font paths on other systems).
2. Run `python scripts/build_resume.py` to create `resume.pdf` and `docs/resume.pdf`.
3. With Quarto installed, run `quarto render`. `_quarto.yml` publishes to `docs/` and copies the root PDF as a resource.
4. When Quarto is unavailable, run `python scripts/refresh_pages.py`. This focused refresh uses Pandoc to update Home, About, and Resume inside their existing Quarto HTML shells; it preserves the project listing and its bundled assets. It also refreshes the changed search entries, navigation, stylesheet, and Colonel Blotto source link. It is not a replacement for a full Quarto build after theme, listing, or project-content changes.

Commit both sources and the corresponding `docs/` output. `_site/` is an older, inactive build snapshot; `_quarto.yml` targets `docs/`.

## Content notes

The current USC Norris role emphasizes REDCap survey setup, Excel data cleaning, literature searches, reports, and research coordination. Its start date is intentionally omitted pending confirmation: the supplied career history contains a date later than the audit date. No performance metrics, advanced clinical programming responsibilities, or completed mathematics minor are asserted without confirmation.

The previous ARCH title and quantitative impact claims were replaced with the documented technician/shop assistant role and Python file organization work. All original project pages and Shiny app destinations are preserved; the Colonel Blotto GitHub repository is additionally linked from the project and resume.

See [AUDIT.md](AUDIT.md) for the audit and verification record.
