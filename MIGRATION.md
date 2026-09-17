# Glezper: Publii → bilingual Hugo / Blowfish

## Production and preview

This is the MAIN corporate site, `glezper.com`, in `christianglezper/glezper`.
The separate `christian.glezper.com` portfolio has not been modified.

The Hugo replacement lives in `hugo/` on `migration/hugo-blowfish-bilingual`.
The public Publii homepage and 360 page received a narrow privacy fix removing
Christian's phone number on 2026-09-17. The exact original export remains in the
backup branch. Other Publii export files remain intact at repository root. The review
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
`scripts/import_publii.py`; email links are made clickable. Existing edited pages
are now skipped by the importer, and private phone details are excluded. The English
homepage keeps the original business description and three divisions. Contact
details come from the existing site. Spanish is an editorial working translation
and **has not been approved**. Christian may provide replacement Spanish copy.
Its `editorialStatus` field records this without displaying a notice to visitors.

The OPF-only CTA has been replaced with a Glezper inquiry form. No rates,
approvals, savings or financing guarantees were added. The original OPF referral
URL remains recoverable in the backup for future reviewed referrals.
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
- No analytics or CRM integration added. FormSubmit is proposed for email delivery;
  submission is disabled pending explicit authorization and delivery verification.

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
   Activate and verify form delivery as described below.
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

## Business inquiries — September 17 review

- Private visual preview: https://glezper-hugo-preview.chrisgptorruella.chatgpt.site
- Financing, POS and automation can be selected separately or together.
- Financing revenue bands distinguish under $10,000/month, at least $10,000/month,
  and unknown/manual review. This is an internal triage signal, not an eligibility
  determination. No inquiry is automatically forwarded to OPF, B2B Funding, B2B
  payments, ECS or an automation partner. B2B Funding remains pending an agreement.
- POS differentiates new business setup, first system, rate comparison and expansion.
- Automation records the process, tools, weekly effort and desired outcome.
- Hidden sections are disabled so stale answers do not travel with a later selection.
- Contact consent is required; sensitive documents and financial identifiers are not collected.
- All visible arrows use an inline SVG instead of font/emoji glyphs.
- Public phone details removed from both languages and the current Publii pages.

### Email delivery gate

`params.businessFormEnabled` is **false**. Both forms show a preview notice and
disable submission. While disabled, the form action has no external destination.
The proposed endpoint is configured separately in `businessFormEndpoint`.
Automatic approval review rejected the setup test because sending Christian's
email to FormSubmit requires explicit authorization for that third-party service.
No email delivery, activation or inbox receipt has been verified.

After Christian approves FormSubmit, submit one clearly labeled setup test,
complete its email-address verification, enable the form and verify a test email
arrives at christianglezper@gmail.com. Keep the default CAPTCHA enabled. Do not
report success on the client before provider acceptance. Use the correct site's
baseURL so the `_next` return URL matches the preview or final domain.
Alternatively, authenticate Zoho and wire this intake to an authorized Zoho form.

FormSubmit docs: https://formsubmit.co/documentation
Known limitation: the no-JavaScript fallback displays all sections and sends
unclassified inquiries for manual review; it does not enforce conditional fields.

### Verification

Hugo build and route/translation/asset/privacy checks passed. Local DOM tests
covered both languages, the $10,000 boundary, pre-revenue and unknown answers,
multiple interests, conditional requirements, stale-field exclusion, readable
email payloads and disabled submission. Those tests used in-memory events only;
they did not transmit inquiries. End-to-end delivery remains gated above.

## Proposed image direction

Keep the cream, charcoal and gold palette with a small number of wide images:

| Placement | Suggested visual |
| --- | --- |
| Homepage | A real Ponce/Puerto Rico streetscape showing active local businesses; one wide image beneath the introduction. |
| 360 | A collage of real creative work: a campaign, a web layout and an outdoor placement, with accurate project context. |
| Media | Actual Valor and Agaynda covers/site screenshots composed as an editorial spread. The Agaynda wordmark is already in Cloudinary. |
| Business | A real retailer at a POS or reviewing operations; supporting line illustrations for capital, payments and automation. |

These are suggestions, not newly sourced or licensed photo assets. Do not present
stock people as Glezper staff or former portfolio work as current Glezper clients.
