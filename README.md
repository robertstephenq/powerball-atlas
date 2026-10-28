# Powerball Atlas

Interactive Powerball history, state maps, jackpot visualization, and a Worker that refreshes official public data.

## Build and validate

Requires Node.js.

```sh
node scripts/build.mjs
node scripts/validate-artifact.mjs
```

For an interface-only preview, run `python -m http.server 8000 --directory public` and open http://localhost:8000. The live `/api/live` endpoint needs a compatible Cloudflare Worker/Sites runtime.

## Files

- `public/`: HTML, CSS, JavaScript, bundled draw data, maps, and D3.
- `worker/index.js`: static responses and live official-source aggregation.
- `scripts/`: build and artifact validation.
- `prepare.py` and `media.html`: source data preparation and captured reference material.

## Original implementation notes

Build with `node scripts/build.mjs`; validate with `node scripts/validate-artifact.mjs`.

The Worker serves the files in `public/` and a same-origin `/api/live` endpoint. The endpoint checks the Powerball home page for the next jackpot, cash option, drawing time and latest numbers; the Powerball Media Center for published claims; and NY Open Data for draw history. Responses include the source check time and any partial failures. Upstream fetches are cached for up to three minutes.

The page refreshes on opening, every five minutes while visible, and when returning after a minute away. This is request-driven data access: no unattended job or notification is needed. No credentials are required for the public source feeds. Saved draws stay in browser storage. Bundled data provides a fallback; unavailable sources and estimates whose drawing time has passed are labeled explicitly.

`public/current.json` is a dated fallback estimate, not the live source. When source markup changes, update and verify `parseHome` or `parseClaims` in `worker/index.js`; malformed source data must not replace the last available result.

## Source backup

Saved from the available ChatGPT project files on October 27, 2026. Authored source, assets, and configuration are included. Installed dependencies, local environment files, credentials, and Git internals are excluded. The original Sites identity is preserved; uploading this repository does not deploy or change the website.
