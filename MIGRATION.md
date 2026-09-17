# Glezper: Publii → bilingual Hugo / Blowfish

## Production is unchanged

This is the MAIN corporate site, `glezper.com`, in `christianglezper/glezper`.
The separate `christian.glezper.com` portfolio has not been modified.

The Hugo replacement lives in `hugo/` on `migration/hugo-blowfish-bilingual`.
All original Publii export files remain intact at repository root. The review
workflow builds and tests Hugo, but has **no deployment step or Pages permissions**.

## Verified backup

- Backup branch: `backup/publii-2026-09-17`
- Original production commit: `7ad691a72a3bc545647e6d1eafc0c8809a01da9c`
- Original tree: `4682c3fdf31311527d138629eb870055a6f0db70`
- Includes published HTML, CSS, JavaScript, images, feeds, sitemap and CNAME.
- Download: https://github.com/christianglezper/glezper/archive/refs/heads/backup/publii-2026-09-17.zip

This is a backup of the **published static site**, not Publii's editable desktop
database, application settings or unsynchronized drafts. Keep the local Publii
project and export a native Publii backup separately if future desktop editing
needs to remain possible.

## Content and routes

| Page | English | Spanish | Previous URL preserved |
| --- | --- | --- | --- |
| Home | `/` | `/es/` | `/hecho-para-quienes-hacen-negocios.html` → Spanish home |
| Glezper 360° | `/360/` | `/es/360/` | `/glezper-360deg.html` |
| Glezper Media | `/media/` | `/es/media/` | `/glezper-media.html` |
| Glezper Business | `/business/` | `/es/business/` | `/glezper-business.html` |
| Contact | `/contact/` | `/es/contact/` | New convenience page |

English service copy is mechanically imported from the original HTML by
`scripts/import_publii.py`; email/phone links are made clickable. The English
homepage keeps the original business description and three divisions. Contact
details come from the existing site. Spanish is an editorial working translation
and **has not been approved**. Christian may provide replacement Spanish copy.
Its `editorialStatus` field records this without displaying a notice to visitors.

Financing-provider eligibility language and the existing OPF partner URL are
preserved. The existing application URL uses `lan=es` in both languages; it was
not silently modified. No rates, approvals or financing guarantees were added.
The existing Valor and Agaynda external URLs were retained, not reverified.

The removed Madrid essay is intentionally not resurrected on the corporate site.
The old empty author/tag indexes and feeds are retained in the backup but are not
copied as corporate content. Hugo generates its own RSS, JSON search and sitemaps.

## Theme / build

- Blowfish v3.6.0, submodule pinned to `4643c46bd5e921fee51c420575fadebf9f4b3681`.
- Hugo Extended 0.165.0 (within this theme release's supported version range).
- Custom corporate homepage uses Blowfish's documented `custom` homepage slot;
  service pages, navigation, search, language controls and dark mode use the theme.
- Existing gold wordmark and media paths are mounted from the Publii export.
- No analytics, cookies for tracking, CRM integration or form submission service added.

```sh
git clone --branch migration/hugo-blowfish-bilingual --recurse-submodules https://github.com/christianglezper/glezper.git
cd glezper
hugo --source hugo --gc --minify
python3 scripts/check_hugo.py hugo/public
hugo server --source hugo
```

The Actions workflow saves `glezper-hugo-review`, a downloadable build artifact
with a 30-day retention. It is not a hosted preview URL. Source and backup branches
are durable beyond that retention. Serve the artifact over HTTP; opening its
index file directly with `file://` will not correctly resolve root-relative assets.

## Before launch

1. Christian reviews Spanish copy and confirms the design.
2. Complete browser QA at desktop and phone widths (this workspace's cloud browser
   could not access its localhost preview).
3. Verify contact links, search, theme switch and page-to-page language switching.
4. Confirm existing GitHub Pages source/settings in the account.
5. Only after explicit launch approval, configure a production Hugo Pages workflow
   to deploy `hugo/public`, preserving the apex CNAME. Do not overwrite the portfolio.
6. Verify live HTTPS, legacy redirects, indexing and social previews.
7. Stop publishing the old Publii project to this repo after cutover, to avoid
   overwriting the Hugo source/workflow with another static export.

## Rollback

The backup branch is an exact static export and can be deployed as the Pages
source if a cutover needs to be reversed. Record the current Pages settings before
cutover, disable the replacement deployment workflow, and restore the old Pages
branch/directory configuration using the backup branch. No force-push or history
erasure is needed. DNS does not need to change for this migration.
